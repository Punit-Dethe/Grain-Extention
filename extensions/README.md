# Community extensions

One directory per submitted extension, `extensions/<id>/`. **This is the
submission tree** — what you add a PR to when you publish your own extension.
Start from [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

Each directory holds a *source pointer*, never a built artifact:

```
extensions/<id>/
  submission.toml    id, source repo, pinned tag + commit, categories, licence, contact
  README.md          store copy
  screenshots/       optional
```

## Learn from the examples

- **`com.example.hello`** — the canonical minimal example: a scripted transcript
  transform. Read it to see the smallest complete submission.

Grain's own first-party extensions live in [`../core/`](../core/) — read those
for worked examples of specific patterns, but submit *your* extension here.
