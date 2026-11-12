"""The Active Inference education contract: one schema for units, edges and terms.

The canonical schema is ``specs/education/schema.json``; the group contract that
explains it is ``docs/workflows/education.md``. This package is the single
implementation every member calls or vendors:

* :mod:`~software.src.education_contract.schema` -- load the schema, hash it, validate
  a document or a member pointer against it,
* :mod:`~software.src.education_contract.rules` -- the coherence rules JSON Schema
  cannot express (acyclicity, edge/prerequisite agreement, term resolution),
* :mod:`~software.src.education_contract.registry` -- member adoption state and the
  copy-with-integrity-check drift test,
* :mod:`~software.src.education_contract.catalog` -- transcription of this
  repository's course tree into a bundle.
"""

from __future__ import annotations

from .catalog import build_bundle, render_bundle
from .registry import (
    ADOPTED,
    DIVERGED,
    PENDING,
    UNAVAILABLE,
    ContractReport,
    MemberSpec,
    MemberState,
    Registry,
    check_contract,
    check_member,
    load_registry,
)
from .rules import run_cross_rules, run_rules
from .schema import Issue, schema_digest, validate_document, validate_pointer

__all__ = [
    "ADOPTED",
    "DIVERGED",
    "PENDING",
    "UNAVAILABLE",
    "ContractReport",
    "Issue",
    "MemberSpec",
    "MemberState",
    "Registry",
    "build_bundle",
    "check_contract",
    "check_member",
    "load_registry",
    "render_bundle",
    "run_cross_rules",
    "run_rules",
    "schema_digest",
    "validate_document",
    "validate_pointer",
]
