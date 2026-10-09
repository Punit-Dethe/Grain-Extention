# Source review and publication policy

Third-party native extensions and MCP descriptors, including each update, need an
independent human source review at its exact pinned commit. A successful build,
attestation, author manifest or publisher workflow is not that approval.

For the tester alpha only, the maintainer explicitly authorized owner approval
of the exact first-party `com.grain.github` 0.1.0 submission. The existing signer
accepts a bounded `alpha_maintainer_approval` reference in operator-held policy,
with review ID zero. It verifies the merged PR/head/author/source/listing, exact
submission/candidate/producer pins, CI attestation, expiry and dedicated alpha
publisher before key access. This is not an independent GitHub review. Other
submissions and changed versions still require independent review. The exception
is temporary and must be removed/replaced when permanent approval policy is set.

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
