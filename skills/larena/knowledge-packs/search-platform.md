# Larena Search Platform

Use this knowledge pack when a task touches Larena search, indexing, global search, searchable entities, search adapters, reindex jobs or AI/MCP context search.

## Canonical Position

`larena/search` is a future cross-package search and indexing layer. It must not be treated as a local feature of `larena/storage`, `larena/admin`, `larena/rest`, `larena/mcp`, `larena/filesystem` or `larena/docara-core`.

Source of truth in `simai/larena`:

```text
docs/developer/search/search-package-tz.md
docs/developer/package-graph/packages/larena-search.yaml
```

## Core Rules

- Search owns search contracts, runtime search registry, index schema, indexing/reindex jobs, search execution, result normalization and diagnostics.
- Search does not own business data. Source packages keep data ownership.
- Search must be access-aware before data leaves the service layer.
- Protected list/search/export/context gathering must use `AccessQueryScope`.
- Search must be locale-aware for localized data.
- Search must be bounded by default and safe for REST/MCP.
- Search must not run arbitrary SQL, arbitrary routes or arbitrary package methods.
- Search must not index secrets, raw tokens, passwords, private keys, signed URLs or sensitive audit payloads.
- Search backends are adapters; backend choice must not change security semantics.

## Package Contract Direction

System and product packages should eventually declare searchable entities through a dedicated `search.yaml`.

The contract should describe:

- stable searchable entity type;
- source provider;
- searchable fields;
- filterable/facetable fields;
- localized fields;
- access operation and query scope;
- lifecycle events;
- index policy;
- result shape;
- forbidden fields;
- capability requirements;
- audit event mapping.

## Licensing Direction

Baseline search is Free only when it is bounded and index-backed.

Advanced search belongs to paid capabilities when it introduces:

- advanced external adapters;
- facets and weighted relevance;
- scheduled reindex;
- larger indexes;
- analytics;
- semantic/vector search;
- external clusters.

Trial mode must not make search a bulk-export or data-exfiltration path.
