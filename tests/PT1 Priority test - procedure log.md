# PT1: procedure log (after freezing)

**Pre-registration:** tests/PT1 Priority test - pre-registration.md (frozen 7 October 2026, commit bbe553b, SHA-256 begins a4aab81d).

## Step 2: projection publication dates confirmed (7 October 2026; documentation, before any data)

| Edition | Published | Source |
|---|---|---|
| 2011-based interim | 28 September 2012 | GLA Intelligence Unit briefing, Update 23-2012 (data.london.gov.uk) |
| 2012-based | 29 May 2014 | ONS bulletin, "Subnational population projections for England: 2012-based" (ons.gov.uk/.../subnationalpopulationprojectionsforengland/2014-05-29) |
| 2014-based | May 2016 | PT1-S2 |
| 2016-based | 24 May 2018 | PT1-S2 |

**The rule's assignment** (the latest edition published before 1 February of the calendar year in which the financial year begins):

| Budget year | Edition |
|---|---|
| 2014-15 | 2011-based interim |
| 2015-16 | 2012-based (29 May 2014 is before 1 February 2015) |
| 2016-17 | 2012-based |
| 2017-18 | 2014-based |
| 2018-19 | 2014-based |
| 2019-20 | 2016-based |

**No change from the expected assignment.**

## Step 3: analysis code tested on synthetic data (7 October 2026)

- **Code:** tests/scripts/pt1_councils.py (SHA-256 begins 995abfc5).
- **Synthetic checks:** tests/scripts/pt1_synthetic.py. Results in tests/results/PT1-synthetic/README.md: 6 of 7 scenarios as built. S7 was a chance false positive at seed 1, and correct at seeds 2 to 4.
- **Two bugs fixed before data,** one of them adding the duplicate-name rule (an implementation note).
- **Limitation recorded:** the frozen G25 test has no smallest meaningful effect.

**Next:** step 4, download (public data, Open Government Licence), then step 5, the structure-only inspection.

## Step 4: download (7 October 2026)

**All files downloaded into data/pt1/** (git-ignored). Sources and checksums are in data/README.md and data/pt1/MANIFEST.txt. **No file has been opened for values.** Only file types, archive listings and the CPI file's metadata header were checked.

**Source choices** (fixed now, before the structure inspection):
1. **Spending:** the latest revised final-outturn files on each year's GOV.UK page. 2014-15: RO2, RO4, RO5 and RO6 as xls, and RO3 as the 2014-15 revision (xlsx). 2015-16 and 2016-17: xlsx. 2017-18 to 2019-20: ods.
2. **Mid-year estimates: the 2020 vintage** (mid-2001 to mid-2019 detailed time series, MYEB), **not** the later revision rebased on the 2021 Census. This is the series contemporaneous with the window. Within it, **the file on 2019 geography** (MYEB2 "(2019)"; the "(2019_geog20)" variant is on 2020 boundaries). The single year of age and the population come from the MYEB2 population column. **Direction: neutral** (both vintages are official; the contemporaneous one matches what budget-setters saw).
3. **Projections:** persons by single year of age from each edition: 2012, 2014 and 2016 (ONS z1 files), and the interim 2011-based edition (from the UK Government Web Archive copy of the ONS release page, as no current ONS page holds it).
4. **Funding:** Core Spending Power from the 2019-20 final settlement tables, which give 2015-16 to 2019-20 on a comparable basis.

**Next:** step 5, the structure-only inspection (sheet names, header rows and labels; no values), then the parser, with its settings logged here before the counting step.

## Step 5: structure inspection and parser settings (7 October 2026; logged before the counting step)

**Inspection** (no values printed):
- **Scripts:** tests/scripts/pt1_structure.py (text cells only, numbers masked) and tests/scripts/pt1_parse.py --structure.
- **Outputs:** data/pt1/structure/ (git-ignored).

**What the inspection found:**
- **RO files:**
  - one data sheet per form and year (2014-15: three sheets per form);
  - a header row whose first cell is "E-code" (row 9 or 12 in 2014-15, row 4 in 2017-18, row 6 otherwise);
  - line names in the nearest row above the header that holds names (group banners in "***" skipped);
  - one block of columns per line, with net current expenditure in the column headed "Net Current Expenditure" (in 2014-15, on the third sheet);
  - council rows identified by an E-code in column 0;
  - an ONS code column and a Class column.
- **Class codes:** L, MD, UA, SD, SC, O. "L" (London) is mapped to LB.
- **Mid-year estimates (MYEB2, 2019 geography):** one row per council, single year of age (0 to 90, 90 = 90 and over) and sex, with population_2001 to population_2019.
- **Projections:**
  - 2012, 2014 and 2016 editions: persons CSVs, single year of age plus "90 and over" and "All ages", with year columns;
  - interim 2011-based: an xls sheet "Population - persons", header row "Code, Area, Age group", years 2011 to 2021.
- **Core Spending Power:** sheet "input" in the 2019-20 summary workbook, with ons_code and csp_2015 to csp_2019 in £ millions.

**Parser settings (implementation notes, fixed now):**
1. **Net current expenditure** is the column headed "Net Current Expenditure" in each line's block. Non-numeric cells become missing.
2. **Population groups** are summed from single years of age, both sexes: all ages, 0 to 17, 65 and over, 18 and over. "90 and over" is age 90; the "All ages" rows are not used. The same applies to projections (persons).
3. **CPI** is the mean of the 12 monthly D7BT values from April to March for each financial year.
4. **Core Spending Power** is converted from £ millions to £ thousands (×1000). The analysis uses ratios, so units do not affect results.

**Deviations from the pre-registration (name matching, Section 3).** These are of the kind the pre-registration anticipates ("a changed name"), and were decided from names only, before any values.

- **D-1. Name crosswalk.** 21 data names in the window years differ from the 2025-26 guidance names that the classification uses. They are mapped by tests/PT1_line_name_crosswalk.csv, with a reason for each.
  - **The differences:** abbreviations ("other LA roads"); singular and plural ("Library service"); earlier names ("Open spaces", "Sports and recreation facilities"); and the RO4 temporary accommodation and homelessness lines, which are finer in the window than in 2025-26.
  - **Without the crosswalk,** the frozen exact-name rule would drop core lines (libraries, parks, sports facilities, most temporary accommodation and homelessness) for a purely editorial reason.
  - **Direction: neutral.** Names only, no values.
- **D-2. Many-to-one lines summed.** Where the crosswalk maps several window-year lines to one 2025-26 line, they are summed into that line for each council and year (missing only if every component is missing). Examples: leased by the authority + leased by registered social landlords → line 81; homelessness administration + prevention → line 87.
  - **This follows the official 2020-21 recoding,** which combined these lines (PT1-S1).
  - **Without it,** the duplicate-name rule would drop them.
  - **Direction: neutral.**
- **D-3. A labelling error in the source** (RO5, 2019-20). Two adjacent blocks are both labelled "Sports development and community recreation". In every other year, the second position is "Sports and recreation facilities, including golf courses". The second block is relabelled by position.
  - **Without the fix,** the duplicate-name rule would drop both sports lines in every council.
  - **Direction: neutral.**
- **D-4 (a limitation, no intervention).** From 2019-20, "Allotments" is reported separately from "Parks & Open Spaces". Both open-spaces names map to line 131. The 2019-only allotments line drops out under the all-years rule. If allotments sat inside "Open spaces" before 2019-20, line 131 has a small definitional fall in 2019-20. **Not corrected; reported.**

**Known risk, to be checked by count in step 6:**
- **The cause:** the projections of 2011 and 2012 use the council codes of their time. A council whose code changed before 2014 (stable within the spending window) may lack early projections under its later code.
- **Consequence:** its 2014-15 to 2016-17 projected growth is then missing, and those rows drop out of PT1.
- **What happens next:** the counting step reports the number. **If it is material, a documented code-history mapping is a candidate deviation for James to decide** before the run.

**Next:** step 6, build the tidy files and run the counting step (counts only, no outcome values).

## Step 6: tidy files built and counting step run (7 October 2026)

**Tidy files:** data/pt1/tidy/ (checksums in data/pt1/tidy/MANIFEST.txt), from tests/scripts/pt1_parse.py --build. Row counts: spend 491,518; pop 12,680; proj 117,948; csp 1,960; cpi 38.

**Counts** (tests/scripts/pt1_count.py; tests/results/PT1/counts.json; no outcome values):

**Councils:**
- **121 kept:** 32 London boroughs, 36 metropolitan districts, 53 unitaries. These are single-tier councils with the same code in all six years. The City of London and the Isles of Scilly are excluded.

**Lines:**
- **95 matched in all six years.**
- **Dropped as not present in all years:** bus lane enforcement (absent in 2014-15) and allotments (2019-20 only, D-4).

**Series:**
- 11,495 council-line series in total.
- **Dropped:**
  - 6,345 with zero or negative spending in some year (lines a council does not run, and income-generating lines such as parking);
  - 443 below the £100,000 mean;
  - 0 for duplicate names;
  - 0 incomplete.
- **Kept: 4,707.**
- **By class:** A 1,334; B 1,214; C 1,233; ambiguous 926.

**Rows:**
- 23,535 with an outcome.
- **Usable for PT1:** 23,373.
- **Usable for G25:** 18,905 (ambiguous lines excluded).

**Missing projections:**
- **243 rows,** all for 2014-15 to 2016-17, in two councils whose codes changed before the window: Northumberland (E06000057) and Gateshead (E08000037).
- **That is 1.0% of PT1 rows. Not material,** so no code-history deviation is proposed; the rows drop out as the frozen code handles missing values.

**Next:** step 7, the single analysis run (tests/scripts/pt1_councils.py, unchanged; SHA-256 begins 995abfc5).

## Step 7, attempt 1: the run stopped with an error before any result (7 October 2026)

- **Command:** `python tests/scripts/pt1_councils.py --data data/pt1/tidy --out tests/results/PT1` (code unchanged, SHA-256 begins 995abfc5).
- **What happened:** the script stopped in G25-C, when it reshaped the Core Spending Power table: "Index contains duplicate entries, cannot reshape" (tests/results/PT1/run.log). **Nothing was printed before the error and no summary file was written. No result has been seen.**
- **Cause:** the Core Spending Power "input" sheet gives one ONS code, E31000040, to two bodies: Greater Manchester Fire and the Greater Manchester Combined Authority (which took over fire functions in 2017). Neither is a single-tier council or in the panel (all 121 panel councils have E06, E08 or E09 codes). Checked by code and name only, numbers masked.
- **Proposed D-5 (awaiting James):** the parser keeps only E06, E08 and E09 codes in the Core Spending Power table (tests/scripts/pt1_parse.py, build_csp). The analysis code stays unchanged. No council in scope is affected. **Direction: neutral.** After the fix, data/pt1/tidy/csp.csv is rebuilt and its checksum replaced in the manifest, coverage of the 121 councils is checked, and the run is repeated once. Because attempt 1 produced no result, the repeat is not a choice among results.

**D-5 approved by James and applied (7 October 2026).** data/pt1/tidy/csp.csv rebuilt: 635 rows, 127 codes, no duplicates. All 121 panel councils present, with no missing spending power cells. New checksum begins ba78a1e9; the other four tidy files are unchanged. Analysis code unchanged (995abfc5).

## Step 7, attempt 2: the single run (7 October 2026)

- **Command and code:** as attempt 1 (SHA-256 995abfc5, unchanged), on data/pt1/tidy after D-5. Exit 0. Output: tests/results/PT1/summary.json, run.log; results written up in tests/results/PT1/README.md.
- **Computed verdicts (not adjudicated):** PT1 inconclusive (insufficient precision); PT1-S not run; G25 supported (half weight); G25-C not supported; SS descriptive.
- **One warning** ("divide by zero encountered in log", in G25-C): traced by a diagnostic run (output to a scratch folder, not kept) to zero Core Spending Power for the Dorset reorganisation codes, none of which is in the panel. It does not reach any estimate.

**Next:** step 9, computation replicated by a second model (prompt tests/prompts/PT1-R1.txt).

## Step 9: computation replicated by a second model (7 October 2026)

- **GPT's audit and script:** raw/2026-10-07_chatgpt_PT1-R1.md; script extracted unedited to tests/scripts/pt1_check.py and run on the same tidy files (exit 0).
- **Result: replicated exactly.** Same counts at every step; PT1, G25 and G25-C estimates, standard errors, p values and verdicts identical to at least eight digits; every shared sensitivity identical. Only SS (descriptive) differs, because GPT keeps ambiguous lines in the spending total (320 against 349 council-years; 96.9% against 96.8%).
- **Audit findings checked against the data;** none changes a scored estimate (tests/results/PT1-R1/README.md). One source check added: the population files have no missing single-age cells.

**Next:** step 10, blind adjudication (prompt tests/prompts/PT1-ADJ1.txt, fresh GPT chat).

## Step 10: blind adjudication (7 October 2026)

- **GPT, fresh chat** (raw/2026-10-07_chatgpt_PT1-ADJ1.md). **Verdicts, accepted as given:** PT1 Inconclusive (full weight); G25 Supported (half weight); G25-C Not supported (half weight). PT1-S correctly not run. SS descriptive. No faults; none of D-1 to D-5, the missing projections or G1 to G6 changes a verdict.
- **Recorded** in v0.18 Sections 10 to 13 and in CONTROL. **PT1 closed.**
