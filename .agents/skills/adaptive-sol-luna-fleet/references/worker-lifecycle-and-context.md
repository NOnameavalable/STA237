# Worker Lifecycle and Context

**Read when:** deciding whether to continue an active Luna or spawn a fresh one; a worker's scope expands; a follow-up appears after completion; active slots are full; several waves are needed; or context handoff is unclear.

This reference covers lifecycle and handoff edge cases. [SKILL.md](../SKILL.md) contains the operating rules.

## Active task or new task?

An active Luna can receive clarification, a missing file location, or an updated constraint that remains within its current bounded objective. Once that objective is complete, the worker externalizes its result and retires. A later repair, new audit, or newly identified issue that requires a new bounded worker task should normally go to a fresh Luna, regardless of task size.

If an active worker's scope expands materially, Sol should reassess dependencies and ownership. Split off a new bounded task when it can be handed to a fresh worker without losing necessary context. Do not rely on an indefinitely continuing worker as the task's state store.

## Multi-wave scheduling

The ceiling concerns **simultaneously active** Luna Workers. For example, four workers can complete and retire in wave one, then three fresh workers can be used in wave two; the task has used seven workers in total while never exceeding four active at once. When all available slots are occupied, schedule additional bounded work for a later wave after an active worker completes and releases its slot; never exceed the active-worker ceiling. Runtime capacity may set a lower ceiling.

Parallelize independent tasks when their inputs are ready. Sequence production before an audit that requires its artifact. Avoid creating an idle verifier before there is a meaningful result to inspect.

## Minimum sufficient handoff

A fresh worker usually needs:

- Its objective and acceptance criteria.
- Current paths or locations of relevant artifacts and sources.
- Verified findings and unresolved issues that affect the task.
- Constraints, dependencies, and known risks.
- The expected output and completion condition.

Prefer precise file references, diffs, and compact findings over a full conversation transcript. A departing worker should externalize enough information for Sol or another fresh worker to continue without its private history.

## Worker result example

```text
Completed work: Updated the specified sections and regenerated the PDF.
Changed artifacts: notes.md; notes.pdf.
Checks: Required topics present; rendered affected pages inspected.
Evidence: Diff and page numbers for each corrected issue.
Unresolved: One source claim remains ambiguous.
Suggested Commander decision: Verify that claim or accept the stated uncertainty.
```

This is an example, not a mandatory output format. Keep reports concise and useful for Sol's review and later handoff.
