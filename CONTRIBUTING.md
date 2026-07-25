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
  README.md          your store page — rendered in full on the detail view
  media/
    cover.webp       the card image (16:9). WEBP or GIF. Shown first, everywhere.
    *.webp | *.gif   further screenshots, in filename order
```

## Your store listing (just drop the files in)

There is **no extra metadata file** to write. The listing is assembled from
files you already keep:

| What the store shows | Where it comes from |
|---|---|
| Name, version, capabilities | `manifest.json` |
| One-line description on the card | `description` in `manifest.json` |
| Cover image (top of the card) | `media/cover.webp` (or `.gif`) |
| Screenshots on the detail page | the rest of `media/` |
| The full detail page body | `README.md` |
| Install count | measured by us; you never supply it |

Images must be **WEBP or GIF** (no video, no PNG/JPEG) — they are
content-addressed and served as small immutable blobs, so the store stays fast
and an image can never be swapped under a published version. Keep a cover near
16:9 and under ~200 KB.

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
