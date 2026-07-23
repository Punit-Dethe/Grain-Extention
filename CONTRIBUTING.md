# Contributing an extension

Submitting is a pull request that adds **one directory** under `extensions/`.
You submit a *source pointer*, never a built artifact.

## The author's path

```bash
grain-ext init my-extension     # scaffold: manifest + entry + generated types
grain-ext dev                   # build → run in Grain → hot reload
grain-ext doctor                # the EXACT checks CI will run, locally
grain-ext submit                # opens the PR against grain-extensions
```

`submit` writes one directory to this repo and opens a pull request:

```
extensions/<id>/
  submission.toml    id, source repo, pinned tag + commit, categories, licence, contact
  README.md          store copy
  screenshots/       optional
```

## Required

- A **public** source repository.
- A **pinned tag and commit** — we build exactly that.
- An SPDX **licence** (CI fails without one).
- A one-line **summary**, at least one **category**, and a **contact**.

## Not required

- A built artifact (we build it).
- An account, a signing key, or a payment method.

## What CI checks (all blocking)

- Manifest validates against `grain-sdk`; capabilities are known names.
- **No invisible or bidirectional Unicode** anywhere in submitted source.
- No minified/obfuscated source in the source tree (we produce the minified
  artifact ourselves).
- Size caps; the artifact is reproducible from the pinned commit.
- `id` is reverse-DNS, unique, and not a near-miss of an existing id (typosquat
  check).
- Licence present.

## Flagged capabilities

Some capability combinations mean "this extension can see something private *and*
send it somewhere". They do not block publication, but they require a written
justification and a closer read:

- `screen:capture` + `net:*`
- `events:transcripts` + `net:*`
- any `native` tier with `net:*`

If your extension legitimately needs one, explain why in the PR. See
[REVIEW-POLICY.md](REVIEW-POLICY.md).
