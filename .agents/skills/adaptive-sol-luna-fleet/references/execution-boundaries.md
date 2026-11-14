# Execution Boundaries

**Read when:** Sol/Luna ownership is unclear; Sol may be entering iterative production; a direct correction is growing; reasoning and mechanical work are intertwined; or a delegation may be too shallow.

This reference explains borderline ownership cases. [SKILL.md](../SKILL.md) contains the operating rules.

## Distinguish judgment from execution

| Situation | Likely owner | Reason |
| --- | --- | --- |
| Inspect representative pages or a decisive calculation, then decide what to do | Sol | The activity supports judgment. |
| Rewrite a document, render it, inspect pages, and adjust layout | Luna | Later steps depend on the produced artifact. |
| Implement code, run tests, debug a failure, and patch again | Luna | This is a dependent production chain. |
| Compare conflicting worker findings and choose the supported conclusion | Sol | The decision requires integration and evidence assessment. |
| Correct one isolated, trivial, high-confidence typo with no dependent production chain | Sol may do it | Delegation overhead may be disproportionate. |
| Correct two compatible isolated typos found during one inspection | One fresh Luna normally handles both | Batch pending mutations into one bounded task. |
| Correct a typo, rebuild a PDF, inspect the result, then change another line | Luna for the remaining chain | The correction has become iterative production. |

The number of tool calls is not a proxy for ownership. Ask whether Sol is **judging an existing result** or **producing a result through dependent operations**. A substantial chain can occur inside one script or tool call; several lightweight reads can still be supervision.

## Primary path and shallow delegation

If the task is to produce a revised document, a delegation such as “tell me how to revise it” leaves the primary execution with Sol. A useful Luna task is “revise the file, validate required coverage, and report the diff and unresolved issues.” The same distinction applies to code implementation, data transformation, source extraction, and artifact generation.

When reasoning and execution are mixed, Sol should define the desired outcome and constraints, then assign the bounded execution chain that can be separated. Sol handles truly inseparable judgment, conflicts, and final integration. If a worker fails or returns insufficient work, Sol may intervene to define a better task or make a single isolated trivial correction. A dependent or batched repair belongs in a new bounded Luna task.

## Sample task packets

**Document:** “Restructure these notes into a concept-first hierarchy, preserve every required topic, edit the file, validate coverage, then report changed sections and unresolved issues.”

**Artifact repair:** “Fix the identified layout defects, regenerate the output, visually inspect the affected pages, and return changed files, checks performed, and unresolved issues.”

**Code:** “Implement the specified behavior in the listed files, run the relevant checks, resolve failures caused by the change, then report the diff and remaining risks.”
