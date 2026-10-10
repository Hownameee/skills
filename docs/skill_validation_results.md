# Skill Efficiency Validation

Date: 2026-09-28

## Scope

The audit fixes cover repeated discovery, routing boundaries, unnecessary approval requests, draft-versus-execution stops, conditional validation, unsupported CV details, and repository installation behavior. The upstream package is retained under `skills/ai-skill-creator/` with its declared name and attribution updated for the local rename; its evaluation resources and workflow remain otherwise unchanged.

## Checks And Evidence

| Check | Result | Reproduce or inspect |
| --- | --- | --- |
| Package validation | Passed for 41 skills | `python3 -B scripts/validate_skills.py` |
| Installer and catalog regressions | Passed | `python3 -B -m unittest discover -s tests -v` |
| Diff whitespace | Passed | `git diff --check` |
| Preservation of protected package | All 18 files byte-identical to the pre-edit snapshot | SHA-256 comparison during this run |
| CV license preservation | Complete MIT notice retained in the bundled `LICENSE` | Compare with the original notice in the prior `SKILL.md` |
| Trigger matrix completeness | All 41 packages have a row | Catalog regression test |
| Behavior examples | Eight same-author inline sanity reviews recorded | [Prompts and assertions](../evals/evals.json), [responses and evidence](../evals/inline_review.json) |
| Independent old/new comparison | Not run to completion: both executor agents hit the account usage limit before producing outputs | Retry the paired procedure below when execution is available |
| Fresh-host activation and measured efficiency | Not run | [Trigger matrix](./skill_trigger_tests.md) |

Installer tests use disposable paths only. They cover preservation of unrelated/system skills, replacement of managed packages and supporting files, exclusion of evaluation workspaces with and without snapshots, rejection of malformed/nested packages, preservation on copy failure, symlink refusal, and nonzero failure reporting. No global installation, live infrastructure action, or dependency installation was performed.

## Behavior Review Limits

The eight cases cover lightweight planning with an unknown assignee, static SQL review, a factual CV bullet, focused test completion, existing incident authorization, resource-server-only security tests, discovery reuse, and a simple Ponytail completion message.

The editor generated the inline responses and reviewed them against the known assertions. This is a sanity check, not independent evidence that the new skills outperform the old ones. No baseline outputs, token counts, timing measurements, or cross-host activation rates are claimed. The static review page was generated with the unchanged upstream `eval-viewer/generate_review.py`; the JSON files retain the examples for later review or regeneration.

## Repeatable Evaluation

1. Snapshot the versions being compared outside `skills/` or in an ignored `<name>-workspace/` directory. Use identical supplied facts for each version.
2. Read a case from `evals/evals.json`. Give fresh executors only its prompt and the listed skill files, separately for old and revised versions. Keep expected outputs and assertions out of the executor inputs.
3. Save each response and action log under `eval-<id>-<name>/<variant>/outputs/` and grade against the stored assertions with exact evidence. Record actual failures and unavailable measurements without substituting zeros or character counts for token telemetry.
4. Generate a static viewer with the existing script using Python 3.10 or newer (Python 3.11 was available and used in this run; the system Python 3.9 failed on the upstream type annotations):

   ```bash
   python3.11 skills/ai-skill-creator/eval-viewer/generate_review.py /path/to/evaluation-workspace --static /path/to/review.html
   ```

5. Review the outputs and test fresh-host routing separately. Use multiple runs before making comparative quality, time, or token claims.

The upstream aggregator currently expects `run-*` directories and can substitute output characters for missing token counts. Its instructions also assume Claude-specific model and tool behavior. Those findings remain intentionally unfixed; do not use them to claim a measured improvement without resolving or explicitly accounting for those limitations.
