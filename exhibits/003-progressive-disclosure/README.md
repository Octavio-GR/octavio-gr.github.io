# EX-003 — Progressive Disclosure

## Question
How can a system reveal deep technical complexity on demand without cluttering the primary user interface?

## Observation
Modern portfolios often fail by overwhelming visitors with data or hiding essential context behind complex interactive states. Toroide solves this by implementing layered information architecture: primary views state clear boundaries, while detailed documentation, architectural decision records (ADRs), and raw evidence remain accessible via clean, predictable paths.

## Architecture & Implementation
- **Surface Layer**: Concise summaries, high-level status indicators, and clear entry points on the main observatory view.
- **Deep Layer**: Dedicated exhibit directories (`exhibits/XXX`) containing structural evidence and comprehensive Markdown logs.
- **Zero Scripts**: Navigation relies purely on semantic HTML anchor tags and native browser routing, avoiding performance penalties or hydration overhead.

## Verification
Inspect the repository structure to verify that complex logs and secondary proofs are decoupled from the core presentation layer, maintaining a clean visual hierarchy across all viewports.