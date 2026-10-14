"""Encoding-manifest claims that were already stale on 2026-10-14.

Each entry is one claim in one manifest under .axiom/encoding-manifests/:
the file it attests, the sha256 the manifest records for that file, the
sha256 the file had on 2026-10-14, the sha256 of the manifest file itself,
and the commits that changed the file after it was attested.

All of these changes landed in July 2026 (rulespec-gh#30), while this
repository's generated-RuleSpec guard was off (run-generated-guard: false
until 2026-10-11), so CI never compared the edited files with their
manifests.

The manifests are manual attestations (runner: manual-attestation, schema
axiom-encode/applied-rulespec/v1), not encoder apply records. Listing a
claim here records the drift. It does not attest the current bytes, and the
manifest still attests the earlier ones.

The list is closed and may only shrink. test_encoding_manifests.py fails if
a listed file changes again or a listed manifest is edited while it stays a
manual attestation. It reports an entry as resolved once the supervised
encoder replaces the module's manifest; delete the entry then. Do not add
entries: new drift fails CI and is fixed through the encoder.
"""

from __future__ import annotations

from typing import NamedTuple


class StaleAttestation(NamedTuple):
    manifest: str
    manifest_sha256: str
    path: str
    attested_sha256: str
    current_sha256: str
    changed_by: tuple[str, ...]
    change: str


#: Number of entries when the list was adopted. The list may only shrink.
ADOPTED_COUNT = 10

KNOWN_STALE_ATTESTATIONS: tuple[StaleAttestation, ...] = (
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/policies/free-shs/fee-free-structure.json",
        manifest_sha256="e67bca700d7143e9066fb2af87cec2c224b08109a0a7f33797f7e735c858614f",
        path="gh/policies/free-shs/fee-free-structure.yaml",
        attested_sha256="5cc55e31bdbec7277a6229a02bb9e5e3c0934359b9e817f9551c1fa04dd36c45",
        current_sha256="0ce8f2a567186197d3965c1cd497b0ad75f2cfcb699780cef83d34d92fb70927",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "no formula, parameter or import changed: module citation list "
            "collapsed to one corpus_citation_path, upstream_source_check "
            "removed"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/policies/gsfp/feeding-grant.json",
        manifest_sha256="a5cff377606cda90f1473002e70d061f93a1de8b96d4e308159da9885125f8ab",
        path="gh/policies/gsfp/feeding-grant.yaml",
        attested_sha256="8498ffebdd8c5e654f28ed65923bf3d8aabbdd276efbedc42b533d50d0c99de5",
        current_sha256="bc4a94258cf73c3406f71dd49548c92a613cff00fc18cdf547e59615a36ae613",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "no formula, parameter or import changed: module citation list "
            "collapsed to one corpus_citation_path, upstream_source_check "
            "removed"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/policies/mogcsp-leap/payment-cycle-grants.json",
        manifest_sha256="18b259a263f2e11baf03d52048e436fb76778e22b3ee712216d73439560dfc04",
        path="gh/policies/mogcsp-leap/payment-cycle-grants.yaml",
        attested_sha256="85365f9b12741e5db5377e630deb14ab0cb9e183aefe19327fc1aad9c2aabbe4",
        current_sha256="47ec3e09f31148e24db48d6ab729aadd8298b79600b968d8283b73f30d05b151",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "no formula, parameter or import changed: module citation list "
            "collapsed to one corpus_citation_path, upstream_source_check "
            "removed"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/statutes/act-1068/covid-19-health-recovery-levy-2021/section-1-imposition-of-levy.json",
        manifest_sha256="de7ff58443e96e1429152e815d506a605fed269cbad09897a357b2d33df17663",
        path="gh/statutes/act-1068/covid-19-health-recovery-levy-2021/section-1-imposition-of-levy.yaml",
        attested_sha256="e5ad3b3cb35606486ae7ecdd5dc2e8502b629e69fbd9ae4695ace0f8ae0cc578",
        current_sha256="0c6757e78712a06235ff965b4187af43b582ef941eae9c8e236f88e197c25735",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "no formula, parameter or import changed: module citation list "
            "collapsed to one corpus_citation_path"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/statutes/act-1071/income-tax-amendment-no2-2021/second-schedule-substitutions.json",
        manifest_sha256="3d0eeca300eb2e5f40671e570ba21cd97806153b0f00b49a3de4f311e5b1126f",
        path="gh/statutes/act-1071/income-tax-amendment-no2-2021/second-schedule-substitutions.yaml",
        attested_sha256="4ed2a85be03f2997018fc61e9e56af57a4fa077fb6476f79e79ec9d3a4f5563e",
        current_sha256="1c4b4954841be7b7bb33251b06bd4c524458f1c44c3caeb5ecd98c6b6fc687ed",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "no formula, parameter or import changed: module citation list "
            "collapsed to one corpus_citation_path"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/statutes/act-1141/energy-sector-levies-amendment-2025/schedule-shortfall-row-substituted.json",
        manifest_sha256="89e891019f76763a5728712a9a39e8941a9e8ec4e990b678133787bd1e537e49",
        path="gh/statutes/act-1141/energy-sector-levies-amendment-2025/schedule-shortfall-row-substituted.yaml",
        attested_sha256="35c9e50cdd6264c21caed0b4deb7325e7ea4d456ae2e4ebef7d3cd785ff56490",
        current_sha256="789650588968dab946c85e5fe1b13bb2c7c2885c6c715b7fc152961bab8e2464",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "three levy rates now look up parameters imported from "
            "gh:statutes/act-1145/energy-sector-levies-amendment-no2-2025/schedule-road-and-energy-fund-rows, "
            "which has no manifest; same values and effective dates; also "
            "module citation list collapsed to one corpus_citation_path"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/statutes/act-1151/value-added-tax-2025/section-3-rate-of-the-tax.json",
        manifest_sha256="c5b557349d1a39078a27661da4c5fc4877d5f8cacfb00ee5cb9e110d282bdabc",
        path="gh/statutes/act-1151/value-added-tax-2025/section-3-rate-of-the-tax.yaml",
        attested_sha256="2cfe98f7107e6ed7498f226c88351a494b53b6eeff009ba9f2fae25da6c43336",
        current_sha256="7360014bd8ec208f5d8bf15a159b2ccb2eebcbe80be7b7111ecb7499ea750b61",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "no formula, parameter or import changed: module citation list "
            "collapsed to one corpus_citation_path"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/statutes/act-896/income-tax-2015/fifth-schedule.json",
        manifest_sha256="4d78e3fadaa89f1114c4956ac57f2f9e4cd135a8d3d753a163af235cdcc423ee",
        path="gh/statutes/act-896/income-tax-2015/fifth-schedule.yaml",
        attested_sha256="be361f3f2f48ebd01ab54a7011b0296796c25e8037cd0a5e0dc545e4bd19872f",
        current_sha256="9997c3d604e10d88bf452ea768077e4de8bed151edc63b5445887bdfcffedd24",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "five relief amounts now look up parameters imported from "
            "gh:statutes/act-1007/income-tax-amendment-2019/fifth-schedule-personal-reliefs, "
            "which has no manifest; same values and effective dates; also "
            "module citation list collapsed to one corpus_citation_path"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/statutes/act-896/income-tax-2015/first-schedule-8-rates-of-withholding-tax.json",
        manifest_sha256="82ffd2f0788f1d19ef34f63e5d2c39baecdacd99d035c62f2469e983b8f7ba43",
        path="gh/statutes/act-896/income-tax-2015/first-schedule-8-rates-of-withholding-tax.yaml",
        attested_sha256="927c60a19a46ee8050c407db6c013c5357de13562281e00b754b336e986c09ba",
        current_sha256="1586ffcf8e2f556a7b79444bec4d4d05c2636c6974a5e3b26fe76bb999564cba",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "no formula, parameter or import changed: module citation list "
            "collapsed to one corpus_citation_path"
        ),
    ),
    StaleAttestation(
        manifest=".axiom/encoding-manifests/gh/statutes/composed/pilot-worker-disposable-income-pipeline.json",
        manifest_sha256="439c9fa3c42f671c730306903e16bade9f3e8771c052c37a1a2710fcf3d894fc",
        path="gh/statutes/composed/pilot-worker-disposable-income-pipeline.yaml",
        attested_sha256="a15af5356ef95c9956dc3f018f086cc9dca37593eed165c260dbe3e1d885003f",
        current_sha256="6a373279fd1b18b73541e819f594f537f380420418e2373ba6705a1ffa9d003d",
        changed_by=("1e3b93b3a674d7c59a638889a8673edafa966cd5",),
        change=(
            "no formula, parameter or import changed: module citation list "
            "collapsed to one corpus_citation_path, upstream_source_check "
            "removed"
        ),
    ),
)
