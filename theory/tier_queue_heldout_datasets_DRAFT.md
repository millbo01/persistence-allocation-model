# Held-out datasets for the tier-queue stress tests (draft for James, 5 October 2026)

**Status:** core set H1 to H5 agreed by James (5 October 2026). The datasets named in it are first candidates, not final: see Section 6. **No dataset on this list has been opened**, and no landing page, data dictionary or results paper for these datasets was read to write it. Descriptions come from Claude's prior knowledge and may be wrong in detail. Every "to confirm" item is checked by a documentation run on another model, barred from reporting values (CLAUDE.md, phase 5), once James agrees the list.

**Purpose.** Step 2 of the way forward (TIER_QUEUE_MODEL_v0.5.md, Section 8): keep the best datasets unopened for the final stress tests, once the model is consistent. The stress tests are phase 5, so the full rules apply: predictions from the model committed before data, pass/fail rules fixed, blind adjudication, and replication by a second model.

## 1. What makes a dataset worth holding out

A dataset is worth holding out if it has most of these:

1. **Individual-level time series**, not only group means.
2. **A held output** (rule R) **and at least one state signal** recorded in the same individuals, so "the record sees compromise, not stress" can be tested directly.
3. **A known or measurable load or buffer**: the imposed load, its rate, or the size of the reserve.
4. **It reaches the predictions not yet tested**, above all:
   - **F7:** higher energy demand moves the fasting threshold to a higher fat level (the most informative untested prediction from the fasting test);
   - **N5 (flatness):** a larger buffer gives a longer flat record and a sharper break;
   - **G3:** the break comes at the same cumulative load, whatever the rate;
   - **G10 and the shortfall check:** reserves grow less after one severe acute episode than after a long mild one with the same total load (TQ8);
   - **P8:** isohydric and anisohydric plants as the coupled and opaque regimes (signal gain);
   - **the demand-cut sink (TQ8, S4):** where signals are weak, a part that cuts its own demand becomes a sink for displaced load.
5. **Not used in the surface tests**, and its published results not known in detail to Claude or James. Partial contamination is declared below.
6. **Obtainable** by James (open, credentialed, or on request).

## 2. Proposed core set (five, one per system already surface-tested)

| No. | System | Dataset (to confirm) | Record (held output) | State signals | Load or buffer | Predictions it can reach | Access (to confirm) | Contamination |
|---|---|---|---|---|---|---|---|---|
| H1 | **Blood loss** | Individual lower-body negative pressure (LBNP) runs to presyncope, from the US Army Institute of Surgical Research group (Convertino, Rickards, Ryan and others) | Arterial pressure | Heart rate, stroke volume, compensatory reserve index, cerebral flow | Imposed central blood-volume loss at a known rate; tolerance per person (the buffer) | **N5 flatness**, **G3** (if protocols differ in rate), G1, G4, refinement A; **G12** (record dynamics from beat-to-beat pressure; the release profile, tapering or switch, must be fixed from documented physiology before the data are opened) | Not known to be open. Likely by request or collaboration | **Partial:** group-level summaries from the same programme were read in the surface test (blood loss S2 to S4). Individual traces not seen |
| H2 | **Fasting** | Individual body mass and phase records from long-fasting birds or seals: king or emperor penguins (Strasbourg, CNRS: Le Maho, Groscolas, Robin, Cherel), or northern elephant seals (Crocker, Costa) | Plasma glucose (F4); breeding or incubation kept up (the egg) | Specific daily mass loss, plasma urea and uric acid, β-hydroxybutyrate | Fat store at the start (buffer); energy demand varied by cold, huddling or activity | **F7**, **F4**, **G3** (phase III at a set fat level whatever the rate of loss: the refeeding signal and abandoned incubation as the switch) | Unknown. Probably by request to the groups | **Partial:** the phase pattern is known from the fasting surface test (S1). Individual data not seen; F7 data not found then |
| H3 | **Kidney** | MIMIC-IV (PhysioNet; Beth Israel Deaconess intensive care, about 2008 to 2019), or eICU-CRD, for episodes of acute kidney injury and recovery | Serum creatinine | Urine output; cystatin C where measured; electrolytes and acid-base | The acute injury (staged by creatinine and urine output); prior chronic kidney disease as a compromised start | **G6** (record recovers before state), recovery order, G4 (compromised start fails sooner), G7 | Credentialed: James completes PhysioNet credentialing and training and downloads. Claude never enters credentials | Low. Claude knows general AKI literature, not analyses of these episodes |
| H4 | **Honeybees** | Hive-scale time series with weight and entrance traffic, for example the HOBOS hives (Würzburg; weight, temperature, humidity and bee flow, distributed as "Beehive Metrics"), and USDA ARS hive-scale studies (Meikle and colleagues) | Stores and brood held (hive weight once the season is controlled for) | Forager traffic, brood-nest temperature stability | Nectar dearths and winter (load); stores at the start (buffer) | **G3/G4** (failure at a set depletion; larger stores, longer silence), **the shortfall check** (do colonies store more after a dearth?), G1 | HOBOS-derived data believed open; USDA data possibly on Ag Data Commons | **Partial:** the bee model work (K1, K1b) and the honeybee surface test are known in shape. No hive-scale records seen |
| H5 | **Plants under drought** | SAPFLUXNET (open global database of whole-plant sap flow with soil water and weather; Poyatos and colleagues, about 2021) | Transpiration and carbon gain kept up | Sap flow per plant, leaf water potential where recorded, soil water | Soil-water depletion (buffer), atmospheric demand (VPD) as load | **P8** (isohydric against anisohydric as coupled against opaque), **G3**, G1, the demand-cut sink (leaf shedding sites) | Believed open (Zenodo) | Low. Not used in the plant surface test, which read drought-legacy and xylem studies |

## 3. Reserve list (held out too, unless James releases them)

| No. | System | Dataset (to confirm) | Why kept | Why not core |
|---|---|---|---|---|
| R1 | Blood loss | VitalDB (open intraoperative vital signs from several thousand surgical patients, Seoul National University Hospital) | Open; blood loss, pressure, heart rate and the anaesthetist's interventions at high resolution | The record is defended by an outside loop (drugs, fluids), which confounds the buffer. Usable if H1 is unobtainable |
| R2 | Plants | International Tree-Ring Data Bank (NOAA) | Recovery after acute against chronic drought (G10 in plants), demand-cut scars | Drought-legacy results (Anderegg and colleagues, 2015) are known in outline |
| R3 | Kidney | Living kidney donor follow-up (SRTR or OPTN, United States) | Abrupt loss of half the nephrons: displaced load onto survivors (G5), fixed capital (G7) | Restricted access by application; long lead time |
| R4 | Dairy cattle | Early-lactation records: milk yield, body condition, fertility | Possibly the cleanest natural tier queue: milk held, body reserve drawn, reproduction dropped. Higher-yielding cows test F7 by analogy | No specific open dataset identified yet |
| R5 | Muscle | NASA Life Sciences Data Archive bed-rest studies | Disuse and recovery, record against capacity tests (rule R) | Access by request; small samples |
| R6 | Kidney or general | UK Biobank | Creatinine, cystatin C, albuminuria, linked records, at scale | Application and fee |
| R7 | Wild populations | Soay sheep, St Kilda | Winter crashes: break at a set depletion, buffer by body weight | Access by collaboration |

## 4. Rules while the list is held

1. **No opening.** Claude does not open any listed dataset, its files or its data dictionary before the test's rules are committed. Structure comes from published documentation gathered by another model barred from reporting values.
2. **Quarantine on results too.** During the surface testing still to come, nobody reads papers that analyse a listed dataset. If one is met by accident, it is logged and the contamination is declared on that test.
3. **Surface tests continue elsewhere.** The same systems can still be surface-tested from other sources, but those sources are named, so it is clear they are not the held-out data.
4. **Predictions come from the model,** not from knowledge of the dataset (CLAUDE.md). Each stress test maps its system with Section 5 of the model before any data are seen.
5. **Release.** James can release a dataset to surface testing at any time. A released dataset leaves the held-out list for good.

## 5. Decisions for James

1. **Agree the core set** (H1 to H5), or swap in reserves.
2. **Access requests.** H1 and H2 probably need emails to the research groups. Should Claude draft them now? Asking early is cheap; the data stay unopened until each test's rules are committed.
3. **Credentialing for H3.** If MIMIC-IV stays on the list, James needs PhysioNet credentialing. Claude cannot do this step.
4. **Documentation runs.** Once the list is agreed, Claude builds one documentation prompt per dataset for another model, one at a time, barred from reporting values. These confirm what each dataset contains, its access route, licence and size.

## 6. Discovery searches before any access request (James, 5 October 2026)

The candidates above were drafted from Claude's memory, with no search. James: the available datasets have not been exhausted, so no conclusion should be drawn from a first pass. Before any email or access request:

1. **One discovery search per system**, run by another model, one at a time, with a fully assembled prompt. The model reports structural metadata only (contents, variable names, number of individuals, access route, licence), never values or findings, and logs every repository and query searched so exhaustiveness can be judged.
2. **Order:** fasting (H2) first, then blood loss (H1), kidney (H3), honeybees (H4), plants (H5).
3. **Raw returns** are stored verbatim in raw/ before any commentary.
4. **Then choose:** the best openly available individual-level dataset for each system goes to the held-out list. Emails or credentialing are used only where the search finds no open dataset that can test the system's key predictions.

| Search | System | Prompt | Status |
|---|---|---|---|
| TQ-DS1 | Fasting (H2) | tests/prompts/TQ-DS1.txt | Run 5 October 2026 (ChatGPT deep research; raw/2026-10-05_chatgpt_TQ-DS1.md). **Not exhaustive; superseded by TQ-DS1a to 1d** (see below) |
| TQ-DS1a | Fasting: penguins and other birds | tests/prompts/TQ-DS1a.txt (template v2) | Run 5 October 2026 (ChatGPT deep research; raw/2026-10-05_chatgpt_TQ-DS1a.md). Literature pass not done; see assessment |
| TQ-DS1a-L | Fasting, birds: literature enumeration only | tests/prompts/TQ-DS1a-L.txt | Run 5 October 2026 (Gemini deep research). Raw stored verbatim from Gemini's export (raw/2026-10-05_gemini_TQ-DS1a-L.md; SHA-256 begins 4a5da98f). The export adds a works-cited list of 36 web sources not in James's paste; all 36 titles were read: a few state findings (amino-acid oxidation under water restriction in sparrows; pre-migratory fattening involving more than fat), none bearing on F7, F4 or G3. Logged as minor contamination. See assessment |
| TQ-DS1b | Fasting: seals and other marine mammals | tests/prompts/TQ-DS1b.txt (template v3) | Run 5 October 2026 (Gemini; raw/2026-10-05_gemini_TQ-DS1b.md, SHA-256 begins 3871a047). See assessment |
| TQ-DS1c | Fasting: hibernators, seasonal fasters and laboratory rodents | tests/prompts/TQ-DS1c.txt (template v3.1) | Run 5 October 2026 (Gemini; raw/2026-10-05_gemini_TQ-DS1c.md, SHA-256 begins c807c4e1). Too thin; see assessment |
| TQ-DS1c-R | Fasting: laboratory rodents only (narrowed rerun) | tests/prompts/TQ-DS1c-R.txt | Run 5 October 2026 (Gemini; raw/2026-10-05_gemini_TQ-DS1c-R.md, SHA-256 begins f78271a4). See assessment. Hibernators and seasonal fasters to be rerun separately if needed |
| TQ-DS1d | Controlled trials: human fasting, dieting, weight regain and weight cycling; animal weight cycling (Minnesota excluded; surveys and observational designs excluded, James) | tests/prompts/TQ-DS1d.txt (template v3.1) | Run 5 October 2026 (Gemini; raw/2026-10-05_gemini_TQ-DS1d.md, SHA-256 begins 7ff68c17). See assessment |
| TQ-DS2 | Blood loss (H1) | tests/prompts/TQ-DS2.txt (template v1) | Held. To be rebuilt on template v2, and probably split by group, once TQ-DS1a confirms the template works |
| TQ-DS3 | Kidney (H3) | | |
| TQ-DS4 | Honeybees (H4) | | |
| TQ-DS5 | Plants (H5) | | |

### TQ-DS1 assessment (5 October 2026)

- **No values or findings reported:** passed. One dataset title states a finding about oxidative stress, unrelated to the model's predictions.
- **Exhaustiveness:** failed. About 5 to 10 hits screened per repository; queries were web-search style ("penguin fasting Dryad") rather than run in each repository's own search; rodent and human groups barely searched; no literature pass for data in supplements or for individual values printed in paper tables.
- **"Not public" table:** unreliable. Several entries appear misattributed or invented (for example, research groups placed at the wrong institutions; a "manuscript in review"; guessed sample sizes), and none cites where an access statement appears. Treated as unverified and not used.
- **One open dataset found:** northern elephant seals in the breeding fast (Dryad, CC0; 63 individuals, two time points each, oxidative-stress markers). Catalogued, not opened. Two time points and these variables cannot test F7, F4 or G3.

**Template v2** (from TQ-DS1a on): no inferred entries (every row needs a cited source; "not stated" instead of estimates); a minimum depth (each repository's own search, a fixed query list, at least 50 results screened per query); a literature pass of at least 150 papers checking data statements, supplements and individual values printed in tables; a self-check; and one animal group per run, because breadth thinned depth (as in the earlier PN3 split).

### TQ-DS1a assessment (5 October 2026)

- **No values or findings reported:** passed.
- **Literature pass:** failed. It claimed 150+ papers screened but listed one ("screening notes omitted for brevity"), against the template's logging rule. Its statement that no paper prints individual-animal tables cannot be relied on.
- **Repository search:** thin but plausibly done ("first 50 screened"), without per-query counts. Nothing relevant found.
- **The one dataset is not a fasting dataset:** single-capture morphometry and blood isotopes of Pygoscelis penguins (Palmer LTER; Gorman et al. 2014). One time point per bird; no fast. Not relevant to H2.
- **Conclusion:** two ChatGPT runs have not established whether open bird fasting data are rare or the searches too shallow. Next: switch tool (Gemini deep research), and run the literature pass alone with a forced numbered table of at least 150 papers (TQ-DS1a-L), since classic fasting physiology often holds its individual data in papers and supplements rather than repositories.

### TQ-DS1a-L assessment (5 October 2026)

- **No values or findings reported:** passed in the table and text. Some paper titles state findings (for example on protein catabolism in long flights, and starvation mortality in African penguins); none bears directly on F7, F4 or G3. Logged as minor contamination.
- **Depth:** much better than the ChatGPT runs. 174 rows, citation chaining described, full texts opened for about 40 papers.
- **Quality:** weak. About 40% of rows are off topic (nest maintenance, species distributions, climate, a polar bear and a fish paper, a mouse microbiome paper). About 50 rows have no identifier ("Title not stated, Journal not stated, Identifier not stated"), against Rule 2. Several DOIs do not match their citations. The self-check claims full compliance, which is false. Most classic fasting-physiology papers (Cherel, Le Maho, Robin, Groscolas) were seen as abstracts only, so whether they print individual values is unknown. At least one central paper is missing (the refeeding-signal study in emperor penguins).
- **Usable leads (structure only, not opened):**
  - snow geese fasted in captivity with refeeding: individual body-mass series in a figure, 20 birds (Legagneux et al. 2011, Proc R Soc B, 10.1098/rspb.2011.1351);
  - king penguins fasting while incubating: individual values in a figure, 8 birds (Guerin et al. 2010, J Exp Biol);
  - brent geese at staging, with refeeding: individual values in a figure (Front Ecol Evol 2022, 10.3389/fevo.2022.749534);
  - eiders: corticosterone and mass, deposited on Dryad (Am Nat 2012), two time points.
- **Conclusion for birds:** three runs have found no open, individual-level dataset of a long bird fast with repeated measures and varied energy demand, which is what F7 needs. The best leads are figure-level individual data in a few papers (usable only by digitising) and the classic fasting groups' own records. This meets James's test for an access request **for birds**, but H2 can be met by any fasting system, so the seal, rodent and human searches run first. The CNRS Strasbourg fasting group and the snow goose authors are the first contacts if needed.

**Template v3** (from TQ-DS1b on): only papers whose subjects were measured at least twice during a fast (off-topic papers counted, not listed); no row without a verifiable identifier; full text opened for every paper on the core list before its data label is given, or the row marked "data label unknown (abstract only)"; repository search kept, with per-query counts; Gemini deep research, which went deeper than ChatGPT.

### TQ-DS1b assessment (5 October 2026)

- **No values or findings reported:** passed. Some works-cited titles state findings (insulin signalling and Glut4 in fasting seals; amino-acid isotopes in fasting); tangential to F7, F4 and G3. Logged as minor contamination.
- **Relevance filter (template v3) worked:** 9 rows, nearly all genuine repeated-measures fasts; per-repository counts logged.
- **Inconsistency:** 612 papers screened and 592 discarded implies 20 qualifying, but 9 are listed; the self-check misses it. Template v3.1 adds a rule that counts must reconcile.
- **Structural finding:** most seal fasting studies compare separate early-fast and late-fast animals rather than following individuals.
- **Leads (structure only, not opened):**
  - grey seal pups, post-weaning fast: individual values in figures, 30 pups, body mass, body fat, fast duration and age at departure (Physiol Biochem Zool 2008, 10.1086/528777);
  - grey seal pups with starting mass and fat varied by supplementary feeding (Pomeroy, Fedak and colleagues 2007, J Exp Biol, 10.1242/jeb.009381): a manipulated buffer, relevant to G4; abstract only;
  - harp seal pups, fasting and refeeding, 20 pups (Worthy and Lavigne 1983);
  - Steller sea lion pups, captive fasts with urea, ketones and refeeding (Rea, Rosen and Trites 2000).
- **Conclusion for seals:** no open individual-level dataset with energy demand varied, as F7 needs. The grey seal supplementary-feeding experiment (Sea Mammal Research Unit) is the strongest design for G4 and would need a request. Birds and seals both now meet James's test for an access request; hibernators, rodents and humans are searched first.

### TQ-DS1c assessment (5 October 2026)

- **No values reported:** mostly passed. The narrative describes the three phases of prolonged fasting in textbook terms (known from the fasting surface test; no new contamination). The one listed paper's title states a finding about energy savings in fasting polar bears (Whiteman et al. 2015, Science 349:295): it bears on energy demand during a fast and is logged as contamination for F7.
- **Depth:** failed. Three literature queries, 89 papers screened, one kept (polar bears, two captures). Rodents were excluded wholesale as terminal-sampling designs, but classic prolonged-fasting work in rats used daily body mass and metabolic-cage nitrogen in the same animals. Repeated-capture bear studies, ground squirrels, bats and hedgehogs are missing.
- **Correct exclusions:** standard mouse phenotyping fasts last hours, not days (Mouse Phenome Database); metabolomics datasets come from terminal tissue.
- **Next:** a narrowed rerun on laboratory rodents only (TQ-DS1c-R), with the non-destructive repeated measures that qualify spelled out, at least 15 queries and 300 papers. Rodents are where energy demand is varied experimentally (cold, exercise), which F7 needs.

### TQ-DS1c-R assessment (5 October 2026)

- **Depth:** much improved: 410 records screened, 14 kept, counts reconcile. But every row is abstract-only, so data availability is unknown for all 14.
- **Identifiers:** at least two DOIs do not match their citations (Hillebrand 2005 and Atchley 2006 carry DOIs of 2003 and 1995 papers); the self-check claims all were verified.
- **Contamination:** one works-cited title states a finding on priority ("Brain More Resistant to Energy Restriction Than Body"), known in outline from the blood-loss and fasting tests. Logged.
- **Leads (not opened):** the CNRS Strasbourg rat fasting series (Cherel, Le Maho, Robin, Belkhou; daily body mass and nitrogen excretion through the three phases, with refeeding); lean against obese mice in total fasting (Cuendet et al. 1975; starting fat varied); the activity-based anorexia model (body mass and wheel running daily; ambient temperature varied in one study), which is restricted feeding, not a total fast.
- **Repositories:** none qualifying; modern deposits use short fasts or terminal sampling.

### Where H2 stands after six searches (5 October 2026)

No open repository holds a long fast followed in individual animals with repeated measures and varied energy demand. The classic individual series (rats, king and emperor penguins, geese) sit with one group, CNRS Strasbourg (IPHC), and the grey seal buffer experiment with the Sea Mammal Research Unit. These are the targets if access requests are made (James's call).

**Dieting and weight cycling (James, 5 October 2026):** catalogued first (TQ-DS1d), controlled designs only; surveys and observational data excluded even if supportive. Once the catalogue is in, the studies are split between a surface check of G15 and the held-out list, so the same studies are not used for both.

### TQ-DS1d assessment (5 October 2026)

- **No values reported in the text.** Several titles state findings. One bears on G15: the MATADOR trial (intermittent against continuous energy restriction), whose title states a result on weight-loss efficiency and whose name states its aim (minimising adaptive thermogenesis and obesity rebound). Logged as contamination for any weight-cycling test; MATADOR is not a candidate for holding out.
- **Coverage:** 8 controlled trials, all human; no human trial of repeated loss-and-regain cycles and no animal weight-cycling experiment was kept (animal studies were excluded as terminal designs, although the template allowed repeated body mass in the same animals). Classic metabolic-ward studies of weight perturbation are missing.
- **One label is wrong:** CALERIE phase 2 is listed as "deposited"; its data are released by application through the CALERIE portal (calerie.duke.edu), which James would have to make.
- **Leads (not opened):**
  - **CALERIE phase 2** (NCT00427193): two-year randomised trial of 25% calorie restriction against ad libitum, 220 adults, body composition, resting and total energy expenditure, hormones, at baseline, 12 and 24 months. A follow-up after the restriction ended is believed to exist (to confirm). This is a controlled human case of **chronic** restriction, and with a follow-up it would test G10 (reserve recovered first and overshooting after chronic scarcity) and G15;
  - **FS2** (Ebbeling et al. 2018, BMJ; NCT02068885): weight-loss maintenance after loss, total energy expenditure by doubly labelled water, 164 adults; no data statement;
  - **Hall et al. 2015** (metabolic ward crossover, 19 adults): group means only.

**Proposal (for James):** add **CALERIE phase 2** to the held-out list as a sixth system (H6: chronic energy restriction and its aftermath, humans), unopened; Claude knows the trial only in outline and not its regain results. For the G15 surface check, use sources outside the held-out list: animal weight-cycling experiments and metabolic-ward weight-perturbation studies, with predictions committed first.

### Decisions (James, 5 October 2026)

- **H6 added: CALERIE phase 2** (chronic energy restriction in humans and its aftermath; NCT00427193). Held out and unopened; data by application, to be made by James when the test is set up.
- **Weight cycling is not held out.** James: it is where anything that might shape the model further is likely to be, so it stays open for surface testing (G15), with predictions committed first. Sources: animal weight-cycling experiments and metabolic-ward weight-perturbation studies; MATADOR is already contaminated.
- **Access requests for fasting (H2):** drafts prepared (tests/correspondence/); James sends them within hours if the searches have not found enough.
