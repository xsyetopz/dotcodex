# Audit Signals

| Signal | Likely cause | Corrective direction |
| --- | --- | --- |
| high input, tiny output, repeated turns | polling | blocking wait |
| many poll-only goal turns | goal continuation loop | wait outside inference |
| parent and worker touch same task | shadow delegation | root integrates only |
| large child contexts | history fork | `fork_turns:"none"` |
| repeated timeout tool errors | bad timeout argument | omit override/use integer default |
| post-compaction task loss | weak recovery state | compact checkpoint/recovery |
| Astra/root waiting loops | expensive orchestration | bounded worker only |
| more than two direct spawn calls | delegation fan-out | inspect task ownership and duplicate work |
| rapid automatic goal continuations without change events | possible continuation loop | inspect goal state and turn boundaries |

## Evidence grades

- **Measured:** event counts, token fields, tool names, fork arguments, exit
  codes, and compaction markers present in the selected rollout.
- **Correlated:** a measured event sequence matches a specific configuration,
  prompt, hook, or skill rule.
- **Inferred:** intent, duplicated reasoning, or worker/coordinator
  responsibility reconstructed from authorized content inspection.

Record malformed JSONL and unreadable files as input limitations. Do not
silently treat a partial report as a clean audit. Repeated waits mean adjacent
wait calls; a single long blocking wait is expected behavior.
Repeated `functions.wait` calls for one cell and their `yield_time_ms`
distribution are measured separately. A command's output bytes measure recorded
output volume, not usefulness or mutation. Automatic continuation and
no-change-event counts are likewise prompts for review, not findings by
themselves.

Do not assume cached input is free for subscription quota accounting. Compare
rollout behavior, rate-limit movement, and repeated context size instead of
estimating subscription cost from API pricing.
