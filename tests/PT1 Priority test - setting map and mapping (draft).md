# PT1 (and G25): setting map and mapping (DRAFT, 7 October 2026)

**Status:** phase 5 preparation. **No spending data has been opened.**
- **Structure:** documentation runs PT1-S1 and PT1-S2 (raw/), assessed in tests/PT1 Priority test - design note (draft).md.
- **The statutory classification:** PT1-C1b and C1c (GPT, blind, rule-based), frozen as tests/PT1_statutory_classification.csv (176 lines; SHA-256 begins faf45875).
- **Model:** v0.18 as amended (theory/PERSISTENCE_ALLOCATION_MODEL_v0.18.md). The extension layer (nested systems) is **not** used.
- **Decisions for James** are marked **[D1] to [D6]**.

## 1. Setting map

| Item | Content |
|---|---|
| **The system** | One English single-tier council (unitary, metropolitan district or London borough): its general fund, the revenue budget that is not ring-fenced |
| **Whose persistence** | The council's, as a legal body. **Viability** means a lawful balanced budget each year. **Collapse** is a section 114 notice (spending stopped by the chief finance officer). **The route back:** the council itself, or a government-appointed intervention, restores a lawful budget |
| **The record** | The council's statutory core visibly delivered: a lawful budget set, statutory services provided, the council functioning |
| **The governor** | The budget-setting process (members, the section 151 officer, the executive). It acts through **explicit allocation**: budget lines, one way of setting access (v0.18, Section 3) |
| **The resource** | General revenue: council tax plus non-ring-fenced government funding. **One resource,** so the multi-resource problem does not arise (theory/PAM_maths_literature_map.md) |
| **The stores** | Usable reserves (general fund and earmarked) |
| **The scarcity** | The fall in core funding over the window (Core Spending Power and Settlement Funding Assessment, by council and year) against rising demand |
| **Do the model's conditions hold?** | **Yes.** A governor holds a level (a lawful budget and statutory services) by regulating access to one finite resource among parts (service lines) that do not set their own budgets. A shortfall arrives from both sides: falling funding and rising requirement |
| **Confounds the setting produces** | (1) **Ring-fenced and earmarked funding:** schools (Dedicated Schools Grant); public health (ring-fenced grant, 2013-14 to 2019-20); adult social care (Better Care Fund, the improved Better Care Fund from 2017-18, the adult social care council-tax precept from 2016-17). Earmarked money protects a service whatever its rank. (2) **Accounting and definition breaks** (2013-14, 2014-15; RO4 recoding in 2020-21). (3) **Income:** net current expenditure nets out fees and charges, so a service can "lose" net spending by raising charges. (4) **Transfers between lines,** which shift spending without changing service. (5) **Councils as nested systems:** officers and members plan ahead and lobby. A positive H-dynamic result may reflect human anticipation entering the governor (stated in the design note). (6) **Services absent in some councils** (foreshore, port health, airports): zero lines |
| **Contrast setting** (where the model predicts a weaker effect) | **Council-years without real funding scarcity.** Under v0.18 (results R1 and R2), the order of sacrifice is expressed only when the resource falls short: hierarchy is latent in abundance. **The gap between statutory classes should be smaller where funding fell least,** and absent where it rose |
| **Contamination (declared)** | (1) **Claude knows the broad pattern:** discretionary services (culture, libraries, planning) were cut most; social care was relatively protected. **This bears on G25:** reduced weight. (2) **The classifier (GPT) declared similar background knowledge** and disclaimed its use. Each class cites duties. (3) **Claude does not know** whether projected client-group growth predicts protection once statutory class and current demand are held constant (**PT1's question**), nor the shape of that relationship |

## 2. Mapping under v0.18 (Section 8)

1. **Boundary, currency, protected level.**
   - **Boundary:** the council's general fund.
   - **Currency:** pounds of net current expenditure, real terms (CPI, as the official statistics use).
   - **Protected level:** a lawful balanced budget with statutory services delivered.
   - **The viable set:** no section 114 notice.
   - **Outside support:** government intervention (commissioners, capitalisation directions) is **admissible.** It decides collapse against death; no deaths are expected in the window.
2. **Resources.**
   - **General revenue:** one resource; complementarity does not apply.
   - **Carrier:** the budget.
   - **Stores:** usable reserves.
   - **Spill:** not applicable.
3. **The governor and its levels.** It acts through budget lines (explicit allocation). The levels it holds are statutory delivery and budget balance.
4. **Parts: service lines.**
   - **Rank (H-fixed):** the statutory class from the frozen classification: **A before B before C** (the documented access property).
   - **Reference allocation:** each line's real net current expenditure in the base year, per head of its client group.
   - **Support parts and intake:** none mapped. The test reads the order of sacrifice among ordinary parts.
5. **Repair network:** not mapped (not tested).
6. **Links:** none mapped between service lines (not tested).
7. **Nested systems:** none listed. The extension layer is not used.
8. **Modes and gates** (added to the model 7 October 2026): **none claimed.** PT1 does not invoke access-limited load. Any shortfall in a service line is read as supply-limited or requirement-limited.
9. **The clock:** financial years.
10. **Predictions:** Section 3.

**The expected future value (H-dynamic's variable).**
- **What it is:** the **projected growth** of each line's client group over the next five years, from the ONS subnational population projection **published before that year's budget was set.** The rule: the latest edition published before 1 February of the year in which the budget takes effect.
- **Client groups,** fixed now from documentation, not data:
  - adult social care: 65 and over, and 18 to 64;
  - children's social care and children's centres: 0 to 17;
  - statutory concessionary fares: 65 and over (the older people's pass);
  - waste, street cleansing, libraries, culture, sport, parks, regulatory services, planning, highways and other lines: the total population.
  - **[D5]** a household-based group for waste and housing lines, if household projections are used.
- **Current demand:** the same groups, from ONS mid-year estimates.

## 3. Hypotheses (outline for the pre-registration)

- **PT1, primary (fixed against dynamic priority).**
  - **The test:** within a council and year, does a line's projected client-group growth predict how well its spending per head is protected, once the line, the council-year and current client-group growth are held constant?
  - **H-fixed predicts** no effect. **H-dynamic predicts** a positive effect.
- **PT1, secondary (graded against stepped).** If there is an effect, is it **graded** (rising with projected growth) or **stepped** (a threshold)?
  - **A graded effect** with no declared role change earns dynamic priority for this system.
  - **A stepped effect** is compatible with a governor mode.
- **G25 (reduced weight).** Statutory class predicts the order of sacrifice under scarcity: A protected more than B, more than C, within council-years.
- **G25 contrast.** The class gap is larger where the council's real funding fell more (scarcity reveals the order).
- **Strict against shared (secondary, not scored).** Did C lines absorb whole cuts before A lines lost anything (strict), or did all classes lose in proportion (shared)?

## Decided (James, 7 October 2026): D1 to D6, all as recommended

Carried into tests/PT1 Priority test - pre-registration.md.

## 4. Decisions for James

| No. | Decision | Claude's recommendation |
|---|---|---|
| D1 | **Window:** 2013-14 to 2019-20, or 2014-15 to 2019-20 | **2014-15 to 2019-20,** subject to one documentation check that adult social care lines were restructured in 2014-15 (not from data). This also avoids the academies and "services for young people" changes. Six years |
| D2 | **Councils:** single-tier only, with the same code in every year | **Yes.** The Isles of Scilly and the City of London are excluded |
| D3 | **Adult social care,** with its earmarked funding (the improved Better Care Fund from 2017-18; the precept from 2016-17) | **Excluded from the primary analyses; included in a sensitivity analysis.** Earmarked money protects it whatever its rank or projected growth. Projected-growth variation remains from children (0 to 17), concessionary fares (65 and over) and the total population |
| D4 | **Lines in scope** | **Included:** RO2, RO4, RO5 and children's social care lines in RO3. **Excluded:** public health (ring-fenced; its class is an artefact of the 2011 source); RO1 (mostly funded by the Dedicated Schools Grant); RO6 central and overhead lines (a sensitivity analysis keeps the client-facing ones); levies (RO5 226, 244); police and fire; any line not present in every year of the window; any line with zero base-year spending in a council (for that council) |
| D5 | **Client groups** for waste and housing | **Total population** (simpler, one source). Households as a sensitivity analysis only if household projections are documented for the window |
| D6 | **Ambiguous classes** (35 lines) | **Primary:** ambiguous lines excluded from G25. **Sensitivity analyses:** each ambiguous line set to each of its candidates (lowest and highest bounds). PT1's H-dynamic test does not need classes, but uses line fixed effects, so it keeps every line |

**After the decisions:**
1. The pre-registration: outcome measure, models, tests, verdict table, sensitivity analyses, deviations and the decision log with directions.
2. A documentation check for D1.
3. The analysis code, tested on synthetic data.
4. James confirms; it is frozen.
5. The data is downloaded.
