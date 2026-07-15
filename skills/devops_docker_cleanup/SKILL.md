---
name: devops_docker_cleanup
description: "Clean up and prune Docker containers, images, volumes, networks, and build cache safely. Use when the user asks to clean up Docker, remove Docker resources, reset Docker, reclaim Docker disk space, run Docker prune operations, or remove everything from a Docker host. Do not use for ordinary Dockerfile or Compose authoring."
---

# Docker Cleanup

## Scope And Modes

Treat cleanup as destructive maintenance. Choose exactly one scope before deleting anything:

- **Project cleanup:** Remove resources belonging to the current Compose project. Use this by default when the request is made inside a repository with a Compose file.
- **Selective host cleanup:** Remove only unused resource types or resources matching an explicit filter.
- **Full host reset:** Remove all containers, images, volumes, non-default networks, and build cache. Use only when the user explicitly requests host-wide removal.

Do not interpret a request to optimize a Dockerfile, rebuild a service, or restart a project as permission to prune resources.

## Inventory First

Before cleanup, inspect the active Docker context and current resources:

```bash
docker context show
docker system df -v
docker compose ls
docker ps -a
docker image ls
docker volume ls
docker network ls
docker buildx ls
```

- Identify running containers, Compose projects, database services, named volumes, external resources, and unrelated workloads.
- If Docker reports a daemon or socket permission error, resolve access first. Do not treat an empty or failed command as proof that no resources exist.
- Record enough before-state information to verify what the cleanup changed.

## Approval Gate

- Require explicit confirmation before deleting named volumes, active database data, unrelated projects, or all resources on a Docker host.
- A precise request such as "remove all Docker resources on this host, including volumes" establishes intended scope, but still inventory before execution.
- If inventory reveals active or persistent resources that were not evident from the request, show them and pause before deletion.
- Do not add force flags merely to avoid an approval prompt. Use them only after the destructive scope is confirmed.
- Prefer exact resource names or IDs for selective cleanup. Do not broaden a project request into host-wide cleanup.

## Project Cleanup

1. Inspect the resolved Compose project:

```bash
docker compose config
docker compose ps -a
docker compose images
docker compose volumes
```

2. For ordinary project cleanup, stop and remove project containers and networks:

```bash
docker compose down --remove-orphans
```

3. Add destructive options only when the request explicitly includes those resources:

```bash
docker compose down --volumes --remove-orphans
docker compose down --rmi all --remove-orphans
docker compose down --volumes --rmi all --remove-orphans
```

- `--volumes` deletes project-declared named volumes and attached anonymous volumes.
- External volumes and networks are not project-owned. Inventory and remove them separately only with explicit approval.
- Use the same Compose files, profiles, environment, and project name that created the resources.

## Selective Host Cleanup

- Prefer resource-specific prune commands so the deletion scope remains visible.
- Use filters such as age or labels when the request is narrower than "all unused resources."
- Review the command's candidate scope before adding `--force`.

Examples after scope confirmation:

```bash
docker container prune --filter "until=24h"
docker image prune --filter "until=24h"
docker network prune --filter "until=24h"
docker volume prune --filter "label!=keep"
docker builder prune --filter "until=24h"
```

## Full Host Reset

After inventory and confirmation, execute in dependency order:

1. Gracefully stop every running container with `docker stop <running-container-ids>`.
2. Remove every container with `docker rm <all-container-ids>`. If graceful removal fails, use `docker rm -f <container-ids>` only within the confirmed full-reset scope.
3. Remove unused named and anonymous volumes:

```bash
docker volume prune -a -f
```

4. Remove networks no longer attached to containers:

```bash
docker network prune -f
```

5. Remove all images not referenced by containers:

```bash
docker image prune -a -f
```

6. Remove build cache:

```bash
docker builder prune -a -f
```

- Removing containers before volumes and networks is mandatory because stopped containers can still reference both.
- Docker's built-in `bridge`, `host`, and `none` networks are expected to remain.
- If multiple Buildx builders exist, inspect them and prune additional builders only when they are included in the confirmed scope.
- Docker cleanup does not delete host directories used as bind mounts. Never delete bind-mounted host data unless the user separately requests it.

## Recovery

- **Resource is in use:** Find the referencing container with inventory commands, then stop and remove only that container within the approved scope.
- **Named volumes remain:** Re-run `docker volume ls`, inspect the remaining volumes, and remove or prune them only after confirming they are unused.
- **Resources reappear:** Check restart policies, Compose projects, system services, and external automation before repeating deletion.
- **Wrong Docker context:** Stop and confirm the intended context. Never continue cleanup against an unexpected local or remote daemon.
- **Cleanup command partially fails:** Re-inventory before retrying. Do not assume earlier steps completed atomically.

## Verification And Report

Run after cleanup:

```bash
docker system df
docker ps -a
docker image ls
docker volume ls
docker network ls
```

Report:

- the selected cleanup mode and Docker context
- resources removed and resources intentionally preserved
- remaining running containers, images, volumes, and non-default networks
- reclaimed disk space when Docker reports it
- failures, skipped resources, or follow-up actions

Do not claim a full reset succeeded unless containers, images, volumes, and build cache are empty and only expected default or explicitly preserved networks remain.
