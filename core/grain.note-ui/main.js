// Note Window — the worker. Its only job is to open the window when the
// shortcut fires; everything a person does happens inside the surface, which
// talks to the host on its own channel with its own token.
//
// Deliberately this small. The worker is asleep until the shortcut wakes it,
// does one thing, and is reaped — nothing here is resident. The window it opens
// is the host's: built hidden once, slept on close, destroyed when idle.

grain.onShortcut(function (id) {
  if (id !== "open") return;
  return grain.workspace.open().catch(function (e) {
    grain.log.warn("note-ui: couldn't open the window: " + ((e && e.message) || e));
  });
});
