# Education workflow group — shared curriculum contract

> **Navigation**: [docs hub](../README.md) | [Documentation index](../documentation-index.md) | [Run guide](../RUN_GUIDE.md) | [Canonical schema](../../specs/education/schema.json) | [Member registry](../../specs/education/contract.json)

Eleven repositories circulate the same four things: **units**, **prerequisite edges**,
**learning objectives**, and **glossary terms**. This document is the contract that makes
them one vocabulary. It is enforced by `./run.sh contract`, which reads
[`specs/education/schema.json`](../../specs/education/schema.json) and every member
checkout named in [`specs/education/contract.json`](../../specs/education/contract.json).

The lead repository is `courses`. Members keep their own gate; nothing here replaces it.

---

## 1. The four records

One document per repository, `education-contract/v1`, validated against the canonical
schema. A worked example is
[`specs/education/examples/reference.json`](../../specs/education/examples/reference.json);
this repository's own bundle is
[`specs/education/active-inference.json`](../../specs/education/active-inference.json).

### Unit

| Field | Required | Meaning |
| --- | --- | --- |
| `unit_id` | yes | Stable identity, `^[a-z0-9][a-z0-9._-]*$`. Repository-qualified key is `<repository>#<unit_id>`. |
| `title` | yes | Learner-facing title, verbatim from the authored source. |
| `objectives` | yes | At least one [learning objective](#learning-objective). |
| `prerequisites` | yes | The inbound **hard** edges, denormalized. Must equal the edge set (rule EC108). |
| `course_id` | no | Owning course, when the repository has courses. |
| `topic` | no | One of the eight-topic spine: `systems`, `agents`, `perception`, `cognition`, `action`, `learning`, `communication`, `planning`. |
| `stratum` | no | One of the eight pedagogical strata of the validated prerequisite graph: `math_foundations`, `probability`, `information_theory`, `variational_methods`, `free_energy_principle`, `active_inference`, `computation`, `applications`. |
| `audience_level` | no | `es`, `family`, `ms`, `hs`, `101`, `core`, `401` — the ladder in [`course_development/AGENTS.md`](../../course_development/AGENTS.md). |
| `glossary_terms` | no | Term ids this unit uses; each must resolve in the same document (rule EC110). |
| `source_path` | no | Repository-relative path of the authored source. |

`topic` and `stratum` are different axes and both are optional: `topic` is the
curriculum's fixed eight-topic spine, `stratum` is the pedagogical layer of the
prerequisite graph that `Active_Skillference` renders. A unit may carry both.

### Prerequisite edge

| Field | Required | Meaning |
| --- | --- | --- |
| `from_unit` | yes | The unit that must come first. |
| `to_unit` | yes | The unit that depends on it. |
| `kind` | yes | `hard` blocks progress and must stay acyclic; `soft` is advisory and never enters `unit.prerequisites`. |
| `rationale` | yes | Why the edge exists, quoting the authored statement. |

### Learning objective

| Field | Required | Meaning |
| --- | --- | --- |
| `objective_id` | yes | Unique within its unit. Generated bundles use positional `obj-1..N`; authored bundles may use any stable id. |
| `statement` | yes | The objective, verbatim, at least 8 characters. |

### Glossary term

| Field | Required | Meaning |
| --- | --- | --- |
| `term_id` | yes | Stable identity. `Active_Skillference` and `cognitive` must reuse the same id for the same concept. |
| `term` | yes | Display form. |
| `definition` | yes | At least 20 characters. A cross-reference such as "See D_KL." is not a definition. |
| `source` | yes | Repository-relative path of the authored definition, or the citation. |
| `aliases`, `notation` | no | Alternate names; the symbol the term is written with. |

---

## 2. Canonical home per concern

| Concern | Canonical home | Why there | What a member does |
| --- | --- | --- | --- |
| Document schema (all four records) | [`specs/education/schema.json`](../../specs/education/schema.json) in `courses` | The lead owns the multi-course corpus and the only Python engine with a test gate. | Vendors a byte-identical copy at `specs/education/schema.json`. |
| Schema evaluation | [`software/src/education_contract/schema.py`](../../software/src/education_contract/schema.py) | Reads the schema file at call time; no second copy of the rules. | Calls it, or vendors it with the schema. |
| Coherence rules (DAG, edge/prerequisite agreement, term resolution) | [`software/src/education_contract/rules.py`](../../software/src/education_contract/rules.py) | JSON Schema cannot express them; one implementation for the group. | Runs it over its own bundle before committing. |
| Prerequisite graph semantics and rendering | `Active_Skillference` `src/curriculum/model.py` and `src/curriculum/graph.py` | It is the only member with a validated, rendered, exported prerequisite DAG (`CurriculumGraph.validate()`, `topological_order()`, `prerequisite_edges()`). | Exports its graph to `education-contract/v1`; the lead validates the export. |
| Glossary term corpus | `cognitive` `knowledge_base/glossary.md` | Largest authored term set in the group, with typed frontmatter and `[[wikilink]]` identity. | Emits terms with `term_id` equal to its wikilink target. |
| Member adoption state and drift | [`software/src/education_contract/registry.py`](../../software/src/education_contract/registry.py) | One place decides adopted / pending / diverged. | Commits the pointer and the vendored schema. |
| Course-tree transcription | [`software/src/education_contract/catalog.py`](../../software/src/education_contract/catalog.py) | Turns `course_development/` into a bundle without inventing fields. | Copies the extractor for its own tree shape. |

---

## 3. Rules

Schema violations are `EC0xx`; coherence rules are `EC1xx`; adoption rules are `EC2xx`.

| Rule | Rejects |
| --- | --- |
| EC101 | A `unit_id` declared twice in one document. |
| EC102 | An `objective_id` declared twice in one unit. |
| EC103 | A `term_id` declared twice. |
| EC104 | The same `from_unit` → `to_unit` edge declared twice. |
| EC105 | A unit that requires itself. |
| EC106 | An edge endpoint that is not a declared unit. |
| EC107 | A cycle in the **hard** edges. |
| EC108 | `unit.prerequisites` that does not equal the unit's inbound hard edges. |
| EC109 | The same pair declared both `hard` and `soft`. |
| EC110 | A `glossary_terms` entry that is not declared in `glossary`. |
| EC111 | The same term text defined twice under different ids. |
| EC112 | The same objective statement repeated inside one unit. |
| EC120 | Two repositories claiming the same `unit_id` (cross-document). |
| EC121 | One `term_id` meaning different things in two repositories (cross-document). |
| EC201–EC208 | A member pointer or bundle that is missing, unreadable, or invalid. |
| EC210–EC213 | The registry's own digest, contract identity, or contract-document path. |

---

## 4. Members

Gate commands are the member's own entry point, quoted from its file. `docs index` is the
member's documentation hub; `manuscript` is the command that renders its manuscript, or
`none` when the repository has no manuscript surface.

| Member | Gate command | Docs index | Manuscript | GNN pin |
| --- | --- | --- | --- | --- |
| `courses` | `./run.sh {lint,types,no-mocks,test,test-full,docs,contract,gnn,metrics,all}` (`run.sh:88`) | `docs/README.md`, `docs/documentation-index.md` | none (course outputs via `publish.py`) | `.github/gnn-pin.json` — `v5.0.3`, `8f293d9` |
| `cognitive` | **red**: `./run.sh` execs `code/scripts/gate.py`, which does not exist (`run.sh:4`); CI runs the arms directly (`.github/workflows/quality.yml:37,54-56,62,98-99,170,177`) | `docs/README.md` (no `documentation-index.md`) | `python -m scripts.build_manuscript --no-pdf --output <dir>` (`quality.yml:99`) | `specs/gnn-pin.json` — `v5.0.3`, `commit` |
| `fundamentals` | `./gate.sh {lint,fast,full,docs,validators,manuscript-check,manuscript,gnn,all}` (`gate.sh:166`) | `docs/README.md` (no `documentation-index.md`) | `./gate.sh manuscript` → `scripts/render_manuscript.py` | `specs/gnn-pin.json` — `v5.0.3`, `commit` |
| `GEN24` | `./run.sh {lint,test-fast,docs,gnn,test-full,fast,all}` (`run.sh:90`) | `docs/README.md`, `docs/documentation-index.md` | none | `NHIM/gnn-pin.json` — `v5.0.3`, `release` |
| `gen25` | `./run.sh {lint,links,counts,gnn,check,all,measure}` (`run.sh:136`) | `docs/README.md`, `docs/documentation-index.md` | none | `.github/gnn-pin.json` — `v5.0.3`, `8f293d9` |
| `Parr_et_al_2022_ActInf_Textbook` | `./run.sh {lint,plaintext,docs,vfe,gnn,fast,full,report}` (`run.sh:16`) | `docs/README.md`, `docs/documentation-index.md` | none (`Chapters/` notebooks, `TextbookContent/PlainText`) | `.github/gnn-pin.json` — `v5.0.3`, `8f293d9` |
| `ActiveInferenceImplementations` | `./run.sh {setup,lint,test-fast,test,docs,gnn,notebooks,gate}` (`run.sh:157`) | `docs/README.md`, `docs/documentation-index.md` | none | `specs/gnn-pin.json` — `v5.0.3`, `commit` |
| `ActiveInferenceCategoryTheory` | `./run.sh {docs,links,metadata,index,gnn,setup,all,measure}` (`run.sh:37`) | `docs/README.md`, `docs/documentation-index.md` | none | `.github/gnn-pin.json` — `v5.0.3`, `8f293d9` |
| `Symposium` | `./gate.sh {lint,test,test-fast,build,program,site,docs,gnn,list,all}` (`gate.sh:80`) | `docs/README.md`, `docs/documentation-index.md` | none | `.github/gnn-pin.json` — `v5.0.3`, `8f293d9` |
| `Start` | `uv run start-gate {lint,types,fast,full,docs,numbers,gnn,gnn-exemplar,artifacts,smoke,audit,lock,smoke-macos}` (`scripts/gate.py:65`, `pyproject.toml:73`) | `docs/README.md`, `docs/documentation-index.md` | none | `.github/gnn-pin.json` — `v5.0.3`, `8f293d9` |
| `Active_Skillference` | `./gates.sh {default,all,record,sync,lint,types,fast,test,artifacts,checks,docs,gnn,render}` (`gates.sh:107`) | `docs/README.md`, `docs/documentation-index.md` | `./gates.sh render` → `scripts/render_manuscript.py` | none — `GNN_ROOT` names a prepared checkout (`gates.sh:89`) |

Every member carries an `.aii/config.yaml` sidecar at `aii-sidecar/v1`. Ten of the eleven
list `docs/INTEGRATION.md` under `docs:`, and that file exists in none of them; `gen25`,
`ActiveInferenceImplementations`, `ActiveInferenceCategoryTheory` and `Symposium` also list
`docs/AGENTS.md`, which is absent in those four. `Parr_et_al_2022_ActInf_Textbook` is the
exception: ten entries, every one present. The sidecar's document list is unvalidated in
every member — a defect this contract records rather than inherits.

---

## 5. What the group repeats today

Measured on 2026-11-12 in the member checkouts. A concern copied in two repositories is
duplication; copied in four it is a contract.

| Concern | Copies | Evidence |
| --- | --- | --- |
| Gate-arm dispatch shell (`case` over arm names) | 10 | `courses/run.sh:88`, `fundamentals/gate.sh:166`, `GEN24/run.sh:90`, `gen25/run.sh:136`, `Parr_et_al_2022_ActInf_Textbook/run.sh:16`, `ActiveInferenceImplementations/run.sh:157`, `ActiveInferenceCategoryTheory/run.sh:37`, `Symposium/gate.sh:80`, `Active_Skillference/gates.sh:107`, `Start/scripts/gate.py:65` |
| Relative-link checker | 6 Python + 1 npx + 1 pytest | `courses/software/scripts/check_docs.py:51-55`, `Parr_et_al_2022_ActInf_Textbook/scripts/check_docs.py:33-36`, `Symposium/scripts/check_docs.py:24-70`, `ActiveInferenceCategoryTheory/.github/scripts/check_docs.py:45-68`, `GEN24/scripts/check_docs_links.py`, `ActiveInferenceImplementations/scripts/check_docs_links.py`, `Active_Skillference/scripts/check_docs_links.py`, `gen25/run.sh:138` (markdown-link-check), `fundamentals/gate.sh:59` (pytest contracts) |
| Gate-metrics generator | 4 | `courses/software/scripts/generate_gate_metrics.py`, `GEN24/scripts/gate_metrics.py`, `ActiveInferenceImplementations/scripts/measure_gates.py`, `Active_Skillference/scripts/z_generate_gate_metrics.py` |
| GNN pin loader + tag/commit peel + version assertion | 7 | `courses/software/scripts/verify_gnn_conformance.py:33-81`, `Parr_et_al_2022_ActInf_Textbook/scripts/check_gnn_conformance.py:36-57`, `ActiveInferenceCategoryTheory/.github/scripts/check_gnn.py:25-45`, `fundamentals/scripts/validate_gnn_spec.py:3-33`, `ActiveInferenceImplementations/scripts/validate_gnn_spec.py:3-63`, `Start/scripts/check_gnn_pin.py:19-46`, `gen25/scripts/gnn_conformance.py:32-72` |
| GNN pin file location and field names | 3 spellings | `revision`+`tag` (`courses/.github/gnn-pin.json`), `commit`+`tag`+`parser_files` (`cognitive/specs/gnn-pin.json`), `commit`+`release`+`parser_files` (`GEN24/NHIM/gnn-pin.json`); pin path is `.github/`, `specs/`, or `NHIM/` |
| Manuscript variable builder | 2 | `fundamentals/manuscript/variables.yaml` + `scripts/render_manuscript.py`, `Active_Skillference/src/manuscript/variables.py:24` + `scripts/render_manuscript.py` |
| Learning objectives written three times per unit | 513 units, 4 772 statements | `module.md` 1 835, `README.md` 1 307, `dashboard.html` 1 630; **0** units agree on all three, 283 agree between `module.md` and `dashboard.html` |
| Glossary authored per course in four formats | 14 files, 0 shared term ids | `course_development/*/resources/glossary.md`; bold-bullet, `###`-heading, and mixed layouts |
| Prerequisite chain expressed as ASCII art | 1 per course | `course_development/active_inference/resources/learning_pathways.md:12-21` |

The objective and glossary rows are why the schema exists: the same fact is authored
three times and already disagrees with itself.

---

## 6. Adoption

A member adopts the contract by committing three things:

1. `specs/education/schema.json` — a byte-identical copy of the canonical schema.
2. `education-contract.json` at the repository root:

   ```json
   {
     "contract": "education-contract/v1",
     "schema_sha256": "<sha256 of specs/education/schema.json>",
     "bundles": ["specs/education/<name>.json"]
   }
   ```

3. Each bundle named in `bundles`, validating against the schema and the rules above.

`./run.sh contract` reports `adopted`, `pending`, or `diverged` per member. A diverged
member fails the gate; `--strict` also fails a pending one. The digest is the drift test:
edit the canonical schema and every member that has not re-vendored it is reported as
diverged, with the expected and actual digests.

### Migration step per member

| Member | Migration step |
| --- | --- |
| `courses` | Done for `active_inference`: `specs/education/active-inference.json` is generated by `software/scripts/export_education_bundle.py --course active_inference` and checked by `--check`. Remaining: run the extractor for the other six spine-shaped courses (`active_inference_101`, `_401`, `_es`, `_family`, `_hs`, `_ms`), add each output to `bundles`, and author `prerequisite_edges` for the chain that `resources/learning_pathways.md` states as prose. `domains/` needs an authored `topic` per unit before it can be transcribed. |
| `cognitive` | Fix `run.sh` to exec an existing gate (or delete it and document the CI arms). Emit `specs/education/cognitive.json` from `knowledge_base/`: one unit per knowledge-base page, `glossary_terms` from `knowledge_base/glossary.md` with `term_id` equal to the `[[wikilink]]` target, and `prerequisite_edges` from `knowledge_base/learning_roadmap.md`. |
| `fundamentals` | Emit `specs/education/fundamentals.json`: one unit per `chapters/chapter_NN`, objectives from the chapter source, terms from `manuscript/98_symbols_glossary.md`. Add `./gate.sh contract` calling the vendored checker. |
| `GEN24` | Emit `specs/education/gen24.json` for the `GEN-24/` and `NHIM/` units; declare `topic` only where the unit maps to the spine. Normalize `NHIM/gnn-pin.json` to the group's pin spelling in the same change. |
| `gen25` | Emit `specs/education/gen25.json` for the generated course units; `gen25` has no test arm, so the contract check is its first executable content check. |
| `Parr_et_al_2022_ActInf_Textbook` | Emit `specs/education/parr-2022.json`: one unit per `Chapters/` notebook and per `TextbookContent/PlainText` chapter, objectives from the chapter text, `prerequisite_edges` from the book's own chapter order. |
| `ActiveInferenceImplementations` | Emit `specs/education/implementations.json`: one unit per notebook, `objectives` from the notebook's first markdown cell, `prerequisite_edges` from the notebook's stated dependencies. |
| `ActiveInferenceCategoryTheory` | Emit `specs/education/category-theory.json` from `IntroAdventureSyllabus.md` and `gnn/`; the syllabus is already a learning plan, so its sections become units. |
| `Symposium` | Emit `specs/education/symposium.json` from the `program` arm's session data; sessions are units, `prerequisite_edges` stay empty unless the program states them. |
| `Start` | Emit `specs/education/start.json` from `learning/curriculum_creation`; `Start` already generates learning plans, so its plan steps become units and its ordering becomes `prerequisite_edges`. |
| `Active_Skillference` | **Reference implementation.** Export `build_curriculum()` to `specs/education/skillference.json`: `Skill` → unit (`skill_id` → `unit_id`, `objective` → the first objective, `stratum` → `stratum`), `Skill.prerequisites` → `hard` edges, `Skill.related` → `soft` edges, `prerequisite_edges()` → `prerequisite_edges`. Then run the lead's checker over the export; a disagreement is a real defect in one of the two models. |

---

## 7. Verification

```bash
./run.sh contract                      # registry + every member copy
./run.sh contract --strict             # also fail members that have not adopted
./run.sh contract --json               # machine-readable report
./run.sh contract specs/education/active-inference.json   # one bundle
cd software && uv run python scripts/export_education_bundle.py --check
```

`./run.sh contract` is part of `./run.sh all`. It reads member checkouts; it never writes
to them.
