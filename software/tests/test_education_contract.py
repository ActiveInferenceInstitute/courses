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
        member_root=ROOT.parent,
        canonical_schema=DEFAULT_SCHEMA_PATH,
        repo_root=ROOT,
    )
    assert "EC212" in codes(report.registry_issues)
    assert not report.ok


def test_live_registry_reports_this_repository_as_adopted() -> None:
    """The lead repository is a member of its own contract and must satisfy it."""
    report = check_contract(
        load_registry(REGISTRY),
        member_root=ROOT.parent,
        canonical_schema=DEFAULT_SCHEMA_PATH,
        repo_root=ROOT,
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
