# AGENTS.md

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

## Tests and evidence

- Derive expected behavior independently from the implementation. Test the
  narrowest affected boundary, including relevant failure and recovery paths.
- Keep tests deterministic, isolated, and explicit about concurrency and
  cleanup. Do not copy actual output into expectations or mock away the defect.
- Report authoritative facts, observed evidence, assumptions, and risks
  distinctly. Report only checks actually run.

Optional delegation is authorized for substantial, independent work under the
shared configuration limits.

Use `just` for new task orchestration and Mermaid for diagrams.

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
