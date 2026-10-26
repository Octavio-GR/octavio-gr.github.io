# F6-VAL-01 — System Audit

## Objective

Validate Toroide as an observable system after Phase 5 Materialization, using the repository validation suite and recorded evidence.

## Status

COMPLETED WITH LIMITATIONS

## Scope

- Internal navigation and relative paths.
- Exhibits EX-001 through EX-005.
- Documentation and materialization consistency.
- Shared CSS checks and repeated-declaration warnings.
- HTML structure and text encoding.
- Runtime and accessibility limitations.

## Evidence

### E-01 — Internal links

**Result: PASS.**

The execution of `scripts/validate.ps1` reported:

`PASS: no broken local links found.`

This establishes the result of the repository's local-link checker at the time of execution.

### E-02 — Referenced assets

**Result: PASS.**

The validation suite reported:

`PASS: referenced assets appear to exist.`

### E-03 — HTML structure

**Result: PASS.**

The validation suite reported:

`PASS: HTML structural checks passed.`

This is the result of the existing structural checker, not a claim of complete HTML conformance across all browsers.

### E-04 — CSS checks

**Result: PASS WITH WARNINGS.**

The CSS checker reported:

`PASS: CSS checks passed.`

The duplicate-declaration scanner reported repeated CSS declarations across shared stylesheets. Its own output explicitly states that these are warnings, not automatic failures. Repetition alone does not establish a cascade defect or justify a refactor.

### E-05 — Text encoding

**Result: PASS.**

The encoding checker reported:

`PASS: text files are valid UTF-8.`

It also identified UTF-8 BOMs in multiple tracked files. These were informational findings; the checker did not classify them as failures.

### E-06 — Validation suite completion

**Result: PASS.**

`scripts/validate.ps1` completed without a terminating PowerShell exception and printed `VALIDATION COMPLETE`.

### E-07 — Runtime and accessibility

**Result: NOT VERIFIED BY THIS RUN.**

The validation suite does not establish the absence of browser-console errors, full responsive rendering consistency, keyboard interaction behavior, production security headers, or complete WCAG 2.1 AA conformance.

These items remain outside the evidence established by this execution.

## Findings

### F6-VAL-01-F01 — Internal navigation and referenced assets

**Severity:** Low
**Status:** Passed by the existing validation suite.

No broken local links were reported, and referenced assets passed the existing asset check.

### F6-VAL-01-F02 — Repeated CSS declarations

**Severity:** Informational
**Status:** Warnings remain.

The duplicate scanner identifies repeated declarations. The scanner itself treats these as warnings. No functional defect is established by repetition alone, and no broad CSS refactor is authorized by this finding.

### F6-VAL-01-F03 — UTF-8 BOM presence

**Severity:** Informational
**Status:** Recorded; no encoding failure reported.

The checker listed files containing UTF-8 BOMs while also reporting that text files are valid UTF-8. This audit does not require a repository-wide encoding rewrite.

### F6-VAL-01-F04 — Browser runtime and accessibility

**Severity:** Undetermined
**Status:** Unverified.

The static validation results do not substitute for browser-based runtime testing or a complete accessibility conformance assessment.

## Conclusion

F6-VAL-01 is closed as **COMPLETED WITH LIMITATIONS**.

The existing validation suite passed its link, asset, HTML structure, CSS, and UTF-8 checks. Repeated CSS declarations remain warnings rather than confirmed defects.

This closure is limited to the checks explicitly recorded above. It does not claim browser runtime verification, visual regression testing, or full WCAG 2.1 AA conformance.

## References

- `scripts/validate.ps1`
- `scripts/check-links.ps1`
- `scripts/check-assets.ps1`
- `scripts/check-html.ps1`
- `scripts/check-css.ps1`
- `scripts/check-encoding.ps1`
- `scripts/check-duplicates.ps1`
- `docs/AUDITS/F6-VAL-02.md`
- `docs/AUDITS/F6-VAL-03.md`
- `docs/AUDITS/F6-VAL-04.md`
- `docs/AUDITS/F6-VAL-05.md`
- `docs/AUDITS/F6-VAL-06.md`
- `docs/AUDITS/F6-VAL-07.md`
- `docs/AUDITS/F6-VAL-08.md`

## Change Control

This record documents the results supplied by the validation suite. It does not authorize unrelated source changes, broad CSS refactoring, or changes to the remaining local patch files.