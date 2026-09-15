# Research decisions and unresolved claims

## Evidence boundaries

The [corpus inventory](corpus.json) covers all 164 Reddit documents and both
shared engineering documents present at the baseline. Full text was indexed
and searched; titles and extracted issue descriptions were triaged throughout
the collection. Detailed semantic review concentrated on the consequential
claims below. This is not a claim that every comment, screenshot, external
link, price, benchmark, or proposed remedy was independently verified.

Each original is retained. The readability document received formatting-only
repairs, including a shorter equivalent code comment; its original bytes remain
in the baseline snapshot. Duplicate posts remain available and are grouped by
source URL in the inventory rather than counted as independent evidence.
Upvotes and repeated complaints establish neither causality nor reproducibility.

The user's failure catalog supplies concrete acceptance scenarios across
authority, interpretation, architecture, sources, tools, correctness,
verification, stopping, coordination, skills, memory and communication. It is
not copied wholesale into runtime instructions. A proposed solution in that
catalog still needs a matching mechanism and evidence.

## Claim ledger

| Claim or disagreement | Assessment | Decision |
| --- | --- | --- |
| Astra announces testing and then returns without acting. | Matches the user's premature-hand-back and activity-as-progress failures. [Community report][announcing] supplies a symptom, not a proven client cause. | State continuation and honest stopping explicitly; do not install an automatic retry loop. |
| Goals cure premature stopping. | [Stopping discussion][stopping] recommends goals, while [goal-loop discussion][goal-loop] reports runaway continuation. Native goal status rules are specific and do not certify an artifact. | Keep goals opt-in. Preserve native blocking rules and separate goal budgets from context budgets. |
| Experimental compaction preserves every detail. | [Context-size discussion][context-size] contains that assertion. [Official experiment guidance][context-doc] describes eligibility and notes/history, not guaranteed persistence. The reset handler lacks a save-success check. | Retain the opt-in, remove the guarantee, verify successful notes and recovery access before a reset. |
| Notes/history 404 errors can precede destructive context reset. | [Upstream issue][notes-issue] describes this on 0.153.4 with a modified catalog and no unmodified control. It is not a reproduction on this account or version. | Treat endpoint success as unverified; do not copy a local substitute backend or extrapolate the issue as universal. |
| Set a larger context window to improve continuity. | Comments disagree on cost and effectiveness. Local client/source cannot establish subscription multipliers or a task-specific optimum. | Do not enlarge context limits or invent compaction thresholds. |
| Skills stop loading after 220 lines. | [Incomplete-read report][partial-read] describes observed partial shell reads. Pinned source has a separate, path-specific 8,000-byte main-prompt cap. | Split oversized entrypoints for the constrained path; preserve critical distinctions and reference-loading conditions. |
| Remove all skills for Astra. | [Skill discussion][skills-discussion] contains conflicting views. [Official Astra guidance][astra-guide] favors focused, relevant guidance rather than indiscriminate deletion. | Retain domain knowledge, fix actual routing/metadata defects, and avoid claiming a measured quality or quota gain. |
| Lower effort always uses less quota. | The corpus contains both low-effort success and high-effort completion/usage anecdotes. Workload, retries, context and server accounting differ. | Retain current effort assignments; no automatic escalation policy or pricing-derived subscription estimate. |
| Astra should always/never orchestrate. | Both positions occur in the corpus, including direct-work success and delegation failures. Neither proves a universal model policy. | Remove mandatory coordination and the blanket Astra prohibition; keep named roles as optional tools. |
| Omitted `fork_turns` copies full history. | [Fork discussion][fork-report] is supported by the pinned V2 parser, which defaults to `all`. Reported token totals remain anecdotal. | Retain fresh-context enforcement and explicit task packets. |
| A universal 60-second wakeup is the cause of quota loss. | [Waiting discussion][waiting] mixes prompt wording, tool timeouts and billing claims. Configurable waits and current schemas must be distinguished from model continuation and server accounting. | Retain blocking waits and quiet custom prompts. Do not promise that eliminating polls removes all quota drain. |
| Compression tools always save usage. | The corpus includes a contrary multi-setup report. The audit's Headroom attempt did not usefully compress a large prose batch. | Retain the available integration, but do not make it mandatory or equate availability with a useful reduction. |
| Passing tests or a worker's final answer proves completion. | Contradicted by the user's evidence-overreach, mock-away and false-completion failures. | Require artifacts and relevant checks; label static, mechanical and live evidence separately. |
| Minified code and shell wrappers are harmless token efficiency. | [Ronacher's examples][ronacher] show readability and tool-use concerns, in a harness that is not identical to this one. | Preserve readable code, direct editing and narrowly scoped responsibilities. Do not transfer Pi-specific behavior as a Codex implementation fact. |
| A trusted hook hash verifies the executable. | Pinned discovery hashes the normalized definition, not the referenced executable bytes. | Preserve native trust settings, review changed scripts explicitly, and document reload/review requirements. |
| Flex is available because the JSON schema accepts it. | The [schema][schema] uses a string; pinned session code separately gates every tier behind fast mode and filters catalog support. | Use the authorized standard fallback and never priority. No fake `standard` wire identifier or ineffective Flex promise. |
| Always mark every plan step complete before replying. | Conflicts with honest reporting of a real external blocker. A checklist status is not an artifact check. | Mark only verified outcomes complete; leave blocked work accurate. |
| Invoking a skill establishes persistent cross-context instructions. | Not established by the provider's loading paths. Explicit-only policy in portable frontmatter was also invalid in four packages. | Put client policy in the supported metadata file and stop claiming guaranteed persistence across context windows. |

## Deciding scenarios

| Failure case | Expected result | Evidence available |
| --- | --- | --- |
| Executable authorized work remains after a checkpoint. | Continue work rather than return a promise. | Instructions revised; no model trial. |
| A real external dependency blocks a planned item. | Preserve unfinished status and report the exact blocker. | Instruction review; no model trial. |
| Config/profile/role selects priority or enables fast mode. | Validator rejects the override. | Executed configuration tests. |
| Checkpoint save fails after older evidence exists. | Failure is observable and older evidence is invalidated. | Executed subprocess fixture. |
| Corrupt, cross-session, cross-directory or cross-transcript checkpoint. | No recovery injection; failure is observable; checkpoint is consumed. | Executed subprocess fixtures. |
| A saved assistant message claims success or contains recovery delimiters. | Quoted historical evidence, not current authorization or completion proof. | Executed bounds/escaping fixture; no claim of complete prompt-injection prevention. |
| Same recovery event is replayed. | A consumed checkpoint is not injected twice. | Executed subprocess fixture. |
| Long Unicode or escape-heavy snippets. | Bounded complete output retains recovery instructions. | Executed subprocess fixtures. |
| Native notes save fails or tools are absent. | Do not assume recoverability or manufacture native tools/state. | Source trace and instruction review; backend trial unavailable. |
| Explicit skill versus adjacent task. | Respect invocation policy and load the relevant detailed route only. | Metadata, links and manual scenario review; model-selected activation unmeasured. |

## Review limits

No agents, paid model comparisons, synthetic benchmark platform, upstream
build, emulator guest, editor host, destructive provider operation, or private
notes-backend experiment was run. Whole-corpus inventory is complete; external
claims and domain execution remain explicitly unresolved where not checked.
Changed technical claims about this harness are tied to the pinned source.

[announcing]: https://www.reddit.com/r/codex/comments/1wedfpu/astra_sometimes_gets_stuck_announcing_work/
[stopping]: https://www.reddit.com/r/codex/comments/1wfto54/astra_stopping_all_the_time/
[goal-loop]: https://www.reddit.com/r/codex/comments/1w9my9c/finally_figured_out_why_goal_used_100_of_my_usage/
[context-size]: https://www.reddit.com/r/codex/comments/1wbpfko/should_i_upgrade_max_context_size_for_astra_from/
[context-doc]: https://learn.chatgpt.com/docs/models?surface=app#experimental-context-management
[notes-issue]: https://github.com/openai/codex/issues/43194
[partial-read]: https://www.reddit.com/r/codex/comments/1t1rbqt/codex_may_only_read_the_first_220_lines_of_a/
[skills-discussion]: https://www.reddit.com/r/codex/comments/1wc1teh/should_you_still_use_skills_with_astra/
[astra-guide]: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
[fork-report]: ../reddit/So_just_learned_that_fork_turns_defaults_to__all__=_astra_subagents_get_dumped_with_800k+_initial_context_bloat.md
[waiting]: https://www.reddit.com/r/codex/comments/1wffvur/codex_system_prompt_still_forces_agents_to_wake/
[ronacher]: https://lucumr.pocoo.org/2026/9/7/astra-why/
[schema]: https://developers.openai.com/codex/config-schema.json
