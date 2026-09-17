# EX-005 — Accessibility

## Question
How can a web interface ensure semantic hierarchy, strong contrast, and keyboard accessibility without relying on client-side scripts or heavy overlays?

## Observation
This exhibit demonstrates accessibility fundamentals through semantic HTML, high-contrast color tokens, and preservation of native browser interaction behavior.

## Architecture & Implementation
- **Semantic Structure**: Layout relies on native document elements (`<main>`, `<article>`) and logical heading hierarchies (`<h1>`, `<h2>`).
- **Contrast**: The primary color tokens `--text: #F5F5F7` and `--bg: #0B0B0C` produce a calculated contrast ratio of approximately **18.07:1**.
- **Focus Behavior**: The stylesheet contains no `:focus`, `:focus-visible`, `outline`, or `box-shadow` rules, leaving focus behavior to the browser's native interaction model.
- **Zero Script Reliance**: No JavaScript is used to manage focus, ARIA state, or dynamic contrast adjustments.

## Verification
Inspect the HTML source for semantic elements and heading hierarchy, verify the `--text` and `--bg` token values and their calculated contrast ratio, and navigate interactive elements with the `Tab` key to observe browser-provided focus behavior.
