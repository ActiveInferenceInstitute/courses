"""Tests for the education contract: schema, rules, transcription, and member drift.

Every test reads a real file or writes one into ``tmp_path``; nothing is mocked.
"""

from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

import pytest

from src.education_contract import (
    ADOPTED,
    DIVERGED,
    PENDING,
    MemberSpec,
    build_bundle,
    check_contract,
    check_member,
    load_registry,
    render_bundle,
    run_cross_rules,
    run_rules,
    schema_digest,
    validate_document,
    validate_pointer,
)
from src.education_contract.registry import REGISTRY_PATH
from src.education_contract.schema import DEFAULT_SCHEMA_PATH, load_schema

ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT / "specs" / "education" / "examples" / "reference.json"
BUNDLE = ROOT / "specs" / "education" / "active-inference.json"
REGISTRY = ROOT / REGISTRY_PATH


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def codes(issues) -> set[str]:
    return {issue.code for issue in issues}


@pytest.fixture()
def reference() -> dict:
    return load(REFERENCE)


def test_canonical_schema_declares_every_record() -> None:
    schema = load_schema()
    assert schema["$defs"].keys() >= {"id", "pointer", "unit", "objective", "edge", "term"}
    assert schema["properties"]["schema"]["const"] == "education-contract/v1"


def test_reference_example_conforms(reference: dict) -> None:
    assert validate_document(reference) == []
    assert run_rules(reference) == []


def test_committed_bundle_conforms() -> None:
    document = load(BUNDLE)
    assert validate_document(document) == []
    assert run_rules(document) == []
    assert len(document["units"]) == 32
    assert len(document["glossary"]) == 69


def test_committed_bundle_matches_the_course_tree() -> None:
    """The bundle is a transcription; a changed tree must fail this test, not drift."""
    assert render_bundle(build_bundle("active_inference")) == BUNDLE.read_text(encoding="utf-8")


def _document_with(record: str, instance: dict) -> dict:
    """Place one record instance into an otherwise valid document."""
    document = {
        "schema": "education-contract/v1",
        "provenance": {"repository": "ActiveInferenceInstitute/courses"},
        "units": [],
        "prerequisite_edges": [],
        "glossary": [],
    }
    if record == "unit":
        document["units"] = [instance]
    elif record == "objective":
        document["units"] = [
            {
                "unit_id": "u",
                "title": "U",
                "objectives": [instance],
                "prerequisites": [],
            }
        ]
    elif record == "edge":
        document["units"] = [
            {"unit_id": "a", "title": "A", "objectives": [{"objective_id": "o", "statement": "x" * 8}],
             "prerequisites": []},
            {"unit_id": "b", "title": "B", "objectives": [{"objective_id": "o", "statement": "y" * 8}],
             "prerequisites": ["a"]},
        ]
        document["prerequisite_edges"] = [instance]
    else:
        document["glossary"] = [instance]
    return document


@pytest.mark.parametrize("record", ["unit", "objective", "edge", "term", "pointer"])
def test_every_required_field_is_enforced(record: str) -> None:
    """Bind the Python validator to the schema file: each required key must be required."""
    schema = load_schema()
    required = schema["$defs"][record]["required"]
    assert required, f"{record} declares no required fields"

    if record == "pointer":
        instance = {
            "contract": "education-contract/v1",
            "schema_sha256": schema_digest(),
            "bundles": ["specs/education/x.json"],
        }
        for field in required:
            broken = {key: value for key, value in instance.items() if key != field}
            assert "EC008" in codes(validate_pointer(broken)), field
        return

    document = load(REFERENCE)
    instance = {
        "unit": document["units"][0],
        "objective": document["units"][0]["objectives"][0],
        "edge": document["prerequisite_edges"][0],
        "term": document["glossary"][0],
    }[record]
    for field in required:
        broken = {key: value for key, value in instance.items() if key != field}
        assert "EC008" in codes(validate_document(_document_with(record, broken))), field


def test_unknown_field_is_rejected(reference: dict) -> None:
    document = copy.deepcopy(reference)
    document["units"][0]["difficulty"] = "hard"
    assert "EC009" in codes(validate_document(document))


def test_unknown_topic_is_rejected(reference: dict) -> None:
    document = copy.deepcopy(reference)
    document["units"][0]["topic"] = "metaphysics"
    assert "EC003" in codes(validate_document(document))


def test_hard_cycle_is_rejected(reference: dict) -> None:
    document = copy.deepcopy(reference)
    document["prerequisite_edges"].append(
        {
            "from_unit": "computer-science",
            "to_unit": "philosophy",
            "kind": "hard",
            "rationale": "closes the loop on purpose",
        }
    )
    document["units"][0]["prerequisites"] = ["computer-science"]
    assert "EC107" in codes(run_rules(document))


def test_prerequisite_denormalization_must_match_edges(reference: dict) -> None:
    document = copy.deepcopy(reference)
    document["units"][1]["prerequisites"] = []
    assert "EC108" in codes(run_rules(document))


def test_soft_edge_is_advisory(reference: dict) -> None:
    document = copy.deepcopy(reference)
    document["prerequisite_edges"].append(
        {
            "from_unit": "philosophy",
            "to_unit": "mathematics",
            "kind": "soft",
            "rationale": "useful background, not a gate",
        }
    )
    assert run_rules(document) == []


def test_same_pair_cannot_be_hard_and_soft(reference: dict) -> None:
    document = copy.deepcopy(reference)
    document["prerequisite_edges"].append(
        {
            "from_unit": "philosophy",
            "to_unit": "cognitive-science",
            "kind": "soft",
            "rationale": "contradicts the hard edge",
        }
    )
    assert "EC109" in codes(run_rules(document))


def test_unknown_glossary_reference_is_rejected(reference: dict) -> None:
    document = copy.deepcopy(reference)
    document["units"][0]["glossary_terms"] = ["free-energy-principle"]
    assert "EC110" in codes(run_rules(document))


def test_duplicate_term_text_is_rejected(reference: dict) -> None:
    document = copy.deepcopy(reference)
    document["glossary"].append(
        {
            "term_id": "active-inference-alias",
            "term": "active inference",
            "definition": "A second definition of the same concept under another id.",
            "source": "specs/education/examples/reference.json",
        }
    )
    assert "EC111" in codes(run_rules(document))


def test_cross_document_term_drift_is_rejected(reference: dict) -> None:
    other = copy.deepcopy(reference)
    other["provenance"]["repository"] = "ActiveInferenceInstitute/cognitive"
    other["glossary"][0]["definition"] = "A different definition of the same term id."
    issues = run_cross_rules(
        {
            "ActiveInferenceInstitute/courses": reference,
            "ActiveInferenceInstitute/cognitive": other,
        }
    )
    assert "EC121" in codes(issues)


def test_cross_document_unit_collision_is_rejected(reference: dict) -> None:
    other = copy.deepcopy(reference)
    other["provenance"]["repository"] = "ActiveInferenceInstitute/Start"
    issues = run_cross_rules(
        {
            "ActiveInferenceInstitute/courses": reference,
            "ActiveInferenceInstitute/Start": other,
        }
    )
    assert "EC120" in codes(issues)


def test_pointer_digest_must_be_sha256() -> None:
    pointer = {"contract": "education-contract/v1", "schema_sha256": "abc", "bundles": ["x.json"]}
    assert "EC004" in codes(validate_pointer(pointer))


def _adopt(member_dir: Path, *, schema_bytes: bytes, digest: str, bundle: dict | None) -> None:
    """Write a member checkout that claims adoption of the contract."""
    member_dir.mkdir(parents=True, exist_ok=True)
    (member_dir / "specs" / "education").mkdir(parents=True, exist_ok=True)
    (member_dir / "specs" / "education" / "schema.json").write_bytes(schema_bytes)
    bundles = []
    if bundle is not None:
        (member_dir / "specs" / "education" / "bundle.json").write_text(
            json.dumps(bundle, indent=2) + "\n", encoding="utf-8"
        )
        bundles.append("specs/education/bundle.json")
    (member_dir / "education-contract.json").write_text(
        json.dumps(
            {"contract": "education-contract/v1", "schema_sha256": digest, "bundles": bundles},
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def test_member_without_pointer_is_pending(tmp_path: Path) -> None:
    (tmp_path / "member").mkdir()
    state = check_member(
        tmp_path, MemberSpec("member", "ActiveInferenceInstitute/member"),
        canonical_schema=DEFAULT_SCHEMA_PATH,
    )
    assert state.state == PENDING
    assert state.issues == ()


def test_member_with_matching_copy_is_adopted(tmp_path: Path, reference: dict) -> None:
    _adopt(
        tmp_path / "member",
        schema_bytes=DEFAULT_SCHEMA_PATH.read_bytes(),
        digest=schema_digest(),
        bundle=reference,
    )
    state = check_member(
        tmp_path, MemberSpec("member", "ActiveInferenceInstitute/member"),
        canonical_schema=DEFAULT_SCHEMA_PATH,
    )
    assert state.state == ADOPTED, state.issues
    assert state.bundles == ("specs/education/bundle.json",)


def test_member_with_stale_schema_copy_diverges(tmp_path: Path, reference: dict) -> None:
    """The drift test: a member that vendored an older schema is reported, not accepted."""
    stale = DEFAULT_SCHEMA_PATH.read_bytes().replace(b"education-contract/v1", b"education-contract/v0")
    _adopt(
        tmp_path / "member",
        schema_bytes=stale,
        digest=schema_digest(),
        bundle=reference,
    )
    state = check_member(
        tmp_path, MemberSpec("member", "ActiveInferenceInstitute/member"),
        canonical_schema=DEFAULT_SCHEMA_PATH,
    )
    assert state.state == DIVERGED
    assert "EC205" in codes(state.issues)


def test_member_with_stale_pointer_digest_diverges(tmp_path: Path, reference: dict) -> None:
    _adopt(
        tmp_path / "member",
        schema_bytes=DEFAULT_SCHEMA_PATH.read_bytes(),
        digest="0" * 64,
        bundle=reference,
    )
    state = check_member(
        tmp_path, MemberSpec("member", "ActiveInferenceInstitute/member"),
        canonical_schema=DEFAULT_SCHEMA_PATH,
    )
    assert state.state == DIVERGED
    assert "EC203" in codes(state.issues)


def test_member_with_invalid_bundle_diverges(tmp_path: Path, reference: dict) -> None:
    broken = copy.deepcopy(reference)
    broken["units"][0]["prerequisites"] = ["mathematics"]
    _adopt(
        tmp_path / "member",
        schema_bytes=DEFAULT_SCHEMA_PATH.read_bytes(),
        digest=schema_digest(),
        bundle=broken,
    )
    state = check_member(
        tmp_path, MemberSpec("member", "ActiveInferenceInstitute/member"),
        canonical_schema=DEFAULT_SCHEMA_PATH,
    )
    assert state.state == DIVERGED
    assert "EC108" in codes(state.issues)


def test_member_without_checkout_is_unavailable(tmp_path: Path) -> None:
    state = check_member(
        tmp_path, MemberSpec("absent", "ActiveInferenceInstitute/absent"),
        canonical_schema=DEFAULT_SCHEMA_PATH,
    )
    assert state.state == "unavailable"


def test_registry_digest_mismatch_is_reported(tmp_path: Path) -> None:
    registry_data = load(REGISTRY)
    registry_data["schema_sha256"] = "0" * 64
    registry_data["members"] = [{"id": "courses", "repository": "ActiveInferenceInstitute/courses"}]
    path = tmp_path / "contract.json"
    path.write_text(json.dumps(registry_data), encoding="utf-8")
    report = check_contract(
        load_registry(path),
        member_root=tmp_path,
        canonical_schema=DEFAULT_SCHEMA_PATH,
        repo_root=ROOT,
    )
    assert "EC212" in codes(report.registry_issues)
    assert not report.ok


def test_live_registry_reports_this_repository_as_adopted(tmp_path: Path) -> None:
    """The lead repository is a member of its own contract and must satisfy it."""
    report = check_contract(
        load_registry(REGISTRY),
        member_root=tmp_path,
        canonical_schema=DEFAULT_SCHEMA_PATH,
        repo_root=ROOT,
        member_paths={"courses": ROOT},
    )
    assert report.registry_issues == ()
    courses = next(member for member in report.members if member.id == "courses")
    assert courses.state == ADOPTED, courses.issues
    assert report.ok


def test_registry_names_every_group_member() -> None:
    registry = load_registry(REGISTRY)
    assert [member.id for member in registry.members] == [
        "courses",
        "cognitive",
        "fundamentals",
        "GEN24",
        "gen25",
        "Parr_et_al_2022_ActInf_Textbook",
        "ActiveInferenceImplementations",
        "ActiveInferenceCategoryTheory",
        "Symposium",
        "Start",
        "Active_Skillference",
    ]


def test_contract_document_exists() -> None:
    registry = load_registry(REGISTRY)
    assert (ROOT / registry.contract_doc).is_file()


def test_extractor_rejects_a_course_without_units(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        build_bundle("no-such-course")


def test_extractor_is_deterministic() -> None:
    first = render_bundle(build_bundle("active_inference"))
    second = render_bundle(build_bundle("active_inference"))
    assert first == second


def test_vendored_copy_helper_round_trips(tmp_path: Path) -> None:
    """A member that copies the canonical schema byte-for-byte is accepted."""
    target = tmp_path / "copy.json"
    shutil.copyfile(DEFAULT_SCHEMA_PATH, target)
    assert target.read_bytes() == DEFAULT_SCHEMA_PATH.read_bytes()
    assert schema_digest(target) == schema_digest()


def test_explicit_member_root_uses_actual_isolated_checkout(tmp_path: Path, reference: dict) -> None:
    actual = tmp_path / "unrelated-isolated-lane-name"
    _adopt(actual, schema_bytes=DEFAULT_SCHEMA_PATH.read_bytes(), digest=schema_digest(), bundle=reference)
    guessed = tmp_path / "member"
    guessed.mkdir()
    (guessed / "education-contract.json").write_text("not JSON")
    state = check_member(
        tmp_path, MemberSpec("member", "ActiveInferenceInstitute/member"),
        canonical_schema=DEFAULT_SCHEMA_PATH, repo_root=actual,
    )
    assert state.state == ADOPTED, state.issues
    direct = check_member(
        None, MemberSpec("member", "ActiveInferenceInstitute/member"),
        canonical_schema=DEFAULT_SCHEMA_PATH, repo_root=actual,
    )
    assert direct.state == ADOPTED
    assert direct.bundles == ("specs/education/bundle.json",)
    assert (guessed / "education-contract.json").read_text() == "not JSON"


@pytest.mark.parametrize("field", ["units", "prerequisite_edges", "glossary"])
def test_malformed_bundle_does_not_abort_valid_peer(tmp_path: Path, reference: dict, field: str) -> None:
    from scripts.check_education_contract import run_bundles

    malformed = copy.deepcopy(reference)
    malformed[field] = None
    bad = tmp_path / "malformed.json"
    good = tmp_path / "valid.json"
    bad.write_text(json.dumps(malformed))
    good.write_text(json.dumps(reference))
    code, report = run_bundles([bad, good], DEFAULT_SCHEMA_PATH)
    assert code == 1
    assert report["ok"] is False
    assert [bundle["ok"] for bundle in report["bundles"]] == [False, True]
    assert report["bundles"][0]["issues"]


def test_null_prerequisite_is_schema_failure_not_rule_crash(tmp_path: Path, reference: dict) -> None:
    actual = tmp_path / "isolated-member"
    malformed = copy.deepcopy(reference)
    malformed["units"][0]["prerequisites"] = None
    _adopt(actual, schema_bytes=DEFAULT_SCHEMA_PATH.read_bytes(), digest=schema_digest(), bundle=malformed)
    state = check_member(
        None, MemberSpec("member", "ActiveInferenceInstitute/member"),
        canonical_schema=DEFAULT_SCHEMA_PATH, repo_root=actual,
    )
    assert state.state == DIVERGED
    assert state.issues and state.documents == ()


@pytest.mark.parametrize("field", ["pointer", "schema_path", "bundle"])
@pytest.mark.parametrize("escape", ["relative", "absolute", "symlink"])
def test_member_adoption_paths_are_contained_in_explicit_root(
    tmp_path: Path, reference: dict, field: str, escape: str,
) -> None:
    actual = tmp_path / "isolated"
    _adopt(actual, schema_bytes=DEFAULT_SCHEMA_PATH.read_bytes(), digest=schema_digest(), bundle=reference)
    outside = tmp_path / "outside.json"
    outside.write_text(json.dumps(reference))
    if escape == "relative":
        candidate = "../outside.json"
    elif escape == "absolute":
        candidate = str(outside)
    else:
        (actual / "linked.json").symlink_to(outside)
        candidate = "linked.json"
    if field == "bundle":
        pointer = load(actual / "education-contract.json")
        pointer["bundles"] = [candidate]
        (actual / "education-contract.json").write_text(json.dumps(pointer))
        spec = MemberSpec("member", "ActiveInferenceInstitute/member")
    else:
        spec = MemberSpec("member", "ActiveInferenceInstitute/member", **{field: candidate})
    before = outside.read_bytes()
    state = check_member(None, spec, canonical_schema=DEFAULT_SCHEMA_PATH, repo_root=actual)
    assert state.state == DIVERGED
    assert state.issues
    assert outside.read_bytes() == before


def test_group_rules_see_every_member_bundle(tmp_path: Path, reference: dict) -> None:
    from src.education_contract.registry import Registry

    def document(identity, repository, definition):
        value = copy.deepcopy(reference)
        value["provenance"]["repository"] = repository
        value["units"] = [copy.deepcopy(reference["units"][0])]
        value["units"][0]["unit_id"] = identity
        value["units"][0]["prerequisites"] = []
        value["units"][0]["glossary_terms"] = [identity]
        value["prerequisite_edges"] = []
        value["glossary"] = [copy.deepcopy(reference["glossary"][0])]
        value["glossary"][0].update(
            term_id=identity, term=f"Concept {identity}", definition=definition,
        )
        return value

    specs = []
    paths = {}
    for identity in ("alpha", "beta"):
        repository = f"ActiveInferenceInstitute/{identity}"
        root = tmp_path / f"actual-{identity}-lane"
        first = document("shared", repository, f"Definition from {identity}.")
        _adopt(root, schema_bytes=DEFAULT_SCHEMA_PATH.read_bytes(), digest=schema_digest(), bundle=first)
        tail = root / "specs/education/tail.json"
        tail.write_text(json.dumps(document(
            f"{identity}-tail", repository, "A distinct concept defined in this member's second bundle.",
        )))
        pointer = load(root / "education-contract.json")
        pointer["bundles"].append("specs/education/tail.json")
        (root / "education-contract.json").write_text(json.dumps(pointer))
        specs.append(MemberSpec(identity, repository))
        paths[identity] = root
    (tmp_path / "contract.md").write_text("Fixture contract document.")
    registry = Registry(tmp_path / "registry.json", "education-contract/v1", schema_digest(),
                        "contract.md", tuple(specs))
    report = check_contract(registry, member_root=tmp_path / "unused-parent",
                            canonical_schema=DEFAULT_SCHEMA_PATH, repo_root=tmp_path,
                            member_paths=paths)
    assert all(len(member.documents) == 2 for member in report.members)
    assert all(member.state == ADOPTED for member in report.members)
    assert {"EC120", "EC121"} <= codes(report.registry_issues)
    assert report.ok is False


@pytest.mark.parametrize("multi_bundle_owner", ["alpha", "beta"])
@pytest.mark.parametrize("matching_bundle", [0, 1])
def test_group_term_drift_checks_every_owner_definition(
    tmp_path: Path, reference: dict, multi_bundle_owner: str, matching_bundle: int,
) -> None:
    """A peer matching either definition must not hide the other bundle's drift."""
    from src.education_contract.registry import Registry

    definitions = ("A definition of the shared concept.", "A different definition of that concept.")
    specs = []
    paths = {}
    for identity in ("alpha", "beta"):
        repository = f"ActiveInferenceInstitute/{identity}"
        root = tmp_path / f"actual-{identity}-lane"
        member_definitions = (
            definitions if identity == multi_bundle_owner else (definitions[matching_bundle],)
        )
        for index, definition in enumerate(member_definitions):
            document = copy.deepcopy(reference)
            document["provenance"]["repository"] = repository
            document["units"] = [copy.deepcopy(reference["units"][0])]
            document["units"][0].update(
                unit_id=f"{identity}-{index}", prerequisites=[],
                glossary_terms=[reference["glossary"][0]["term_id"]],
            )
            document["prerequisite_edges"] = []
            document["glossary"] = [copy.deepcopy(reference["glossary"][0])]
            document["glossary"][0]["definition"] = definition
            if index == 0:
                _adopt(root, schema_bytes=DEFAULT_SCHEMA_PATH.read_bytes(),
                       digest=schema_digest(), bundle=document)
            else:
                (root / "specs/education/tail.json").write_text(json.dumps(document))
                pointer = load(root / "education-contract.json")
                pointer["bundles"].append("specs/education/tail.json")
                (root / "education-contract.json").write_text(json.dumps(pointer))
        specs.append(MemberSpec(identity, repository))
        paths[identity] = root
    (tmp_path / "contract.md").write_text("Fixture contract document.")
    registry = Registry(tmp_path / "registry.json", "education-contract/v1", schema_digest(),
                        "contract.md", tuple(specs))
    report = check_contract(registry, member_root=tmp_path / "unused-parent",
                            canonical_schema=DEFAULT_SCHEMA_PATH, repo_root=tmp_path,
                            member_paths=paths)
    assert all(member.state == ADOPTED for member in report.members)
    assert [len(member.documents) for member in report.members] == (
        [2, 1] if multi_bundle_owner == "alpha" else [1, 2]
    )
    assert codes(report.registry_issues) == {"EC121"}
    assert report.ok is False


def test_duplicate_registry_identity_is_not_silently_overwritten(tmp_path: Path) -> None:
    data = load(REGISTRY)
    data["members"] = [data["members"][0], data["members"][0]]
    path = tmp_path / "registry.json"
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="duplicate member"):
        load_registry(path)
