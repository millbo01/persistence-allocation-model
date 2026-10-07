# Check 1, systematic search 1: results (7 October 2026)

**Protocol:** theory/PAM_check1_search_protocol.md (committed before running, 2b22980). **Scripts:** scripts/check1_search.py (search), scripts/check1_screen.py (screening record). **Files:** raw_records.csv, dedup_records.csv, screening.csv (a decision and note for every record), counts.json.

## Counts

| Step | Number |
|---|---|
| Retrieved: PubMed strand A / OpenAlex strand A | 9 / 12 |
| Retrieved: PubMed strand B / OpenAlex strand B | 12 / 117 |
| Total retrieved | 150 |
| After deduplication (DOI, then title) | 139 (strand A 18; strand B 121) |
| No abstract (screened on title and source) | 15 |
| Screened | 139 |
| **Included (formal model, two or more organs, order under shortage)** | **0** |
| F: formal function priority (maintenance, growth, reproduction) | 4 (R0006, R0008, R0009, R0017) |
| E: empirical order, no model | 2 (R0031, R0059: fat against lean loss in fasting) |
| X1 no formal model / X2 one compartment / X3 pharmacokinetic / X4 not about shortage / X5 off topic | 32 / 13 / 4 / 26 / 58 |

**Near misses noted:**
- R0018: host and symbiont share nitrogen, and the symbiont extracts host tissue under shortage (two organisms; relevant to the capture probe, P2).
- R0040: a hierarchical whole-body metabolism framework.
- R0081 to R0085: optics against photoreceptors compete for resources (design optimisation).

## What this search shows, and what it does not

**It found no formal model of organ order under shortage.** But **its sensitivity is low, and the null result cannot be used in the paper.** Three reasons:

1. **Known-item failure.** The one relevant formal model already known, Göbel and colleagues (2010), a brain-against-periphery competition model in *Theory in Biosciences* (doi 10.1007/s12064-010-0105-9), was **not retrieved**. Nor was any Selfish Brain paper (search terms: "selfish", "brain-centered", "brain controlled": 0 hits). Its abstract uses "competition for energy", "compartment model", "brain" and "periphery", not the protocol's priority, hierarchy or sparing terms with organ or tissue.
2. **A class the terms missed: plant source-sink allocation.** Two records (R0070, R0110) point to plant models in which sink organs (seeds, fruits, stems, roots) draw assimilate from a phloem flow with explicit sink priority or sink strength: Münch-type transport models, transport-resistance models, crop-model partitioning rules. That is close to exactly the question. The protocol's terms (organ, tissue, starvation, fasting, hemorrhage) did not include "sink", "assimilate", "partitioning" or "carbon allocation".
3. **Precision collapsed in OpenAlex strand B:** OpenAlex stems search words, so "fasting" also matched "fast". This produced a large off-topic tail (58 X5). That costs precision, not recall, but it shows the strings behave differently across databases.

**Function priority (F) and empirical order (E)** records go to the unification table and to check 2 respectively. All four F records are DEB-family models of soma against reproduction or structure against reserve; none adds a new kind of priority.

## Next (proposed, not run)

A second search with its own protocol, fixed before running, with:
- **a known-item set** that the strings must retrieve before the search counts as sensitive (Göbel et al. 2010; Peters and Langemann 2009; a transport-resistance plant allocation model; the DEB workload model);
- **strand C:** plant source-sink allocation models ("sink priority", "sink strength", "carbon allocation model", "assimilate partitioning");
- **strand D:** organ competition for energy ("competition for energy", "energy allocation" with organ or brain and periphery, "selfish brain");
- **OpenAlex strings checked for stemming** before the run (exact phrases where needed).
