"""PT1, step 6: counting step. Prints and saves counts only; no outcome values.

Usage: python pt1_count.py --data data/pt1/tidy --out tests/results/PT1
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pt1_councils as A  # noqa: E402


def main(data, out):
    d = A.load(data)
    panel, counts = A.build_panel(d)
    c = dict(counts)
    c["rows_in_panel"] = int(len(panel))
    c["rows_with_outcome"] = int(panel["y"].notna().sum())
    c["rows_missing_population"] = int(panel["P"].isna().sum())
    c["rows_missing_projection"] = int(panel["g_proj"].isna().sum())
    miss = panel[panel["g_proj"].isna()]
    c["councils_with_missing_projection"] = sorted(miss["ons_code"].unique().tolist())
    c["missing_projection_by_year"] = {int(k): int(v) for k, v in miss.groupby("year").size().items()}
    c["rows_usable_PT1"] = int(panel.dropna(subset=["y", "g_proj", "g_real"]).shape[0])
    cl = A.class_cols(panel)
    c["rows_usable_G25"] = int(cl.dropna(subset=["y", "g_real"]).shape[0])
    c["series_by_class"] = {k: int(v) for k, v in panel.groupby("cls")[["ons_code", "line_id"]]
                            .apply(lambda g: g.drop_duplicates().shape[0]).items()}
    c["lines_in_panel"] = sorted(panel["line_id"].unique().tolist())
    c["councils_in_panel"] = int(panel["ons_code"].nunique())
    c["councils_by_type"] = {k: int(v) for k, v in panel.groupby("la_type")["ons_code"].nunique().items()}
    os.makedirs(out, exist_ok=True)
    json.dump(c, open(os.path.join(out, "counts.json"), "w"), indent=2)
    print(json.dumps(c, indent=1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    main(a.data, a.out)
