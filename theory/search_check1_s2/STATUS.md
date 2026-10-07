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

## Update (7 October 2026, third session): CHECK records resolved; H1 diagnosed in part

**The five CHECK records:** resolved in check_records_resolved.md.
- 3 read in full and included: the tilt model (I-access), spreading depression (I-emergent) and GLUT1 deficiency (I-emergent, weak).
- 1 included provisionally from its abstract (the 0 g to 3 g model, I-access; paywalled).
- 1 probable exclude from its abstract (the leptin glucoregulation model; paywalled).

**Strand D (PubMed part) now has 16 includes.**

**Why held-out H1 (Thornley 1972) was missed, so far:**
1. **Not in PubMed.** *Annals of Botany* 1972 has no PubMed records (a search for the journal and year returns 0), so only OpenAlex could find it.
2. **Its title has none of strand C's terms.** The title is "A Balanced Quantitative Model for Root: Shoot Ratios in Vegetative Plants". It contains "model" but none of: sink priority, sink strength, assimilate partitioning, source-sink, phloem transport, transport-resistance, carbon allocation, carbon partitioning, dry matter partitioning. It speaks of root:shoot ratios.
3. **Crossref holds no abstract** for it. Whether OpenAlex holds one is to be checked when the budget resets. If it does not, the miss is fully explained by vocabulary plus a title-only record.

**Implication for strand C:** older, foundational plant models are described in root:shoot and growth vocabulary, not allocation vocabulary. This confirms the protocol's statement that strand C has limited sensitivity, and supports deviation D-1 (reviews).

**Still blocked:** OpenAlex strand D and the H1 abstract check. The free budget was still exhausted at 13:37 UTC on 7 October; it resets at midnight UTC.

## Update (7 October 2026, fourth session): OpenAlex strand D fetched and screened; search 2 complete

**Fetch** (scripts/check1_s2_openalex_D.py; report openalex_D_report.json):
- 7,372 records; 563 matched existing records; 6,809 new.
- Final deduplicated set: 18,363 records (dedup_records.csv). Existing record numbers are unchanged.

**Known items, final:** K1 to K4 found; H2 found; **H1 missed**.

**H1 diagnosis complete.** OpenAlex holds H1 with an abstract ("transport and utilization of two required substrates... root: shoot ratios"). Neither the title nor the abstract contains any strand C phrase. The miss is vocabulary alone.

**Screening** (deviation D-2; screening_D_openalex.csv; counts_D_openalex.json):

| Decision | Number |
|---|---|
| Excluded at the title pass | 6,493 |
| Abstract read, off-topic | 199 |
| **Included, I-access** | **4**: Selfish Brain supply-chain papers (2007, 2008); a brain-centred four-compartment model in a fractional reformulation (2026 preprint); a lifespan brain-health model built on Goebel et al. 2010 (2025 abstract) |
| **Included, I-fixed (weak)** | **1**: a 1982 computer model in which an autonomous tumour drain draws first |
| Duplicates of existing includes | 7 |
| CHECK (title or abstract only) | 5 |
| Near miss (DEB, two organisms) | 11 |
| Formal, but no allocation under shortage | 19 |
| Neighbours (unification table) | 40 |
| Empirical | 30 |

**Two empirical records to note, logged as found:**
- **S11597** (Mulligan and Tisdale, Biochem J 1991, 2-deoxyglucose): in tumour-bearing mice the tumour became the second glucose consumer after the brain, and the brain's glucose use fell, whether or not the mice were cachectic. **Corrected 7 October 2026 (full abstract read, PMID 1859359; the full text is a scanned PDF, so tissue-by-tissue values are not available):** the brain's **glucose** use fell, but "brain metabolism in the tumour-bearing state was maintained by an increased use of lactate and 3-hydroxybutyrate". The brain switched fuel; its energy was not cut. **Not against brain priority:** for the brain the resource is energy, and glucose and ketones are substitutes (the complementarity check, v0.18 Section 8). The earlier entry misread a truncated abstract.
- **S15185** (J Surg Res 1989): the tumour gained protein while liver and gut mucosa were depleted. This is an order among host tissues under a parasitic sink.

**Search 2 is complete.** Strand D, with both databases screened, has 21 includes:
- 12 I-access (8 from PubMed, 4 from OpenAlex);
- 7 I-emergent;
- 1 weak I-emergent;
- 1 weak I-fixed.

There is also 1 provisional I-access, 5 OpenAlex CHECK records, and 1 probable exclude from PubMed.

**No new class of model appeared.** The Selfish Brain family, the DEB tumour-in-host models and the haemodynamic and neuron-glia models found earlier remain the whole of strand D.

