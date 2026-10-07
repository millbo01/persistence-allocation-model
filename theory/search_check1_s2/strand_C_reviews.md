# Check 1, search 2, strand C via reviews (deviation D-1): plant allocation models among organs

**Selection** (rule fixed in the protocol before searching):
- The title filter matched 73 strand C records. Claude selected those reviewing or theorising **models** of allocation among plant organs.
- All four hand-search reviews were also retrieved by the search: Lacointe 2000 (S02028), Génard et al. 2008 (S01996), Franklin et al. 2012 (S01230), Minchin and Lacointe 2005 (S01429).

**Access:**

| Status | Records |
|---|---|
| **Read in full** | Marcelis and Heuvelink (2007), *Concepts of modelling carbon allocation among plant organs* (S02001; open PDF, Wageningen repository) |
| **Abstract only (bot-check, CAPTCHA, wall; not bypassed)** | Lacointe 2000; Franklin et al. 2012 |
| **Abstract only (paywalled)** | Minchin and Lacointe 2005; neutral theory 2024 (S00388) |
| **Abstract only** | 1989 and 1993 reviews; Chinese review 2006 (S02795); EcoMeristem 2016 (S02467); eco-evolutionary optimality 2023 and 2026 (S04573, S02322) |
| **Title only (paywalled, no abstract in records)** | Cannell and Dewar 1994 (S01989); Génard et al. 2008 (S01996); agricultural crop models 2008 (S02007); rice 1996 (S02806) |
| **Excluded on reading** | S02132 and S02645, "theory of sink strengths": materials physics (point defects under irradiation), not plants |

## The classes of model, and how each sets the order among organs under shortage

From Marcelis and Heuvelink 2007 (in full) and Lacointe 2000 (abstract); consistent with the 2006 review and Franklin et al. 2012 (abstracts).

| Class (authors' names) | How allocation is set | Order under shortage | Code | Key works named |
|---|---|---|---|---|
| **Descriptive allometry** / empirical allocation coefficients | Predetermined ratios between organ growth rates, changing with development stage | Fixed fractions; shortage scales all organs together | I-fixed | Goudriaan and Van Laar 1994; most crop models (Wilson 1988) |
| **Functional equilibrium** / growth rules / "goal-seeking" (teleonomic) | Root to shoot mass in balance with their activities (W_r/W_s ∝ A_s/A_r) | **Shortage of a resource shifts allocation towards the organ that acquires it** (less nitrogen: more to roots; less light: more to shoots) | I-emergent (teleonomic) | Brouwer and De Wit 1969; Reynolds and Thornley 1982; Mäkelä 1986; Ågren and Ingestad 1987 |
| **Optimal response, game-theoretic, adaptive dynamics, eco-evolutionary optimality** | Allocation maximises a fitness proxy, or arises from eco-evolutionary dynamics | Set by marginal costs and benefits | I-emergent (optimisation) | Franklin et al. 2012; DAESIM2-Plant (2026); eco-evolutionary optimality (2023) |
| **Sink regulation, proportional** | f_i = S_i / ΣS: share by sink strength (potential growth rate), from one common pool | **Shortage shared in proportion to sink strength** | I-emergent (proportional) | Marcelis 1994, 1996; Heuvelink 1995; GreenLab (Kang and De Reffye) |
| **Sink regulation, hierarchical** ("hierarchical models", Lacointe 2000) | A priority sequence of organ groups: the first group is supplied by sink strength; later groups only from what is left | **Strict priority: later groups lose first** | **I-fixed (strict)** | Wermelinger et al. 1991 (grapevine); Grossman and DeJong 1994 (PEACH) |
| **Transport-resistance** (Münch flow, electric-network analogy) | Flow from source to sink proportional to a pressure or concentration gradient over a transport resistance; use in the sink by Michaelis-Menten kinetics | **Priority emerges from the transport system and sink kinetics.** "Sink priority being an emergent property of the model"; carbon flow depends "not only on the properties of the sink, but also on the properties of the whole transport system" (Minchin and Lacointe 2005) | **I-access** | Thornley 1972, 1976; Dewar 1993; **Minchin et al. 1993**; Minchin and Lacointe 2005; Prusinkiewicz et al. 2007; Allen et al. 2007 |
| **Canonical** (power-law flux equations) | Fluxes between compartments in a standard power-law form | Depends on fitted influences | I-emergent | Voit and Sands 1996; Renton et al. 2007 |
| **Neutral theory** (2024; null model) | Random allocation over the biochemical network from photosynthesis | **A "neutral hierarchy": storage, then defence, then respiration, then growth, by biochemical distance from photosynthesis** | I-emergent (network distance) | S00388 (2024) |

**What the reviews also say:**
- **On weakness:** "The simulation of carbon allocation among plant organs is one of the weakest features of crop growth models" (Marcelis and Heuvelink 2007). There is "still no unequivocal theory". Lacointe 2000: the model classes "can be conceptually closer to each other than is readily apparent".
- **Against transport as the deciding factor in crops:** "in many crops dry-matter allocation among plant organs is primarily determined by the sink strengths of the organs, whereas neither the source strength nor the transport path are dominating factors" (Marcelis 1996). Transport-resistance models are therefore "in many cases unnecessarily complex", though transport "may become important" in large plants such as trees.

## [comparison] What this means for PAM

1. **PAM's reduced form has a direct precedent.** Its ordered draw by phase and rank (maths, Section 2) is the plant "hierarchical model": groups supplied in a fixed priority sequence, later groups only from what is left (Wermelinger et al. 1991; Grossman and DeJong 1994). Strict lexicographic priority among organs under shortage has been formalised and used in tree and vine models since the early 1990s. **Cite it; do not claim it.**
2. **PAM's claim (a), that order follows from access, has its plant form in transport-resistance models,** where sink priority emerges from the transport network and sink unloading (Thornley 1972; Minchin et al. 1993; Minchin and Lacointe 2005). This matches v0.18's definition of rank as "a coarse-grained property of the network: topology, pathway capacity, gating" and the maths' max-flow pathways. **The strongest convergence found so far, and a precedent for (a).**
3. **The crop-model counterpoint matters, and must be stated:** in many crops the order follows sink strength, not the transport path. In PAM's terms, sink strength is access at the receiving end (unloading capacity, transporters), like DEB's carrier-density account of κ. So it is still "access", but the paper must say that receiving-end gates can dominate the route, and that rank is not set by the network topology alone.
4. **Functional equilibrium converges with PAM's intake rule.** Under nitrogen shortage, plants shift allocation to roots, the organ that takes the scarce resource in. That is PAM's "the intake is maintained at all costs" and support before ordinary work, already formalised for root and shoot in 1969.
5. **Optimality models are the contrast.** Franklin et al. (2012) frame allocation as maximising a fitness proxy. PAM treats persistence as a constraint, not a quantity maximised (v0.18, scope), and its rank is fixed from access, not derived by optimisation. **A real difference of approach,** to state in the paper alongside DEB's argument against fitness maximisation (DEB reading, S4).
6. **The neutral theory's "neutral hierarchy"** (order from biochemical distance to the source) is an order emerging from network topology alone. It is a null model PAM's access-based rank must be distinguished from.
7. **What the plant models do not contain, as far as these reviews show:**
   - they model the partitioning of new growth; none describes loss of existing units, switching off, repair competing for access, scars or the template;
   - there is no conserved account of where unmet demand goes;
   - there is no viability criterion;
   - nothing is applied outside plants.
   
   Fruit abortion under low source-sink ratio (Marcelis 1994) is the nearest thing to a loss rule.

**Answer to check 1, strand C:** yes. Formal models of organ order under shortage exist in plant science, including **strict priority** (hierarchical models) and **order emerging from access** (transport-resistance). The answer is limited by held-out item H1 being missed, and by most reviews being read as abstract only; neither weakens a positive finding.
