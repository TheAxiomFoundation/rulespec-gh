# rulespec-gh Agent Notes

This repo stores Ghana RuleSpec source registry materials, oracle references, and encoded policy rules. Ghana is a unitary state, so all encoded law lives under a single `gh/` national namespace.

## Scope

- `gh/statutes/`: Ghana Acts of Parliament — Income Tax Act 2015 (Act 896) as amended, and other primary law needed for tax-benefit modeling.
- `gh/regulations/`: Legislative Instruments (L.I.) and Executive Instruments (E.I.) made under the governing Acts.
- `gh/policies/`: GRA administrative guidance, PAYE rate surfaces, practice notes, and social-protection programme rules (LEAP) set administratively.
- `data/corpus/`: source inventory, ingestion notes, provision locators, and promoted official-source extracts.
- `data/coverage/`: tax-benefit coverage backlog and source map.
- `data/oracles/`: executable or documentary comparison references. These are never legal authority.

## Do

- Treat the scope as a Ghana tax-benefit surface backed by Ghana upstream law.
- Start from the furthest upstream available source: Ghana Publishing Company (Assembly Press) official printed Acts and Instruments first, GRA rate tables/guides and MoGCSP/LEAP documentation only after the governing Act or Instrument is identified.
- Add RuleSpec under `gh/statutes/`, `gh/regulations/`, or `gh/policies/` with companion `.test.yaml` files.
- Keep source law provenance in corpus artifacts and cite those corpus paths from RuleSpec modules via `module.source_verification.corpus_citation_path`.
- Use the current Ghanaian tax year (2026) as the validation year for encoded amounts; indexed/annual values must be corpus-grounded, never invented.
- Keep exact oracle versions in `data/oracles/oracle-index.json` when GHAMOD (or another executable comparison surface) is pinned. GHAMOD attaches only when the UNU-WIDER SOUTHMOD/GHAMOD bundle clears licensing.
- Sync `axiom-encode` and `.axiom/toolchain.toml` before substantial encoding runs.

## Do Not

- Use GRA calculator pages, PAYE ready-reckoners, or third-party summaries as the first legal source when an Act or Instrument governs the rule.
- Invent, round, or interpolate any Ghanaian monetary amount, rate band, or relief figure. Every number must come verbatim from a captured official provision.
- Migrate GHAMOD, EUROMOD/SOUTHMOD, or agency calculator code mechanically as RuleSpec.
- Add generated source payload dumps, formula artifacts, `parameters.yaml`, or standalone YAML fixtures outside allowed RuleSpec roots.
- Hand-copy statute text into RuleSpec without a corpus `citation_path`.
