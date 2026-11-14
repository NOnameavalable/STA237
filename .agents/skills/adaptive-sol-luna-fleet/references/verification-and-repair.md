# Verification and Repair

**Read when:** repair-pool grouping is unclear; an audit fails; a finding is disputed; the artifact changes after verification; the needed re-check scope is unclear; producer/verifier roles become mixed; or multiple repair rounds occur.

This reference covers verification decisions and repair edge cases. [SKILL.md](../SKILL.md) contains the operating rules.

## Choose verification effort

| Result or risk | Useful check |
| --- | --- |
| Ordinary bounded output | Executor self-check and Sol review may suffice. |
| Important calculation or contested claim | Independent derivation or source check. |
| Substantial artifact | Inspect actual structure, diff, rendered output, or behavior; use an independent verifier when useful. |
| Repair after failed audit | Check the repaired area and affected dependencies; expand to full review when the change may have broader effects. |

Select checks that reduce meaningful uncertainty. Favor decisive evidence, reproducible calculations, source quality, and direct inspection over additional worker count.

## Decide whether verification still applies

Content edits, behavior changes, layout changes, altered source data, and meaningful regeneration can invalidate an earlier pass. A filename-only or nonsemantic packaging change may need only a targeted integrity check if it cannot affect the verified property. Judge the effect on the **property previously verified**, not the apparent size of the edit.

For example, changing a PDF title in the source may change layout and requires inspecting the new render. Renaming the already verified PDF without altering bytes may require confirming the delivered file is the same artifact. A repair after `FAIL` requires checking the repaired result; the earlier failure and any earlier pass do not certify it.

## Handle failed or disputed audits

1. Sol inspects all verifier findings, rejects unsupported ones, and groups valid corrections by artifact, execution chain, and dependency.
2. Sol finishes useful inspection and defines the smallest bounded repair task or tasks. Two compatible isolated corrections can share one Luna; a single dependent chain still belongs to Luna.
3. A fresh Luna performs each assigned repair chain and externalizes the resulting artifact and checks. A single isolated trivial fix may be made directly by Sol under the skill's repair-pool rule.
4. Sol chooses targeted or broader re-verification according to what changed and what remains uncertain.

Do not spawn a new repair worker for every reported defect. Complete pending corrections before final verification. If a new correction changes an already verified artifact, verify the affected final state again.

If the verifier modifies the artifact during an audit, treat that worker as a producer for the changed state. Its earlier observations do not by themselves independently verify the modified artifact. Arrange a separate check if independence matters.

For a disputed finding, Sol assesses the relevant artifact state, source, reproduction steps, or calculation and resolves the conflict. If additional investigation or calculation is needed, Sol defines that bounded work for a fresh Luna. Agreement among workers is weaker than direct evidence. Avoid another audit round unless it addresses a concrete unresolved question.
