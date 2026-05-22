# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **Claude Code skills distribution repository**. It contains no application code — only AI-assistant skill definitions sourced from `mattpocock/skills` on GitHub. Skills are invocable workflows (slash commands) that automate engineering tasks like triage, PRD generation, TDD, architecture review, and more.

## Managing skills

Skills are tracked in `skills-lock.json`, which records each skill's source repo, file path within that repo, and a content hash. This file acts like a lock file (similar to `package-lock.json`). Skill definitions live under `.agents/skills/<skill-name>/SKILL.md`.

To add or update skills, use the `write-a-skill` skill or manually update `skills-lock.json` and place the corresponding `SKILL.md` under `.agents/skills/`.

## Available skills

| Skill | Purpose |
|-------|---------|
| `triage` | State machine for filtering and labeling issues |
| `to-issues` | Breaks plans/specs into independent issues |
| `to-prd` | Generates PRDs from conversation context |
| `tdd` | Red-green-refactor testing workflow |
| `improve-codebase-architecture` | Refactoring and architecture analysis |
| `prototype` | Rapid design iteration (UI and logic branches) |
| `grill-with-docs` | Design review against domain model |
| `grill-me` | Adversarial design interview |
| `diagnose` | Debugging and root cause analysis |
| `handoff` | Prepare work for async handoff |
| `write-a-skill` | Scaffold new custom skills |
| `caveman` | Simplified task planning |

## GitHub

Never write on GitHub without an explicity authorization.

## Setup

Before using skills in a target project, run the `setup-matt-pocock-skills` skill to configure the issue tracker and domain documentation (`CONTEXT.md`, `docs/adr/`). Skills like `improve-codebase-architecture` and `grill-with-docs` depend on those files being present.

## Agent skills

### Issue tracker

Issues live in GitHub Issues (`edpittol/aula-do-roveda`). See `docs/agents/issue-tracker.md`.

### Triage labels

Default label vocabulary — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout — `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
