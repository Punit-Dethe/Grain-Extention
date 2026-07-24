// Voice Actions — the worker. Runs on the finalized transcript: matches the
// user's configured triggers, fires their side effects (open a URL / launch a
// user-approved app), and returns the transcript with the trigger removed.
//
// Security note: this code never launches anything on its own. `grain.open.url`
// is scheme-allowlisted by the host, and `grain.open.app` only launches a path
// the user picked through `grain.open.pickApp()` (see config.html). The worker
// merely relays the user's own configured rules.

function normalize(s) {
  return String(s || "").toLowerCase().trim();
}

// Open the config surface from the contributed shortcut.
grain.onShortcut(function (id) {
  if (id === "configure") grain.workspace.open();
});

// The transform hook: strip matched triggers, fire their targets.
grain.onTransform(function (text) {
  return grain.storage.get("rules").then(function (rules) {
    rules = Array.isArray(rules) ? rules : [];
    if (!rules.length) return text;

    var out = text;
    var fired = [];
    rules.forEach(function (r) {
      var trigger = normalize(r && r.trigger);
      if (!trigger) return;
      var idx = out.toLowerCase().indexOf(trigger);
      if (idx !== -1) {
        out = out.slice(0, idx) + out.slice(idx + trigger.length);
        fired.push(r);
      }
    });

    // Fire-and-forget so a slow launch never blocks the paste path.
    fired.forEach(function (r) {
      try {
        if (r.kind === "app") grain.open.app(String(r.target));
        else grain.open.url(String(r.target));
      } catch (e) {
        /* a launch failure must never break the transcript */
      }
    });

    return out.replace(/\s+/g, " ").trim();
  });
});
