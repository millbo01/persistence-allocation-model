# H1 G18 follow-up (exploratory, post hoc, not scored)

**Date:** 8 October 2026. **Asked for by:** James's v2 prompt, decision D5.
**Status:** exploratory and post hoc. It is not part of the H1 test, it changes no verdict, and it carries no weight. H1's verdict stands: G12 Fails, at half weight.

**Method.**
- **Script:** `tests/scripts/h1_g18_followup.py`. It imports the frozen H1 code (`tests/scripts/h1_vdb_g12.py`, SHA-256 9fbe80d7) unchanged and re-runs its cohort selection from the frozen `counts.json` (fallback cohort; high-loss threshold 15% of estimated blood volume; 25 high-loss cases).
- **Output:** `g18_followup.json`, with every case's correlations.
- **Check:** it reproduces the frozen G18 figures exactly (MAP-HR +0.1258, 25 cases; MAP-SV −0.0018, 12 cases).

**What the frozen G18 figure measures.**
- **Tracks:** mean arterial pressure (MAP) from the Solar8000 arterial line. Heart rate (HR) is the Solar8000 HR track, valid 20 to 250. Stroke volume (SV) is the Vigileo/SV track, or EV1000/SV where Vigileo is absent: a 2-second numeric value in mL per beat from a cardiac output monitor, valid 5 to 250, per the VitalDB track list (`raw/2026-10-06_gemini_H1-VDB-S1.md`). How those monitors derive stroke volume is not stated here (to be sourced).
- **Correlation:** in each 10-minute window, the Pearson correlation of detrended MAP with detrended HR (or SV), in 10-second bins.
- **Windows:** early (E) is 31 to 21 minutes before the fall; late (L) is 11 to 1 minutes before it.
- **The figure:** per case, the change from E to L at the fall, less the median change at control times in the same case (stable stretches of the same high-loss cases). It is the median of that across cases.

**Raw correlations (medians, with interquartile ranges in g18_followup.json).**

| Pair | Cases | At the fall, E | At the fall, L | Controls, E | Controls, L | Cases moving away from zero |
|---|---|---|---|---|---|---|
| MAP-HR | 25 | +0.157 | +0.327 | +0.196 | +0.122 | 72% |
| MAP-SV | 12 | −0.068 | −0.008 | −0.019 | −0.022 | 42% |

**Reading.**
- **The HR correlation was positive and moved away from zero:** median +0.16 to +0.33 before falls, against +0.20 to +0.12 at control times. In the late window pressure and heart rate moved together, not in opposition.
- **The SV correlation stayed near zero,** with half the cases negative in each window, and did not move away from zero.
- **What this cannot show:** the measure cannot separate a support loop absorbing knocks from the arithmetic link between the two (mean arterial pressure is made partly of heart rate; to be sourced before it is stated in the paper) or from a common driver. A loop that buffers pressure would be expected to move against it. That expectation is a physiology claim, to be sourced before it is used.
