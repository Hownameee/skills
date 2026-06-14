---
name: data_sql_data_modeling
description: SQL and relational data modeling standards for schema design, constraints, indexing, and query review.
---

# Specialist SQL & Data Modeling

## 1. Schema Design

- Model domain invariants with database constraints when the database can enforce them.
- Use primary keys, foreign keys, uniqueness constraints, and check constraints intentionally.
- Avoid nullable columns unless the domain has a real unknown, missing, or not-applicable state.
- Name tables, columns, indexes, and constraints consistently with the existing schema.
- Store timestamps with clear timezone semantics.

## 2. Query Safety

- Use parameterized queries only; never concatenate user input into SQL.
- Select only the columns needed by the caller.
- Bound result sets with pagination or a proven small cardinality.
- Keep transactions short and avoid external network calls inside transactions.
- Use explicit isolation level only when the default is insufficient and the anomaly is documented.

## 3. Indexing

- Add indexes for proven query patterns, constraints, and join paths.
- Check query plans before adding complex or expensive indexes.
- Avoid redundant indexes that duplicate a prefix of an existing useful index unless justified.
- Consider write overhead, storage, and migration cost before indexing low-value columns.
- Use partial or covering indexes when they match a stable high-value query.

## 4. Review Checklist

- Verify cardinality assumptions.
- Verify authorization and tenant filters are part of the query path.
- Verify sort order is deterministic for paginated queries.
- Verify deletes and updates have precise predicates.
- Verify data migrations preserve referential integrity and can be rerun safely.
