# EX-002 — Zero JavaScript Runtime

Status

Implemented

---

## Question

Can a modern engineering portfolio communicate effectively without relying on client-side JavaScript?

---

## Observation

Toroide renders as static HTML.

Navigation, typography, and content remain available without executing client-side code.

The visitor receives the complete document immediately.

---

## Evidence

Observable today:

- Static HTML pages.
- No client-side framework.
- No hydration.
- No SPA routing.
- Inspectable source code.
- Progressive enhancement remains possible.

---

## Current Implementation

Toroide intentionally prioritizes simplicity, inspectability, and long-term durability over runtime complexity.

JavaScript is optional.

Understanding is not.

---

## Related Documents

- FOUNDATIONS
- EVIDENCE
- TECH_DEBT
