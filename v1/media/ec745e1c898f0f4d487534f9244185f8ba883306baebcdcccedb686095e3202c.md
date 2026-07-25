# Starter Prompts (grain.starter-prompts)

Three post-processing prompts to choose between: **General**, **Coding** and
**Email**. Install it and they appear in the prompt list in Post-processing,
grouped under this extension's name so it stays clear which of your prompts are
yours and which came from a pack.

Grain ships with one prompt, and writing a good one is more work than it looks —
most of a post-processing prompt is spent forbidding the model from being
helpful. These three are written to clean and nothing more.

| Prompt | What it does | What it refuses to do |
|---|---|---|
| General | Punctuation, capitalization, spoken numbers, filler removal, sentence and paragraph breaks. | Paraphrase, summarise, answer a question it finds, add anything unsaid. |
| Coding | Restores identifiers (`use effect` → `useEffect`), backticks code, paths, flags and commands, spells tools the way their projects do. | Write, complete or explain code. Formalise terse phrasing. |
| Email | Real paragraphs in the order you said things, grammar fixed, register kept. | Invent a greeting, sign-off or subject. Add pleasantries. Make it corporate. |

All three keep the language you dictated in, return nothing at all for an empty
transcript, and treat the transcript as text to clean rather than instructions
to follow.

## What it demonstrates

- **A prompt pack** — `payloads.prompts` in the manifest. The prompts are
  applied to your list under `ext:grain.starter-prompts:<id>` when you enable
  it, and removed by that prefix when you turn it off; if the one you had
  selected disappears, selection falls back rather than dangling.
- **A pure-data extension** — tier `pack`, no entry script, no permissions, no
  runtime and no storage. Nothing executes; there is nothing to grant. The
  manifest is the whole extension.

Because the prompts live in the pack, they are read-only in Settings. Edit one
by copying its text into a prompt of your own — that copy is yours, and updates
to this pack will not touch it.

## Files

| File | Role |
|---|---|
| `starter-prompts.grainpack.json` | The published pack: manifest + the three prompts. |
| `submission.toml` | Registry submission metadata. |
