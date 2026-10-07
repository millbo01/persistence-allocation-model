# PAM: open checks before the paper claims its ground (started 7 October 2026)

**Purpose.** The DEB reading (theory/PAM_DEB_reading.md) left PAM four candidate contributions:
- (a) an order of loss across parts under shortage, fixed beforehand from documented access;
- (b) a repair network that competes for access, with the template deciding scar against recovery;
- (c) one governor with modes and gates named at mapping;
- (d) the ledger of where load goes.

Three checks were set before the paper claims any of them:
1. DEB work after 2010 on organ-level priority under starvation.
2. The physiology of organ sparing.
3. The neighbouring theories: allostasis, control theory, repair.

**Rules:** as for the DEB reading. Primary sources, read in full by Claude where open; only the abstract where a source is paywalled, and said so; comparisons marked **[comparison]**; not evidence for PAM.

## Check 1: DEB after 2010, organ-level priority under starvation

**Done (7 October 2026), within limits.** Six web searches with distinct wording (multiple structures, organs, starvation, the workload model, brain sparing, organ-specific maintenance), plus the leads already held.

**Found:**
- **No DEB model that orders organs by access under shortage.** The organ extensions remain the static and dynamic κ rules of the book (allocation by growth fraction or by workload), and starvation remains whole-body (shrinking, rejuvenation, changes in κ).
- **Two leads, unread:**
  - a DEB review for plants (*Conservation Physiology* 10, coac061, 2022), which might hold root-shoot priority under stress;
  - an insect growth model that splits maintenance into a "non-negotiable" and a "negotiable" part, with negotiable maintenance cut under food restriction (PMC10556006). **This is close to PAM's split between basal upkeep and renewal,** and is to be read.

**Systematic search 1 (7 October 2026; protocol theory/PAM_check1_search_protocol.md; results theory/search_check1/README.md):**
- PubMed and OpenAlex: 139 records screened, **0 included**; 4 function-priority models (all DEB-family) and 2 empirical records noted.
- **Sensitivity failed a known-item check:** Göbel et al. (2010) was not retrieved, and plant source-sink allocation models (organs with sink priority drawing on a phloem flow) fell outside the terms.
- **The null cannot be used in the paper.** A second search, with a known-item set and strands for plant source-sink models and organ competition for energy, is proposed.

**Systematic search 2 (protocol theory/PAM_check1_search2_protocol.md, revision 1 and deviation D-1; results theory/search_check1_s2/):**
- Sensitivity: all four design items found; held-out H1 (Thornley 1972) missed, so strand C is of limited sensitivity.
- **Answer to check 1: yes, formal models of organ order under shortage exist,** in three places:
  1. **Plant allocation models** (strand_C_reviews.md):
     - **hierarchical models,** with a strict priority sequence among organ groups (Wermelinger et al. 1991; Grossman and DeJong 1994);
     - **transport-resistance models,** where sink priority emerges from the transport network and sink kinetics (Thornley 1972; Minchin et al. 1993; Minchin and Lacointe 2005).
  2. **The Selfish Brain formal models** (Göbel, Peters and colleagues 2008 to 2013): brain priority through insulin-gated access.
  3. **DEB tumour-in-host models** (van Leeuwen et al. 2003; Tosca and colleagues 2018 to 2021): tumour and host compete by workload.
- **What none of them has** (as far as abstracts and the one full review show): loss of existing units, switching off and scars; repair competing for access; a conserved account of where unmet demand goes; viability; and application outside its own domain.
- **Open:** OpenAlex strand D (blocked by the daily budget); five CHECK records needing full text.

**Limit (earlier):** web searches are not a systematic review. If the paper is to say "no DEB model orders organs by access", that sentence needs a proper search: a database search with stated terms, run by Claude or by a sourcing model with a prompt. **Proposal for James below.**

## Check 2: organ-sparing physiology, formal models of the order of loss (7 October 2026)

**Method:** a targeted PubMed search with five stated strings, all 1,279 titles read, candidates read as abstracts. Record: theory/search_check2/README.md; script scripts/check2_search.py. Not a systematic review.

**Findings:**
- **Haemorrhage and central hypovolaemia: a large formal tradition exists.** The Guyton model and its descendants (HumMod, BioGears, Muse) and lumped-parameter closed-loop models with baroreflex control simulate regional redistribution. In recent calibrated models, renal resistance rises before carotid resistance (43 swine; Sadid et al. 2026) and splanchnic vasoconstriction is the dominant compensation in both sexes (35 adults under LBNP; Bergauer et al. 2026). Schlichtig et al. (1991) measured and modelled redistribution in dogs: liver and kidney shares of O2 delivery fell, and redistribution delayed whole-body O2 supply dependency.
- **The order is not written in as a rule.** It emerges from each bed's resistance, reflex gain and autoregulation, fitted to data. That is order from access properties, the same class as the plant transport-resistance models (check 1).
- **Fetal brain sparing:** formal fetal circulation models (Garcia-Canadilla et al. 2014; Luria et al. 2012) set the redistribution by cerebral against peripheral-placental resistance.
- **Starvation, many organs: no formal model of the order of organ loss found.** Formal starvation models found are two-compartment: Hall (2006; fat and lean) and the Selfish Brain (brain and body). The multi-organ order is held as data (Chossat-type tables; CALERIE 2 MRI organ masses), not as a model.
- **Empirical find:** Plaçais and Preat (2013, *Science*). Under starvation the Drosophila brain switches off costly aversive long-term memory; restoring it artificially costs survival.

**[comparison]**
- **PAM's blood-loss case is a domain case of the Guyton tradition.** Literature before formula: if PAM's engine is run on haemorrhage, it should take its circulation from an established lumped-parameter model, not invent one. PAM's contribution there is the reading (rank from access, the ledger, the threshold switch), not the haemodynamics.
- **The multi-organ starvation order remains a place where PAM's formal rule has no formal predecessor found,** within the limits of this search ("not identified is not absent").
- The haemodynamic models carry no repair, no units, no scars, and no account of where unmet demand lands beyond the circulation.

## Check 3 (begun): the nearest neighbours turned out to be two programmes outside DEB

The check 1 searches found two research programmes closer to PAM's governor than DEB is. **They change the novelty position more than anything in DEB did.**

### N1. Bobba-Alves, Juster and Picard (2022). The energetic cost of allostasis and allostatic load. *Psychoneuroendocrinology* 146:105951 (PMC10082134). Read in full.

**The model (EMAL), in the authors' terms:**
- A **finite total energy budget**, set by the capacity to transform energy (glycolysis, oxidative phosphorylation, limits to dissipation), not by food supply in modern humans.
- **Partition (Figure 2):** vital functions; growth, maintenance and repair ("GMR"); a **reserve capacity**, meaning spare transformation capacity, not stored fat; and the added cost of stress, "allostasis and stress-induced energy expenditure" (ASEE).
- **The transition from allostasis to allostatic load** "arises when the added energetic cost of stress competes with longevity-promoting growth, maintenance, and repair". Stress costs first consume the reserve; past it they "impinge on" GMR, and the "compression" of GMR "accelerat[es] the decay of structures" (Figure 3).
- **Priority:** "the most urgent processes divert or steal energy from less urgent ones"; stress responses carry "evolutionary-endowed biological urgency". Examples: exercise trading against reproduction and immunity; immune activation curbing growth in children; immune surveillance and wound healing "take a backseat".
- **Load can be hidden:** the organism "could divert energetic resources away from GMR, potentially **without elevating total energy expenditure**", measurable only by "the molecular sequelae of halting or slowing of GMR" (DNA damage, telomere shortening, reduced haematopoiesis).
- **Predictions:**
  1. Systems that need constant renewal (high-turnover immune cells, neurogenic hippocampus) are preferentially vulnerable.
  2. Vulnerability is greatest when growth costs are high (childhood).
- **Levels:** allostatic load at whole-body, cellular and mitochondrial levels, as the same process.
- **Buffers:** exercise and caloric restriction (efficiency or a larger budget); social support (cost savings).
- **Status:** narrative review and perspective. **No formal model, no order fixed in advance, energy only.**

**[comparison]**
- **The overlap with PAM is large:**
  - a requirement rise (stress) is met first from a reserve, then by cutting lower-priority work;
  - repair and renewal are cut first;
  - the cut is hidden from total expenditure (PAM's held record) and shows as residue in cells (PAM's state ledger);
  - high-turnover parts are hit first (PAM's renewal cut first; G23 a);
  - the same process at several levels (PAM's nested systems);
  - social support as an outside source (PAM's load met from outside the boundary).
- **For the biomedical case of chronic stress, EMAL already states PAM's story in words.** PAM cannot present that story as new there.
- **What PAM adds against EMAL:**
  1. a **formal** model;
  2. **any finite resource and any system**, not energy in bodies;
  3. an **order fixed beforehand from access properties**, where EMAL appeals to "urgency" judged after the fact;
  4. **a conserved ledger** (where every unit of load lands, including stores and across the boundary);
  5. **viability:** collapse against death, and the route back;
  6. **the template and scars.**
- **EMAL's prediction 1 is PAM's G23 (a) in other words.** If PAM's paper cites EMAL as convergent, G23 (a) cannot be presented as a novel prediction for immune and neural renewal.

### N2. Achim Peters and colleagues: the Selfish Brain theory (Peters et al. 2004 onward; formal models by Göbel and colleagues, 2010 to 2011)

**Read:**
- Sprengell, Kubera and Peters (2021a). Brain more resistant to energy restriction than body: a systematic review. *Front Neurosci* 15:639617 (PMC7900631). **Read in full.**
- Sprengell, Kubera and Peters (2021b). Proximal disruption of brain energy supply raises systemic blood glucose: a systematic review. *Front Neurosci* 15:685031. **Abstract and first page only** (full PDF held locally, not yet read).
- Göbel and colleagues (2010), *Theory in Biosciences* (doi 10.1007/s12064-010-0105-9). **Abstract only (paywalled).**
- Shaulson, Cohen and Picard (2024), the brain-body energy conservation model of ageing, *Nature Aging*. **Abstract only (paywalled).**

**The theory, in its authors' terms:**
- The brain is "an independent, self-regulating organ delimited by the blood-brain barrier", which gives "priority to the own energy metabolism" and occupies "a primary position in a hierarchically organized energy metabolism".
- It is both consumer and "superior regulatory instance". The rival theory, gluco-lipostatic, treats the brain as passively supplied.
- **Mechanism, named as access gates:**
  - an energy-deprived brain (neuronal ATP sensors in the ventromedial hypothalamus and amygdala) activates the sympathoadrenal system;
  - this **suppresses insulin** ("cerebral insulin suppression");
  - which shuts the **insulin-dependent** glucose route into muscle and fat (GLUT-4);
  - while the brain draws through the **insulin-independent** route (GLUT-1), which "safeguards basal energy supply of vital organs, like brain and immune cells".
- **Supply-chain framing:** "As in economic supply chains, where goods stay on the shelves when customers don't buy, energy accumulates in adipose tissue when the brain demands less energy" (Peters and Langemann 2009).
- **Method:** each prediction is tested by a **pre-registered systematic review** (PROSPERO; PRISMA), with a hypothesis-decision algorithm fixed in advance, set against a rival theory's prediction.
- **Result (2021a):**
  - under caloric restriction (13 studies; 8 decidable; rats, mice, sand gazelles, women), all 8 confirmed "minor mass (energy) changes in the brain as opposed to major changes in the body";
  - brain −7.4% to +0.3%, against body −11% to −40%.
- **Göbel's model:** a compartment model (periphery, blood, brain) with insulin as the brain's feedback signal and "competition for energy between brain and body periphery", formally specified and simulated (abstract only).
- **The brain-body energy conservation model** (abstract only): when cells accumulate damage they signal hypermetabolism to the brain, which "deploys energy conservation responses, which suppress low-priority processes, producing fatigue, physical inactivity, blunted sensory capacities, immune alterations and endocrine 'deficits'".

**[comparison]**
- **This is PAM's architecture for one top part and one resource, already formalised and tested:**
  - a protected top that is also the regulator;
  - access set by a signal (insulin) acting on gates with documented properties (insulin-dependent against insulin-independent transporters);
  - the periphery losing first;
  - stores (adipose) filling when the top's draw falls;
  - and a rival "passively supplied" theory that predicts otherwise.
- **The order of loss here is fixed from documented access properties,** which is exactly PAM's claim (a), for two compartments.
- **The method is PAM's phase 5 method, before PAM:** pre-registered tests of predictions that separate the theory from a rival.
- **The brain-body energy conservation model is PAM's governor economising** ("suppress low-priority processes" on a sensed signal of rising requirement).
- **What PAM adds against the Selfish Brain:**
  1. **many parts and a full order** (heart and brain spared, gut and kidney cut, skin cut first), not brain against periphery;
  2. **several resources** (oxygen, protein, iron, money);
  3. **systems other than bodies** (institutions: PT1's G25);
  4. the repair network and scars;
  5. viability;
  6. the conserved ledger.
- **The paper must cite this programme as the nearest formal precedent for (a) and (c) in physiology,** and frame PAM as the generalisation.

### Check 3 continued (7 October 2026, second session): eight more neighbours

**Read in full:** Sterling 2018 (*eLife*, PMC6025954); Noakes 2012 (*Front Physiol*, PMC3323922); Straub 2014 (*Arthritis Res Ther*, PMC4249495); Ames 2006 (*PNAS*, PMC1693790).
**Abstracts only:** Sterling 2012 (*Physiol Behav*); Schulkin and Sterling 2019 (*Trends Neurosci*); Noakes 2000 (*Scand J Med Sci Sports*); Hochachka et al. 1996 (*PNAS*; the open copy is a scanned PDF); Buttgereit and Brand 1995 (*Biochem J*); McCann and Ames 2009 (*Am J Clin Nutr*) and 2011 (*FASEB J*); Drenos and Kirkwood 2005 (*Mech Ageing Dev*); Powers 1973 (*Science*); Gucciardi et al. 2026 (*Health Psychol Rev*); Kiecolt-Glaser et al. 1995 (*Lancet*).

### N3. Sterling: allostasis, predictive regulation (2012; 2018; Schulkin and Sterling 2019)

**The theory, in its author's terms:**
- Regulation is predictive, not error-correcting. The brain "predicts needs and set[s] priorities", "coordinates effectors to mobilize resources from modest bodily stores and enforces a system of flexible trade-offs: from each organ according to its ability, to each organ according to its need" (2012, abstract).
- Efficiency principles: match the capacities of components to avoid bottlenecks; "resources are shared between systems to minimize reserve capacities"; only express circuits that are needed.
- A worked example of routing: "if gut is empty, send blood from gut to muscle; otherwise, send blood from kidney to muscle" (2018, Figure 1).
- A circadian clock sets catabolic mode for foraging and anabolic mode "to grow and repair".
- **Hypertension under treatment (2018):** the brain predicts a need for high pressure. A diuretic shrinks the volume; the brain compensates through the vessels. A calcium antagonist relaxes the vessels; the brain raises cardiac output. A beta blocker closes that route, and the patient can no longer exercise. "All of our control systems are designed with multiple compensatory loops."
- Chronic prediction remodels the parts: arteries thicken and stiffen, and the system "loses the ability to resume normal pressure".
- **Status:** essay and review. No formal model; no order fixed in advance.

**[comparison]**
- Sterling's brain is PAM's governor in words: a predictive regulator that sets priorities and routes flows, with modes (catabolic and anabolic).
- **The hypertension sequence is PAM's ledger in words:** blocking one route moves the load to the next route until the last route is closed, and the cost lands on exercise capacity. Load relocated, not removed, as a clinical story.
- Arterial remodelling is PAM's scar: a lasting structural change that stops the return to baseline.
- "To each organ according to its need" is not PAM's rule. PAM fixes the order from access, not from need judged by the brain. Sterling gives no order of loss.
- **What PAM adds:** a formal model; an order fixed beforehand; the ledger as an account, not a story; viability; units.

### N4. Noakes: the central governor model of exercise (2000; 2012)

**The theory, in its author's terms:**
- Exercise is "regulated in anticipation specifically to insure that no such biological failure can ever occur". A governor in the brain sets how many motor units are recruited, from feedforward expectation and continuous feedback.
- **There is always a reserve:** only 35 to 50% of active muscle is recruited in prolonged exercise and about 60% in maximal exercise. The end spurt shows the reserve was there.
- Exercise "terminates whilst homeostasis is retained in all bodily systems"; there is no catastrophic failure of any organ at exhaustion.
- Fatigue is a brain-generated sensation used as the control signal. Tucker's model: a subconscious "template" for the rise of perceived exertion, matched against feedback by adjusting power output.
- Hill's 1924 model already contained a "governor" to protect the ischaemic heart; it dropped out of the textbooks.
- **Status:** narrative review; conceptual model; tested piecemeal in experiments, not as a formal model.

**[comparison]**
- **The governor stops the work before passive failure, and always keeps a reserve.** That is the refinement proposed from the blood-loss test (natural test 1, mismatch 2: an active threshold switch in the control part, before passive failure), and the fasting phase III switch. Noakes states it for exercise.
- **Units switched off:** de-recruited motor units are PAM's switched-off units, held in reserve and recoverable.
- The protected quantity is "homeostasis in all bodily systems", not a ranked order. Noakes does not set which part loses first.
- **Vocabulary clash:** Noakes and Tucker's "template" is a pacing plan for perceived exertion. PAM's template is a different thing. The paper must say so if both appear.
- **What PAM adds:** the order of loss; repair; the ledger; resources other than muscle drive; a formal model.

### N5. Straub: the selfish immune system and the "controllable amount of energy" (2014)

**The theory, in its author's terms:**
- Insulin resistance is "an acute catabolic program" that moves fuel from insulin-dependent stores (fat, muscle, liver) to insulin-independent consumers: the brain and the immune system. Straub calculates the size: about 974 kJ a day from hepatic insulin resistance, roughly 39% of the brain's need or 61% of resting immune cells' need.
- **A floor and a negotiable remainder:** about 8,500 kJ a day (the minimal metabolic rate) is "not up for negotiation between the different organs". The rest, up to the gut's absorptive limit, is the "controllable amount of energy" (CAEN), "regulated and negotiated between organs".
- **Two governors:** "either the immune/repair system or the central nervous system is a dominant regulator of the CAEN", on "the same hierarchical level". In chronic inflammation the immune system silences the brain (sickness behaviour); in chronic stress the brain inhibits the immune system.
- **Time limit set by the store:** stores last 19 to 43 days under systemic inflammation, so energy-consuming programmes were selected to end within 3 to 6 weeks. A chronic programme is "a misguided acute program".
- The immune system is named throughout as "the immune/repair system", and a large energy consumer (up to 20,000 kJ a day in extensive burns).
- **Status:** review with explicit energy arithmetic; "aspects of hypothetical character". No formal model.

**[comparison]**
- **The floor and the CAEN are PAM's protected floor and the free flow above it,** with numbers.
- **Access by insulin dependence** is the Selfish Brain's gate, extended to the immune system: order set by a documented transport property.
- **Repair as a claimant that can take priority** (trauma, infection) is PAM's repair competing for access, in words.
- **The acute against chronic split** matches PAM's acute-chronic flip; the store sets how long a costly mode can run, which is PAM's store-limited mode duration.
- **Two governors: absorbed (James, 7 October 2026).** Straub's two co-equal regulators are two **modes** of one governor function, not two governors. In v0.18 the governor is a function, not an organ (Section 14), and "a signal produced inside a part belongs to the governor function" (Section 1, item 6), so cytokines and stress hormones are both governance signals. "Taking control" is a signal selecting a mode (Section 4, item 4): inflammation selects an immune/repair setting, threat a fight-or-flight setting; insulin resistance is the gate each opens. No new mechanism. The rank stays fixed; what changes is the mode (so a change of allocation here is not a rank reversal).
- **Kept as evidence for an open question:** Straub's chronic cases (inflammation silencing the brain-led setting; chronic stress suppressing the immune setting) bear on v0.18 Section 12, "Governors as modes, and whether rarity sets which wins". A possible later prediction about mode precedence, not a mechanism.
- **What PAM adds:** a formal model; many parts and a full order; resources other than energy; the ledger as a conserved account; viability; units.

### N6. Hochachka: a unifying theory of hypoxia tolerance (1996; abstract only)

**The theory, in the authors' terms (abstract):**
- Two phases: **defence** and **rescue**.
- Defence: "a balanced suppression of ATP-demand and ATP-supply pathways", with energy charge held at a new steady state while ATP turnover falls up to 10-fold. Ion pumping is cut by channel arrest (liver cells) and spike arrest (neurons); protein synthesis by translational arrest.
- Rescue: an oxygen sensor (a haem protein) and signal transduction lead to gene-based "metabolic reprogramming", with the down-regulation held.
- In hypoxia-sensitive cells the translational arrest "seems irreversible".

**[comparison]**
- Defence then rescue are **modes,** switched by a sensor: PAM's modes and gates at cell level.
- Arrest of channels, spikes and translation is **units switched off,** with the held figure (energy charge) defended while throughput falls.
- **Tolerant against sensitive** is PAM's collapse against death: the same arrest is reversible in one cell type and terminal in another.
- Translational arrest (growth and renewal) is among the first cuts: compare N8.
- **What PAM adds:** the order among consumers as a rule; the ledger; scars.

### N7. Ames: the triage theory of micronutrient allocation (2006; McCann and Ames 2009, 2011)

**The theory, in the author's terms:**
- "As the scarcity of a micronutrient increases, and **after homeostatic adjustments, such as induction of transport proteins,** a triage mechanism for allocating scarce micronutrients is activated that favors short-term survival at the expense of long-term health, in part through **an adjustment of the binding affinity of each protein** for its required micronutrient."
- **At every level:** "in metabolic reactions, enzymes involved in ATP synthesis would be favored over **DNA-repair enzymes**; in cells, erythrocytes would be favored over leukocytes; and in organs, the heart would be favored over the liver."
- Mechanisms named: isozymes with different binding constants; preferential distribution (dietary vitamin K1 to the liver to keep coagulation); iron "prioritized to erythroid and hemoglobin synthesis, putting the nonerythroid tissues at risk".
- The cost is hidden and slow: "insidious changes accumulate", raising cancer, ageing and neural decay, while critical functions such as ATP production stay intact.
- **Tested against a classification fixed first:** McCann and Ames classified vitamin K-dependent proteins (2009; 16 proteins) and selenoproteins (2011; 12) as essential or not from knockout lethality, then checked which lose first under deficiency. "On modest selenium deficiency, nonessential selenoprotein activities and concentrations are preferentially lost, with one exception" (Dio1 in thyroid, which they predict is conditionally essential). The selenium mechanism is an access property: a tRNA form sensitive to selenium deficiency.
- **Status:** hypothesis papers with literature tests. No formal model; not pre-registered.

**[comparison]**
- **This is the closest neighbour outside energy.** Order under shortage set by **access properties** (binding affinity, transport, distribution, tRNA), for **many resources** (about 40 micronutrients), at **several levels** (enzymes, cells, organs), with **intake raised first** (transporter induction) and **repair cut first** (DNA repair against ATP synthesis).
- **The hidden cost** that shows later as disease is PAM's state ledger: the held record (ATP production) stays normal while damage accumulates.
- **Iron** is one of PAM's own mapped resources; Ames already states erythroid priority for iron.
- **Method:** a classification fixed from independent evidence (knockout lethality), then checked against the order of loss. That is close to PAM's discipline of fixing rank before outcomes, though the classification uses essentiality, not access, and the tests were not pre-registered.
- **For PAM's claims:**
  - (a) Order from documented access now has precedents in three resources (glucose, Selfish Brain; carbon, plant transport-resistance; micronutrients, Ames) and in haemodynamics (check 2).
  - (b) "Repair is cut first" is stated by Ames for DNA repair, by EMAL for growth, maintenance and repair, and by Hochachka for protein synthesis. PAM cannot present the idea as new; only its formal network (rank among repair recipients, the template and scars, G23 b).
- **What PAM adds:** a formal model; one rule across energy, oxygen, micronutrients and non-biological systems; the conserved ledger; viability; units; pre-registered tests.

### N8. Buttgereit and Brand (1995): a measured hierarchy of ATP consumers (abstract only)

- In stimulated thymocytes (over 80% of ATP use accounted for), "there was a clear hierarchy of the responses of different energy-consuming reactions to changes in energy supply": **protein synthesis and RNA/DNA synthesis most sensitive, then sodium cycling, then calcium cycling; mitochondrial proton leak least sensitive.**
- Metabolic control analysis: control over ATP flux "widely shared; no block of reactions had more than one-third of the control". "Each ATP consumer had strong control over its own rate but very little control over the rates of the other ATP consumers."

**[comparison]**
- **A measured order of loss among consumers of one resource, at cell level:** growth and renewal (macromolecule synthesis) lose first, ion homeostasis is held, the leak is last. The same order as PAM's (renewal cut first; the support that keeps the part alive held).
- **The order emerges from the kinetics of each consumer (its elasticity to supply), with no central regulator.** At this level there is no governor; control is distributed. That is a case PAM's governor must reduce to, or a level where PAM's governor is only a description.
- **Established mathematics:** metabolic control analysis (elasticities, control coefficients) is the standard formalism for how supply shortage is shared among consumers. Added to the maths work queue (literature before formula).

### N9. Control theory: perceptual control theory and cascade control (abstracts and background)

- **Powers (1973):** behaviour is "the control of input, not output". Control is hierarchical: "the output of a higher-order system is not a muscle force, but a reference level (variable) for a lower-order controlled quantity". The top references are inherited; "reorganization" changes the structure.
- **Gucciardi et al. (2026)** apply it to stress: stress arises from goal conflict, "where simultaneous reference values cannot be satisfied, leading to persistent error"; reorganisation resolves it by revising references or creating new control systems.
- **Cascade control** (engineering, background knowledge, not read here): an outer loop sets the set-point of an inner loop.

**[comparison]**
- PAM's governor setting the held figures for lower parts is a cascade or perceptual-control hierarchy. **The maths of the governor is standard control theory,** as the maths map already records; PCT adds the idea that a governor controls its sensed figures, which is PAM's held record and the measurement rule (the record can stay normal while state moves).
- **Goal conflict as persistent error** is close to PAM's two held figures that cannot both be met under shortage, where the rank decides. PCT has no rank; conflict persists until reorganisation. PAM's rank is the rule that resolves the conflict before reorganisation.
- PCT has no resource, no store and no ledger: it is a theory of control structure, not of allocation.

### N10. Repair under competing demand

- **Disposable soma** (Kirkwood; Drenos and Kirkwood 2005, formal): optimal investment in somatic maintenance and repair is "less than what would be required for indefinite longevity", traded against growth and reproduction. **An optimisation account,** like the plant optimality models: repair is set by fitness, not by access. A contrast for PAM, as in check 1 (Franklin et al.).
- **Kiecolt-Glaser et al. (1995):** a 3.5 mm punch wound took 48.7 days to heal in 13 women caring for a relative with dementia against 39.3 days in 13 matched controls; their leucocytes made less IL-1β. Repair slowed under chronic load, in an experiment.
- **Plaçais and Preat (2013, check 2):** under starvation the fly brain switches off costly aversive long-term memory; forcing it back on costs survival. The protected top economises inside itself: PAM's units switched off within the top part, and the cost of overriding the governor.
- **Not yet read:** wound-healing energetics and nutrition (protein and micronutrient limits on healing), and repair-capacity models outside biology (maintenance backlogs). Left for the paper's repair section.

### What this does to the four candidate contributions

| Claim | Before these checks | Now |
|---|---|---|
| (a) Order of loss from documented access | Candidate (not in DEB) | **Precedent in physiology for two compartments** (Selfish Brain: insulin-gated access; brain spared). PAM's contribution is the **general rule:** many parts, per resource, any system, order fixed beforehand. G25 in councils is a test outside physiology |
| (b) Repair competing for access | Candidate (not in DEB) | **Stated in words by EMAL** (growth, maintenance and repair squeezed first; high-turnover systems hit first). PAM's contribution is the **formal network** (rank among repair recipients, G23 b, the template and scars), not the idea that repair is cut first |
| (c) One governor, modes, gates | Candidate (DEB adds control case by case) | **Precedent:** Selfish Brain (the brain as consumer and superior regulator, formal model) and the brain-body energy conservation model (suppressing low-priority processes). PAM's contribution is **generality and the mapping discipline** (modes and gates named before data) |
| (d) The ledger of where load goes | Candidate | **Not found in DEB, EMAL or the Selfish Brain as a conserved account.** EMAL's "steal" and "hidden" diversion is the idea in words; the Selfish Brain's supply chain is close. Still the strongest candidate |

**Working conclusion (Claude's, for James).** PAM's novelty is now best stated as:
1. **a general, formal theory** of regulated access to finite resources under shortage, across parts, resources and kinds of system, of which DEB (energetics), the Selfish Brain (brain against periphery) and EMAL (stress against growth, maintenance and repair) are domain cases;
2. **the conservation ledger** (load relocated, never removed);
3. **the discipline** that fixes order, modes and gates from documented access before outcomes;
4. **viability and the template** as the account of collapse, death and scars.

That is a smaller and more defensible claim than "the governor and order of loss are new". It also gives the paper a clear structure: three domain theories, one general model, and predictions that separate it (G25 outside biology; G23 b; G24 cascades; the ledger).

**Update after N3 to N10 and check 2 (Claude's, for James):**
- **(a) Order from access:** precedents now in glucose (Selfish Brain), carbon (plant transport-resistance), micronutrients (Ames triage, several levels) and blood flow (haemodynamic models, check 2), with a measured cell-level order (Buttgereit and Brand). In most of them the order **emerges** from access properties rather than being fixed beforehand from them. PAM's distinct step is fixing the rank from documented access **before** outcomes and applying the same rule to any resource and system.
- **(b) Repair cut first:** stated in words by EMAL, Ames (DNA repair), Hochachka (translational arrest) and Straub (the immune/repair system as a claimant); measured by Buttgereit and Brand (macromolecule synthesis most sensitive). PAM's remaining contribution is the formal repair network (rank among repair recipients, G23 b, the template and scars).
- **(c) The governor:** in words in Sterling, Noakes and Straub; formal in the Selfish Brain and the haemodynamic models. Straub's two co-equal governors are absorbed as two modes of one governor function (James, 7 October 2026). Noakes's governor stopping work before passive failure, with a reserve always kept, supports the threshold-switch refinement from natural test 1.
- **(d) The ledger:** still not found as a conserved account of where unmet demand lands. Sterling's hypertension sequence (each blocked route moves the load to the next) and Straub's kJ arithmetic are the nearest statements. **Still the strongest candidate,** with viability, units and scars.

## James's position (7 October 2026)

Reframe accepted as the working basis, with his reasons:
1. PAM reached the same structure without having read EMAL or the Selfish Brain. It was PAM's own proposition, even though the paper cannot claim priority.
2. The Selfish Brain theory is a single-domain theory; PAM is more general. Every theory builds on earlier ones.
3. Had PAM been published without finding them, the novelty would still have been mainly the combination and unification of PAM's own and others' findings. **Prior findings validate and add weight.** Many more existing works will need acknowledging.

**Claude's note, agreed framing:** the independence is partial. PAM drew on the same physiology (fasting tables, haemorrhage, shorebirds), so the paper presents convergence, not separate discovery.

**How prior work will be handled: a unification table** (to build as reading goes on). Rows are prior theories; columns are PAM's components (governor, access and rank, stores, the units rule, repair, the load ledger, viability and the template); each cell says whether the theory has the component and in what form. The table is the unification argument. Its empty columns show what is PAM's own. Each new find fills a cell instead of threatening the claim.

## Still open

- **Check 1:** OpenAlex strand D (after the daily reset); five CHECK full texts; why held-out H1 was missed.
- **Check 2:** done at search level (above). Read in full, if the paper leans on them: Sadid et al. 2026 and Bergauer et al. 2026 (calibrated order of bed resistances); Peters and Boyd 1968 (organ weights in starvation).
- **Check 3:**
  - Peters and Langemann (2009), the brain's supply chain (open access, to read);
  - the second Selfish Brain review in full;
  - the insect "negotiable maintenance" model;
  - Hochachka 1996 in full (scanned PDF) and Buttgereit and Brand 1995 in full (PMC1136240);
  - wound-healing energetics and repair-capacity models outside biology.
- **Unification table:** first version built (theory/PAM_unification_table.md); fill cells as reading goes on.

## Sources found in this check (links)

- Bobba-Alves, Juster, Picard (2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC10082134/
- Sprengell, Kubera, Peters (2021a): https://pmc.ncbi.nlm.nih.gov/articles/PMC7900631/
- Sprengell, Kubera, Peters (2021b): https://www.frontiersin.org/articles/10.3389/fnins.2021.685031/full
- Göbel et al. (2010), abstract: https://link.springer.com/article/10.1007/s12064-010-0105-9
- Shaulson, Cohen, Picard (2024), abstract: https://www.nature.com/articles/s43587-024-00716-x
- Sterling (2018): https://pmc.ncbi.nlm.nih.gov/articles/PMC6025954/
- Noakes (2012): https://pmc.ncbi.nlm.nih.gov/articles/PMC3323922/
- Straub (2014): https://pmc.ncbi.nlm.nih.gov/articles/PMC4249495/
- Hochachka et al. (1996): https://pmc.ncbi.nlm.nih.gov/articles/PMC38456/
- Ames (2006): https://pmc.ncbi.nlm.nih.gov/articles/PMC1693790/
- Buttgereit and Brand (1995): https://pmc.ncbi.nlm.nih.gov/articles/PMC1136240/
- McCann and Ames (2009), PubMed 19692494; (2011), PubMed 21402715
- Plaçais and Preat (2013), PubMed 23349289
- Negotiable maintenance in insects: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556006/
- DEB for plants (2022): https://academic.oup.com/conphys/article/10/1/coac061/6701566
