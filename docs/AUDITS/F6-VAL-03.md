# F6-VAL-03 — HTML/CSS Audit

## Objective

Verify structural integrity, semantic hierarchy, and CSS utilization across all HTML pages and exhibits in Toroide.

## Scope

- Semantic HTML tags (`<main>`, `<header>`, `<section>`, etc.)
- Correct stylesheet linking (`assets/css/index.css` and `../assets/css/index.css`)
- Absence of inline styles or redundant CSS declarations
- Viewport and character encoding meta tag consistency

## Status

COMPLETED / VERIFIED

## Findings

### Structure & Semantics
- [x] All documents use proper DOCTYPE and language attributes (`lang="en"`)
- [x] Semantic tags organize content hierarchy effectively
- [x] Clean separation of structure and presentation

### Stylesheet Management
- [x] Shared stylesheet referenced correctly across root and subdirectories (`docs/`)
- [x] No unnecessary or duplicated CSS stylesheets found
- [x] Layout classes (`exhibit-page`, `exhibit-header`, etc.) applied consistently

## Exit Condition

All HTML files conform to a unified structural baseline and leverage the central CSS system cleanly.
