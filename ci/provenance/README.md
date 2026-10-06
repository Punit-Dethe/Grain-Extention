# Candidate provenance checkpoint

## Pinned remote source handoff

`build-source-candidate.yml` is the provisional reusable source lane. It validates
the shared submission using pinned Grain tools, checks out the exact public GitHub
source commit, and builds native code only on an unprivileged disposable runner.
Native builds require a committed npm lock and `dist/main.js`; `npm ci` disables
install scripts, but `npm run build` deliberately executes author code. It has no
OIDC permission, environment secrets, publishing credentials or dependency cache.
This is privilege separation, **not an outbound-network sandbox**. MCP descriptors
skip author execution entirely; no MCP server is started or authenticated in CI.

A fresh read-only runner checks out the source again with tags, verifies downloaded
maintainer executable bytes against the trusted request job digest before executing
them, copies only the bounded native output as data, and runs actual preparation /
received-byte catalogue validation. No author build script or output is executed
there. A fourth job downloads checked data and grants OIDC only to the immutable
GitHub attestation action. All actions/Grain/toolchain/Node versions are pinned;
checkout credentials are not persisted. Seven-day immutable v4 artifacts retain
the producer, receipt, submission, candidate and genuine bundle. The current
profile requires an untracked/ignored `dist` folder and supports no custom build
output path, private source credentials, live MCP process or automatic approval.

`source-build-checkpoint.yml` invokes this lane for two controlled root projects
on isolated `fixtures/native-tools` and `fixtures/mcp-tools` branches, with exact
release-tag commits in `extensions/com.example.source-*/submission.toml`. These
are real remote source/tag inputs, not ownership or human review certification.
The schema-2 Grain signer separately requires a merged registry PR and the latest
effective independent GitHub approval for its exact reviewed head, matching merged
submission/listing bytes. A CI success or attestation cannot satisfy that gate.
Never supply a publishing key to these workflows or merge the incomplete legacy
publisher as part of this checkpoint.

Cleanup ledger: both `fixtures/*-tools` branches and `fixtures-*-v0.1.0` tags,
the two example submissions, the branch-push checkpoint wrapper and its retained
artifacts are temporary controlled regression inputs. Retire them after reviewed
real author submissions replace this evidence; retain the reusable source lane.
The older controlled fixture lane below remains historical coverage under the
physical-removal hold; do not grow either lane into an Agent harness.

## Earlier controlled provenance lane

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
