# App Modes (grain.app-modes)

Your own formatting instructions, applied only inside a specific app or website.
Define a mode — a name, a target (an app or a website host), and a prompt — and
whenever you dictate with that app in the foreground, the transcript is
reformatted with that mode's instructions. This is the externalised form of
Grain's Context Awareness *modes*.

## What it demonstrates

- **`transform:transcript`** — the worker (`main.js`) rewrites the finalized
  transcript when a mode matches.
- **`capture:app`** — reads which app is foreground (the same primitive Grain's
  own Context Awareness uses) to decide which mode, if any, applies. No match →
  no LLM call is made.
- **`llm`** — sends the transcript plus the mode's prompt to the user's own
  configured AI provider.
- **the custom settings card** — `config.html` renders in a sandboxed iframe as
  a `panel`, anchored at `context.after`, so the editor sits right below the
  Context settings. It stores modes in the extension's own `modes` setting.

## Files

| File | Role |
|---|---|
| `manifest.json` | Declares the tier, permissions, activation, and the `panel` settings card at `context.after`. |
| `main.js` | The worker: on transform, match the foreground app and reformat via the LLM. |
| `config.html` | The custom card: add/edit/remove modes (name, app/web target, capture, prompt + templates). |

The published single-file pack is produced from these by `grain-registry
build-pack` (entry + card HTML inlined).
