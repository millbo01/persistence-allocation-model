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
