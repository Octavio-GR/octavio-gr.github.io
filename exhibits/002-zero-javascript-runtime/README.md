# EX-002 — Zero JavaScript Runtime

## Question

How can a web interface provide its core content and navigation without requiring client-side JavaScript execution?

## Observation

This exhibit demonstrates that its core content, structure, presentation, and navigation can be delivered using native HTML and CSS without requiring client-side JavaScript.

## Architecture & Implementation

- **Semantic HTML**: The exhibit structure is implemented using native HTML elements and standard document semantics.
- **CSS-Driven Presentation**: Layout, spacing, and typography are handled through the shared stylesheet without DOM manipulation scripts.
- **Native Navigation**: Navigation relies on standard HTML links and browser behavior rather than client-side routing.
- **No Client-Side Runtime**: The exhibit does not load or execute JavaScript for its core content or navigation.

## Verification

Inspect the exhibit source code and search the exhibit directory for script tags, JavaScript references, inline event handlers, and JavaScript URLs. The current implementation contains none of these dependencies, while its core content and navigation remain functional through native HTML and CSS.
