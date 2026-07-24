// App Modes — the worker. On the finalized transcript, if the FOREGROUND app
// matches one of the user's modes, reformat the transcript with that mode's
// instructions via the configured AI provider. No match → the text is returned
// unchanged (and no LLM call is made).
//
// Config lives in the extension's own `modes` setting (edited by the custom card
// in config.html), the shape:
//   [{ id, name, match: { kind: "process" | "url_host", value }, prompt, enabled }]
//
// Security: capture:app only reveals which app is focused; llm sends text to the
// user's own configured provider. Both are grants the user approved.

function normProc(s) {
  return String(s || "").toLowerCase().replace(/\.exe$/, "").trim();
}
function normHost(s) {
  return String(s || "")
    .toLowerCase()
    .replace(/^https?:\/\//, "")
    .replace(/^www\./, "")
    .replace(/\/.*$/, "")
    .trim();
}

grain.onTransform(function (text) {
  if (!text || !text.trim()) return text;
  return grain.settings.get("modes").then(function (modes) {
    modes = Array.isArray(modes) ? modes : [];
    var active = modes.filter(function (m) {
      return m && m.enabled !== false && m.prompt && m.match && m.match.value;
    });
    if (!active.length) return text;

    // Only now do we look at the foreground app — nothing to match against
    // otherwise.
    return grain.focusedApp().then(function (app) {
      if (!app) return text;
      var mode = null;
      for (var i = 0; i < active.length; i++) {
        var m = active[i];
        var hit =
          m.match.kind === "url_host"
            ? app.urlHost && normHost(app.urlHost) === normHost(m.match.value)
            : app.exe && normProc(app.exe) === normProc(m.match.value);
        if (hit) { mode = m; break; }
      }
      if (!mode) return text;

      var prompt = mode.prompt + "\n\nTranscript:\n" + text;
      return grain.llm.complete(prompt).then(function (r) {
        var out = r && r.text != null ? r.text : (typeof r === "string" ? r : null);
        return out && String(out).trim() ? String(out).trim() : text;
      }).catch(function () { return text; });
    }).catch(function () { return text; });
  }).catch(function () { return text; });
});
