# Review policy

**Every extension, and every update, is read by a human before it is published.**
Nothing auto-publishes. If it is in the store, a person read its source at that
exact version.

## What that means for you

- There is **one reviewer** (the project owner). This is the real capacity
  constraint, and we are honest about it: if the reviewer is unavailable, the
  queue goes to a visible **paused** state rather than ageing silently.
- We build the artifact ourselves from your pinned commit, so an **update** is
  reviewed as a *source diff*, not a fresh codebase. An update that changes no
  capabilities and passes all checks is a quick diff read.

## Turnaround targets

| Class | What it is | The read | Target |
|---|---|---|---|
| **No capabilities** | tier `pack`, no permissions | payload sanity; there is no code | same day |
| **Ordinary** | anything else | full source read, focused on declared capabilities | 2–3 days |
| **Flagged** | a flagged combination (below) | full read **plus** a written justification per flagged capability, and a runtime observation | up to a week; may be refused |

## Flagged combinations

These mean "can see something private *and* can send it somewhere". They block
nothing automatically; they set how deep the read goes and what the store card
tells the user:

- `screen:capture` + `net:*`
- `events:transcripts` + `net:*`
- any `native` tier with `net:*`

The single source of this list is `grain-sdk`; CI and the app read the same list,
so what the user sees is what the reviewer was warned about.

## Negative states

- **`deprecated`** — no new installs; existing installs keep working; the card
  says why. For abandonment.
- **`revoked`** — the kill switch. On the next index refresh the client disables
  the extension, shows a red banner naming the reason, and offers one-click
  removal. Your data is kept unless you purge it.

Both are delivered by the signed `revocations.json`.

## Security contact

Report a malicious or compromised extension to **security@** (placeholder until a
domain is purchased). Revocation is rehearsed against a fixture before the store
opens, so the kill switch is never used for the first time in an emergency.
