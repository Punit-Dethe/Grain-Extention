# Note Window (grain.note-ui)

A window for reading and editing your Grain Space notes.

**It is optional, and that is the point.** Grain Space keeps notes as ordinary
Markdown files, so most people read them somewhere they already are — an
Obsidian vault, an editor, or through Grain's own Recall and the MCP bridge.
Nothing about capture, search, reminders or retrieval needs this installed.

Install it if you want a window: a list of your notes, an editor, and a place to
browse rather than search.

## Why an extension

Because a window you ship is a window that runs. Grain's argument is that a
feature you are not using costs nothing, and a note viewer compiled into the app
was the one place that was not quite true. As an extension it costs nothing
until you install it, and a rough edge in it is a rough edge in an extension you
chose rather than in the app underneath.

## What it can reach

One capability: `notes` — read and change your Grain Space notes. That is the
whole grant, and it is exactly what a note window needs. It asks for no network
access, so nothing it reads can leave this machine.

## Files

| File | Role |
|---|---|
| `main.js` | The worker. Opens the window when the shortcut fires; nothing else. |
| `ui.html` | The window itself, in a sandboxed frame with its own token. |
