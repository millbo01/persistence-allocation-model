"""PT1: parser from the downloaded files to the tidy CSVs read by pt1_councils.py.

Written after the frozen pre-registration (step 5, structure inspection). Every setting below is logged in
tests/PT1 Priority test - procedure log.md before the counting step.

Modes:
  --structure   prints layout facts only (sheet, header row, name row, line names, number of councils, class codes).
                No values are printed.
  --build OUT   writes spend.csv, pop.csv, proj.csv, csp.csv and cpi.csv to OUT.
"""
import argparse
import json
import os
import re
import sys
import zipfile

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "data", "pt1")
YEARS = {"2014-to-2015": 2014, "2015-to-2016": 2015, "2016-to-2017": 2016, "2017-to-2018": 2017,
         "2018-to-2019": 2018, "2019-to-2020": 2019}
SKIP = ("***", "revenue outturn", "net current", "hide or", "row_no", "col_no", "additional information", "£",
        "£")
CROSSWALK_FILE = os.path.join(HERE, "..", "PT1_line_name_crosswalk.csv")


def text(v):
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return ""
    return str(v).strip()


def read_book(path):
    engine = "odf" if path.endswith(".ods") else None
    xl = pd.ExcelFile(path, engine=engine)
    return {sh: pd.read_excel(path, sheet_name=sh, header=None, engine=engine) for sh in xl.sheet_names}


def parse_sheet(df):
    """Return dict(header_row, name_row, blocks=[(name, nce_col)], councils_rows, code_col, class_col) or None."""
    h = None
    for r in range(min(40, len(df))):
        if text(df.iat[r, 0]) == "E-code":
            h = r
            break
    if h is None:
        return None
    hdr = [text(x) for x in df.iloc[h].tolist()]
    code_col = hdr.index("ONS Code") if "ONS Code" in hdr else None
    class_col = hdr.index("Class") if "Class" in hdr else None
    name_row, names = None, []
    for r in range(h - 1, -1, -1):
        cells = [(c, text(df.iat[r, c])) for c in range(df.shape[1])]
        cells = [(c, t) for c, t in cells if t and not t.lower().startswith(SKIP) and not t.startswith(SKIP)]
        if len(cells) >= 3:
            name_row, names = r, cells
            break
    if name_row is None:
        return None
    starts = [c for c, _ in names] + [df.shape[1]]
    blocks = []
    for i, (c, nm) in enumerate(names):
        nce = [k for k in range(c, starts[i + 1]) if hdr[k].lower().startswith("net current expenditure")]
        blocks.append((nm, nce[0] if nce else None))
    rows = [r for r in range(h + 1, len(df)) if re.match(r"^E\d{4}$", text(df.iat[r, 0]))]
    return dict(header_row=h, name_row=name_row, blocks=blocks, council_rows=rows, code_col=code_col,
                class_col=class_col)


def ro_files():
    out = []
    for yd, y in YEARS.items():
        d = os.path.join(ROOT, "ro", yd)
        for f in sorted(os.listdir(d)):
            m = re.search(r"(RO\d)", f)
            out.append((y, m.group(1), os.path.join(d, f)))
    return out


def structure():
    rep = {}
    for y, form, path in ro_files():
        book = read_book(path)
        for sh, df in book.items():
            p = parse_sheet(df)
            if p is None:
                continue
            classes = sorted({text(df.iat[r, p["class_col"]]) for r in p["council_rows"]}) if p["class_col"] is not None else []
            names = [nm for nm, _ in p["blocks"]]
            with_nce = sum(1 for _, c in p["blocks"] if c is not None)
            key = f"{form}|{y}|{sh}"
            rep[key] = dict(header_row=p["header_row"], name_row=p["name_row"], n_blocks=len(names),
                            n_blocks_with_nce=with_nce, n_councils=len(p["council_rows"]), classes=classes,
                            names=names)
            print(f"{form} {y} [{sh}] header row {p['header_row']}, name row {p['name_row']}, blocks {len(names)} "
                  f"(with NCE column {with_nce}), councils {len(p['council_rows'])}, classes {classes}")
    json.dump(rep, open(os.path.join(ROOT, "structure", "_parser_structure.json"), "w"), indent=1)


def norm(name):
    t = str(name).lower()
    t = re.sub(r"^\s*line\s*\d+\s*", "", t)
    return re.sub(r"[^a-z0-9]", "", t)


def crosswalk():
    cw = pd.read_csv(CROSSWALK_FILE)
    return {(r.form, norm(r.data_name)): r.classification_name for r in cw.itertuples()}


RELABEL = {("RO5", 2019): ("Sports development and community recreation",
                           "Sports and recreation facilities, including golf courses")}


def build_spend():
    cw = crosswalk()
    rows = []
    for y, form, path in ro_files():
        book = read_book(path)
        for sh, df in book.items():
            p = parse_sheet(df)
            if p is None:
                continue
            seen = {}
            for nm, col in p["blocks"]:
                seen[nm] = seen.get(nm, 0) + 1
                if (form, y) in RELABEL and nm == RELABEL[(form, y)][0] and seen[nm] == 2:
                    nm = RELABEL[(form, y)][1]          # source labelling error, corrected by position (logged)
                if col is None:
                    continue
                name = cw.get((form, norm(nm)), nm)
                for r in p["council_rows"]:
                    v = pd.to_numeric(df.iat[r, col], errors="coerce")
                    rows.append(dict(ons_code=text(df.iat[r, p["code_col"]]), la_type=text(df.iat[r, p["class_col"]]),
                                     year=y, form=form, line_name=name, data_name=nm, nce_thousands=v))
    sp = pd.DataFrame(rows)
    sp["la_type"] = sp["la_type"].replace({"L": "LB"})
    # crosswalk merges (different data names, same classification name) are summed; true duplicates are left
    key = ["ons_code", "la_type", "year", "form", "line_name"]
    g = sp.groupby(key)
    merged = g["data_name"].transform("nunique") > 1
    once = sp.groupby(key + ["data_name"])["data_name"].transform("size") == 1
    to_sum = sp[merged & once]
    rest = sp[~(merged & once)]
    summed = to_sum.groupby(key, as_index=False).agg(nce_thousands=("nce_thousands", lambda s: s.sum(min_count=1)),
                                                     data_name=("data_name", lambda s: " + ".join(sorted(s))))
    out = pd.concat([rest, summed], ignore_index=True)
    return out[["ons_code", "la_type", "year", "form", "line_name", "nce_thousands", "data_name"]]


def groups_from_single_age(df, code, age, years):
    """df rows: one per area and single age (age numeric 0..90, 90 = 90 and over). Returns long table."""
    d = df[[code, age] + years].copy()
    d[age] = pd.to_numeric(d[age].astype(str).str.replace(" and over", "", regex=False), errors="coerce")
    d = d.dropna(subset=[age])
    out = []
    for gname, mask in (("all", lambda a: a >= 0), ("0_17", lambda a: a <= 17), ("65plus", lambda a: a >= 65),
                        ("18plus", lambda a: a >= 18)):
        s = d[mask(d[age])].groupby(code)[years].sum()
        s = s.reset_index().melt(id_vars=code, var_name="year", value_name="population")
        s["group"] = gname
        out.append(s.rename(columns={code: "ons_code"}))
    o = pd.concat(out, ignore_index=True)
    o["year"] = o["year"].astype(str).str.extract(r"(\d{4})")[0].astype(int)
    return o


def build_pop():
    z = zipfile.ZipFile(os.path.join(ROOT, "mye", "ukdetailedtimeseries20012019.zip"))
    d = pd.read_csv(z.open("MYEB2_detailed_components_of_change_series_EW_(2019).csv"))
    d = d[d["country"] == "E"]
    years = [f"population_{y}" for y in range(2010, 2020)]
    d = d.groupby(["ladcode19", "age"], as_index=False)[years].sum()     # both sexes
    return groups_from_single_age(d, "ladcode19", "age", years)


def build_proj():
    out = []
    # interim 2011-based (xls; header row with 'Code', 'Area', 'Age group' then year columns)
    z = zipfile.ZipFile(os.path.join(ROOT, "snpp", "syoa_2011i_persons.zip"))
    tmp = os.path.join(ROOT, "structure", "_tmp_2011i.xls")
    open(tmp, "wb").write(z.read("persons2011snpp.xls"))
    raw = pd.read_excel(tmp, sheet_name="Population - persons", header=None)
    os.remove(tmp)
    h = [r for r in range(20) if text(raw.iat[r, 0]) == "Code"][0]
    cols = [text(x) for x in raw.iloc[h].tolist()]
    cols = [str(int(float(c))) if re.match(r"^\d{4}(\.0)?$", c) else c for c in cols]
    d = raw.iloc[h + 1:].copy()
    d.columns = cols
    years = [c for c in cols if re.match(r"^\d{4}$", c)]
    d[years] = d[years].apply(pd.to_numeric, errors="coerce")
    g = groups_from_single_age(d, "Code", "Age group", years)
    g["edition"] = "2011i"
    out.append(g)
    for ed, member, code, age in (("2012", "2012 SNPP Population persons.csv", "areacode", "AgeGroup"),
                                  ("2014", "2014 SNPP Population persons.csv", "AREA_CODE", "AGE_GROUP"),
                                  ("2016", "2016 SNPP Population persons.csv", "AREA_CODE", "AGE_GROUP")):
        z = zipfile.ZipFile(os.path.join(ROOT, "snpp", f"z1_{ed}based.zip"))
        d = pd.read_csv(z.open(member))
        years = [c for c in d.columns if re.match(r"^\d{4}$", str(c))]
        g = groups_from_single_age(d, code, age, years)
        g["edition"] = ed
        out.append(g)
    return pd.concat(out, ignore_index=True)[["ons_code", "edition", "year", "group", "population"]]


def build_csp():
    d = pd.read_excel(os.path.join(ROOT, "csp", "Core_Spending_Power_Summary.xlsx"), sheet_name="input")
    d = d[d["ons_code"].notna()]
    # deviation D-5: keep single-tier council codes only (Greater Manchester Fire and the Combined Authority share
    # E31000040, which made the analysis pivot fail; no council in scope is affected)
    d = d[d["ons_code"].astype(str).str[:3].isin(["E06", "E08", "E09"])]
    long = d.melt(id_vars="ons_code", value_vars=[f"csp_{y}" for y in range(2015, 2020)], var_name="year",
                  value_name="csp_millions")
    long["year"] = long["year"].str[-4:].astype(int)
    long["csp_thousands"] = pd.to_numeric(long["csp_millions"], errors="coerce") * 1000.0
    return long[["ons_code", "year", "csp_thousands"]]


def build_cpi():
    rows = []
    for line in open(os.path.join(ROOT, "cpi", "d7bt.csv"), encoding="utf-8"):
        m = re.match(r'^"(\d{4}) ([A-Z]{3})","([\d.]+)"', line.strip())
        if m:
            rows.append((int(m.group(1)), m.group(2), float(m.group(3))))
    d = pd.DataFrame(rows, columns=["y", "mon", "cpi"])
    mi = {m: i for i, m in enumerate(["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"])}
    d["fy"] = np.where(d["mon"].map(mi) >= 3, d["y"], d["y"] - 1)
    fy = d.groupby("fy")["cpi"].agg(["mean", "size"])
    fy = fy[fy["size"] == 12]
    return pd.DataFrame(dict(year=fy.index, cpi=fy["mean"].values))


def build(out):
    os.makedirs(out, exist_ok=True)
    for name, fn in (("spend", build_spend), ("pop", build_pop), ("proj", build_proj), ("csp", build_csp),
                     ("cpi", build_cpi)):
        df = fn()
        df.to_csv(os.path.join(out, f"{name}.csv"), index=False)
        print(name, "rows:", len(df))      # row counts only


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--structure", action="store_true")
    ap.add_argument("--build", default=None)
    a = ap.parse_args()
    if a.structure:
        structure()
    if a.build:
        build(a.build)
