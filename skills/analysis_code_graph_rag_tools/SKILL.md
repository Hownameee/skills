---
name: analysis_code_graph_rag_tools
description: "Investigate indexed source repositories with Code-Graph-RAG MCP tools. Use when Codex must locate behavior, query callers or type relationships, retrieve implementations, inspect repository files, diagnose stale index results, or explain code architecture with graph, semantic, and source evidence."
---

# Use Code-Graph-RAG MCP Tools

Investigate code with the narrowest suitable MCP tool, then verify important
claims against source. Treat graph and semantic results as discovery evidence,
not proof of runtime behavior.

## Establish Context

Before calling a repository-scoped tool:

1. Obtain the absolute `repository_path` visible to the MCP server. Docker
   deployments commonly expose repositories under `/workspaces/<repo>`.
2. Determine whether the request is read-only or explicitly authorizes index
   mutation.
3. Check the tools actually exposed by the connected server. `semantic_search`
   is registered only when its optional Qdrant, PyTorch, and Transformers
   dependencies are installed.
4. Keep one `repository_path` throughout a workflow. Never combine a qualified
   name returned for one repository with another repository path.

Use `list_directory` when the server-visible repository path or relative file
layout needs confirmation. Use `list_projects` to check index presence, not
index freshness.

## Select the Tool

| Need | Start with | Follow with |
| --- | --- | --- |
| Discover behavior when symbol names are unknown | `semantic_search` | `get_code_snippet`, then `query_code_graph` for relationships |
| Find callers, callees, imports, definitions, containment, inheritance, implementations, overrides, references, construction sites, or external dependencies | `query_code_graph` | `get_code_snippet` for decisive nodes |
| Read one known indexed function, method, or class | `get_code_snippet` | `read_file` for imports and surrounding context |
| Inspect configuration, manifests, docs, module setup, or neighboring declarations | `read_file` | Continue with a paginated range only when needed |
| Discover valid relative paths | `list_directory` | `read_file` or a graph query |
| Answer a multi-step architectural question spanning several components | `ask_agent` | Verify critical claims with direct tools |
| Check indexed project identifiers | `list_projects` | Diagnose path or missing-index issues |
| Create or fully rebuild an index | `index_repository` | Query only after completion |
| Synchronize changed, added, or deleted files | `update_repository` | Repeat only the stale lookup |
| Remove a project's graph and embeddings | `delete_project` | Confirm the exact project name first |

Prefer direct tools for simple questions. Use `ask_agent` only when the question
inherently requires several discovery, graph, and source-reading steps.

## Apply Tool-Specific Rules

### Discover behavior with `semantic_search`

- Describe concrete behavior, such as "validate a JWT and load the current
  user," instead of using a broad keyword such as "authentication."
- Remember that only source-backed `Function` and `Method` nodes are embedded.
  Files, classes, modules, and relationships are not independent vector entries.
- Treat `score` as similarity ranking, not probability or confidence.
- Copy an exact returned `qualified_name` into `get_code_snippet`; do not guess
  one from a short symbol name.
- Expect fewer than `top_k` results in a multi-repository database because the
  current implementation selects global Qdrant candidates before filtering by
  project.
- If results are empty, clarify the behavioral query or moderately increase
  `top_k`, then fall back to graph and filesystem tools. If the tool is absent,
  continue without semantic search.

### Query relationships with `query_code_graph`

Use graph queries for these indexed relationship families:

- hierarchy: `CONTAINS_PACKAGE`, `CONTAINS_FOLDER`, `CONTAINS_FILE`,
  `CONTAINS_MODULE`;
- ownership: `DEFINES`, `DEFINES_METHOD`;
- modules: `IMPORTS`, `EXPORTS`, `EXPORTS_MODULE`, `IMPLEMENTS_MODULE`;
- types: `INHERITS`, `IMPLEMENTS`, `OVERRIDES`;
- behavior: `CALLS`, `REFERENCES`, `INSTANTIATES`;
- dependencies: `DEPENDS_ON_EXTERNAL`.

Phrase a query with the target entity, relationship direction, requested
fields, result limit, and bounded traversal depth when relevant. For example:

> Find functions and methods with incoming `CALLS` relationships to
> `UserService.create_user` within two call levels. Return each caller's exact
> qualified name and path. Limit 30.

After every important query:

1. Read `summary` for an error, timeout, or truncation.
2. Inspect `query_used` for the intended project scope, labels, relationship
   direction, depth bound, and limit.
3. Retry with explicit relationship terminology if the generated Cypher chose
   the wrong interpretation.
4. Retrieve decisive implementations with `get_code_snippet`.

Never request an unbounded transitive path. Never interpret an empty generated
query result as definitive before checking `query_used` and index freshness.

### Retrieve source with `get_code_snippet`

- Supply an exact indexed `qualified_name` returned by another tool.
- Use the result for a focused implementation; use `read_file` for imports,
  decorators outside the indexed span, neighboring declarations, or module
  initialization.
- If `found` is false, disambiguate the entity with `query_code_graph` or read
  the known file directly.
- If the snippet is shifted or unrelated, assume that live source and indexed
  line metadata may differ. Request authorization for `update_repository`
  before mutating the index.

### Inspect files with `list_directory` and `read_file`

- Pass paths relative to `repository_path`.
- Discover uncertain paths instead of inferring them from host conventions.
- Read the smallest useful range, commonly 80-150 lines, then paginate from the
  next offset only when the current evidence requires more context.
- Prefer filesystem tools for configuration, manifests, documentation, SQL,
  templates, and code that is not represented as a graph entity.

### Synthesize flows with `ask_agent`

- Ask one scoped architectural question at a time and state its boundary, such
  as "trace the HTTP entrypoint through middleware to the database call."
- Treat the response as synthesized analysis rather than independent proof.
- Verify high-impact symbols and transitions with `query_code_graph`,
  `get_code_snippet`, or focused `read_file` calls.
- Do not use the internal safe-shell helper as permission to execute arbitrary
  commands or exceed the user's requested scope.

## Follow Standard Workflows

### Discover unknown behavior

1. Search for a concrete behavior with `semantic_search` when available.
2. Retrieve the strongest matching implementations with `get_code_snippet`.
3. Query callers, dependencies, ownership, or construction sites with
   `query_code_graph`.
4. Read surrounding files only when imports or configuration affect the
   interpretation.
5. Report exact qualified names, paths, direct evidence, and uncertainty.

### Trace a call or type relationship

1. Resolve a short symbol name with `query_code_graph`.
2. Query the required direction using a bounded depth and result limit.
3. Inspect `query_used`, `summary`, and truncation.
4. Retrieve source for the target and important neighboring nodes.
5. Separate graph-proven edges from inferred runtime behavior.

### Explain an end-to-end flow

1. Use `ask_agent` for a genuinely multi-component flow; otherwise begin with
   `query_code_graph`.
2. Identify the entrypoint and major transitions.
3. Verify key transitions with focused relationship queries.
4. Retrieve source for decisive steps.
5. Present the flow in execution order and identify static-analysis gaps.

### Recover from empty or stale results

1. Confirm `repository_path` with `list_directory`.
2. Check whether its derived project exists with `list_projects`.
3. Inspect `query_used` for graph queries and retry with explicit symbols and
   relationships when translation was weak.
4. Check semantic-tool availability and retry a clearer query when applicable.
5. Compare indexed locations with live content using `read_file`.
6. If the project is missing, ask for authorization before `index_repository`.
7. If source changed after indexing, ask for authorization before
   `update_repository`.
8. After indexing finishes, repeat only the original failed lookup.

## Enforce Mutation and Concurrency Safety

- Never call `index_repository`, `update_repository`, or `delete_project` for a
  read-only request without explicit user authorization.
- Treat `index_repository` as destructive for the selected project's existing
  graph and embeddings; same-project reads may be empty or partial until the
  rebuild completes.
- Treat `update_repository` as a state-changing synchronization, not a routine
  prerequisite for every query.
- Confirm the exact derived project name before `delete_project`. Never delete a
  project merely to repair an empty result.
- Account for the server-wide mutation lock: index, update, and delete calls are
  serialized. Read-only requests can continue but may observe transitional
  same-project state or brief database contention.

## Report Evidence and Limits

For a behavioral conclusion, seek three evidence layers when applicable:

1. discovery evidence from semantic search or symbol lookup;
2. structural evidence from graph relationships;
3. source evidence from a snippet or focused file range.

Name the repository path, qualified symbols, and relative file paths used.
Distinguish direct tool evidence from inference. State that graph relationships
come from static analysis rather than runtime traces when reflection, dynamic
imports, dependency injection, generated code, monkey patching, or unresolved
external symbols could change the result.

Before finalizing, confirm that:

- all repository-scoped calls used the same intended `repository_path`;
- qualified names came from tool output rather than guessing;
- important graph queries had sensible direction, depth, scope, and limits;
- behavioral claims were checked against source;
- empty results were diagnosed rather than treated as proof;
- no index mutation occurred without authorization.

If present in the repository, read `docs/mcp-tools-agent-skill.md` for the
canonical selection guide and `docs/mcp-tools-reference.md` for complete
schemas, arguments, response behavior, and JSON-RPC examples. If those docs are
absent, rely on this skill and the connected MCP server's live tool schemas.
