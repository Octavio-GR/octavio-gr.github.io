# EX-002 — Zero JavaScript Runtime

## Question

How can a web interface provide its core content and navigation without requiring client-side JavaScript execution?

## Observation

Many modern web interfaces depend on client-side JavaScript for rendering, navigation, and interaction. Toroide demonstrates that an exhibit can provide its core content, structure, and navigation using native HTML and CSS, without requiring a JavaScript runtime.

## Architecture & Implementation

- **Semantic HTML**: The exhibit structure is implemented using native HTML elements and standard document semantics.
- **CSS-Driven Presentation**: Layout, spacing, typography, and responsive presentation are handled through stylesheets without DOM manipulation scripts.
- **Native Navigation**: Navigation relies on standard HTML links and browser behavior rather than client-side routing.

## Verification

Inspect the exhibit source code and network activity to verify that the page does not load or execute client-side JavaScript while its core content and navigation remain functional.
