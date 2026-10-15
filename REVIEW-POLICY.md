# Source review and publication policy

## Ownership policy and tester adoption

`ownership.json` records extension IDs, canonical GitHub sources, artifact kinds,
authorized registry submitters and eligible reviewers. It is public reviewable
intent, not a credential or automatically trusted file. The current maintainer
approved registry PR 8 and adopted the exact two first-party grants on 16 October
2026, SHA256 `d471cf0c145dd8a83b131c2e669284f026f78659e0c649f095cd8935423771c3`.
This tester adoption is separate from each exact release approval. Other operators
must independently review/adopt their current file. It changes no OAuth permissions
and does not certify production GitHub protection or signing-key custody.

Before using the signer, review this configuration and adopt its exact bytes
into the current protected operator location outside author/build workspaces.
The signer requires `--authority` and schema-3 approval policy containing its
`authority_sha256`, in addition to the independent approval-policy digest. Never
use an author-provided file/digest as the approval trust anchor. Operator custody
of the current file matters: supplying an old copy alongside an old approval
would be an operator trust-boundary violation. GitHub branch/environment controls
and key custody require a separate reviewed operational decision; this proposal
does not configure them or claim that they already exist.

External submissions, including updates, require a live independent GitHub review
from an eligible reviewer. The PR submitter must be an authorized maintainer for
the ID/source/kind. First-party grants may explicitly opt into
`allow_maintainer_approval`: an eligible reviewer who is also a listed owner may
then provide an exact per-release operator approval reference in
`maintainer_approval`, with review ID zero. The reference is an audit record,
not a separate authenticated credential or independent GitHub review. Policy
custody and its independently selected digest establish authorization. The grant
does not approve a version by itself. Every release still binds the merged PR,
head, submitter, source/listing, candidate, producer, previous index and current
publishing identity, with approval expiry of at most seven days. Successful CI
or an author's manifest never grants review authority.

### Enrollment, transfer and withdrawal

- New IDs: review source-repository control, ID, artifact kind and submitting
  accounts, then separately approve enrollment. A submission cannot reserve or
  take over an ID by declaring a name.
- Updates: keep the registered identity and approve the new exact version. No
  Grain source edit or compiled per-version exception is required.
- Transfers/source or kind changes: record consent from current and receiving
  owners, review the new source, then explicitly change the grant. Review changes
  to maintainers, reviewers or self-approval eligibility as authority changes,
  separately from an author's release PR.
- Withdrawal: remove the grant/account/reviewer from the protected current file;
  changed ownership bytes invalidate prior pinned approvals. Reapprove other
  pending releases against the new digest. Withdrawing a published extension
  additionally requires the existing signed revocation/publication procedure;
  removing ownership only stops future signing.

See Grain's maintained [signer/ownership runbook](https://github.com/Punit-Dethe/Grain/blob/extensions/main-integration-20261010/crates/grain-registry-tools/README.md#ownership-enrollment-and-changes).

## Historical tester approvals

For the tester alpha only, the maintainer explicitly reauthorized publication
of these exact first-party artwork candidates on 15 October 2026, superseding
the earlier accidental approval/withdrawal in the same session:

- `com.grain.github` 0.1.2, source `d5ae55e7dafaa0f9749a05f1518d0152bffcc803`,
  structured submission SHA256 `6e434021102e57675b2fe1edd2b65a851878c4dfff277444091ac03c7caeb127`.
- `com.grain.notion` 0.1.1, source `d44b782581702935d5b1c5f75457d3ac2bac7b70`,
  structured submission SHA256 `b486000c5c953a3a4491d70cdd90fbfb90fa75e93f20a5b7af4ab730f25c35bb`.

These replace the earlier GitHub0.1.1 / Notion0.1.0 signing exceptions, not
existing published entries. The user's authorization is recorded in the Grain
progress document; it is not presented as an independent GitHub review.
These approvals do not authorize other versions or submissions. They used the
previous tester-only signer profile; schema-3 tooling refuses that old policy
format and its `alpha_maintainer_approval` field. Existing signed publications
remain unchanged. New releases require adoption of the ownership configuration
and a fresh exact approval through one of the routes above. No earlier chat
approval is silently converted into authorization for a future candidate.

## Current contract

Extensions supply Agent-callable tools. They do not receive Grain prompt
priorities, prompt customization, screen/selection/OCR, Space or OS-specific
capabilities. Native tools use only the current SDK and declared brokered service
access; an MCP descriptor identifies its remote service and declared connection
configuration. Agent-owned context stays outside the extension contract.

Review the exact source diff, tool input/output schemas, declared destinations,
credentials/authorization requirements, dependency/build changes, DESCRIPTION.md
and media. Flag destructive actions, broad write access, credential handling,
exfiltration risk, result ambiguity and unexpected dependencies. Source approval
must still match the current submission, tag, commit and protected review policy
when signing; a stale approval cannot authorize changed bytes.

## Build, sign, activate

Use [the maintainer runbook](PUBLISHING.md) for the complete command sequence and
recovery boundaries. `ci/grain-tooling-commit.txt` selects the single reviewed
Grain source version for source preparation and activation. Updating this pin
is a tooling review, not an author-controlled release input or automatic approval.

1. Dispatch `build-and-check` on the trusted registry branch with the reviewed
   submission ID. The reusable builder isolates author execution from OIDC and
   signing/publication permission. MCP descriptors require no author build.
2. Revalidate fresh source identity, checked artifact/listing bytes and pinned
   producer/attestation using Grain's existing review/signing commands. Keep the
   explicit publisher key outside author workspaces and build runners. The
   current signer requires explicit Minisign key unlocking; key custody and
   protected approval policy are operator prerequisites, not self-certified CI.
3. Assemble/export the complete signed hosting bundle, then commit only `v1/`
   and `.registry-publication/` above the independently expected current `main`.
4. Review the full candidate SHA and independent bundle receipt digest before
   manually dispatching `publish`. Initial publication has no previous receipt;
   later updates require the previous authenticated proof. The runner verifies
   exact bytes, conditional remote update and remote result. No automatic retry
   follows an uncertain result, and no workflow bypasses branch protection.
5. Verify hosted HTTP metadata/assets and real Grain discovery/install behavior
   before treating publication as accepted. Those checks are distinct from Git
   confirmation. The extension store stays hidden until the release gate passes.

Current signed revocations remain the client enforcement channel. Do not carry
old extension identities/settings/history forward merely to support the
experimental platform. The maintainer docs record commands, evidence and the
remaining activation/coherence work. This draft does not assert configured
production environment reviewers, a published security address or launch SLAs.
