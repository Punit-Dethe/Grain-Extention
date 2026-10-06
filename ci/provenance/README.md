# Candidate provenance checkpoint

This lane exercises real GitHub/Sigstore provenance for native and MCP candidate
bytes through the production maintainer commands. It is not a production publisher
or evidence of human review/source ownership. No publishing key is accessed in CI.

`candidate-provenance.yml` uses a controlled branch push/manual checkpoint with no
caller inputs. A read-only, non-OIDC prepare job builds the exact pinned Grain
commit with locked dependencies and Rust 1.96.0. `fixtures.py` creates temporary
standalone example Git projects, runs real `grain-ext submit` and
`grain-registry prepare-artifact`/`prepare-catalogue`, then disposes the source
repos. Native source contains an intentionally failing build script which must
never run. Output contains only public submission/preparation/candidate data and
producer hashes. The separate OIDC attestation job downloads data and invokes
the maintained GitHub attestation action; it executes no artifact code.

Actions are pinned by immutable commit. Checkout credentials are not persisted;
no repository/environment secrets, release writes or production upload appear.
Seven-day artifacts retain candidates and the actual cryptographic bundle.
Independently approve the exact workflow/source commit and producer digests before
using the bundle with `sign-reviewed-candidate`. Merely downloading this metadata
does not establish review authority.

The legacy `build-and-check.yml` and `publish.yml` are unchanged and remain
incomplete; their presence/activity is not production approval. This new branch
lane does not repair or activate them. Before production, require actual pinned
author source/build isolation, protected review-derived policy, branch/environment
protection verification, complete signed serving paths and serialized promotion.

Maintenance: this is a narrow product provenance regression, not another Agent
harness. Keep the two data fixtures only while they prove the signing interface.
When real reviewed author builds replace this temporary checkpoint lane, retire
its branch-push trigger and obsolete fixture preparation; retain a minimal manual
provenance regression only if useful. Bump the Grain source pin deliberately at
a maintainer contract checkpoint. Never turn the example origins or fixture
reviewer into production approval, or introduce an attestation bypass.
