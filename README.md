# CI Pipeline Templates

[![Validate](https://github.com/mustafaautomation/ci-pipeline-templates/actions/workflows/validate.yml/badge.svg)](https://github.com/mustafaautomation/ci-pipeline-templates/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Templates-2088FF.svg?logo=github-actions&logoColor=white)](https://docs.github.com/en/actions)

Production-ready GitHub Actions workflow templates for every stack. Copy, paste, ship. Each template includes lint, test, build, and artifact upload with battle-tested action versions.

---

## Templates

| Template | Stack | File |
|----------|-------|------|
| **Node.js** | npm + TypeScript + Vitest/Jest | [`workflows/node/ci.yml`](workflows/node/ci.yml) |
| **Python** | pip + pytest + ruff + mypy | [`workflows/python/ci.yml`](workflows/python/ci.yml) |
| **Java** | Maven + JUnit 5 + Allure | [`workflows/java/ci.yml`](workflows/java/ci.yml) |
| **.NET** | dotnet 8 + NUnit/xUnit | [`workflows/dotnet/ci.yml`](workflows/dotnet/ci.yml) |
| **Rust** | cargo + fmt + clippy | [`workflows/rust/ci.yml`](workflows/rust/ci.yml) |
| **Playwright** | Multi-browser E2E with traces | [`workflows/playwright/e2e.yml`](workflows/playwright/e2e.yml) |
| **Docker** | Build + push to GHCR | [`workflows/docker/build-push.yml`](workflows/docker/build-push.yml) |

---

## Usage

```bash
# Copy the template you need
cp ci-pipeline-templates/workflows/node/ci.yml .github/workflows/ci.yml

# Or curl directly from GitHub
curl -o .github/workflows/ci.yml \
  https://raw.githubusercontent.com/mustafaautomation/ci-pipeline-templates/main/workflows/node/ci.yml
```

---

## What's Included in Each Template

### Node.js
- `.nvmrc` based Node version
- `npm ci` with cache
- Lint → Format → Typecheck → Test → Build
- Artifact upload for coverage/reports

### Python
- Matrix: Python 3.11 + 3.12
- pip cache
- ruff lint → mypy typecheck → pytest with JUnit XML + coverage
- Per-version artifact upload

### Java
- Split: Build job (always green) → Test job
- Maven cache
- JUnit 5 with Surefire reports

### .NET
- Split: Build → Test
- dotnet restore cache
- TRX test results upload

### Rust
- Stable toolchain
- Cargo cache (registry + git + target)
- fmt → clippy → build → test

### Playwright
- Split: Build & Lint → E2E (per browser)
- Matrix: chromium + firefox
- HTML reports + traces on failure

### Docker
- Multi-platform with Buildx
- GitHub Container Registry
- Layer caching with GHA cache
- Auto-tag: branch, semver, SHA

---

## All Templates Use

- `actions/checkout@v4`
- `actions/setup-node@v4` / `setup-python@v5` / `setup-java@v4` / `setup-dotnet@v4`
- `actions/upload-artifact@v4`
- `actions/cache@v4`

No `@v6` or `@v7` — those don't exist.

---

## Project Structure

```
ci-pipeline-templates/
├── workflows/
│   ├── node/ci.yml
│   ├── python/ci.yml
│   ├── java/ci.yml
│   ├── dotnet/ci.yml
│   ├── rust/ci.yml
│   ├── playwright/e2e.yml
│   └── docker/build-push.yml
├── .github/workflows/validate.yml    # Validates all YAML templates
└── README.md
```

---

## License

MIT

---

Built by [Quvantic](https://quvantic.com)
