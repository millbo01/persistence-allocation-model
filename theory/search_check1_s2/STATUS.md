# Check 1, search 2: status (7 October 2026, paused for James)

**Run 2 (after revision 1):**
- PubMed strand C: 1,616 records; PubMed strand D: 385. Both fetched.
- OpenAlex strand C: 11,834, identical string to run 1, so taken from run 1 (theory/search_check1_s2_run1/).
- **OpenAlex strand D (revised): not yet fetched.** OpenAlex's free daily budget for this network's IP address was used up (HTTP 429, "insufficient budget"; resets at midnight UTC). A free API key, which James would create, would remove the limit.
- Deduplicated so far: 11,554 records (strand C 11,175; strand D only 379; 4 overlap with search 1). File: dedup_records_partial.csv.

**Known items (run 2):**

| Item | Role | Result |
|---|---|---|
| K1 | design | found (PubMed D) |
| K2 | design | found (PubMed D) |
| K3 | design | found (OpenAlex C) |
| K4 | design | found (PubMed D, via revision 1) |
| H2 | held-out | found (PubMed D) |
| **H1** | held-out | **missed** (Thornley 1972; probably older vocabulary; to confirm when OpenAlex is available) |

Strand C is therefore of limited sensitivity, as the protocol requires.

**Result already clear before screening:**
- **K3, Minchin, Thorpe and Farrar (1993), is an include:** a formal phloem-transport model in which sink priority follows from transport properties. **Class I-access.**
- Formal organ-allocation models are common in plant science.
- **Title pass of strand C, first 410 of 11,175 titles:** about 30 candidates. Among them:
  - S00304: GreenLab, a functional-structural plant model with sink-strength allocation (review);
  - S00388: a neutral theory of plant carbon allocation;
  - S00037: phloem catastrophe, a bifurcation analysis;
  - S00202: spatial sucrose sink profiles and phloem transport;
  - S00154: compartmental modelling of phloem transport;
  - S00132: optimality-based modelling of belowground allocation under low nitrogen;
  - S00183: a model of the leaf biomass partitioning coefficient;
  - S00253: simulated dry matter partitioning in cucumber fruits;
  - S00155: a wheat growth model with a growth-defence trade-off;
  - S00299: a vegetation demography model;
  - S00314: simulated defoliation and leaf-to-nodule plasticity;
  - S00344: an oil palm model;
  - S00362: inferred drought allocation shifts;
  - S00380: "Beyond source and sink control" (review);
  - S00310: source against sink limitation (review);
  - S00011: carbohydrate content and growth-storage allocation in recovery.

**Paused for a decision:** finish the exhaustive title pass of strand C (about 11,000 titles), or replace it with a targeted reading of reviews of plant allocation models (logged as a deviation).
