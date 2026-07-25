# Technical Debt

Tracks known technical work that is intentionally postponed.

Technical debt is not failure.

Technical debt is a conscious decision to preserve architectural stability.

---

## TD-001

Title:
Octagon visual refinement

Status:
Open

Priority:
Low

Reason:

The octagon currently communicates the intended geometric presence, but its diagonal edges lose contrast at normal viewing distances.

It is functional.

It is not yet visually optimal.

---

## TD-002

Title:
Asset optimization pipeline

Status:
Deferred

Priority:
Medium

Reason:

HTML/CSS minification, SVG optimization and asset compression will be introduced when the build pipeline is implemented.

Current development prioritizes architecture over optimization.

---

## TD-003

Title:
Automated link validation

Status:
Deferred

Priority:
Medium

Reason:

Broken-link detection will be handled through future CI automation.

Manual validation is sufficient during the current phase.

---

## TD-004

Title:
Hero CTA hierarchy

Status:
Open

Priority:
Low

Reason:

Current Hero satisfies structural goals.

Primary and secondary action hierarchy can be refined after content exists.

---

## Principles

Technical debt must be:

- Explicit.
- Documented.
- Intentional.
- Reviewable.

Undocumented debt does not exist.
