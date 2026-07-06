# rulespec-gh

Ghana RuleSpec source registry.

This repository targets a Ghana tax-benefit surface: national income tax (PAYE and self-assessment), personal reliefs, social contributions, and the cash-transfer and social-protection programs needed for household-level calculations. Ghana is a unitary state, so all encoded law lives under a single `gh/` national namespace; there is no regional layer.

The first encoded slices are the individual income-tax rate schedule and personal reliefs from the Income Tax Act 2015 (Act 896) as amended, the current Ghana Revenue Authority (GRA) PAYE/individual rate surface, and the Livelihood Empowerment Against Poverty (LEAP) programme.

## Source Priority

Policy must come from the furthest upstream available source.

1. Ghana Publishing Company Limited (Assembly Press) official Acts of Parliament and Legislative/Executive Instruments — the printed authentic text of Act 896 and its amending Acts.
2. Ghana Revenue Authority (GRA) rate tables, PAYE guides, and practice notes only after the governing Act or Instrument is identified.
3. Ministry of Gender, Children and Social Protection (MoGCSP) / LEAP Management Secretariat official programme documentation for social-transfer rules that are set administratively rather than by Act.
4. Oracles only for household-level parity tests against an external source that can calculate the same household case, never as law.

## Oracle Scope

An oracle is an executable, pinned external calculator that accepts household-level inputs and returns household-level tax-benefit outputs comparable to Axiom outputs. Aggregate simulators, distributional reports, parameter documentation, and public model summaries are not oracles for RuleSpec parity, even when they are useful as background references.

The Ghana household oracle target is **GHAMOD**, the SOUTHMOD tax-benefit microsimulation model for Ghana (UNU-WIDER, in collaboration with the University of Ghana and partners). GHAMOD is **not yet attached**: the oracle wiring lands when the UNU-WIDER SOUTHMOD/GHAMOD model-and-data bundle clears licensing for use as a pinned comparison surface. Until then this repo encodes source-first from Act 896 and GRA/LEAP documentation, with oracle parity tests deferred. `data/oracles/` holds the placeholder index and records the pending-bundle status.

## Layout

- `gh/statutes/`: Ghana primary law encoded as RuleSpec (Acts of Parliament — Income Tax Act 2015, amending Acts).
- `gh/regulations/`: Legislative Instruments, Executive Instruments, and delegated instruments made under the governing Acts.
- `gh/policies/`: GRA administrative guidance, rate surfaces, and social-protection programme rules (e.g. LEAP) when statute/regulation decomposition is not yet complete or the rule is set administratively.
- `data/corpus/`: source inventory, ingestion manifests, provision locators, and promoted official extracts.
- `data/coverage/`: tax-benefit coverage backlog and official source map.
- `data/oracles/`: pinned household-level comparison references (GHAMOD, once the bundle clears).

## Initial Build Strategy

This first pass is a source-first repo scaffold. Ghana has no ELI/consolidated-legislation portal comparable to Belgium's Justel, so official source text is captured with `axiom-corpus`'s generic official-document ingest (`extract-official-documents`): the printed Act 896 PDF from Ghana Publishing and the GRA rate/relief surfaces are fetched, snapshotted, and segmented into corpus provisions under the `gh/` citation-path prefix. RuleSpec modules cite those corpus artifacts before encoding formulas.

Durable ids use `gh:<path>#<rule>` for national rules.

## Money proof-atom coverage

Every policy-bearing monetary value — currency parameters, currency parameter-table cells, and currency literals in derived formulas — must carry a proof atom whose source cites a provision. The shared `validate-rulespec` workflow enforces this with `axiom-encode proof-validate --money-atoms-only`, reading the repo-root ratchet `known-missing-money-atoms.yaml`.

`known-missing-money-atoms.yaml` is seeded at `total_allowed: 0`: because the repo starts with no encoded monetary values, there is no backlog to burn down, and CI enforces a strict zero allowance from the first encoded module onward. Every monetary value added by encoding must ship with a proof atom citing a Ghana provision. This floor may only be lowered, never raised.
