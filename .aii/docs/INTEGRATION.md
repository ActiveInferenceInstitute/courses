# InstituteOS integration — courses

## Identity

| Field | Value |
| --- | --- |
| Repository | `ActiveInferenceInstitute/courses` |
| Affiliation | `institute` |
| Category | `education` |
| Status | `active` |
| Maturity | `released` |
| Steward | Active Inference Institute |
| Default branch | `main` |
| Current release | — |
| License | `CC-BY-4.0` |
| Citation | Active Inference Institute — courses. |

## Federation

| Setting | Value |
| --- | --- |
| Dashboard mode | `repos` |
| Analytics | `true` |
| Dashboard | `true` |
| Sync policy | `pull` |
| Registries | — |
| Tags | courses, education, learning, active-inference, html |

## Ecosystem relations

| Repository | Relation | Note |
| --- | --- | --- |
| `ActiveInferenceInstitute/InstituteOS` | `referenced-by` | Federated via the InstituteOS .aii manifest. |
| `ActiveInferenceInstitute/Active_Inference_Ontology` | `references` | Uses Active Inference Ontology terms. |
| `ActiveInferenceInstitute/ActiveInferenceJournal` | `referenced-by` | Featured in Institute materials. |

## Key artifacts

| Path | Kind | Description |
| --- | --- | --- |
| `README.md` | `doc` | Repository overview. |
| `AGENTS.md` | `doc` | Agent guidance. |
| `LICENSE` | `doc` | License. |
| `CHANGELOG.md` | `doc` | Changelog. |

## Portable tasks

| Task | Command | Working directory | Description |
| --- | --- | --- | --- |
| `inventory` | `git ls-files` | `.` | List tracked files. |

## Validation

```bash
python -m aii_platform.aii_sidecar.validate <repo> --completeness
python -m aii_platform.aii_sidecar docs <repo> --overwrite
python -m aii_platform.aii_sidecar.run <repo> --list
```

The sidecar is valid when `validate` prints `OK` and reports no missing artifact,
manifest, link, or declared-doc path. Completeness is a curation target, not a
runtime requirement.

## Data boundary

This sidecar carries metadata only. It does not grant execution permission, does not
replace the repository's own documentation, and must not be used to move private
content into a public repository. Task execution is limited to trusted checkouts.
