# Grain Space

A local scratch space for the things you would otherwise forget.

Speak a note. Select something and press a key. Ask a question out loud and get
an answer built from your own notes — without opening an app, and without your
writing leaving the machine.

Everything is plain Markdown on your disk. No account, no sync service, no
database you can't read.

## What you actually do with it

**Capture without stopping what you're doing.**

- **Quick Add** silently saves whatever text you have highlighted, anywhere.
- **Create Note** opens the Grain pill so you can speak *or* type. If you have
  text selected, that becomes the note and you just say what it's for.
- Each note gets a short title, a one-sentence summary, extracted to-dos, and a
  reminder if you asked for one — from the AI provider you already configured.
  No provider? The note is saved verbatim instead. Nothing is lost either way.

**Ask instead of browsing.**

Press the Recall shortcut and say the half-remembered fragment: *"what did I
decide about the buffer size?"* Grain searches your notes and answers, with the
notes it used listed underneath so you can open any of them. It can also edit a
note from the same conversation — say what changed and it merges the change in.

## Where your notes live

Two stores, one hard switch:

- **Grain's own store** — plain Markdown files in Grain's data folder. Nothing
  to set up.
- **Your Obsidian vault** — pick a vault and a subfolder. Captures become
  ordinary Markdown files inside it, searchable here and editable there, synced
  by whatever your vault already uses. Every other `.md` in the vault becomes
  searchable too, and is never written to.

Switching is a swap between the two, not a migration. Nothing is deleted.

## How search works

Three signals, fused:

- **Keyword search** for exact things — an error string, a filename, a flag.
- **Semantic search** for paraphrases, so "the auth timeout thing" finds a note
  that never used those words. Opt-in: it needs a 130 MB embedding model, and
  Grain asks before downloading anything.
- **Recency**, so this week's answer outranks last year's.

The results are then re-ranked and the best few are handed to the model. Long
documents are excerpted around what you asked about rather than truncated.

## Why it is light

Grain Space is built to cost nothing when you aren't using it:

- **Zero resident memory while its surfaces are closed.** No background daemon,
  no file watcher, no idle timer. The index is refreshed by a quick stat-scan at
  the moment you search.
- **The embedding model loads on first use and is dropped the instant the window
  closes.** It can run in half precision to halve even that.
- **Disabled means disabled** — shortcuts unregister immediately, the window is
  destroyed rather than hidden, nothing loads.
- The search index lives in Grain's data folder, never inside your vault, and is
  rebuildable from your files at any time.

## Privacy

- Notes are files on your disk. Grain never uploads them.
- Note text is sent to an AI provider **only** for the two things you asked for:
  writing a title/summary at capture, and answering a Recall question. Both use
  the provider you configured. With none configured, the feature still captures
  and still searches — it just doesn't write summaries or answer in prose.
- `capture:selection` reads the text you have highlighted, and only when you
  press the capture shortcut.
- The embedding model runs entirely on your machine.

## Uninstalling

Uninstalling turns the feature off. **It does not delete a single note.** Your
Markdown files stay exactly where they are — in Grain's data folder or in your
vault — and reinstalling picks them straight back up.

## Note on this extension

Grain Space is a **builtin** extension: it is listed, installed, enabled and
uninstalled like any other, but its implementation is compiled into Grain rather
than shipped as JavaScript. It has to be — it owns a local embedding engine, a
vector index, a native window and global shortcuts, none of which belong in a
sandboxed worker. The capabilities listed on this page are still the honest set
of what the feature touches.
