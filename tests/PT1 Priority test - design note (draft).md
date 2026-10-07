# PT1: fixed against dynamic priority. Design note (DRAFT, 7 October 2026)

**Status:** step 1 of the test design: what would discriminate, and where to look.
- **No data has been opened,** and no outcome literature for any candidate was searched. Candidates are judged by their structure only. Claude's existing knowledge of each is declared.
- **Model:** v0.18 (Section 4, item 2; Section 12, Tier 1).
- **Next after James's choice:** a structure-only documentation run by another model, then the setting map, the mapping and the pre-registration, as for H1.

## 1. The two hypotheses, stated from v0.18

**H-fixed (the current engine reading).**
- For each resource r, the order of sacrifice πᵣ is fixed at mapping, from documented properties of access.
- **An apparent reversal is allowed only through routes the model already contains, and each must be declared at mapping:**
  - **R1, role change:** a part becomes support for the top (the top now depends on its output), or becomes the intake (it now has something to take in);
  - **R2, local autoregulation:** a part's access rises with its own current work or state;
  - **R3, a governor mode:** a signal selects a different governor with its own fixed order (open, Tier 2). It gives a **small number of discrete orders,** switched at a threshold of the signal.

**H-dynamic (v0.16's claim, kept flagged).** The order follows each part's current marginal value to persistence, **including its expected future value.**

## 2. What would discriminate

**Perplexity's conditions.** A discriminating case needs all four:
1. the same part changes its order of protection;
2. the change is predicted from independently measured state, demand, dependency or horizon;
3. fixed rank plus reassignment predicts it wrongly;
4. the prediction is made before the outcome is seen.

The cleanest version manipulates **the expected next task** while holding the parts and recent losses constant.

**v0.18 adds two requirements:**
- **Same resource, same time:** two recipients compete for one scarce resource at once, so serving one deprives the other (F2).
- **Every rescue route is declared before outcomes:** R1 to R3 are listed at mapping. A reversal explained afterwards by an undeclared role change or mode counts as **fitted,** not as support for H-fixed.

**The core contrast.** Hold the two recipients, their roles and their current work matched. Vary only **the expected future value** of one of them.
- **H-fixed predicts** no change in order (R1 and R2 are excluded by the matching).
- **H-dynamic predicts** a shift towards the part with the higher expected future value.

**A sharper secondary contrast: modes against a continuous rule.** If the expected future value can be varied in **several steps**:
- **R3 (modes)** predicts a **stepped** response: a few discrete orders, switching at a threshold;
- **H-dynamic** predicts a **graded** response that rises with expected value.

So a graded response that tracks expected value, with no declared role change, is the result that would earn dynamic priority. A null or a stepped response keeps H-fixed (with modes).

**What would not discriminate:**
- **Root against shoot in plants** (shade against drought). The organ taking in the limiting resource gains, but that is R1 (it becomes the intake for the scarce resource), so both hypotheses predict the same.
- **Skin in heat against haemorrhage.** One part, not two competing (James's correction, F2).
- **Photoperiod switching** (day length setting reproduction against immune allocation). v0.17 already names day length as a mode selector (R3), so a single switch does not discriminate. A graded photoperiod series might.

## 3. Candidate settings (structure only)

| No. | Setting | Two recipients, one resource | How expected future value varies | Data | Claude's prior knowledge (declared) | Assessment |
|---|---|---|---|---|---|---|
| 1 | **English local authorities under austerity, 2010 to 2020** | Service lines competing for the same general revenue (adult social care, children's services, libraries, highways, planning, culture and others) | Projected growth in each service's client group, from population projections published **before** the budgets were set (for example, older people for adult social care) | Revenue outturn by service, by council, by year (about 300 councils over 10 years, public); official subnational population projections (public) | Knows the broad pattern: discretionary services were cut most, social care was protected. **Does not know** whether projected future demand predicts protection once statutory status and current demand are held constant | **Recommended.** Large and public, outside physiology, with real competition for one resource. The key covariate is fixed independently and in advance. Confounds: ring-fenced grants, service transfers, accounting changes |
| 2 | **Graded photoperiod experiments** (small mammals; reproduction against immune or somatic allocation under food restriction) | Reproductive against somatic tissue, competing for energy | Day length in several steps (the expected season) | Published experiments; raw data rarely available | Knows the photoperiod-immunity literature in outline (the winter immunoenhancement hypothesis) | Possible secondary. **Graded-against-stepped is testable only if graded series exist.** Data access is uncertain |
| 3 | **Designed systems with written priority rules** (grid underfrequency load shedding; hospital surge plans; operating-system memory reclaim) | Loads, patients or processes competing for supply, beds or memory | Documented conditions (depth and duration of the shortfall) | Rules are public; event data are mixed | Knows that grid procedures allow priority to depend on depth and duration | **Weak as a test of the model:** it measures what designers wrote. Useful as a scope illustration only |
| 4 | **Migratory birds** (flight muscle against gut, before and during migration) | Tissue protein and energy | The phase of migration | Published studies | Knows the gut and flight-muscle changes in outline | **Not discriminating:** a fixed phase programme (R3) explains it (Perplexity's own caveat) |

## 4. Recommendation

**Candidate 1, English local authorities,** as PT1. The contrast, before mapping:
- **Recipients:** service lines within each council.
- **Resource:** general revenue spending (real terms, per head of the relevant population).
- **Scarcity:** the austerity years, when councils' core funding fell.
- **The order of sacrifice:** which services lost access first and most.
- **Held constant (the H-fixed covariates, fixed at mapping):**
  - statutory against discretionary status: the documented access property, which is the rank under H-fixed;
  - current demand;
  - ring-fenced status.
- **The H-dynamic variable:** projected growth in each service's client group, from projections available before the budgets.
  - **H-fixed predicts** no effect of projected growth once the covariates are held.
  - **H-dynamic predicts** that services facing higher projected demand are protected more.
- **Graded or stepped:** projected growth varies continuously across councils and services, so a graded relationship can be told from a threshold.

**Why it suits the programme:**
- It is institutional, which is the model's origin.
- It uses public data and a large sample.
- It **also carries G25.** Statutory status is an access property documented in advance, and it should predict the order of sacrifice. **Claude's prior knowledge of that pattern is strong,** so G25 would be reported at reduced weight in this dataset.

**Risks, stated now:**
- **Councils are governed by people,** nested systems who plan ahead. A positive result may show human anticipation entering the institution's governor. Under v0.18 that is still H-dynamic for this system, and it would earn the mechanism for institutions, not necessarily for biology.
- **Projected and current demand are correlated.** The test needs enough independent variation; the documentation run should report what is available.
- **Accounting breaks** (the public-health transfer in 2013; the Better Care Fund) must be handled by rule, fixed before data.

## Decided (James, 7 October 2026)

- **Setting:** candidate 1, English local authorities.
- **G25:** in the same dataset, at reduced weight (contamination declared).
- **Next:** documentation prompt PT1-S1 (tests/prompts/PT1-S1.txt).

## 5. Decision for James

1. **Which setting:** candidate 1 (councils, recommended), candidate 2 (graded photoperiod, if data exist), or both in sequence?
2. **G25 in the same dataset** at reduced weight (contamination declared), or a separate, cleaner setting for G25 later?

**After the choice:**
1. The structure-only documentation prompt for another model (what is recorded, at what level, from when, with no values).
2. Then the setting map and the mapping.
3. Then the pre-registration, with every rescue route (R1 to R3) declared.

## PT1-S1 assessment (7 October 2026)

**Stored:** raw/2026-10-07_gemini_PT1-S1.md (SHA-256 begins 5d0150bf).

**Format held.**
- No figures, trends or comparisons appear anywhere.
- **Minor breach of the "no studies" rule,** as in H1. The works-cited list includes titles of analytical pieces: a think-tank report on children in care, a university report, an academic paper, a council audit report and a trade-press article. No findings are given. Logged.

**What it establishes:**
1. **Spending:** the Revenue Outturn suite (RO1 education; RO2 highways and transport; RO3 adult social care and public health; children's social care separate; RO4 housing, excluding the Housing Revenue Account; RO5 cultural, environmental, regulatory and planning; RO6 protective, central and other) and the Revenue Account budget returns, from MHCLG, in ODS and Excel.
   - **Measures:** gross expenditure, income, net current expenditure, and total service expenditure (net of service-specific income).
   - **No recommended measure** for comparing services over time.
2. **Documented breaks:**
   - **2013-14:** public health moves to councils (ring-fenced grant, new RO3 lines); business rates retention begins; police funding is separated.
   - **2014-15:** academies leave RO1; "services to young people" move from education to children's social care.
   - **2020-21:** the temporary-accommodation lines in RO4 are recoded.
   - **The returns warn** that pre-2013-14 data are not reliably comparable with later years.
3. **Funding:** Core Spending Power, Settlement Funding Assessment, Revenue Support Grant and Baseline Funding Level are defined (from current notes). Their availability by year for 2008-09 to 2020-21 is not stated. **CPI** is used for real terms.
4. **Projections:** ONS subnational population projections exist for every edition from 2006-based to 2018-based, at council level, by single year of age and sex, over 25 years, with past editions kept. **Publication dates are stated only for the 2018-based edition** (24 March 2020).
5. **Demand:**
   - **Children in need and looked after** (DfE): editions documented for 2012-13 to 2018-19.
   - **Homelessness:** a break in April 2018 (P1E replaced by H-CLIC).
   - **Adult social care:** only the 2023-24 break (SALT to client-level data) is documented. **The pre-2014-15 collection (RAP) and the start of SALT were not covered.**
   - **Library and highways demand:** not stated.
6. **Statutory duties:** DCLG's "Review of statutory duties placed on local government" (30 June 2011, updated 2018) groups duties by government department. **No official mapping from duties to spending lines exists, and no official statutory or discretionary classification of services.**

**What this means for the design:**
- **The H-fixed covariate must be built.** Statutory status, the documented access property and the rank under H-fixed, has no official mapping to spending lines. It must be constructed from the 2011 review by a rule fixed before any spending data is opened, ideally by another model, blind to outcomes.
  - **For G25** this matters doubly: Claude's prior knowledge of which services were cut makes a Claude-built classification suspect.
- **The window should start in 2013-14** (the comparability break, public health), or treat the 2013-14 and 2014-15 breaks by rule. **Proposed:** 2013-14 to 2019-20 (seven years, before the pandemic), with lines defined consistently across those years.
- **Projection publication dates are needed** to establish what was available before each budget. **Gaps to fill:**
  - projection publication dates;
  - year-by-year availability of the RO data from 2013-14;
  - adult social care demand series before SALT;
  - library and highways demand;
  - which services each council type is responsible for in two-tier areas;
  - reorganisations from 2013 to 2020.

**Next:**
1. A short second documentation run (PT1-S2) on those gaps.
2. A separate blind classification prompt: map the 2011 statutory-duties review to RO service lines by a fixed rule, with no spending data and no outcome knowledge.

## Decided (James, 7 October 2026): a secondary question, strict or shared

**The question.** Under the funding squeeze, did lower-priority services absorb whole cuts first (strict priority, the reduced form), or did all services lose in proportion, with weights (shared)?
- **Status:** a secondary question in the pre-registration. It does not enter the PT1 verdict.
- **Why it matters:** the same question applies to repair (results flag 5).
- **The resource:** PT1 has one scarce resource (general revenue), so the multi-resource problem does not arise (theory/PAM_maths_literature_map.md).

## PT1-S2 assessment (7 October 2026)

**Stored:** raw/2026-10-07_gemini_PT1-S2.md (SHA-256 begins d70dd4c7).

**Format.**
- No figures, trends or comparisons appear.
- **Breach:** the source list includes councils' own documents (reorganisation proposals, budget books, finance strategies, a transport plan), which the prompt forbade. Gemini's self-check wrongly says none were used. They are cited only for which tier delivers which service and for funding definitions, and no values are reported. Logged; the points resting on them are treated as unverified.

**What it establishes:**
1. **Individual-council RO outturn and RA budget data are published for every year from 2013-14 to 2020-21,** with release dates.
   - **Budgets** are published in June or July of the year itself. They are set before the year begins.
   - **Final outturn** follows 5 to 26 months after the year ends.
2. **Projection publication dates:**
   - 2010-based: 21 March 2012;
   - 2011-based interim: autumn 2012;
   - 2012-based: not stated;
   - 2014-based: May 2016;
   - 2016-based: 24 May 2018;
   - 2018-based: 24 March 2020.
3. **Two-tier responsibilities** (from council documents, unverified): counties run adult social care, highways and regulatory services; districts run waste collection and housing; unitaries run everything. **Metropolitan districts and London boroughs: not stated.**
4. **Not stated:**
   - the RO sub-line list and its changes across years;
   - reorganisations and their treatment;
   - the RAP and SALT measures;
   - library and waste series.
5. **Funding:** Core Spending Power per council from 2015-16; Settlement Funding Assessment per council.

**Design decisions this points to** (for the setting map and pre-registration; not yet fixed):
- **Single-tier councils only** (unitaries, metropolitan districts, London boroughs). They deliver the full range, so the two-tier split and its unverified documentation are avoided. The Isles of Scilly and the City of London are excluded as atypical.
- **The council set:** councils present with the same code in every year of the window. This removes reorganised councils mechanically, without needing a documented list.
- **Window:** 2013-14 to 2019-20 (after the public-health transfer, before the pandemic).
- **The H-dynamic covariate** comes from the population projection **published before each year's budget was set** (a fixed rule: the latest edition published before 1 February of the year the budget takes effect). **Each service's client group is defined by age,** fixed at mapping (for example 65 and over for adult social care, 0 to 17 for children's social care, the total population for services with no age-defined group). Current demand uses the same groups from mid-year estimates. This avoids the incomplete demand series.
- **Line list and consistency:** PT1-C1 will list the 2016-17 sub-lines from the guidance. Across years, lines are matched by name. **A line not present in all years of the window is excluded,** by a rule fixed before data.

**Next:** run PT1-C1 (statutory classification), then write the setting map and mapping.
