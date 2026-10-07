# Check 1, systematic search: protocol (fixed before running, 7 October 2026)

**Question.** Has any published **formal model** (mathematical or computational) specified the **order or priority in which two or more organs, tissues or body parts lose supply under resource shortage**? And is that order derived from properties of access (routes, gates, transporters, vascular control), as in PAM's claim (a)?

**Why.** The paper may need to say how far this exists. Two earlier sessions of web searches found only the Selfish Brain's two-compartment model (theory/PAM_open_checks.md). This search makes the statement checkable.

**Status:** a literature search in phase 3. Not a test; no verdict rules. Fixed in advance so that the counts and decisions can be audited.

## Databases and dates

- **PubMed** (NCBI E-utilities), all years, run 7 October 2026.
- **OpenAlex** (api.openalex.org), all years, run 7 October 2026. OpenAlex is included because DEB work appears mainly in ecology journals that PubMed indexes only in part.

## Search strings

**Strand A: DEB and organs or tissues under shortage.**
- PubMed: `("dynamic energy budget"[tiab] OR "DEB model"[tiab] OR "DEB theory"[tiab]) AND (organ*[tiab] OR tissue*[tiab] OR "multiple structures"[tiab] OR "several structures"[tiab] OR compartment*[tiab] OR "body part"[tiab] OR "body parts"[tiab]) AND (starv*[tiab] OR fasting[tiab] OR "food restriction"[tiab] OR "caloric restriction"[tiab] OR "calorie restriction"[tiab] OR shrink*[tiab] OR priorit*[tiab])`
- OpenAlex (title and abstract): `"dynamic energy budget" AND (organ OR organs OR tissue OR tissues OR "multiple structures" OR compartment OR compartments) AND (starvation OR fasting OR "food restriction" OR "caloric restriction" OR shrinking OR priority)`

**Strand B: any formal model of organ priority under shortage.**
- PubMed: `("mathematical model"[tiab] OR "computational model"[tiab] OR "dynamical system"[tiab] OR "compartment model"[tiab] OR "compartmental model"[tiab] OR "simulation model"[tiab]) AND (organ*[tiab] OR tissue*[tiab]) AND (priorit*[tiab] OR hierarch*[tiab] OR sparing[tiab] OR "order of"[tiab] OR "allocation"[tiab]) AND (starv*[tiab] OR fasting[tiab] OR "food restriction"[tiab] OR "caloric restriction"[tiab] OR "energy restriction"[tiab] OR "energy deficit"[tiab] OR hemorrhage[tiab] OR haemorrhage[tiab] OR hypoxia[tiab] OR "nutrient limitation"[tiab])`
- OpenAlex (title and abstract): `("mathematical model" OR "computational model" OR "dynamical system" OR "compartment model" OR "compartmental model") AND (organ OR organs OR tissue OR tissues) AND (priority OR prioritization OR hierarchy OR sparing OR allocation) AND (starvation OR fasting OR "food restriction" OR "caloric restriction" OR "energy restriction" OR hemorrhage OR haemorrhage OR "nutrient limitation")`

**Size rule (fixed now).** If a strand in one database returns more than 1,500 records, the screen is done in two passes. Pass 1 screens titles; pass 2 screens abstracts of title-passes only. Otherwise every abstract is screened. Counts are reported either way.

## Screening (title and abstract, by Claude)

**Include** a record if it presents a formal model in which **two or more organs, tissues or body parts** draw on a shared limiting resource **and** the model specifies how supply among them changes under shortage (an order, priority, hierarchy or allocation rule).

**Classify** each include:
- **I-access:** the order follows from properties of access (gates, transporters, vascular control, routes);
- **I-fixed:** the order is set by an assigned priority or fraction (for example a κ-type rule);
- **I-emergent:** the order emerges from another mechanism (for example workload, demand, mass action).

**Record separately, not as includes:**
- **F (function priority):** priority among functions, not body parts (maintenance against growth against reproduction), with a formal model. These go to the unification table.
- **E (empirical order):** an observed order of organ loss with no formal model. These go to check 2.

**Exclude, with a reason code:**
- X1: no formal model;
- X2: one compartment only;
- X3: pharmacokinetic or drug-distribution model;
- X4: not about shortage of a resource;
- X5: not about organisms or systems (for example engineering texts unrelated to resource priority among parts);
- X6: duplicate.

**Deduplication:** by DOI, then by normalised title.

**Full text:** every include is read in full where open; otherwise its abstract only, and said so.

## Records kept

- theory/search_check1/ holds the raw result lists (identifiers, titles, years, sources), the screening sheet with a decision and reason for every record, and the counts (identified, deduplicated, screened, included by class).
- The write-up goes into theory/PAM_open_checks.md, check 1.

## Limits stated in advance

- Two databases. No hand search of the DEB library (Zotero group) unless the screen points to a gap.
- Title and abstract screening by one reviewer (Claude). A second screen of the decisions by another model is possible if James wants it.
- Terms in other languages are not searched.
