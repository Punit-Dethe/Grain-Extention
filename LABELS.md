# Review labels (the GitHub-native dashboard, §4.3)

GitHub *is* the dashboard: PRs are submissions, labels are state, checks are
evidence, comments are the audit trail. Keep state **structured** from day one so
a dashboard can be generated retroactively across the whole history.

## Decision

| Label | Meaning |
|---|---|
| `decision:accepted` | Merged → published. |
| `decision:changes-requested` | Author must fix and update the pinned commit. |
| `decision:rejected` | Not publishable (reason in the PR). |

## Hold (why a submission is paused)

| Label | Meaning |
|---|---|
| `hold:security` | A flagged combination or a finding needs a closer read / justification. |
| `hold:licence` | Missing or unclear licence. |
| `hold:lifecycle` | Native/resident lifecycle needs work (idle RAM, kill-clean). |
| `hold:reviewer-unavailable` | Queue paused (illness/travel). Shown publicly, not aged silently. |

## Class (how deep the read goes, from the flagged-combination list)

| Label | Meaning |
|---|---|
| `class:no-caps` | tier `pack`, no permissions — payload sanity, same-day target. |
| `class:ordinary` | full source read focused on declared capabilities (2–3 days). |
| `class:flagged` | a flagged combination — full read + written justification + runtime observation (up to a week). |

## Diff-only re-review (§3.4)

Because both versions are built from pinned commits, an update whose capability
set is unchanged and whose checks are green is reviewed as a **source diff**, not
a fresh codebase. The capability-diff line in the check output is the signal:
unchanged capabilities + green → diff read; any capability change or an oversized
diff → full read again. This is what keeps 100% review affordable as updates
outnumber new submissions.

## Sustainability notes

- **We build the bytes**, so there is never a "did this binary match the source"
  question — there is no upload.
- **`grain-ext doctor`** runs the exact CI checks locally, so submissions pass
  first time and round-trips (not review) are what would otherwise feel slow.
- **Our own extensions** built from the `grain` repo by our own CI are `core` by
  construction — same signing job, no queue.
