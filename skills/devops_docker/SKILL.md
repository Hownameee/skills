---
name: devops_docker
description: "Design, review, and troubleshoot Dockerfiles, image builds, Docker Compose configuration, and container runtime security. Use for container build, Compose, health-check, image-size, caching, and runtime configuration tasks. Do not use for pruning or deleting Docker resources; use devops_docker_cleanup instead."
---

# Docker Build And Runtime

## Scope

- Use this skill for Dockerfile, image build, Docker Compose, and container runtime work.
- Use `devops_docker_cleanup` when the task is to prune, reset, remove, or reclaim disk space from Docker resources.
- If a task includes both configuration changes and cleanup, finish and verify the configuration work before applying the cleanup workflow.

## Inspect The Project

1. Read repository instructions and identify the intended development and production environments.
2. Inspect the Dockerfile, Compose files, `.dockerignore`, entrypoint scripts, and application runtime requirements.
3. Confirm the expected build context, target architecture, exposed ports, persistent data, and required services.
4. Match existing repository commands and naming unless they are unsafe or obsolete.

## Dockerfile Rules

- Use multi-stage builds when build tools or intermediate artifacts do not belong in the runtime image.
- Prefer maintained official base images. Choose `slim`, Alpine, or a fuller distribution based on runtime compatibility rather than image size alone.
- Pin image versions to the reproducibility level required by the project. Avoid mutable tags for production deployments.
- Run build steps with only the privileges they require, and switch to a non-root runtime user when the application supports it.
- Copy dependency manifests before application source when this produces a useful cache boundary.
- Keep `RUN` steps deterministic and remove package-manager caches created in the same layer.
- Never pass secrets through `ARG`, `ENV`, copied files, or image history. Use supported build-secret mechanisms.
- Keep `ENTRYPOINT` and `CMD` behavior explicit and ensure signals reach the application process.

## Build Context

- Maintain a `.dockerignore` that excludes at least repository metadata, dependency directories, build output, local logs, caches, and secret files not required by the build.
- Do not copy `.env`, credentials, private keys, or unrelated workspace files into an image.
- Keep the build context as narrow as the project layout allows.

## Docker Compose Rules

- Use the Compose v2 command form: `docker compose`.
- Do not hardcode secrets in Compose files. Use the repository's supported secret or environment-injection mechanism.
- Publish only ports that must be reachable from the host or external systems.
- Use named volumes for data that must persist, and clearly mark resources managed outside the Compose project as external.
- Add health checks when they test meaningful readiness or liveness behavior. Do not add checks that depend on tools absent from the image or that only prove the process exists.
- Use service dependencies for startup ordering only when the application cannot tolerate dependency startup delays; applications should still handle transient connection failures.
- Use `docker compose run --rm` or `docker run --rm` for disposable one-off containers.

## Verification

Run the narrowest commands supported by the repository:

```bash
docker compose config
docker build <build-options> <context>
docker compose build <service>
docker compose up -d --wait <service>
docker compose ps
docker compose logs <service>
```

- Substitute repository-specific files, profiles, targets, and service names.
- Do not start, stop, or replace unrelated running services merely to validate a configuration file.
- Report commands that could not run because the Docker daemon, credentials, network, or platform was unavailable.

## Safety Boundaries

- Do not run `docker system prune`, `docker image prune`, `docker volume prune`, or host-wide removal commands under this skill.
- Do not expose the Docker socket to containers without a documented requirement and explicit security review.
- Do not delete persistent data or external resources as a side effect of build or Compose work.
