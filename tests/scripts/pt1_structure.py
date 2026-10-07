"""PT1, step 5: structure-only inspection of the downloaded files (pre-registration Section 9, step 5).

Prints sheet names, sheet shapes, and the TEXT cells of the top rows and the first columns of each sheet.
Every numeric cell, and every text cell that parses as a number, is masked as '#'. No values are printed.
Output: data/pt1/structure/<file>.txt (data/ is git-ignored), plus a short summary to stdout.
"""
import os
import re
import sys
import zipfile

import pandas as pd

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "pt1")
OUT = os.path.join(ROOT, "structure")
NUM = re.compile(r"^\s*[-+]?(\d[\d,]*\.?\d*|\.\d+)([eE][-+]?\d+)?\s*%?\s*$")


def mask(v):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None
    if isinstance(v, (int, float)):
        return "#"
    s = str(v).strip()
    if not s:
        return None
    return "#" if NUM.match(s) else s


def dump_sheet(name, df, fh, top=20, left=4):
    fh.write(f"--- sheet: {name}  shape={df.shape}\n")
    for r in range(min(top, len(df))):
        cells = [(c, mask(df.iat[r, c])) for c in range(df.shape[1])]
        txt = [f"[{c}]{t}" for c, t in cells if t not in (None, "#")]
        if txt:
            fh.write(f"row {r}: " + " | ".join(txt) + "\n")
    fh.write(f"first {left} columns, text cells (rows {top}..end), distinct values:\n")
    for c in range(min(left, df.shape[1])):
        vals = [mask(v) for v in df.iloc[top:, c].tolist()]
        vals = [v for v in vals if v not in (None, "#")]
        fh.write(f"  col {c}: {len(vals)} text cells; first 8: {vals[:8]}\n")


def inspect_excel(path, fh):
    engine = "odf" if path.endswith(".ods") else None
    xl = pd.ExcelFile(path, engine=engine)
    fh.write(f"sheets: {xl.sheet_names}\n")
    for sh in xl.sheet_names:
        df = pd.read_excel(path, sheet_name=sh, header=None, engine=engine)
        dump_sheet(sh, df, fh)


def inspect_csv(path_or_buf, label, fh, nrows=5):
    df = pd.read_csv(path_or_buf, nrows=nrows, header=0, low_memory=False)
    fh.write(f"--- csv: {label}  columns ({len(df.columns)}): {[str(c) for c in df.columns][:40]}\n")
    for c in df.columns[:6]:
        vals = [mask(v) for v in df[c].tolist()]
        fh.write(f"  {c}: {vals}\n")


def main():
    os.makedirs(OUT, exist_ok=True)
    targets = []
    for d, _, files in os.walk(ROOT):
        if "structure" in d or "pages" in d:
            continue
        for f in files:
            targets.append(os.path.join(d, f))
    for p in sorted(targets):
        rel = os.path.relpath(p, ROOT)
        out = os.path.join(OUT, rel.replace(os.sep, "__") + ".txt")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(f"FILE {rel}\n")
            try:
                if p.endswith((".xls", ".xlsx", ".ods")):
                    inspect_excel(p, fh)
                elif p.endswith(".zip"):
                    z = zipfile.ZipFile(p)
                    for i in z.infolist():
                        fh.write(f"member {i.filename} {i.file_size}\n")
                        if i.filename.lower().endswith(".csv"):
                            with z.open(i) as b:
                                inspect_csv(b, i.filename, fh)
                        elif i.filename.lower().endswith((".xls", ".xlsx")):
                            tmp = os.path.join(OUT, "_tmp_" + os.path.basename(i.filename))
                            open(tmp, "wb").write(z.read(i))
                            inspect_excel(tmp, fh)
                            os.remove(tmp)
                elif p.endswith(".csv"):
                    fh.write("(csv: header block only)\n")
                    with open(p, encoding="utf-8", errors="replace") as f:
                        for k, line in enumerate(f):
                            if k >= 8:
                                break
                            cells = [mask(x.strip('"')) for x in line.strip().split(",")]
                            fh.write("  " + str(cells) + "\n")
                else:
                    fh.write("(not inspected)\n")
            except Exception as e:
                fh.write(f"ERROR {type(e).__name__}: {e}\n")
        print(rel, "->", os.path.basename(out))


if __name__ == "__main__":
    main()
