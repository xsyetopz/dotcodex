# Code Readability for Humans and AI Agents

Code should be readable by three levels of human reader:

- **A1–A2 — beginner:** can follow the local control flow and understand what
  the code is doing.
- **B1–B2 — intermediate:** can modify the code safely without reconstructing
  the entire subsystem.
- **C1–C2 — advanced:** can understand the abstractions, invariants, tradeoffs,
  and architecture without fighting accidental complexity.

The codebase must not require C1–C2 skill merely to understand ordinary
implementation code.

AI agents are not exempt from this rule. They are often fast at producing
locally plausible code and weak at preserving global intent, terminology,
invariants, and architecture. Write code so that both humans and agents have
fewer opportunities to infer the wrong thing.

## Core rule

Optimize for **low ambiguity, low working-memory cost, and predictable
structure**.

Do not optimize for:

- minimum line count;
- cleverness;
- abstraction count;
- novelty;
- compactness;
- showing language knowledge.

Readable code should make the correct interpretation obvious.

## Function limits

Use mechanical limits as guardrails, not as substitutes for judgment.

| Metric | Target | Review |
| --- | ---: | ---: |
| Function body | ≤ 30 NLOC | > 40 |
| Cognitive complexity | ≤ 10 | > 15 |
| Cyclomatic complexity | ≤ 8 | > 10 |
| Nesting depth | ≤ 2 | > 3 |
| Parameters | ≤ 4 | > 6 |
| Local variables | ≤ 7 | > 10 |
| Line width | ≤ 100 | > 120 |

A straight-line 45-line function may be easier to read than a 15-line function
with nested branches, hidden state, callbacks, and overloaded abstractions. Do
not split functions purely to satisfy LOC.

## A1–A2 readability

A beginner should be able to answer:

- What does this function do?
- What are its inputs?
- What does it return or change?
- What is the normal path?
- What can fail?
- Where does execution go next?

To make that possible:

- use descriptive names;
- keep control flow top-to-bottom;
- prefer guard clauses over deep nesting;
- keep one statement per line;
- avoid nested ternaries;
- avoid hidden side effects;
- avoid implicit state;
- avoid unnecessary metaprogramming;
- avoid dense expression chains;
- keep related code physically close;
- use blank lines to separate conceptual phases.

Do not require a beginner to understand the architecture before understanding a
local function.

## B1–B2 readability

An intermediate reader should be able to change behavior safely.

They should be able to identify:

- which module owns the behavior;
- which invariant must remain true;
- which types represent which concepts;
- which operations mutate state;
- which operations perform I/O;
- which errors are expected;
- which tests cover the behavior;
- which neighboring code follows the same pattern.

To make that possible:

- keep terminology consistent across files;
- encode units in names or types;
- use strong types where semantically different values could be confused;
- make ownership and lifetime visible;
- make side effects explicit;
- keep dependencies explicit;
- keep modules cohesive;
- avoid generic `utils`, `helpers`, `misc`, and `common` dumping grounds;
- keep tests structurally similar to the code they specify.

An intermediate reader should not need repository archaeology for ordinary
changes.

## C1–C2 readability

An advanced reader should be able to see the design rather than reverse-engineer
it.

They should be able to identify:

- subsystem boundaries;
- invariants;
- dependency direction;
- ownership rules;
- failure semantics;
- concurrency rules;
- performance-sensitive paths;
- compatibility constraints;
- intentional deviations from normal patterns.

Make these visible in code, types, module structure, and short local comments.

Do not bury architectural rules inside:

- tribal knowledge;
- issue history;
- commit history;
- generated prose;
- distant documentation;
- one maintainer's memory.

Documentation may explain architecture. Code must still reveal enough structure
to obey it.

## Rules for AI agents

AI agents commonly fail in predictable ways.

### 1. They optimize locally

An agent may make one function cleaner while making the repository less
coherent.

Therefore:

- preserve existing architecture unless the task changes it;
- prefer established repository patterns over a new local abstraction;
- do not introduce a new framework, helper layer, or naming scheme without need;
- inspect neighboring code before inventing structure.

Local elegance does not outrank global consistency.

### 2. They infer through ambiguity

If two concepts use similar names, agents may merge them mentally.

If one concept uses several names, agents may treat them as separate.

Therefore:

> One concept → one canonical term.
> Different concepts → different terms.

Do not casually alternate between `repo`, `repository`, `store`, `storage`, and
`db` for the same thing.

### 3. They over-abstract

Agents often extract code because two regions look similar.

Syntactic similarity is not enough.

Extract when the abstraction represents a stable concept.

Do not create helpers that merely rename trivial syntax.

Good:

```text
validate_packet_header()
```

Usually bad:

```text
increment_index()
```

when it only performs `index += 1`.

### 4. They under-abstract

Agents also produce long procedural functions because the code is locally easy
to generate.

Extract when a block:

- has a distinct purpose;
- changes abstraction level;
- has its own invariant;
- can be named more clearly than it can be explained inline.

Do not split arbitrary chunks to reach a line-count target.

### 5. They hide uncertainty with plausible code

Plausible is not correct.

Agents must not guess:

- API behavior;
- ownership;
- units;
- concurrency guarantees;
- platform behavior;
- serialization formats;
- compatibility requirements;
- error semantics.

When the codebase does not establish the answer, the uncertainty must remain
visible until resolved.

Do not convert missing knowledge into confident implementation.

### 6. They create accidental terminology drift

Agents frequently introduce synonyms because each prompt is interpreted
independently.

Repository vocabulary is part of the architecture.

Reuse existing names unless the task explicitly changes terminology.

### 7. They create unnecessary churn

Agents may:

- rename unrelated variables;
- reformat untouched code;
- reorder declarations;
- rewrite working logic;
- replace an established pattern with a preferred one.

Do not.

Keep diffs narrow and intentional.

### 8. They treat passing tests as proof

Passing tests prove only what the tests exercise.

Agents must also inspect:

- invariants;
- boundary conditions;
- error paths;
- concurrency;
- resource lifetime;
- compatibility constraints;
- caller expectations.

A green test suite does not justify ignoring code semantics.

### 9. They imitate bad code

Consistency matters, but reproducing an obvious defect is not a virtue.

Distinguish:

- repository convention;
- historical accident;
- local workaround;
- actual bug.

When a pattern is suspicious, verify before copying it.

### 10. They confuse comments with understanding

Do not compensate for confusing code by adding paragraphs explaining it.

Prefer:

1. better names;
1. clearer structure;
1. stronger types;
1. explicit control flow;
1. a short comment only where the reason cannot be expressed in code.

Comments should explain **why**, constraints, compatibility, or non-obvious
facts.

Do not narrate obvious syntax.

## Structural rules

Prefer this visual shape:

```text
validate

prepare

execute

handle result
```

Avoid this:

```text
if
    if
        loop
            if
                callback
                    mutate hidden state
```

Prefer:

- early exits;
- shallow nesting;
- explicit phases;
- obvious happy path;
- localized error handling.

Avoid:

- hidden control flow;
- surprising operator overloads;
- callback pyramids;
- deeply chained expressions;
- implicit global state;
- magic configuration;
- reflection for ordinary dispatch;
- macros that alter apparent control flow.

## Naming rules

Names should reduce context lookup.

Prefer:

```text
remaining_bytes
connection_timeout_ms
candidate_paths
user_id
```

Avoid:

```text
rem
timeout2
data
thing
tmp2
value
```

Use short names only where the scope and meaning are genuinely obvious.

Boolean predicates should read as predicates:

```text
is_valid
has_header
can_retry
```

Functions should normally reveal intent:

```text
parse_config
load_user
validate_header
save_state
send_notification
```

Names are not decoration. They are part of the program's interface to both
humans and machines.

## State and side effects

A reader should be able to see:

- what data enters;
- what data leaves;
- what state changes;
- what resources are touched;
- what can fail.

Prefer explicit data flow:

```text
inputs -> computation -> outputs
```

Avoid code that depends heavily on:

- globals;
- service locators;
- thread-local state;
- hidden singleton mutation;
- ambient configuration;
- surprising interior mutation.

State that cannot be seen is state that will eventually be misunderstood.

## File and module structure

Use one stable repository-wide ordering.

For example:

```text
imports
constants
public types
public API
private implementation
platform-specific implementation
test module declaration
```

The exact order is less important than consistency.

Keep related behavior together.

Do not create files whose only organizing principle is "things that did not fit
elsewhere."

## Locality

Code that must be understood together should stay near each other.

Keep close:

- validation and the operation it protects;
- invariants and their enforcement;
- types and their important behavior;
- error translation and the boundary that requires it.

Do not over-split code into tiny helpers scattered across files.

Every jump to another file has a cognitive cost for humans and a
context-retrieval cost for agents.

## Types

Use the type system to prevent invalid interpretation.

Prefer different types for semantically different values when practical:

```text
UserId
TenantId
Bytes
Milliseconds
FilePath
Url
```

Do not rely on comments to distinguish several unrelated `string`, `int`, or
`usize` values when mistakes are realistic.

Make illegal states hard or impossible to represent when the language allows it.

## Error handling

Error flow should be visible.

A reader should quickly determine:

- what may fail;
- whether failure is expected;
- where context is added;
- where recovery happens;
- where failure crosses a subsystem boundary.

Avoid:

- swallowing errors;
- log-and-ignore without reason;
- catch-all handlers;
- converting specific errors into meaningless generic errors;
- duplicating logging at every stack layer.

## Comments

Useful comments explain facts that code cannot express clearly:

```text
// Kernel reports 512-byte sectors, regardless of logical block size.
```

Bad comments narrate syntax:

```text
// Increment count.
count += 1
```

Keep comments next to the code they constrain.

If a comment needs several paragraphs to explain an ordinary function, the
function is probably too difficult to read.

## Tests

Tests are executable documentation for humans and agents.

Tests should make clear:

- setup;
- action;
- expected result;
- important boundary condition.

Use names that state behavior.

Avoid generic test helpers that hide the behavior under test.

A reader should not need to debug the test harness before understanding what the
test proves.

## Formatting

Formatting should be mechanical.

Use:

- canonical formatter;
- canonical import sorting;
- lint rules;
- stable declaration order.

Do not let agents invent formatting.

Do not use manual horizontal alignment that produces noisy diffs.

Prefer layouts that remain stable when one argument, field, or case is added.

## Review priority

When reviewing code, check in this order:

1. Is the behavior correct?
1. Are the invariants preserved?
1. Is the architecture still coherent?
1. Is the control flow obvious?
1. Are names and terminology correct?
1. Are state and side effects explicit?
1. Is the abstraction level consistent?
1. Is the working-memory burden reasonable?
1. Is the diff narrower than it needs to be?
1. Only then: style details.

Do not approve confusing code because it is formatted correctly.

## Final standard

Good code should allow:

- **A1–A2:** follow it;
- **B1–B2:** modify it;
- **C1–C2:** reason about the design.

AI agents should be held to the same standard, with additional constraints
against guessing, terminology drift, abstraction churn, broad diffs, and locally
clever solutions.

The target is not "simple code."

The target is code whose correct interpretation requires as little inference as
possible.
