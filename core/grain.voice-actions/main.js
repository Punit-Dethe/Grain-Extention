// Voice Actions — the worker. Runs on the finalized transcript: matches the
// user's configured triggers, opens their websites/apps, and returns the text
// with the trigger removed.
//
// Config lives in the extension's declared settings (rendered natively in the
// Snippets tab — no webview): `actions` is a list of
//   { trigger, websites: [{ url }], apps: [{ path }] }.
//
// Security: this worker never launches anything on its own. `grain.open.url` is
// scheme-allowlisted by the host; `grain.open.app` only launches an app the user
// picked via the app-path control (which records approval). It merely relays the
// user's configured rules.

function normalize(s) {
  return String(s || "").toLowerCase().trim();
}

grain.onTransform(function (text) {
  return grain.settings.get("actions").then(function (actions) {
    actions = Array.isArray(actions) ? actions : [];
    if (!actions.length) return text;

    var out = text;
    var fired = [];
    actions.forEach(function (a) {
      var trigger = normalize(a && a.trigger);
      if (!trigger) return;
      var idx = out.toLowerCase().indexOf(trigger);
      if (idx !== -1) {
        out = out.slice(0, idx) + out.slice(idx + trigger.length);
        fired.push(a);
      }
    });

    // Fire-and-forget so a slow launch never blocks the paste path.
    fired.forEach(function (a) {
      (a.websites || []).forEach(function (w) {
        if (w && w.url) {
          try { grain.open.url(String(w.url)); } catch (e) {}
        }
      });
      (a.apps || []).forEach(function (p) {
        if (p && p.path) {
          try { grain.open.app(String(p.path)); } catch (e) {}
        }
      });
    });

    return out.replace(/\s+/g, " ").trim();
  });
});
