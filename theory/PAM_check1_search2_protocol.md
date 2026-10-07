# Check 1, systematic search 2: protocol (fixed before running, 7 October 2026)

**Why a second search.** Search 1 (theory/search_check1/README.md) found 0 includes, but failed a known-item check: it missed Göbel et al. (2010), and its terms did not cover plant source-sink allocation models. Its null is not usable. This search targets the two gaps, with a stated sensitivity test.

**Question (unchanged):** has any published formal model specified the order or priority in which two or more organs, tissues or body parts lose supply when a shared resource is short, and is that order derived from properties of access?

## Known items (sensitivity test)

**Design set.** Their identifiers and titles were known when the strings were written, so retrieving them shows only that the strings catch papers like them:
- **K1** Göbel B et al. (2010). Systemic investigation of a brain-centered model of the human energy metabolism. *Theory Biosci.* PMID 20734159; doi 10.1007/s12064-010-0105-9. Expected: strand D.
- **K2** Peters A, Langemann D (2009). Build-ups in the supply chain of the brain. *Front Neuroenergetics.* doi 10.3389/neuro.14.002.2009. Expected: strand D.
- **K3** Minchin PEH, Thorpe MR, Farrar JF (1993). A simple mechanistic model of phloem transport which explains sink priority. *J Exp Bot.* doi 10.1093/jxb/44.5.947. Expected: strand C.
- **K4** van Leeuwen IMM, Zonneveld C, Kooijman SALM (2003). The embedded tumour: host physiology is important for the evaluation of tumour growth. *Br J Cancer.* doi 10.1038/sj.bjc.6601394. Expected: strand D.

**Held-out set.** Identified, but their abstracts were **not read** before the strings were fixed. This is the real test of sensitivity:
- **H1** Thornley JHM (1972). A balanced quantitative model for root:shoot ratios in vegetative plants. *Ann Bot.* doi 10.1093/oxfordjournals.aob.a084602. Expected: strand C.
- **H2** Göbel B et al. (2010). Compact energy metabolism model: brain controlled energy supply. *J Theor Biol.* PMID 20230841; doi 10.1016/j.jtbi.2010.02.033. Expected: strand D.

**Rule:** report which known items each database and strand retrieved.
- If a design item is missed, the strings may be revised **once**, with the reason logged, and both runs reported. Held-out items are never used to revise.
- If a held-out item is missed, the strand is reported as **of limited sensitivity**, and any null from it is stated with that limit.

## Databases

- PubMed (E-utilities) and OpenAlex, all years, run 7 October 2026.
- **OpenAlex stems all search terms, even inside quotes** (checked 7 October 2026: "fast", "fasting" and fasting all return 4,585,894 records), and has no unstemmed search. Strings therefore avoid words whose stems are common, and OpenAlex precision is expected to be low.

## Search strings

**Strand C: plant source-sink allocation models.**
- PubMed: `("sink priority"[tiab] OR "sink strength"[tiab] OR "assimilate partitioning"[tiab] OR "source-sink"[tiab] OR "phloem transport"[tiab] OR "transport-resistance"[tiab] OR "carbon allocation"[tiab] OR "carbon partitioning"[tiab] OR "dry matter partitioning"[tiab]) AND (model[tiab] OR models[tiab] OR modelling[tiab] OR modeling[tiab] OR simulation[tiab])`
- OpenAlex: `("sink priority" OR "sink strength" OR "assimilate partitioning" OR "source-sink" OR "phloem transport" OR "transport-resistance" OR "carbon allocation" OR "carbon partitioning" OR "dry matter partitioning") AND (model OR models OR modelling OR modeling OR simulation)`

**Strand D: organs competing for energy.** Three sub-queries, combined with OR:
- PubMed:
  - D1: `"selfish brain"[tiab] OR "brain-centered"[tiab] OR "brain-centred"[tiab] OR ("supply chain"[tiab] AND brain[tiab])`
  - D2: `("competition for energy"[tiab] OR "energy competition"[tiab] OR "energy allocation"[tiab] OR "energy supply"[tiab]) AND (brain[tiab] OR organ[tiab] OR organs[tiab] OR periphery[tiab] OR peripheral[tiab]) AND (model[tiab] OR models[tiab] OR mathematical[tiab] OR "dynamical system"[tiab] OR "compartment model"[tiab])`
  - D3: `"dynamic energy budget"[tiab] AND (tumour[tiab] OR tumor[tiab] OR host[tiab] OR workload[tiab])`
- OpenAlex, the same three as one string: `("selfish brain" OR "brain-centered" OR "brain-centred") OR (("competition for energy" OR "energy competition" OR "energy allocation") AND (brain OR organ OR organs OR periphery) AND (model OR models OR mathematical OR "dynamical system" OR "compartment model")) OR ("dynamic energy budget" AND (tumour OR tumor OR host OR workload))`. Here "energy supply" is dropped, because stemming makes it match "energy" plus "supply" in almost any form.

## Size rule

As search 1: more than 1,500 records in one strand of one database means a title pass first, then abstracts of title-passes. Otherwise every abstract is screened. Because strand C is expected to be large in OpenAlex ("carbon allocation" is a big field), its title pass asks only "could this be a formal model allocating among organs?"

## Screening

As search 1 (codes I-access, I-fixed, I-emergent, F, E, X1 to X6), with one clarification: **for plants, sinks (organs such as roots, shoots, fruits, seeds) count as parts.** A model qualifies if it specifies how supply among sinks changes when assimilate is short.
- Records already screened in search 1 keep their decision.
- Every include is read in full where open; otherwise its abstract only, and said so.

## Records kept

- theory/search_check1_s2/: raw records, deduplicated records, screening sheet, counts, known-item report.
- The write-up goes into theory/PAM_open_checks.md, check 1.

## Revision 1 (logged 7 October 2026, after run 1; the only revision allowed)

**Run 1 known-item result:**
- Design items K1, K2 and K3 were found; **K4 was missed.**
- Held-out item H2 was found; **H1 was missed.** Strand C is therefore of limited sensitivity, and H1 is not used for any revision.
- Run 1 outputs are kept in theory/search_check1_s2_run1/.

**Diagnosis of K4** (its abstract read for this purpose, as a design item): it never uses "dynamic energy budget", "energy allocation" or "competition for energy". It calls itself a "tumour-in-host model" built on "the energetics of tumour and host". Strand D lacked the vocabulary of energetics.

**Revision:** a fourth sub-query added to strand D. Strand C is unchanged.
- PubMed D4: `"tumour-in-host"[tiab] OR "tumor-in-host"[tiab] OR ((energetics[tiab] OR "energy budget"[tiab] OR "energy demands"[tiab]) AND (tumour[tiab] OR tumor[tiab] OR organ[tiab] OR organs[tiab]) AND host[tiab] AND (model[tiab] OR models[tiab] OR mathematical[tiab]))`
- OpenAlex D4, appended to the strand D string with OR: `("tumour-in-host" OR "tumor-in-host" OR ((energetics OR "energy budget" OR "energy demands") AND (tumour OR tumor OR organ OR organs) AND host AND (model OR models OR mathematical)))`
