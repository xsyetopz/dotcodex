# AGENTS.md

## Workflow

- Split complex work into bounded slices; order dependencies and batch work.
- If work exceeds its expected scope, identify the loop or bottleneck and
  change approach. Do not poll repeatedly, re-read unchanged evidence, or redo
  completed work.
- Run the narrowest check that distinguishes the requested behavior. Expand
  only for a failure, material risk, or repository requirement.

## Implementation

- Keep code simple and responsibilities narrow. Use one clear path; remove
  duplication, needless state, and indirection.
- Prefer standard-library and platform APIs, then repository precedent. If none
  exists, follow the relevant project at <https://github.com/xsyetopz/>.
- Use safe types for absence, errors, and unknowns. Never swallow errors, leave
  empty catches, erase types unsafely, or repeat guaranteed validation.
- Fix lint, format, type, and test failures at their cause. Never weaken rules
  or add suppressions without approval. Use the configured formatter.
- Preserve unrelated work; edit generated files or history only when asked.

## Coordination and reporting

- Delegate only when authorized and a material independent slice benefits from
  a specialist. Otherwise work directly. Use one worker; add a reviewer or
  debugger only for independent verification or a demonstrated failure.
- Report findings, changes, checks, and blockers directly. Omit progress and
  meta-commentary. Report only checks actually run.
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
Ask one focused question with relevant symbols or files. If absent, skip it.
<!-- CODEGRAPH_END -->
