## Subagents

Spawn subagents to isolate context, parallelize independent work, or offload bulk mechanical tasks. Don't spawn when the parent needs the reasoning, when synthesis requires holding things together, or when spawn overhead dominates.

Pick the cheapest model that can do the subtask well:
- Haiku: bulk mechanical work, no judgment
- Sonnet: scoped research, code exploration, in-scope synthesis
- Opus: subtasks needing real planning or tradeoffs

If a subagent realizes it needs a higher tier than itself, return to the parent.

Parent owns final output and cross-spawn synthesis. User instructions override.

## Preferred Tools

### Data Fetching

1. **WebFetch**: free, text-only, works on public pages that don't block bots.
2. **agent-browser CLI**: free, local Rust CLI + Chrome via CDP. For dynamic pages or auth walls that WebFetch can't handle. Returns the accessibility tree with element refs (@e1, @e2). ~82% fewer tokens than screenshot-based tools. Install: `npm i -g agent-browser && agent-browser install`. Use `snapshot` for AI-friendly DOM state, element refs for interaction.
3. **Notice recurring fetch patterns and propose wrapping them as dedicated tools.** When the same fetch/parse logic comes up more than once, suggest wrapping it as a named tool (e.g. a skill file or a .py script that calls `agent-browser` with the snapshot and extraction steps baked in for that source). Add the entry to `## Dedicated Tools` below and reference it by name on future calls.

### PDF Files

Use 'pdftotext', not the 'Read' tool. Use 'Read' only when the user directly asks to analyze images or charts inside the document. Read loads PDFs as images.

## Dedicated Tools

<!-- List project-specific tools here. For each, link to its skill or script file (e.g. `tools/reddit_fetch.py`). The orchestration logic lives in those files, not here. -->



<!-- code-review-graph MCP tools -->
## MCP Tools: code-review-graph

**IMPORTANT: This project has a knowledge graph. ALWAYS use the
code-review-graph MCP tools BEFORE using Grep/Glob/Read to explore
the codebase.** The graph is faster, cheaper (fewer tokens), and gives
you structural context (callers, dependents, test coverage) that file
scanning cannot.

### When to use graph tools FIRST

- **Exploring code**: `semantic_search_nodes` or `query_graph` instead of Grep
- **Understanding impact**: `get_impact_radius` instead of manually tracing imports
- **Code review**: `detect_changes` + `get_review_context` instead of reading entire files
- **Finding relationships**: `query_graph` with callers_of/callees_of/imports_of/tests_for
- **Architecture questions**: `get_architecture_overview` + `list_communities`

Fall back to Grep/Glob/Read **only** when the graph doesn't cover what you need.

### Key Tools

| Tool | Use when |
|------|----------|
| `detect_changes` | Reviewing code changes — gives risk-scored analysis |
| `get_review_context` | Need source snippets for review — token-efficient |
| `get_impact_radius` | Understanding blast radius of a change |
| `get_affected_flows` | Finding which execution paths are impacted |
| `query_graph` | Tracing callers, callees, imports, tests, dependencies |
| `semantic_search_nodes` | Finding functions/classes by name or keyword |
| `get_architecture_overview` | Understanding high-level codebase structure |
| `refactor_tool` | Planning renames, finding dead code |

### Workflow

1. The graph auto-updates on file changes (via hooks).
2. Use `detect_changes` for code review.
3. Use `get_affected_flows` to understand impact.
4. Use `query_graph` pattern="tests_for" to check coverage.
