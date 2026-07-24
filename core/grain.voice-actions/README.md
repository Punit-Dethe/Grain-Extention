# Voice Actions (grain.voice-actions)

Say a trigger word and Grain opens the target — a website in your browser, or an
app you chose — then removes the trigger from what gets pasted. This is the
externalised form of Grain's built-in voice actions.

## What it demonstrates

- **`transform:transcript`** — the worker (`main.js`) rewrites the finalized
  transcript, stripping matched triggers.
- **`open:url`** — opens links. The host allows only `http/https/mailto/tel`, so
  a rule can never smuggle a `file:` or `javascript:` URL.
- **`open:app`** — launches an application, but only one the **user** chose
  through Grain's native picker (`grain.open.pickApp()` in `config.html`); the
  host records that approval and refuses any other path. An extension can never
  launch an arbitrary program or its own bundled files.
- **`surface:workspace`** — the config UI (`config.html`) where the user adds
  trigger → link / app rules, stored in `grain.storage`.

## Files

| File | Role |
|---|---|
| `manifest.json` | Declares the tier, permissions, activation, the config surface, and the `Configure` shortcut. |
| `main.js` | The worker: matches triggers on transform, fires the targets. |
| `config.html` | The workspace surface: add/list/remove rules; pick apps. |

The published single-file pack (`voice-actions.grainpack.json`) is produced from
these by `grain-registry build-pack` (entry + surface HTML inlined).
