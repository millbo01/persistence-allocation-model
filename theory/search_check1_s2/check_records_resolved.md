# Check 1, search 2, strand D: the five CHECK records resolved (7 October 2026)

**Inclusion rule** (as in screening_D_pubmed.csv): a formal model; two or more compartments draw on a shared limiting resource; supply under shortage (or raised requirement) specified. Classes as in strand C: I-fixed (order assigned), I-access (order from transport, gating or autoregulation), I-emergent (order emerges from kinetics or fitted dynamics).

| Rec | Record | Read | Decision | Reason |
|---|---|---|---|---|
| S01762 | Fois, Maule, Giudici, Valente, Ridolfi and Scarsoglio 2022, *Front Physiol* (PMC8892183): multiscale 1D-0D model, head-up tilt | **Full text** | **Include, I-access** | Formal, validated against in vivo tilt data. Baroreflex and cardio-pulmonary reflex constrict peripheral resistances and venous tone; cerebral autoregulation (Ursino and Lodi) sets cerebral arteriolar resistance from the mismatch between current and reference cerebral blood flow, and "CBF is almost perfectly conserved over all simulated positions". The brain's protection comes from a local rule at its own bed against a broadcast constriction elsewhere: the same class as the check 2 haemodynamic models |
| S01682 | Tripoli, Ridolfi and Scarsoglio 2026, *J Physiol* (paywalled): multiscale model, 0 g to 3 g | Abstract only | **Include, I-access (provisional)** | An extension of S01762's model (coronary and cerebrovascular-ocular circulations; short-term regulation). Provisional until the full text is read |
| S01848 | Feuerstein, Backes, Gramer, Takagaki, Gabel, Kumagai and Graf 2016, *J Cereb Blood Flow Metab* (PMC5094298): cortical spreading depression | **Full text** | **Include, I-emergent** | A mass-conserving neuron and glia compartment model fitted to microdialysis and FDG-PET data. Under a raised requirement, astrocytes draw their own glycogen store first, which "leaves 80% of blood-borne glucose to neurons"; neurons use lactate only when it is more than 80% above normal. Single-cell and two-cell-without-glycogen versions failed to fit. Order emerges from the store and the kinetics |
| S01690 | Coggan, Shichkova, Markram and Keller 2025, *PLoS Comput Biol* (PMC12002639): neuro-glia-vasculature model, GLUT1 deficiency | **Full text** | **Include, I-emergent (weak)** | Formal; glucose passes blood to endothelium to astrocyte (GLUT1) to neuron (GLUT3) in series. Under reduced import, astrocytic metabolites vary more than neuronal ones ("metabolic shock absorbers"). The order is a by-product of the transport topology, not the paper's subject; neurons still lose ATP (seizures) |
| S01827 | Kadota et al. 2018, *J Theor Biol* (paywalled): brain-centred glucoregulatory model with leptin, type 1 diabetes | Abstract only | **Exclude (probable), X-no-competition** | The abstract describes control of blood glucose by leptin and insulin, not compartments competing for a shared resource under shortage. Revisit only if the full text is obtained |

## What this adds

- **Strand D now has 16 includes:** 8 I-access (the 7 Selfish Brain models, plus the tilt model), 7 I-emergent (the 6 DEB tumour-in-host models, plus the spreading-depression model), and 1 weak I-emergent (GLUT1). There is also 1 provisional I-access (S01682) and 1 probable exclude (S01827).
- **[comparison] Two new forms of access-based protection, both in PAM's terms:**
  - **A local rule at the protected bed** (autoregulation against a broadcast constriction). This is v0.18 Section 1, item 1: "each pathway responds by rules encoded locally".
  - **A neighbour drawing its own store first,** which leaves the shared supply to the protected part (astrocytic glycogen). This is PAM's stores drawn first, at cell level.
- **Neither model loses units, has repair or keeps a ledger,** and both are single-domain.
