const extensionName = "Tools";

grain.actions({
  hello: async () => ({ ok: { title: extensionName, body: "Hello from this tool." } })
});
