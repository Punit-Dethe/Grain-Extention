# grain-extensions

The public submission registry for [Grain](https://github.com/Punit-Dethe/Grain)
extensions. This repository is the **source of truth** for what may be published;
what the Grain app actually reads is a set of **signed static files** published as
GitHub Releases (`v1/index.json`, `v1/roots.json`, `v1/revocations.json`, and
content-addressed `v1/blob/<sha256>.grainpack`) — never the git tree, and never a
website.

- **How to submit:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **How submissions are reviewed:** [REVIEW-POLICY.md](REVIEW-POLICY.md)

## What this is (and is not)

- **Is:** a place to submit a *source pointer* (repo + pinned commit) via pull
  request. We build the artifact ourselves, from your pinned commit, so
  "reviewed" and "installed" are provably the same bytes.
- **Is not:** an upload host. You never submit a built artifact, an account, a
  signing key, or a payment method.

## Trust, in one line

If an extension is listed in the store, **a human read its source at that exact
version.** Trust lives only inside the signed index we produce — never in your
manifest, your pack, your repo, or your domain.

## Layout

```
extensions/<id>/          one directory per extension id (reverse-DNS)
  submission.toml         id, source repo, pinned tag + commit, categories, licence, contact
  README.md               store copy
  screenshots/            optional
.github/workflows/        the two-job CI (build-and-check, then publish on merge)
v1/                        what the app reads (signed; published as Releases)
site/                      the public shop window (generated from the index)
```
