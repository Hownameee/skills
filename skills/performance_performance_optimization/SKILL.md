---
name: performance_performance_optimization
description: Performance optimization rules for profiling, Core Web Vitals, latency, memory, and throughput.
---

# Specialist Performance Optimization

## 1. Measurement First

- Define the user-visible performance target before optimizing.
- Measure baseline behavior with representative data and environment.
- Use profilers, traces, query plans, browser performance tools, or production telemetry before guessing.
- Optimize the bottleneck, not the most visible code.
- Keep before/after evidence in the final answer or PR notes.

## 2. Web Performance

- Prioritize Core Web Vitals for user-facing web pages: loading, responsiveness, and visual stability.
- Avoid layout shifts from images, ads, injected content, fonts, and late-loading UI.
- Reduce render-blocking JavaScript and CSS.
- Split client bundles by route and interaction when the framework supports it.
- Cache static assets with immutable content hashes.

## 3. Backend Performance

- Bound slow operations with timeouts and cancellation.
- Avoid N+1 queries, unbounded scans, and excessive serialization.
- Use caching only when invalidation, consistency, and observability are clear.
- Prefer queueing or asynchronous processing for slow work that does not need to block the request.
- Track p50, p95, and p99 latency separately.

## 4. Memory And Resource Use

- Stream large files and payloads instead of loading them fully into memory.
- Bound batch sizes, concurrency, retries, and queue consumers.
- Watch allocation hot paths before adding object pools or complex caching.
- Treat performance changes that reduce correctness, security, or maintainability as suspect unless explicitly approved.
