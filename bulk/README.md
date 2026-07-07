# Bulk encode (GH)

A durable queue → runner → PR loop for bulk RuleSpec encoding, independent of
any local session. It encodes already-ingested Ghanaian provisions with
`axiom-encode encode <citation> --apply`, pre-checks them with the same gate
battery the PR CI runs, opens one PR per module, and lets each PR auto-merge on
green.

This is the `rulespec-gh` port of the `rulespec-us` dispatcher (structurally
following the `rulespec-uk` single-country port). The encoder and the CI gates
own correctness. This system is **plumbing**: it never edits or invents
generated values. Its only judgement is *which* provisions to queue.

## Pieces

| File | Role |
| --- | --- |
| `bulk/worklist.yaml` | The durable queue. One entry per module. Committed. |
| `bulk/compute_matrix.py` | Turns the worklist into the CI job matrix; single source of truth for status selection. |
| `bulk/roots_for.py` | Maps an applied module path to `guard-generated --roots` (single root `gh`). |
| `.github/workflows/bulk-encode.yml` | The runner: dispatch → matrix → encode `--apply` → gate battery → PR + auto-merge. |

## Running it

```bash
gh workflow run bulk-encode.yml -f batch=A -f limit=4 --repo TheAxiomFoundation/rulespec-gh
```

The `schedule` trigger runs weekly and drains any remaining `pending` entries.
Parallelism is capped at 4; a `concurrency` group serialises whole dispatches.

### Secrets (repo Actions secrets on rulespec-gh)

| Secret | Why |
| --- | --- |
| `OPENAI_API_KEY` | Headless `--backend openai` generation. |
| `AXIOM_ENCODE_APPLY_SIGNING_KEY` | Signs the apply manifest so `guard-generated` accepts the new files. |
| `BULK_ENCODE_TOKEN` | A `repo`+`workflow`-scoped token used to push the branch and open the PR. **Required**: PRs opened by the default `GITHUB_TOKEN` do **not** trigger the `pull_request` event, so the required `validate / validate` check would never run and auto-merge would hang forever. |

## Branch protection (required for the safety model)

Auto-merge is only safe when a required check gates the merge. `main` protection
is configured as required check **`validate / validate`**, **`strict: false`**
(the same shape as `rulespec-uk`), with repo-level "Allow auto-merge" enabled.
Without it, `gh pr merge --auto` could merge before or over a red validate.

## What each job does

1. **dispatch** — runs `compute_matrix.py --status pending` and emits the matrix.
2. **encode** (one leg per module, ≤4 parallel):
   - Checks out the repo into a leaf dir named exactly `rulespec-gh` (the
     `--apply` resolver requirement) using `BULK_ENCODE_TOKEN`.
   - Reads `.axiom/toolchain.toml`, checks out the **pinned** `axiom-encode`,
     `axiom-rules-engine`, and `axiom-corpus`, builds the engine, and runs
     `axiom-encode encode <citation> --apply` (fail-closed: writes nothing on
     validation failure). Manifests are root-level (`.axiom/encoding-manifests`),
     as in `rulespec-uk`.
   - Runs the gate battery in PR-CI order: `guard-generated`, `validate
     --skip-reviewers`, `proof-validate`, then the companion `test`.
   - Opens `bulk/<slug>`, labels it `bulk-encode`, and arms auto-merge on green.

The job **never** uses `--admin`, never bypasses a red check, and never merges
directly. The authoritative gate is the required `validate / validate` check.

### Oracle-coverage pending lane — guarded, activates on toolchain bump

A freshly encoded output is `unmapped` until `axiom-oracles` gains a mapping.
The `oracle-coverage-pending` lane (`axiom-encode ≥ 0.2.1185`, encode#1076)
reclassifies a declared `unmapped` output to `pending_classification` so the
oracle-coverage gate passes. The encoder pinned here (0.2.1174) **predates** that
subcommand, so the dispatcher **guards on its presence**: until
`.axiom/toolchain.toml` is bumped, the sync step is skipped and a new output
HOLDS at the oracle-coverage gate — the expected, accountable held state,
**never** a weakened gate. Do **not** hand-edit `axiom-oracles` concept mappings
to force a canary green.

## Statuses

`pending` (queued) · `in-progress` · `needs-fixtures` (encoded but companion
fixtures hit the #1060 ceiling; PR opens, auto-merge holds) · `pr-open` ·
`merged` · `failed` (encode/gate failed; human triage, never auto-retried).

## Corpus note

The Ghana slices already merged encode Act 896 (Income Tax Act 2015), the Act
1007 relief amendments, and the Act 1111 rate schedule — essentially the whole
ingested clean corpus is already in `gh/statutes/`. The pilot worklist therefore
carries the one substantive un-encoded provision (Act 1134). Extend it as more
Ghana law is ingested; verify each candidate's exact citation_path resolves in
the pinned `axiom-corpus` ref and Supabase `current_provisions`, and skip
cross-reference-heavy provisions (encode#1058).
