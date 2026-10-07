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
