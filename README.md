# Record for "From cells to councils: a conservation law of allocation under scarcity"

**From cells to councils: a conservation law of allocation under scarcity.** James Miller, independent researcher. ORCID: [0009-0009-6595-647X](https://orcid.org/0009-0009-6595-647X).

- **Preprint (SSRN):** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7579199. DOI: [10.2139/ssrn.7579199](https://doi.org/10.2139/ssrn.7579199).
- **This record on Zenodo (all versions):** [10.5281/zenodo.23222615](https://doi.org/10.5281/zenodo.23222615).
- **Version 2 of the paper** (9 October 2026) is release v2.0. Version 1's permanent copies: v1.3, as last posted ([10.5281/zenodo.23241491](https://doi.org/10.5281/zenodo.23241491)), and v1.2, the first posting ([10.5281/zenodo.23224208](https://doi.org/10.5281/zenodo.23224208)). What changed is stated in the paper's section "Changes from version 1".
- **Full commit history in Software Heritage:** swh:1:snp:9d74b3d245ecd46518ffda7b11a718a37bed3e07 (snapshot after release v1.3). The paper cites the earlier snapshot swh:1:snp:cbdafe9b4e6c27ea5f2ce307d86ebcd49ca11fcf (after v1.1), which holds the same history up to that point.

## What this is

This repository is the record behind the paper. It was extracted from the author's working repository with its commit history and dates preserved.

**The paper:**
- **The paper:** `papers/pam-model/From cells to councils.md`.
- **The supplement:** `papers/pam-model/From cells to councils - supplement.md`.
- **The paper as posted to SSRN** (the paper with the supplement appended): `papers/pam-model/From cells to councils.pdf`. It is built from the two Markdown files by `scripts/build_pdf.py`.
  - The current version is version 2, of 9 October 2026 (release v2.0).
  - Version 1 as last posted, the revision of 8 October 2026 that added five figures, is release v1.3; the first SSRN version, of 7 October 2026, is release v1.2.
- **The figures:** `papers/pam-model/figures/`, as PNG and SVG.
  - `scripts/make_figures.py` computes them from the model's reduced form, with nothing fitted. In version 2 the file `fig5` is Figure 4 (PT1), which reads `tests/results/PT1/summary.json`, and `fig4` is Figure S1.
  - The script also writes a square image for a social-media post. That image is not part of the record.
- **The reference check:** `papers/pam-model/Citation check.md`. Every reference was checked against Crossref, PubMed or OpenAlex (or, for one book, its publisher's contents page), with corrections listed.

**The record behind it:**
- **The laws of the model:** `CANON.md`, with its dated log. The model document and the paper are checked against it.
- **The model:**
  - the current version, `theory/PERSISTENCE_ALLOCATION_MODEL_v0.20.md` (version 1's was `theory/PERSISTENCE_ALLOCATION_MODEL_v0.19.md`, kept);
  - the two versions the held-out tests were derived from: `theory/TIER_QUEUE_MODEL_v0.17.md` for H1 and `theory/PERSISTENCE_ALLOCATION_MODEL_v0.18.md` for PT1.
- **The derived propositions and their numerical check:** the working derivations in `theory/PAM_propositions_DRAFT.md`, and the check in `scripts/pam_propositions_check.py` with its output. The check covers version 2's order of the draw, the dependency lag and the recovery lag, and keeps version 1's checks as records. The paper states the propositions in their final form.
- **The comparison with prior theories, the open checks and the probe register:** `theory/PAM_*`.
- **The natural-system checks:** `theory/natural_test_*`.
- **The literature searches:** `theory/search_check*/` and their protocols.
- **The two held-out tests (H1 and PT1):** in `tests/` and `raw/`. That covers their pre-registrations, setting maps, procedure logs, prompts, scripts, results, replications and blind adjudications.
  - **The corrected H1 mapping** (version 2; made after the result, post hoc, and not a test): `tests/H1 VitalDB G12 - mapping corrected (v2).md`, beside the frozen setting map, which is unchanged.
  - **The G18 follow-up** (exploratory, post hoc, not scored): `tests/scripts/h1_g18_followup.py` and `tests/results/H1-VDB-G18-followup/`.

**Why some record files still say "draft":** names such as `setting map and mapping (draft).md`, `design note (draft).md` and `PAM_propositions_DRAFT.md` are kept exactly as they were when the tests were run, because the frozen pre-registrations and other records cite them by name. The paper files were renamed on 8 October 2026 (from `08 Paper draft 3.md`, `03 Supplement draft 1.md` and `04 Citation check.md`), and git keeps their full history across the rename.

**Earlier versions are in the history.** Earlier drafts of the paper, earlier versions of the model (from v0.1 on 5 October 2026), and working files were removed from the current files on 7 October 2026, after release v1.0. They remain in the commit history with their dates.
- **To see them:** open a file's history on GitHub, or run `git log --all -- <path>` and `git show <commit>:<path>`.
- **The v1.0 archive on Zenodo** holds all of them as files.

Commit dates are the working repository's own. Commit hashes differ from the working repository's, because the history was filtered; the map below links the hashes cited in the records to their new values.

**Changes made at extraction:**
- **One superseded file version was removed:** the log of PT1's first run, which stopped with an error before producing any result. It contained local file paths. The run is described in the PT1 procedure log (`tests/PT1 Priority test - procedure log.md`).
- **The local username in file paths was replaced with "USER".**

Nothing else was altered.

## Frozen files and their fingerprints

Each SHA-256 below was checked against the value recorded when the file was frozen, before any outcome data was opened. All match.
- **Line endings matter.** A checkout on Linux or macOS gives LF line endings; a checkout on Windows with default settings gives CRLF. Both values are listed, and the bold one is the form recorded at freezing.
- **To check:** `git show "HEAD:<path>" | sha256sum` gives the LF value.

| File | Frozen | SHA-256, LF | SHA-256, CRLF |
|---|---|---|---|
| `tests/H1 VitalDB G12 - pre-registration.md` | 6 October 2026 (commit 0f69c2c) | **371caf3c998f32accd4e0a8da47aa22ec9fe879ed1c2cd3c4aa98f3c6555863e** | 2e28ebd8fcfd97b63ab7ec76966c28fc29206c2a391650d06283ec6c041e14ca |
| `tests/scripts/h1_vdb_g12.py` (H1 analysis code) | Before the data were opened, 6 October 2026 | 08ef16811b2408acbf1f3e0003c0d56f6ae7b0fe9ef4c7c9c0f43456eecc224c | **9fbe80d7909388fc481210b3488658622ecd9b01cc2b8be0c1af64fd678c0c03** |
| `tests/PT1 Priority test - pre-registration.md` | 7 October 2026 (commit c9916b7) | **a4aab81db592a30d52b847d2d7d5c6977d18fe6881c239713143d729acc8e3c1** | 533558700670fed795a75ce58f70f53d6f9c3083db05dba03e70db4cd27896b6 |
| `tests/scripts/pt1_councils.py` (PT1 analysis code) | Before the data were opened, 7 October 2026 | a9c397172a2eef36a74085912874f02f7aa530210cc74686ce00a4d40d9be7cd | **995abfc5949f07feb1a9cb0d0ad11357bc8f5071062e462accfa1396e4b25540** |
| `tests/PT1_statutory_classification.csv` (blind classification) | Before the data were opened, 7 October 2026 | e89627ae943b2a9f7d52b2d5d094dd0ea2276569e2def22cdead9032fdca6c3e | **faf4587523c85a17461090a2a854b93ed17fb7de264b49ef49784da6fbfe1d52** |

## Commit hashes cited in the records

The records cite commits of the working repository. Each is mapped here to its hash in this repository.
- **"Not in this record"** means the commit changed only working files outside this repository (for example reading notes). Its date is from the working repository.
- **All dates are British Summer Time.**

| Working-repo hash | Date | This repository |
|---|---|---|
| d1ccfaf | 2026-10-04 19:38 | not in this record |
| 4c63b20 | 2026-10-04 20:57 | not in this record |
| 9f19a05 | 2026-10-04 21:10 | not in this record |
| c372d7d | 2026-10-04 22:48 | not in this record |
| 131a005 | 2026-10-05 06:33 | not in this record |
| b5495f7 | 2026-10-05 06:48 | 172f2fd |
| b995525 | 2026-10-05 07:15 | 9c17873 |
| ffba866 | 2026-10-05 08:11 | not in this record |
| 4f013e9 | 2026-10-05 08:28 | 8439000 |
| 3a44916 | 2026-10-05 08:41 | fe70b93 |
| b8dbd1a | 2026-10-05 08:52 | 4be70e5 |
| 53b240f | 2026-10-05 11:46 | 14eec95 |
| 7b71d7b | 2026-10-05 13:00 | 1b7f6ce |
| a06cc46 | 2026-10-05 14:02 | 5519f4d |
| ae7d8a2 | 2026-10-05 15:41 | c4acc87 |
| 64654c7 | 2026-10-06 13:23 | 0f69c2c (H1 pre-registration frozen) |
| bbe553b | 2026-10-07 11:11 | c9916b7 (PT1 pre-registration frozen) |
| 2b22980 | 2026-10-07 13:37 | df8fc23 |

## The adjudication rules G1 and G5

Both held-out tests were adjudicated blind against fixed rules (`tests/ADJUDICATION_RULES.md`).
- **G1 and G5 refer to standards in an earlier document** that was not given to the adjudicator. G5's text names the earlier framework.
- **Both adjudications record that G1 and G5 changed no verdict:**
  - `raw/2026-10-07_chatgpt_H1-VDB-ADJ1.md`;
  - `raw/2026-10-07_chatgpt_PT1-ADJ1.md`.

## The author's earlier framework

The work began from the author's earlier framework for institutions, dated 27 September 2026.
- **It is held privately** and is available from the author on request.
- **Fingerprints:** the SHA-256 of each of its files, as held in the working repository, is listed below. These match the values recorded when the files were exported on 2 October 2026.
- **Checking a copy:** a copy supplied on request can be checked against these values.

| File | SHA-256 |
|---|---|
| 01 | 9125b8261f91533d8237a435bb2c3a6b9d94d6eca4a823eeba7c5a73f5a05428 |
| 02 | c2bc4c396d9934afc45a46f2dda85f128d2a3aa20de3416fbf0d57db1ce21ea6 |
| 03 | f3545b460ab6e0b832e0ed4a9cdb61a7722fc0cbe5d91ad73994a6bca69f25a9 |
| 04 | a34a9c8d53e522632ee3e71a91d3660d5449b6400c9d996fda3787603ace163e |
| 05 | a15fec075262a1ba018253f81c44eebe1e853157003e0b22eaa2fdd2ad7c48ff |
| 06 | 6dca8fbf4af8a1a563df06c3ab388850679404cccb3905dd5c1c7e4d5d508ffe |
| 07 | f861ff11b37c54a7219b1382349e1612202c1c193965aceef6ee6af735333dc7 |
| 08 | a99c18e222834635f8693e82dcf72289e769dba494df14f7eddfa8a88ee2f3a9 |
| 09 | f2d60406f6ce6e68fd9244c604f682d522a8291602da2223bf9e98d736443292 |
| 10 | 833fa7ee145df31337c054648b519d0393683a8e04d0f9e76bd221f5d2d69d1b |
| 11 | 9faad0773e0da7fdcd3cd3448f99a12ebaa4e022238a610ef96ee21a61dae410 |
| 12 | a861662741623de85521213640df696d2cf4ca2b27b95b2c98a37b5a01a0e43b |
| 13 | 60416e64ad3e83eaedfcfbf605e43a661bd27d24061731ff9480d2ce19d9b481 |
| 14 | a150177b786cc4d7f5104c36ae022d1c5c102d38ce068dc157ca45700201b071 |
| 15 | 6ad71c3244fbbe2d06484dff2b086c45cd58437c9378a2e55dcc59452cb43953 |
| 16 | 4cec33171fc665d0cb7b1ff7470605d056e1398f2e9e7ca96423430ffda1f47c |
| 17 | 7564eeeec62a7bd1018619adf3aa9a6cd90a83b944d404e79ad2e47bac8e6ae6 |
| 18 | ea643a2a4cf85ce97dec0e218ff2cb0ff333078d31cd4258737a02d1a0b48a86 |
| 19 | 89b7442122f80ee8b251f562cc26fa4c6ce79456575e8c7ead9737733aae3384 |
| 20 | fcd5b0bfebcfe0bb77a9c4c20b7af410421f739bce6657c391a7cad8350a19f8 |
| 21 | 51fc433cf102e8170741b9d5977b8bce3762b852c622931752e682d2743acc69 |
| 22 | f63a8cf18b4c658b7f4f23b34e921befa0933a3bba4cc2cbdbe250b2e81651b0 |
| 23 | c7568fb518e87122d26496898b4f3d7086288dd7497fe80602589980b2c8d6f4 |
| 24 | 19ca372ca2f1dc8df757258cbea698210a9462785b8719b14241b4cf1327c939 |
| 25 | 80fb8e8050daef7132b7a4905604fb8b4a92ad9a7cb3a405eaddb5ab624bfbd9 |
| 26 | f636cb49af937783860181a53b55a8153440404bc6e3a3bd00adef66a5c66ff5 |
| 27 | 17e889bc322ca886c8c28cff1e71db868d599b5b6aca972a6d7435092583661b |
| 28 | 3931948fb9ddd01696156d104eba7b723e4213c651b5a931fdc7fc11137bc80d |
| 29 | 2f8e9affcc0305d63a9fd045d453c9671171dec15d85c1e93072143cdf91a572 |
| Manifest | 2f1c4f8323822c85328e540a4d7df23e491c90223bd15828b3f4a3a41fde9383 |

## Archives

- **Zenodo** (the files at each release): concept DOI 10.5281/zenodo.23222615, which always resolves to the latest version.
- **Software Heritage** (the full commit history with its dates): snapshot swh:1:snp:cbdafe9b4e6c27ea5f2ce307d86ebcd49ca11fcf, taken on 7 October 2026 after release v1.1.
- **SSRN:** posted on 7 October 2026 (abstract ID 7579199, DOI 10.2139/ssrn.7579199), revised on 8 October (release v1.3), and revised to version 2 (release v2.0). Release v1.2 matches the first posted version.

## Licence

Text, documents and data are under CC BY 4.0; code is under MIT. See LICENSE.md.

## How the work was done

- **Authorship:** the model was built by one author working outside academia, with an AI system (Claude, Anthropic) as collaborator for the mathematics, literature searches, numerical checks and drafting.
- **Predictions first:** predictions were committed before sources or data were opened.
- **Tests:** each held-out test was replicated by a different AI system (ChatGPT, OpenAI). It wrote its own analysis script without seeing the data or the results. The same system then adjudicated blind, against rules fixed in advance, in a separate session with no shared context.
