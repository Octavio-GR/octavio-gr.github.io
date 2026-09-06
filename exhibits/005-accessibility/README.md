# EX-005 — Accessibility

## Question
How can a zero-JavaScript architecture ensure universal usability, high contrast ratios, and clear semantic hierarchy?

## Observation
Accessibility (a11y) is frequently treated as an afterthought solved by heavy accessibility overlays or client-side scripts. Toroide treats accessibility as an inherent property of semantic HTML structure and strict CSS styling, ensuring absolute compliance with native browser tools and assistive technologies.

## Architecture & Implementation
- **Semantic HTML**: Extensive use of structural elements (`<main>`, `<section>`, `<article>`, `<nav>`, `<blockquote>`) instead of generic structural divs.
- **Visual Contrast**: Dark-mode-first aesthetic tuned for optimal contrast ratios on text and interactive anchor links.
- **Native Focus States**: Predictable keyboard navigation powered entirely by native CSS focus outlines without JavaScript event listeners.

## Verification
Run a native browser accessibility audit (Lighthouse) on any exhibit page to verify high performance, correct heading hierarchy, and zero layout shift without client-side scripts.