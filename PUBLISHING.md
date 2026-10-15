# Maintainer publication runbook

Authors use [CONTRIBUTING.md](CONTRIBUTING.md). Maintainers use this sequence for
both native and MCP extensions. Successful CI prepares evidence; it does not
approve a release. Signing remains local to the authorized operator. Activation
uses the existing manual `publish` workflow; there is no publisher service.

## 1. Select the reviewed inputs

Review the source/tag/commit, submission, DESCRIPTION, artwork and account setup.
Merge the exact eligible submission PR before requesting signable evidence.
Record its PR, reviewed head and merged registry commit. The current protected
ownership file must already authorize this ID/source/kind/submitter/reviewer;
the public `ownership.json` is only a proposal until the operator adopts it.

`ci/grain-tooling-commit.txt` is the single full Grain source commit used by
source preparation and publication. Change it only in a reviewed tooling update,
not for each extension version. Both workflows refuse anything other than one
lowercase 40-character commit. The request job passes that same selection into
the producer receipt; author inputs and downloaded metadata cannot select it.
For a release, independently record the pin from the selected trusted registry
revision. If the tooling selection changes before activation, review the change
and revalidate the release; do not silently replace the recorded producer identity.

Dispatch the trusted builder on that reviewed registry revision:

```text
gh workflow run build-and-check.yml --repo Punit-Dethe/Grain-Extention --ref REVIEWED_REGISTRY_REF -f submission_id=EXTENSION_ID
```

Select the resulting successful run by its full head commit and submission ID,
not simply the newest run. Record its run URL, workflow/source commit and the
trusted request job's producer executable SHA256. Download the data artifact:

```text
gh run download RUN_ID --repo Punit-Dethe/Grain-Extention --name attested-source-EXTENSION_ID --dir FRESH_EVIDENCE
```

Never execute a downloaded builder or author script. Preserve required evidence
outside Actions' seven-day retention. A run from an unmerged proposal branch can
test workflow wiring but cannot substitute for the signer's approved registry ref.

## 2. Prepare, approve and stage

Build the maintainer CLI from the recorded Grain commit with locked dependencies.
Follow the maintained [CI intake and exact policy guide](https://github.com/Punit-Dethe/Grain/blob/extensions/main-integration-20261010/crates/grain-registry-tools/README.md#prepare-ci-evidence-for-review)
for `prepare-release-review`. Select the producer digest independently from the
trusted request job; verify both actual GitHub attestations. Intake emits an
**unapproved** schema-3 policy and review summary. Review them, set the valid
approval window and applicable independent review or exact maintainer approval,
then independently pin the final approved policy bytes. Existing tester approvals
do not authorize a new version.

Use `stage-reviewed-release` with that policy/digest, current operator ownership,
the independently pinned local store pointer and explicit publisher key. See the
[staging command and recovery rules](https://github.com/Punit-Dethe/Grain/blob/extensions/main-integration-20261010/crates/grain-registry-tools/README.md#stage-one-reviewed-release).
The joined command rechecks approval/provenance, signs, assembles, conditionally
promotes the local store and verifies the exported `RELEASE/bundle`.
`RELEASE/release.json` records its receipt/snapshot; it is not publication approval.
For multiple extensions, separately approve/stage each against the resulting
local base, then publish the final bundle through the same path.

## 3. Bind the bundle to a Git candidate

Use a fresh standalone operator clone at the independently recorded current
remote `main` SHA. Record the previous `.registry-publication/bundle.json` SHA256.
Prepare a publication branch directly on that base. Replace only these two
directories with the exact exported layout, preserving all bundle history:

| Verified bundle | Registry checkout |
| --- | --- |
| `bundle/v1/` | `v1/` |
| `bundle/bundle.json`, `bundle/current.json`, `bundle/history/` | `.registry-publication/` |

Review and commit only those two paths, with no filters/newline conversion or
unrelated edits. Record the full candidate SHA and SHA256 of the exact bundle
receipt bytes. The candidate must have the expected base as its sole parent.
Run `prepare-github-publication` with the authenticated previous bundle and both
receipt pins as shown in the [commit-bound handoff guide](https://github.com/Punit-Dethe/Grain/blob/extensions/main-integration-20261010/crates/grain-registry-tools/README.md#commit-bound-github-publication-handoff-e4g).
Its unsigned `publication.json` is the concrete tuple to review, not permission
to publish. Push only the candidate branch so Actions can fetch the commit.
Do not merge it or push `main` through another route.

## 4. Approve activation and confirm delivery

Review the exact tuple and approved workflow/tooling revision. Confirm the actual
GitHub dispatch, environment and branch controls are suitable; an environment
named `publish` does not itself enforce approval. The current tester protection
and ownership adoption are still operator decisions, not completed by this doc.
After authorization, dispatch the existing workflow once:

```text
gh workflow run publish.yml --repo Punit-Dethe/Grain-Extention --ref REVIEWED_WORKFLOW_REF -f mode=update -f expected_base_commit=FULL_BASE_SHA -f candidate_commit=FULL_CANDIDATE_SHA -f candidate_receipt_sha256=RECEIPT_SHA256 -f previous_receipt_sha256=PREVIOUS_RECEIPT_SHA256
```

The publisher regenerates the handoff from committed signed bytes, verifies the
current remote base, pushes once with an exact lease, confirms `main`, then checks
public HTTP delivery. Preserve its evidence/run URL. An ordinary version update
requires no Grain source or tooling-pin edit. Git confirmation and HTTP acceptance
are separate results; neither proves the real app/account journey by itself.

## Recovery at the failing boundary

| Observation | Next action |
| --- | --- |
| CI/intake/review refused | Correct that input and prepare a fresh evidence/policy output; never skip the gate. |
| Local staging interrupted | Inspect retained output and the store pointer before deciding what completed. |
| Local promotion confirmed, export failed | Export/verify that exact generation only; do not sign again. |
| Remote base changed | Inspect the new publication, rebuild the candidate on the reviewed current base and revalidate. |
| Push outcome unconfirmed | Inspect remote `main`; never automatically replay. |
| Git confirmed, HTTP failed | Run only `check_hosted_github.py` from the maintained guide against the confirmed commit/receipt. Do not repush. |

No secrets, private keys or passwords belong in submissions, evidence, logs or
chat. Changes to identity, custody or GitHub controls require separate concrete
review. First bootstrap has a separate initial gate; this routine update sequence
must not fabricate previous publication proof.
