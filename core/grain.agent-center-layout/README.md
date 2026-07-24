# Agent — Centre layout (grain.agent-center-layout)

A pure-data **surface variant** for Grain's Agent reply panel. It ships no code:
its whole manifest is an `id`, a name, and a single `variant_slots` entry for
`agent.reply-surface`.

**What it does.** Enabling it adds a **Centre** option to the Agent's reply-panel
position setting. Selecting Centre moves the panel to the middle of the screen;
the host renders it. Disabling or uninstalling it removes the option (the panel
falls back to the side).

**Why it's a good first example.** It is the simplest possible extension — no
runtime, no permissions, no assets — and it demonstrates the variant-slot
contract (SPEC §10.2): a pack *offers* itself for a position without *claiming*
it, so enabling it is never a takeover.
