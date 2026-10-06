"""H1 VitalDB: download the files the frozen analysis needs into data/vitaldb (git-ignored).

Run ONLY after James has accepted VitalDB's registration agreement, and after the pre-registration
(tests/H1 VitalDB G12 - pre-registration.md) and the analysis code (h1_vdb_g12.py) are committed.

The endpoints below are VitalDB's open web API as Claude knows it (cases, trks, labs, and one file per
track id). They are to be checked against the documented route at download; any difference is logged
as a deviation in tests/results/H1-VDB/README.md. Only structure is printed: file names, row counts
and checksums, never values.
"""
import gzip
import hashlib
import io
import os
import sys
import urllib.request

import pandas as pd

API = "https://api.vitaldb.net"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "data", "vitaldb")
TRACKS = ["Solar8000/ART_MBP", "Solar8000/ART_SBP", "Solar8000/ART_DBP", "Solar8000/HR",
          "Vigileo/SV", "EV1000/SV"] + [f"Orchestra/{d}_RATE" for d in ("PHEN", "NEPI", "EPI", "VASO", "DOPA", "DOBU")]


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        b = r.read()
    if b[:2] == b"\x1f\x8b":
        b = gzip.decompress(b)
    return b


def main():
    os.makedirs(os.path.join(OUT, "tracks"), exist_ok=True)
    log = []
    for name in ("cases", "trks", "labs"):
        b = fetch(f"{API}/{name}")
        path = os.path.join(OUT, f"{name}.csv")
        open(path, "wb").write(b)
        log.append((f"{name}.csv", len(pd.read_csv(io.BytesIO(b))), hashlib.sha256(b).hexdigest()))
    trks = pd.read_csv(os.path.join(OUT, "trks.csv"))
    # Only cases the analysis can use: the fallback cohort's eligibility (a superset of the primary's),
    # in either loss group. Other cases' tracks are never read by the analysis, so this has no effect on results.
    sys.path.insert(0, HERE)
    import h1_vdb_g12 as A
    el = A.eligible_cases(A.Data(OUT), fallback=True)
    ids = set(el[(el.ebv_share >= 0.15) | (el.ebv_share <= 0.05)].caseid.astype(int))
    need = trks[trks.tname.isin(TRACKS) & trks.caseid.astype(int).isin(ids)]
    print(f"cases to fetch: {len(ids)}; track files: {len(need)}", file=sys.stderr)
    for i, r in enumerate(need.itertuples()):
        path = os.path.join(OUT, "tracks", f"{r.tid}.csv.gz")
        if os.path.exists(path):
            continue
        b = fetch(f"{API}/{r.tid}")
        with gzip.open(path, "wb") as f:
            f.write(b)
        if i % 500 == 0:
            print(f"{i} of {len(need)} tracks", file=sys.stderr)
    with open(os.path.join(OUT, "MANIFEST.txt"), "w") as f:
        for name, n, h in log:
            f.write(f"{name}\trows={n}\tsha256={h}\n")
        f.write(f"tracks\tfiles={len(need)}\n")
    print(open(os.path.join(OUT, "MANIFEST.txt")).read())


if __name__ == "__main__":
    main()
