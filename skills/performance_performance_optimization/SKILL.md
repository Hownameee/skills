---
name: performance_performance_optimization
description: "Diagnose and improve application performance using reproducible profiles and before-and-after benchmarks. Use for latency, throughput, CPU, memory, database, or Core Web Vitals work; do not change required behavior, weaken security, or load-test shared or production systems without explicit authorization."
---

# Performance Optimization

## Scope And Success Criteria

- Define the user-visible or system-visible problem before editing code.
- Record the primary metric, acceptable regression metrics, target or SLO, workload, data size, concurrency, environment, build, hardware, and correctness invariants.
- Keep security, data integrity, accessibility, durability, compatibility, and observability as hard constraints unless the user explicitly accepts a tradeoff.
- Do not run load, stress, soak, or destructive database benchmarks against production or shared infrastructure without explicit approval and bounded parameters.

## Baseline Protocol

1. Reproduce the issue with a representative workload and the same build mode used for comparison.
2. Warm up JITs, caches, pools, and connections when the production path is warm; measure cold-start behavior separately.
3. Run multiple samples, retain raw results, and report median or p50 plus p95/p99 where latency distribution matters.
4. Record throughput, errors, CPU, memory, allocations, I/O, and saturation alongside latency when relevant.
5. Estimate run-to-run variance. Do not claim an improvement smaller than measurement noise.
6. Capture functional output or existing tests so a faster but incorrect result cannot pass.

Use the repository's benchmark and profiling tools first. If already available, a local command benchmark can use:

```bash
hyperfine --warmup 3 --runs 10 '<existing-command>'
```

Do not add a benchmark dependency solely for convenience without approval.

## Locate The Bottleneck

Choose evidence appropriate to the suspected layer:

- **Browser:** field telemetry when available, DevTools performance and network traces, bundle analysis, and lab Core Web Vitals.
- **Backend:** distributed traces, request profiles, CPU flame graphs, allocation and heap profiles, event-loop or thread-pool saturation, and queue depth.
- **Database:** query logs, lock waits, cardinality, I/O, and query plans. Remember that `EXPLAIN ANALYZE` executes the statement; use it only on safe data and workloads.
- **System:** CPU, memory, garbage collection, file descriptors, disk, network, cgroups, and container throttling.

Distinguish time spent waiting from time spent computing. Optimize the measured critical path, not the largest or most visible function.

## Optimization Loop

1. State a falsifiable hypothesis that links a measured bottleneck to a proposed change.
2. Choose the smallest change that tests the hypothesis.
3. Change one material factor at a time where practical.
4. Run correctness checks.
5. Repeat the baseline protocol in the same environment and cache state.
6. Compare absolute and relative deltas, tail latency, resources, errors, and variance.
7. Keep the change only when evidence exceeds noise and tradeoffs are acceptable; otherwise revert only the agent-owned change.

## Layer-Specific Guardrails

### Web

- Prioritize field Core Web Vitals for real users; use lab data for diagnosis, not as a substitute for field evidence.
- Reserve layout space for images, ads, fonts, and late content.
- Reduce render-blocking work and main-thread tasks before applying premature code splitting.
- Track route and interaction bundle impact. Do not defer code required for correctness or accessibility.
- Cache content-addressed static assets immutably; define safe revalidation for mutable content.

### Backend And Database

- Preserve timeouts, cancellation, backpressure, authorization, and transaction semantics.
- Investigate N+1 calls, unbounded scans, serialization, lock contention, pool exhaustion, retries, and fan-out.
- Add indexes only after checking the plan, selectivity, write amplification, disk use, lock behavior, and production migration method.
- Cache only with an explicit key, scope, TTL, invalidation owner, consistency model, stampede control, tenant isolation, and metrics.
- Move work asynchronous only when the API contract, idempotency, ordering, retries, and failure visibility support it.

### Memory And Concurrency

- Stream large payloads and bound batch size, queue size, retries, worker count, and in-flight requests.
- Profile allocations and retention before adding pools or manual reuse.
- Treat higher concurrency as a resource tradeoff; measure downstream saturation and tail latency.
- Verify cleanup on cancellation and failure to avoid leaks.

## Load-Test Safety

Before an authorized load test, write down:

- exact target and environment;
- request type and non-destructive test data;
- maximum QPS, concurrency, duration, and total requests;
- expected resource ceiling and stop thresholds;
- monitoring owner, rollback, and cleanup.

Stop on elevated errors, unexpected writes, shared-tenant impact, resource exhaustion, or a crossed safety threshold.

## Edge Cases

- Separate cold start from steady state, local from network latency, client from server time, and cache hit from miss.
- Account for JIT, garbage collection, turbo boost, background services, telemetry sampling, rate limits, and noisy neighbors.
- Avoid microbenchmarks that remove the actual allocation, I/O, serialization, contention, or framework cost.
- Check that an optimization does not merely shift work to another service, request, tenant, or later phase.

## Completion Report

Include:

- problem, metric, target, workload, environment, and baseline;
- profile evidence and bottleneck;
- change and hypothesis;
- before/after raw summary, absolute and relative delta, variance, and correctness results;
- resource and tail-latency tradeoffs;
- validation not run, residual risk, and rollback.
