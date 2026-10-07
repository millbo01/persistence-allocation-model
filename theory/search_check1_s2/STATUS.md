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

## Update (7 October 2026, later): deviation D-1 applied; strand D (PubMed) screened

**Strand C via reviews:** theory/search_check1_s2/strand_C_reviews.md.

**Strand D, PubMed part (379 records, all abstracts screened; screening_D_pubmed.csv):**

| Decision | Number | What it covers |
|---|---|---|
| **Included, I-access** | 7 | The Selfish Brain formal models: Göbel et al. 2010, 2011 and 2013; the 2012 review of mathematical models; the 2008 deductive appetite model; the 2009 and 2011 supply-chain models. Brain priority is set by insulin-gated access |
| **Included, I-emergent** | 6 | DEB tumour-in-host models (van Leeuwen et al. 2003; Tosca and colleagues 2018 to 2021): tumour and host compete for energy, with cachexia |
| **CHECK** (full text needed) | 5 | Two multiscale cardiovascular models with organ perfusion under stress; two neuron-glia energy models; a brain-centred glucoregulatory model |
| Near miss (formal, two organisms) | 7 | DEB host-symbiont and host-parasite models |
| Neighbours (no formal model) | 15 | Theories for the unification table (check 3): selfish immune system (Straub); allostasis as brain-centred predictive regulation (2019); central governor in exercise (Noakes 2000); unifying theory of hypoxia tolerance (Hochachka 1996); sepsis as CNS-governed metabolic triage (2026); Allostatic Triage Model (2025); brain energy on demand (2022) |
| Empirical | 3 | Brain sparing under deprivation; brain-muscle trade-off; muscle-tumour competition |
| Off-topic | 336 | Batch-coded after reading: "brain-centred" in clinical or molecular use, "energy supply" in cell biology |

**Still to do in search 2:**
- the OpenAlex part of strand D, after the daily budget resets (midnight UTC), screened the same way;
- the five CHECK records, from full text;
- confirming why held-out item H1 was missed.
