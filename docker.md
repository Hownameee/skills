---
description: Best practices for Dockerfiles and Docker Compose to ensure security and efficiency.
---

# Docker Best Practices

## 1. Multi-Stage Builds

- **ALWAYS** use multi-stage builds to keep final production images as slim as possible.
- Compile/Build in the first stage, copy only the compiled binaries/assets to the final stage.

## 2. Base Images

- Prefer `alpine` or `slim` base images (e.g., `node:20-alpine`, `python:3.11-slim`) unless specific C-bindings require standard images.
- Pin versions strictly (e.g., `ubuntu:22.04`, not `ubuntu:latest`).

## 3. Security (Least Privilege)

- **NEVER** run containers as `root` in production.
- Always create a dedicated user and switch to it before the `CMD` or `ENTRYPOINT` (e.g., `RUN adduser -D myuser && USER myuser`).

## 4. Layer Caching

- Order commands from least likely to change to most likely to change.
- Copy dependency files (e.g., `package.json`, `requirements.txt`) and install dependencies *before* copying the rest of the source code.

## 5. Context and Ignore Files

- Ensure a `.dockerignore` file exists to prevent copying `.git`, `node_modules`, local secrets, and unnecessary logs into the image context.

## 6. Docker Compose

- Use `docker-compose` for local development.
- Do not hardcode secrets in `docker-compose.yml`; use `.env` files or Docker secrets.
- **NEVER use the `latest` tag** for services (e.g., use `postgres:15-alpine` instead of `postgres:latest`) to prevent unexpected breaking changes.

## 7. Resource Management & Cleanup

- **ALWAYS clean up unused resources.** If you run a one-off container or an ephemeral image that is meant to run and exit, make sure to clean it up.
- Use the `--rm` flag when running temporary containers (e.g., `docker run --rm <image>`) so they are automatically removed when they exit.
- Run `docker image prune -f` or `docker system prune -f` periodically or after testing temporary images to clear out dangling unused images and save disk space.

## 8. Health and Monitoring

- **Add HEALTHCHECK:** Always include a `HEALTHCHECK` instruction in your Dockerfile or `docker-compose.yml` to verify that the application is actually ready to receive traffic, not just that the container process has started.
