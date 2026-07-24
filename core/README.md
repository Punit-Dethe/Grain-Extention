# Core extensions (first-party)

These are **Grain's own** extensions, built from Grain's source by our CI and
published with `core` trust. They are **not** the community submission template —
see [`../extensions/`](../extensions/) and [`../CONTRIBUTING.md`](../CONTRIBUTING.md)
for how to submit your own.

They live here for three reasons:
1. **Separation** — the community `extensions/` tree stays a clean set of
   third-party submissions and authoring examples, uncluttered by first-party code.
2. **Reference** — each is a worked, production example of one pattern (a
   pure-data variant, a transcript transform, a context contribution). Read them
   to learn the real shape of an extension.
3. **One catalogue** — they publish into the *same* signed `v1/index.json` as
   community extensions (the index lists both; trust distinguishes them), so the
   app still reads a single catalogue.

| Extension | Pattern it demonstrates |
|---|---|
| `grain.agent-center-layout` | A pure-data **surface variant** (SPEC §10.2) — no code, one `variant_slots` entry. |

CI builds these from their pinned source and signs them with `core` trust; there
is no review queue for our own extensions (the same signing job, applied to a
publisher who is us).
