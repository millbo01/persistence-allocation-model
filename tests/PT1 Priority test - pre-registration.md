# PT1, fixed against dynamic priority (with G25): pre-registration (DRAFT for James, 7 October 2026)

Drafted by Claude, 7 October 2026. **Status: draft. Not frozen until James confirms. No spending, population or funding data for this test has been opened.** After freezing, any change is a new, separately logged experiment.

**Sources:**
- **Model:** theory/PERSISTENCE_ALLOCATION_MODEL_v0.18.md, as corrected on 7 October 2026 (access-limited load; "chronic").
- **Setting map and mapping:** tests/PT1 Priority test - setting map and mapping (draft).md. James decided D1 to D6, all as recommended, on 7 October 2026.
- **Design note:** tests/PT1 Priority test - design note (draft).md (H-fixed against H-dynamic; the rescue routes R1 to R3).
- **Structure only:** raw/2026-10-07_gemini_PT1-S1.md and _PT1-S2.md.
- **The statutory classification:** tests/PT1_statutory_classification.csv (176 lines; SHA-256 begins faf45875). Built blind by GPT under a fixed rule (raw/2026-10-07_chatgpt_PT1-C1b.md, _C1c.md).

## 1. Questions and hypotheses

| Code | Role | Statement |
|---|---|---|
| **PT1** | Primary (Tier 1) | Within a council and year, a service line's **projected client-group growth** (published before the budget) predicts how well its real spending per head of client group is protected, once the line, the council-year and realised client-group growth are held constant. **H-fixed:** no effect. **H-dynamic:** a positive effect |
| PT1-S | Secondary (runs only if PT1 finds an effect) | **Graded or stepped:** is the effect linear in projected growth, or a single threshold? |
| **G25** | Primary, **half weight** (contamination) | Statutory class predicts the order of sacrifice: within council-years, A lines are protected more than B, and B more than C |
| G25-C | Secondary, half weight | **Scarcity reveals the order:** the gap between A and C is larger where the council's real funding fell more |
| SS | Descriptive, not scored | **Strict or shared:** did C lines absorb whole cuts before A lines lost anything? |

**Rescue routes declared now** (design note, Section 1). Under H-fixed, an apparent reversal is allowed only through:
- **R1, a role change:** none declared. No service line is mapped as support for the top or as the intake.
- **R2, local autoregulation:** none declared.
- **R3, a governor mode:** **none declared,** consistent with mapping step 8 (no modes or gates claimed).

**So any PT1 effect counts against H-fixed for this system,** whatever its shape. PT1-S says only which alternative fits better.

**Interpretation, stated in advance.** Councils are governed by people (nested systems) who plan ahead. A positive PT1 result would show anticipation entering this governor. That earns dynamic priority **for institutions of this kind,** not for biology.

## 2. Data (fixed now; downloaded only after freezing)

| Item | Source | Use |
|---|---|---|
| Spending by service line | MHCLG Revenue Outturn, individual local authority data, **final outturn**, 2014-15 to 2019-20 (RO2, RO3, RO4, RO5; RO6 in a sensitivity analysis) | **Net current expenditure** per line, council and year |
| Prices | ONS consumer prices index (CPI), annual average for each financial year (April to March), from the published monthly index | Real terms, 2014-15 prices |
| Current population | ONS mid-year population estimates by single year of age and local authority, mid-2014 to mid-2019 (mid-year t for financial year t to t+1) | Client-group populations; realised growth |
| Projected population | ONS subnational population projections, **the latest edition published before 1 February of the calendar year in which the financial year begins** | Projected five-year growth of each client group |
| Funding | MHCLG Core Spending Power per council, 2015-16 to 2019-20 (final settlement tables) | Scarcity, for G25-C |

**Which projection applies to which budget** (by publication date; dates from PT1-S2, plus one to confirm):
- 2014-15 budget (set before February 2014): **2011-based interim** (published autumn 2012).
- 2015-16 and 2016-17: **2012-based** (publication date not stated in the documentation; **to confirm from the ONS release page** before data is opened, as documentation).
- 2017-18 and 2018-19: **2014-based** (published May 2016).
- 2019-20: **2016-based** (published 24 May 2018).

If the confirmed 2012-based date is later than 1 February 2015, the rule assigns the 2011-based interim edition to the 2015-16 budget instead. **The rule, not a choice, decides.**

## 3. Councils, lines and client groups

**Councils (D2):**
- Unitary authorities, metropolitan districts and London boroughs, excluding the City of London and the Isles of Scilly.
- **The same ONS code in every year from 2014-15 to 2019-20** in the spending data, which removes reorganised councils mechanically.
- **A council missing a final outturn return** in any year is excluded, and the number is reported.

**Lines (D4):**
- **In scope:** the classified lines in RO2 (highways and transport), RO4 (housing), RO5 (cultural, environmental, regulatory, planning) and RO3 children's social care (lines 10 to 27; the total line 30 is excluded).
- **Excluded:**
  - public health (RO3 61 to 90);
  - adult social care (RO3 lines 8, 9 and 32 to 60) from the primary analyses (D3);
  - RO1;
  - RO6 (a sensitivity analysis keeps the client-facing lines 430, 441, 442, 460 and 475);
  - levies (RO5 226, 244);
  - police and fire.
- **Matching across years, by name:**
  - A line is matched across years by **its normalised name within its form** (lower case, punctuation and spacing removed). Codes changed over the period, for example the RO4 temporary accommodation lines.
  - **The classification attaches to the line name** in the 2025-26 guidance.
  - **A line whose normalised name is not found in all six years is excluded.** The number is reported, with the names.
- **Series rules** (per council and line):
  - excluded if net current expenditure is zero or negative in any year (income-generating lines such as parking);
  - excluded if mean real net current expenditure over the window is below £100,000 (2014-15 prices), to avoid noise from tiny lines.

**Client groups (D5), fixed now:**

| Lines | Client group |
|---|---|
| RO3 children's social care (10 to 27) | Aged 0 to 17 |
| RO2 71 statutory concessionary fares | Aged 65 and over |
| All other in-scope lines (RO2 except 71; RO4; RO5) | Total population |
| Adult social care total (sensitivity only) | Aged 18 and over |

## 4. Measures

For council $c$, line $l$, financial year $t$ (2015-16 to 2019-20, each against the year before):

- **Outcome (protection):**
$$y_{clt}=\ln\frac{E_{clt}/P_{clt}}{E_{cl,t-1}/P_{cl,t-1}}$$
  - $E$ is real net current expenditure;
  - $P$ is the client-group population (mid-year estimate).
  - The outcome is **winsorised** at the 1st and 99th percentiles of the pooled sample.
- **Realised client growth:** $g^{\text{real}}_{clt}=\ln(P_{clt}/P_{cl,t-1})$.
- **Projected client growth (H-dynamic's variable):**
$$g^{\text{proj}}_{clt}=\ln\frac{\hat P_{cl}(\tau+5)}{\hat P_{cl}(\tau)}$$
  - $\hat P$ comes from the projection edition assigned to year $t$'s budget (Section 2);
  - $\tau$ is the calendar year in which financial year $t$ begins.
- **Statutory class:** A, B or C from the classification. **Ambiguous lines** are excluded from G25 in the primary analysis (D6).
- **Scarcity** (for G25-C): the change in the council's real Core Spending Power per head (total population) from 2015-16 to 2019-20.

## 5. Models and tests

All standard errors are **clustered by council.** Tests are one-sided at α = 0.05 unless stated.

**PT1 (primary):**
$$y_{clt}=\beta\,g^{\text{proj}}_{clt}+\gamma\,g^{\text{real}}_{clt}+\alpha_l+\alpha_{ct}+\varepsilon_{clt}$$
- $\alpha_l$ are line fixed effects. They absorb each line's average trend, and with it its statutory class.
- $\alpha_{ct}$ are council-by-year fixed effects. They absorb each council's overall cut in each year.
- **The test:** $\beta>0$.

**PT1-S (secondary, only if PT1 finds $\beta>0$):**
- **The comparison:** the linear model above against a **single-threshold model**, in which $g^{\text{proj}}$ is replaced by an indicator that it exceeds a threshold. The threshold is chosen from the nine deciles of $g^{\text{proj}}$.
- **Both are compared by BIC,** counting the threshold as one extra parameter.
- **The reading:**
  - **graded** if the linear model's BIC is lower by more than 2;
  - **stepped** if the threshold model's is lower by more than 2;
  - **indeterminate** otherwise.

**G25 (primary, half weight):**
$$y_{clt}=\delta_A\,[\text{A}]+\delta_B\,[\text{B}]+\gamma\,g^{\text{real}}_{clt}+\alpha_{ct}+\varepsilon_{clt}$$
- C is the reference class; ambiguous lines are excluded.
- **The tests:** $\delta_A>0$ (A protected more than C), $\delta_B>0$, and $\delta_A-\delta_B>0$.

**G25-C (secondary, half weight):** the G25 model with an interaction between $[\text{A}]$ and scarcity.
- **The test:** the A-against-C gap widens where funding fell more. The interaction is positive when scarcity is coded so that a larger value means a deeper fall.

**SS (descriptive):**
- **The council-years counted:** those in which in-scope real spending fell.
- **What is reported:** the share in which any A line's real spending fell while C lines kept more than half of their base-year spending.
- **How to read it:** under strict priority the share is near zero; under shared cutting it is substantial. No verdict.

## 6. Verdict table

**PT1** (the verdict for H-fixed against H-dynamic in this system). The smallest effect that matters is set now: $\beta^{\ast}=0.25$. That means a 10% higher projected five-year client growth goes with 2.5 percentage points more protection per year.

| Result | Verdict |
|---|---|
| $\beta>0$ (one-sided p < 0.05) | **H-fixed fails in this system; dynamic priority earned for institutions of this kind.** PT1-S then reports graded, stepped or indeterminate |
| $\beta$ not significant, and the upper 95% confidence bound below 0.25 | **H-fixed supported:** no meaningful anticipation |
| $\beta$ not significant, upper bound at or above 0.25 | **Inconclusive** (not enough precision) |
| $\beta<0$ with two-sided p < 0.05 | **Contrary to H-dynamic** (protection moves away from growing groups). Logged as found |

**G25** (half weight):

| Result | Verdict |
|---|---|
| $\delta_A>0$ (p < 0.05), with point estimates ordered $\delta_A\ge\delta_B\ge0$ | **Supported** |
| $\delta_A>0$ (p < 0.05), but the order is violated | **Partly supported** |
| $\delta_A$ not significantly greater than 0 | **Fails** |
| $\delta_A<0$ with two-sided p < 0.05 | **Contradicted** |

**G25-C:** supported if the interaction test passes; not supported otherwise. Half weight.

## 7. Sensitivity analyses (reported; not part of the verdicts)

1. **Adult social care included** (the total line, client group 18 and over).
2. **Long difference:** one observation per council and line, from 2014-15 to 2019-20. The projection is the one assigned to the 2014-15 budget; growth is realised over the window.
3. **Ambiguous lines in G25,** set to their lowest and their highest candidate class.
4. **RO6 client-facing lines included** (430, 441, 442, 460, 475).
5. **Ten-year projected growth** in place of five-year.
6. **No winsorising.**
7. **London boroughs excluded.**
8. **The £100,000 minimum** replaced by £50,000 and by £250,000.

## 8. Contamination and weights

- **G25 carries half weight.** Claude knows the broad pattern (discretionary services were cut most; social care was relatively protected). The classifier declared similar background knowledge and disclaimed using it.
- **PT1 carries full weight.** Claude does not know whether projected client growth predicts protection once line, council-year and realised growth are held constant.
- **The classification was produced blind,** before any data, by a model applying a fixed rule with citations.

## 9. Procedure

**Before any data is opened:**
1. **James confirms;** the pre-registration is frozen, and its SHA is recorded in CONTROL.md.
2. **The 2012-based projection's publication date** is confirmed from the ONS release page (documentation) and recorded.
3. **Claude writes the analysis code** (tests/scripts/pt1_councils.py) and tests it on synthetic data built to give each verdict. It is committed with its SHA.

**Opening the data:**
4. **The data is downloaded** into data/ (git-ignored), with sources and checksums in data/README.md.
5. **Structure inspection.** The spreadsheet layouts (sheet names, header rows, line labels, council codes) are not documented, so a structure-only script prints headers and labels, **never values**, to configure the parser. Every parser setting is logged as an implementation note **before** the analysis runs.
6. **A counting step** reports, with no outcome values:
   - councils in and out (and why);
   - lines matched and excluded (with names);
   - series excluded by the positivity and £100,000 rules.

**Running:**
7. **The analysis runs once,** unchanged. Outputs go to tests/results/PT1/ (README.md and summary.json).
8. **Deviations** (a bug, a missing field, a changed name) are logged with reasons, never silently fixed.

**After the run:**
9. **Computation replicated by a second model** from the same files and this pre-registration.
10. **Blind adjudication by GPT** (a fresh chat) against Section 6. Its verdict is recorded verbatim.

## 10. Decision log (methodology choices, with the direction each pushes)

| No. | Choice | Direction |
|---|---|---|
| 1 | Window 2014-15 to 2019-20 (D1) | Neutral: avoids definition breaks and the pandemic |
| 2 | Single-tier councils with stable codes (D2) | Neutral: fewer councils, cleaner responsibilities |
| 3 | Adult social care excluded from the primary analyses (D3) | **Harder for G25:** it removes the largest A-class service, which is expected to look protected. **Neutral for PT1:** earmarked funding would otherwise confound it |
| 4 | Public health excluded (ring-fenced; its class is an artefact of the source) | Neutral |
| 5 | Lines matched by name; lines missing in any year excluded | Neutral: some lines lost |
| 6 | Line and council-year fixed effects in PT1 | **Harder for H-dynamic:** only variation in projected growth within line and council-year counts |
| 7 | Realised growth controlled | **Harder for H-dynamic:** anticipation must show beyond what actually happened |
| 8 | No modes or role changes declared (R1 to R3 closed) | **Harder for H-fixed:** any effect counts against it |
| 9 | Smallest meaningful effect $\beta^\ast=0.25$, which allows "H-fixed supported" from a null | **Easier for H-fixed** (a null can support it). Limited by requiring the confidence bound below $\beta^\ast$; otherwise inconclusive |
| 10 | One-sided tests | **Favours detecting the predicted direction.** "Contrary" uses two-sided tests |
| 11 | Ambiguous lines excluded from primary G25 (D6) | Neutral; bounded by sensitivity 3 |
| 12 | Winsorising at 1 and 99 per cent | Neutral; sensitivity 6 |
| 13 | Positivity and £100,000 series rules | Neutral; sensitivity 8 |
| 14 | Structure inspection of spreadsheets after freezing (no values) | **Procedural:** parser settings logged before the run |
