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

## Deviation D-1 (James approved, 7 October 2026): strand C screened through reviews, not an exhaustive title pass

**What changes:** the exhaustive title pass of strand C (11,175 titles) is stopped after 410 titles. It is replaced by a targeted reading of reviews of plant allocation models. Strand D is still screened in full, as the protocol says.

**Why:**
- The question strand C was built to answer is already answered. Formal models of allocation among plant organs are common, and at least one derives sink priority from transport properties (K3, Minchin et al. 1993; class I-access).
- What the paper needs from this literature is the classes of model and their key works, not a count. Reviews of plant allocation models classify the models directly.
- The exhaustive pass would cost about 680,000 tokens of reading to count instances of an answered question.

**Direction:** neutral to conservative. It cannot hide a precedent's existence, which is already established; it might under-count instances.

**Selection rule (fixed before any reviews are searched for or read):**
1. **From the search records:** strand C titles matching, case-insensitively, (review OR overview OR "state of the art" OR "a search for principles" OR concepts OR theory) AND (allocation OR partitioning OR "source-sink" OR "source and sink" OR sink OR phloem). Claude reads the titles that match and selects those that review **models** of allocation among plant organs.
2. **Hand-search, declared as such:** four reviews known to Claude in advance, added whether or not the search retrieved them:
   - Lacointe (2000), carbon allocation among tree organs in functional-structural tree models (*Ann For Sci*);
   - Génard et al. (2008), carbon allocation in fruit trees, from theory to modelling (*Ann Bot*);
   - Franklin et al. (2012), modeling carbon allocation in trees: a search for principles (*Tree Physiol*);
   - Minchin and Lacointe (2005), phloem physiology and modelling long-distance carbon transport (*New Phytol*).
   
   Whether each was retrieved by the search is reported.
3. **Reading:** each selected review is read in full where open, otherwise its abstract only, and said so.
4. **Extraction, for each review:** the classes of allocation model it names; how each class sets the order among organs under shortage (I-access, I-fixed or I-emergent); the key works cited for each class; and anything resembling PAM's ledger, repair or viability.

## Deviation D-2 (Claude's method decision, logged 7 October 2026): strand D OpenAlex title pass by agents, with a blind check

**What changes:** the size rule requires a title pass of the 6,809 new OpenAlex strand D records. The pass was done by three general-purpose agents, one after another (one chunk each), under a deliberately **liberal** rule: keep anything that could be a formal allocation model, a neighbour theory, or organ-sparing data. Claude then read every kept abstract (316).

**Check:** before any agent ran, Claude screened a random sample of 300 titles (seed 20261007) blind. The agents kept all 10 of Claude's sample keeps and marginals, plus 12 more. Files: theory/search_check1_s2/title_pass_openalex_D/.

**Direction:** towards sensitivity (more records reach the abstract stage). It does not make PAM easier to pass; check 1 asks whether precedents exist, and a looser pass can only find more.

**Network:** OpenAlex was queried from James's own connection (VPN off, James, 7 October 2026), after the shared VPN exit address had used up its free daily budget.

