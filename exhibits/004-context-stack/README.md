# EX-004 — Context Stack

## Question
How can an engineering project preserve operational state and decision history across long development cycles without depending on volatile memory?

## Observation
Documentation decay happens when decisions are made verbally or kept in ephemeral chat windows. Toroide maintains an explicit context stack where every structural shift, requirement adjustment, and architectural choice is committed directly to version control as verifiable documentation.

## Architecture & Implementation
- **Session Continuity**: Selected development decisions are recorded in structured Markdown files under `docs/` and in exhibit registries; record coverage is not exhaustive.
- **Traceable History**: Git history and documentation can help maintainers reconstruct selected decisions; completeness depends on the available records.
- **State Decoupling**: Operational records are represented as static files where applicable. This reduces reliance on transient runtime state but does not guarantee zero drift.

## Verification
Inspect the repository commit history and the `docs/` tree to assess whether selected architectural changes have supporting records. This inspection does not establish that every change is documented.