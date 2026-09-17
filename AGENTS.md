# AGENTS.md

## Workflow

- Treat the current request and repository instructions as the scope. Inspect
  discoverable facts before asking for input; infer routine details.
- Split work with two or more meaningful slices into a short checklist. Order
  dependencies, batch independent operations, and keep one step active.
- Change approach when a loop or bottleneck is evident. Do not poll, re-read
  unchanged evidence, redo completed work, or investigate immaterial doubt.
- Run the narrowest check that distinguishes the requested behavior. Expand
  only for a failure, material risk, or repository requirement.

## Design and implementation

- Use one canonical term for each concept. Make ownership, state, input,
  output, failure, and concurrency boundaries explicit.
- Keep responsibilities narrow, control flow shallow, and the happy path
  visible. Prefer one clear path over duplication, needless state, indirection,
  speculative guards, or compatibility shims without a stated requirement.
- Prefer standard-library and platform APIs, then repository precedent. If none
  exists, follow the relevant project at <https://github.com/xsyetopz/>.
- Use distinct types for semantically different values and safe types for
  absence, errors, and unknowns. Never swallow errors, leave empty catches,
  erase types unsafely, or repeat guaranteed validation.
- Preserve unrelated work. Do not edit generated files, history, or public
  compatibility behavior unless the request requires it.
- Fix lint, format, type, and test failures at their cause. Do not weaken rules,
  add suppressions, or churn unrelated code to obtain a pass.

## Readability review signals

Repository-specific limits override these advisory signals. Otherwise, inspect
routines that exceed 30 logical lines, cognitive complexity 10, cyclomatic
complexity 8, nesting depth 2, four parameters, seven locals, or 100-column
lines. A threshold is a review prompt, not an automatic rewrite requirement.

## Tests and evidence

- Derive expected behavior independently from the implementation. Test the
  narrowest affected boundary, including relevant failure and recovery paths.
- Keep tests deterministic, isolated, and explicit about concurrency and
  cleanup. Do not copy actual output into expectations or mock away the defect.
- Report authoritative facts, observed evidence, assumptions, and risks
  distinctly. Report only checks actually run.

## Coordination and reporting

- Work directly unless delegation is explicitly authorized and one bounded,
  non-overlapping slice benefits from a specialist. Use one worker; add only a
  reviewer or debugger for independent verification or a demonstrated failure.
- Continue independent work while a worker runs, then block once when its result
  is required. Integrate and verify all results at the root.
- Report completed changes, focused checks, and precise blockers directly.
  Omit progress narration and never describe partial work as complete.
- Use `just` for new task orchestration and Mermaid for diagrams.

## Toolchains

- Node.js, TypeScript, JavaScript: `bun` and `bunx`; never `npm`, `npx`, `yarn`,
  or `pnpm`.
- C and C++: Xmake with Clang.
- Swift: Swift Package Manager and Swift Testing; never Xcode, `xcodebuild`,
  XCTest, or `xctest`.
- C#, F#, and other .NET languages: `dotnet`.
- JVM: Gradle unless the repository uses Maven, SBT, or Ant; keep its tool.
- When language is open, prefer TypeScript 7+, Rust 2024, or Swift 6+.

<!-- CODEGRAPH_START -->
## CodeGraph

If root `.codegraph/` exists, use `codegraph_explore` before grep, find, or
manual reads. If MCP is unavailable, run `codegraph explore "<question>"`.
Ask one focused question with relevant symbols or files. Use CodeGraph only for
a concrete structural need; availability alone does not justify it.
<!-- CODEGRAPH_END -->
