# Publishing a Grain extension

Grain extensions provide Agent tools. They can run native tool code or describe
an existing remote MCP service. Users install either kind through the same store.
Retired screen/context/prompt/OS extension APIs are not part of this contract.
Custom MCP configuration is a separate application feature, currently hidden in
alpha/release; it does not require publishing an extension.

## Author checklist

Choose a supported account route before submitting. The maintained
[authentication guide](https://github.com/Punit-Dethe/Grain/blob/extensions/main-integration-20261010/crates/grain-ext-cli/AUTHENTICATION.md)
covers anonymous access, dynamic registration, publisher-owned public clients and
host-specific integrations. `doctor`/`pack` verify local files, not live sign-in.
Document registration ownership and provider permissions in README, normal setup
in DESCRIPTION, and include nonsecret Grain sign-in/read checkpoint evidence.
An unsupported secret-required route is a support decision before publication;
ordinary users should not need to create developer apps to use a store extension.

1. Create a project with Grain's maintained `grain-ext` CLI and document the
   source setup in `README.md`. Put user-facing store content in `DESCRIPTION.md`.
2. Add the listing artwork described below. Keep provider credentials and secrets
   out of the descriptor, repository, listing and submission.
3. Run `grain-ext doctor` and `grain-ext pack`. Push the source commit and a fixed
   version tag to your GitHub source repository.
4. Run `grain-ext submit --registry <local-registry> --repo <source-repo-url>
   --tag <fixed-tag> --commit <full-commit-id> --license MIT --contact <contact>`
   from the project root. This writes a local submission; it does not create a
   GitHub PR or publish the extension. Commit it on a registry branch, push that
   branch, then open a draft with `grain-ext pr --registry <local-registry>
   --id <extension-id> --repo Punit-Dethe/Grain-Extention
   --head-repo <your-account/registry-or-fork>`. Manual GitHub PRs remain supported.

For an update, use `grain-ext submit --update-from <current-registry-version>`
with the new version/tag/commit and the same approved source and artifact kind.
The maintained CLI validates and replaces the complete draft under a per-ID lock;
it refuses stale or unrelated contents. Review the resulting metadata diff. Never
edit served `v1` data by hand. The authoring contract is provisional; use the
same maintained checker version as registry CI.

## Artwork contract

| File | Limits | Placement |
| --- | --- | --- |
| `media/icon.png` | Exactly 512×512 PNG, at most 512 KiB | Square title/Installed icon |
| `media/cover.webp` or `cover.gif` | Wide gallery image, at most 4 MiB | Store card and first detail hero |
| Further `media/*.webp` / `*.gif` | Same gallery rules, filename order | Further detail previews |

Gallery images must be 640–2048px wide and 360–1152px high, with an aspect ratio
between 3:2 and 2:1. Recommended: **1280×720**. Grain displays the full image
inside a 16:9 viewport without stretching/cropping. Square logos are not gallery
images. Up to six gallery images plus one icon; total description/artwork budget
16 MiB. DESCRIPTION is nonempty UTF-8 Markdown, at most 64 KiB. Directories are
flat with no symlinks, duplicate names, or multiple covers. Image decoding is
bounded; GIF checks inspect its first frame, not the entire animation.

Artwork is optional, but provide both roles for a complete listing. Missing
icons use a neutral initial, not the gallery cover. Native extensions also keep
their packaged 512×512 PNG runtime icon. Include attribution/permission for all
artwork; provider marketing images do not imply provider endorsement of Grain.

## Maintainer publication

Maintainers start with [PUBLISHING.md](PUBLISHING.md): one sequence for selecting
trusted CI evidence, exact review, local signing and commit-bound activation.

The submission pins source, tag, commit, artifact kind, description and image
hashes/sizes. Trusted CI prepares those exact bytes, source review authorizes the
exact candidate, and a separate protected signer creates catalogue metadata.
Public activation verifies the complete signed bundle before updating the host.
The client fetches content-addressed files from the signed catalogue, rather
than hotlinking author/provider images at runtime.

Published `(ID, version)` entries are immutable. Artwork-only changes currently
need a new extension version/tag and exact candidate approval. This does not
require a new Grain installer. Existing tester exceptions never approve a
new source commit automatically. The [ownership/review policy](REVIEW-POLICY.md)
defines ID enrollment, permitted submitters and exact per-release approvals;
authors cannot enroll themselves by modifying `ownership.json`. OAuth app registration and account consent
are separate from source publication and never supplied by artwork metadata.

See the maintained Grain [CLI guide](https://github.com/Punit-Dethe/Grain/blob/extensions/main-integration-20261010/crates/grain-ext-cli/README.md)
and [artwork/publishing explanation](https://github.com/Punit-Dethe/Grain/blob/extensions/main-integration-20261010/docs/Extensions%202.0/EXTENSION-ARTWORK-AND-PUBLISHING.md)
for the author and operator details.
