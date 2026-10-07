# Grain extension registry

Source submissions and signed static catalogue for Grain's **tool-only native
and MCP extensions**. Grain is unreleased; the experimental catalogue is being
replaced directly. Old extension/settings compatibility is not required.

The app's current trust seed points to `v1/` on this repository's `main` branch
through GitHub's raw HTTPS host. Signed roots, index and revocations establish
trust; a GitHub Release tag, README, domain or source manifest does not. This
publishing route uses GitHub only and needs no permanent Grain website.

Hosted catalogues include signed `generation.roots_sha256` and
`generation.revocations_sha256` hashes of exact companion JSON bytes. Each
companion must also verify its own signature. Mixed publications and the
unbound offline seed cannot authorize installs or publication. The shared
signer/renewal rebuilds bindings; the app and pinned publication verifier enforce
them. Signing custody and public HTTP/app activation remain operator gates.

The read-only checkpoint retires its old unbound-seed serving/no-op shell lane.
Positive signed bootstrap, renewal, hosting, capture, key rotation and Git races
remain product regressions; actual public CLI checks cover current refusals.

- `extensions/<id>/submission.toml` pins the author repository, full commit and
  exact release tag. `DESCRIPTION.md` is store copy; README is developer prose.
- Native packages and MCP descriptors use the shared current contract/checker.
  Neither receives screen, selection, OCR or prompt customization privileges.
- `build-and-check` is a manual trusted-branch entry point to the maintained
  isolated builder. Author execution, fresh data preparation and attestation are
  separate jobs. No signing key or publication permission reaches author code.
- Source approval and exact producer provenance are checked before signing with
  an explicit operator-owned key. Building/attesting is not human approval.
- `publish` is manually dispatched for an **already signed** publication-only
  commit above the independently reviewed current `main` commit. It invokes
  the pinned Grain verifier, never candidate repository scripts or author builds.
  It uses a scoped workflow token, with no publisher signing key or OIDC.
- `initial` accepts the empty seed-derived bootstrap only when the base has no
  publication proof. `update` requires the previous signed bundle's independent
  receipt pin. Both verify complete committed bytes and push once using an
  exact-base lease. Unknown outcomes are inspected, never automatically retried.

The `publish` environment and branch protection must be configured/reviewed by
the operator. No workflow changes those controls or grants its own approval.
Merging this draft does not deploy a catalogue; initial activation and actual
HTTP/app coherence remain a separate acceptance step. Seven-day CI artifacts
are evidence, not permanent distribution or source approval.

After its confirmed single Git push, `publish` now checks anonymous public HTTP
delivery against the commit-pinned signed bundle: metadata, native/MCP blobs,
DESCRIPTION/media and retained proof at both the exact commit and `main` URLs.
Stale/mixed/missing/changed content fails. The six live metadata files and Git
head are rechecked, with signed freshness verified again after the scan.
A failed delivery check **does not mean the confirmed push failed**: rerun only
Grain's `ci/check_hosted_github.py`, never replay publication. HTTP evidence is
separate from actual app installation and release approval. No signing key,
author execution, public trust override or automatic retry is added.

Read-only inspection on 8 October found no protection rules in the `publish`
environment and no branch protection on `main`. Operator approval/deployment
controls, applicable repository rules, signer custody and actual signed activation
must still be reviewed before using this draft. The workflow changes no controls.

## Layout

```text
extensions/<id>/           pinned current source submission and DESCRIPTION.md
.github/workflows/         isolated builder, manual publisher, read-only checkpoints
ci/provenance/             trusted data preparation only
v1/                        signed metadata and content-addressed blob/media files
.registry-publication/     exact bundle/current/history proof committed with v1
```

The current maintainer CLI, workflow runner, commands, safety boundaries and
checkpoint instructions live in [Grain's registry tooling documentation](https://github.com/Punit-Dethe/Grain/blob/extensions/tool-only-retirement/crates/grain-registry-tools/README.md).
[Review policy](REVIEW-POLICY.md) describes the current author/producer/signing
boundary. Existing local CONTRIBUTING changes are separate and are not replaced
by this publishing block.
