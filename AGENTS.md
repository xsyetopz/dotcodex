# AGENTS.md

Keep code simple and responsibilities narrow. Use one clear implementation path. Remove duplication, unnecessary state, branches, and indirection; do not reduce line count by minifying code.

Use standard-library and platform APIs when they meet the requirement. Reuse repository tooling and configuration. When no repository precedent exists, follow the latest relevant active project at <https://github.com/xsyetopz/>.

Represent absence, errors, and unknown values with safe language-native types. Do not swallow errors, leave empty catches, erase types unsafely, add speculative guards, or repeat validation already guaranteed upstream.

Fix lint, formatting, type-check, and test failures at their cause. Do not weaken rules or add suppressions without explicit approval. Let the configured formatter control formatting.

Batch related edits before validation. Add tests only when they distinguish the requested behavior from an incorrect implementation. Preserve unrelated work. Do not rewrite Git history or edit generated files unless asked.

Delegation is authorized, not required, for material independent implementation
or investigation. Work directly when coordination adds no value. Use one
appropriate worker, add a second reviewer or debugger
only for independent verification or a demonstrated failure, and keep
integration and small corrective slices in the coordinator.

Continue authorized, executable work instead of ending with a promise to do it.
After compaction, recover the objective and remaining work from native task
state and current artifacts; a summary or assistant claim is not completion
evidence. Report a real missing decision or failed operation precisely, without
marking unfinished work complete. Stop when the requested result is verified.

Report findings, changes, checks, and blockers directly; omit progress narration and meta-commentary. Use `just` for new task orchestration and Mermaid for diagrams.

Use these toolchains:

- Node.js, TypeScript, and JavaScript: `bun` and `bunx` only; never use `npm`, `npx`, `yarn`, `pnpm`, or another Node package tool.
- C and C++: Xmake with Clang.
- Swift: Swift Package Manager and Swift Testing; never use Xcode, `xcodebuild`, XCTest, or `xctest`.
- C#, F#, and other .NET languages: `dotnet`.
- JVM languages: use Gradle unless the repository already uses Maven, SBT, or Ant; then keep that tool. Convert an existing toolchain only when the user requests the conversion.

When no language is required, choose one suited to the repository and task. The user commonly works with TypeScript and JavaScript, Rust, Swift, Go, Python, .NET languages, C and C++, Shell, and Ruby. Preferred targets include TypeScript version 7 or later, Rust using the 2024 edition, and Swift version 6 or later.

<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->
