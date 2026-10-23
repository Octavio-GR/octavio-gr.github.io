# F7-QDEE-01 — Technical Audit Report

## Status

COMPLETED WITH LIMITATIONS

## 1. Purpose

Document the evidence reviewed for the Toroide project, distinguish verified
observations from unverified risks, and align the public documentation with
the claims supported by the available evidence.

Repository: `Octavio-GR/octavio-gr.github.io`
Primary branch: `main`
Audit identifier: `F7-QDEE-01`

## 2. Executive Summary

The repository includes static HTML and CSS exhibits, project validation
scripts, evidence documentation, and an exhibit registry. The available
validation run completed successfully for local links, referenced assets,
HTML structural checks, CSS checks, and UTF-8 validity.

The duplicate-declaration scan reports repeated CSS declarations. Its own
output explicitly treats these as warnings, not automatic failures. A repeated
property is not, by itself, proof of a defect: selector scope, cascade order,
media queries, and intended overrides must be considered.

EX-002 previously used language broad enough to imply that no JavaScript was
delivered or needed anywhere in the exhibit. That wording exceeded the
evidence available. The claim has been narrowed to the core layout, content,
and navigation not requiring first-party JavaScript. This does not exclude
third-party scripts.

The audit did not establish a confirmed exploitable vulnerability. It also did
not perform a complete production-header assessment, a full WCAG 2.1 AA audit,
or a comprehensive runtime/network audit of every page. Those areas remain
outside the verified conclusions of this report.

## 3. Scope and Method

The review considered repository documentation, exhibit source, existing
project validation scripts, recorded browser-network observations, and Git
history supplied during the investigation.

The project validation suite was run locally using PowerShell with a
process-scoped execution-policy bypass. No machine-wide or persistent
execution-policy change was made.

This report distinguishes:
- **Observed:** directly supported by inspected source or command output.
- **Partially verified:** evidence supports a limited claim but not its
  broader interpretation.
- **Unverified:** the necessary test or production evidence was not available.
- **Not established:** the evidence does not justify asserting the suspected
  condition as a fact.

This is a repository-level audit with explicit limitations, not a certification
of production security or accessibility.

## 4. Findings

### F7-DOC-01 — Evidence and claim status needed clearer separation

**Severity:** Low
**Priority:** Medium
**Status:** Remediated in the documentation changes associated with this report.

The evidence registry, exhibit registry, and proof matrix describe different
things: implementation state, recorded evidence, and the verification status
of individual claims. Treating these as interchangeable can imply that every
claim on an exhibit has been verified merely because the exhibit is listed as
verified.

The documentation changes clarify that implementation status does not
automatically verify every quantitative or runtime claim. Claim-level evidence
is tracked separately in `docs/PROOF.md`.

**Residual limitation:** the registry should continue to be reviewed whenever
the scope of an exhibit's claims changes.

### F7-EX002-01 — Zero-JavaScript wording exceeded the demonstrated scope

**Severity:** Low
**Priority:** Medium
**Status:** Remediated by narrowing the exhibit's wording.

Earlier EX-002 copy included absolute statements about zero JavaScript bytes,
network payload reduction, and zero hydration overhead. Those statements
require measurements and a clearly defined scope. Static source inspection
alone cannot establish every runtime or network-level consequence.

The exhibit now limits its central claim to the fact that its core content,
layout, and navigation do not require first-party JavaScript.

**Conclusion:** the narrower architectural claim is appropriate. Do not
interpret it as proof that the browser downloads no JavaScript from any source.

### F7-EX002-02 — Third-party JavaScript is outside the core-layout claim

**Severity:** Informational
**Priority:** Medium
**Status:** Partially verified; claim scope clarified.

A browser Network-panel observation supplied during the investigation showed
a request to `static.cloudflareinsights.com`, with script type and HTTP status
200, initiated by the EX-002 page. This observation establishes that a
third-party script request occurred in that observed session. It does not,
by itself, establish that the script is malicious, exploitable, or required
for the exhibit's core layout.

The distinction between first-party requirements and third-party network
activity is therefore material.

**Recommendation:** preserve the scoped wording and avoid claiming a
zero-JavaScript network payload unless a reproducible runtime measurement
supports that exact statement.

### F7-EX002-03 — Static-source checks do not prove zero runtime requests

**Severity:** Informational
**Priority:** Low
**Status:** Partially verified.

Source inspection can identify script elements, inline handlers, and
JavaScript pseudo-protocols in the inspected document. It cannot independently
prove the absence of scripts injected by hosting infrastructure, analytics,
browser extensions, or other runtime mechanisms.

Historical repository documentation records static-source checks for EX-002.
Those checks must not be interpreted as a complete network capture.

**Recommendation:** describe static-source inspection and browser-network
observation as separate evidence types.

### F7-SEC-01 — Production security headers

**Severity:** Undetermined
**Priority:** Medium
**Status:** Unverified; no vulnerability established.

Repository searches during the investigation did not find tracked declarations
for headers such as Content-Security-Policy or X-Frame-Options. A source
search cannot prove that production responses lack these headers: hosting
configuration, CDN rules, or other infrastructure may add them.

No authoritative production response-header capture was available as part of
this audit. Consequently, neither absence of these headers in production nor
a resulting exploitable vulnerability is asserted.

**Follow-up:** inspect actual deployed response headers for representative
HTML responses and document the capture date and URLs tested.

### F7-A11Y-01 — WCAG 2.1 AA conformance

**Severity:** Undetermined
**Priority:** Medium
**Status:** Unverified as a complete conformance claim.

The repository includes accessibility-oriented markup and styling, and the
local HTML structural checks passed. These facts are not equivalent to a
complete WCAG 2.1 AA assessment.

This audit did not establish complete keyboard, focus, screen-reader,
contrast, zoom/reflow, error-identification, and assistive-technology
conformance across all relevant pages and states.

**Follow-up:** perform a documented page-by-page assessment combining
automated checks with keyboard and assistive-technology testing.

### F7-CSS-01 — Repeated CSS declarations

**Severity:** Informational
**Priority:** Low
**Status:** Warnings observed; functional impact undetermined.

The project's duplicate scan reports repeated declarations across several
stylesheets, including `components.css`, `experience.css`, `hero.css`,
`navigation.css`, `octagon.css`, and `sections.css`.

The validation script states that repeated declarations are warnings rather
than automatic failures. Repetition can be intentional because of component
boundaries, responsive overrides, or the CSS cascade.

**Conclusion:** the scan completed; it did not prove that each reported
declaration is redundant or defective. No broad CSS cleanup is authorized by
this finding alone.

### F7-ENC-01 — UTF-8 BOM inventory

**Severity:** Low
**Priority:** Low
**Status:** Warning reported; impact undetermined.

The encoding checker listed files containing UTF-8 BOM markers while also
reporting that text files are valid UTF-8. These results are not contradictory:
a BOM is an encoding marker, not automatically invalid UTF-8.

The audit does not establish that the listed markers cause a runtime defect.
Any normalization should be performed as a separate, targeted change with
diff review.

## 5. Validation Evidence

The following results were observed in the local execution of
`scripts/validate.ps1`:

| Check | Observed result | Interpretation |
|---|---|---|
| Local links | PASS | No broken local links reported by the script |
| Referenced assets | PASS | Referenced assets appeared to exist |
| HTML structure | PASS | Project structural checks passed |
| CSS checks | PASS | Project CSS checks passed |
| Encoding | PASS | Text files were reported as valid UTF-8 |
| Duplicate scan | PASS with warnings | Repeated declarations were reported; scan completed |
| `git diff --check` | PASS for the audit after whitespace correction | No trailing-whitespace errors reported for the audited diff |

These results describe the scripts' checks, not a proof of all possible runtime
states, browser behavior, production configuration, or standards conformance.

## 6. Architecture and Security Observations

1. Keep claims proportional to their evidence and explicitly define their scope.
2. Distinguish first-party code requirements from third-party requests.
3. Keep static-source evidence separate from runtime/network evidence.
4. Do not classify repeated CSS declarations as defects without examining
   selectors, cascade behavior, and responsive contexts.
5. Do not infer production header configuration from repository searches alone.
6. Do not describe an accessibility-oriented implementation as fully WCAG
   conformant without a documented conformance assessment.
7. Keep unrelated CSS, backup, and patch files out of this documentation commit.

## 7. Rejected Conclusions

The evidence reviewed does not justify asserting any of the following:

- A confirmed exploitable security vulnerability exists.
- Production security headers are definitely absent.
- EX-002 produces no JavaScript network traffic from any source.
- Every reported repeated CSS declaration is a defect.
- The entire site has been certified WCAG 2.1 AA conformant.
- A UTF-8 BOM warning necessarily represents a runtime failure.

These are not findings of absence; they are conclusions not established by the
available evidence.

## 8. Evidence References

- `docs/EVIDENCE.md` — evidence documentation and claim-scope notes.
- `docs/PROOF.md` — proof matrix and verification limitations.
- `docs/EXHIBITS.md` — exhibit registry and implementation status.
- `exhibits/002-zero-javascript-runtime/index.html` — EX-002 claim wording.
- `toroide/AUDITS.md` — historical audit notes.
- `scripts/validate.ps1` — local validation orchestrator.
- `scripts/check-links.ps1` — local-link checks.
- `scripts/check-assets.ps1` — referenced-asset checks.
- `scripts/check-html.ps1` — HTML structural checks.
- `scripts/check-css.ps1` — CSS checks.
- `scripts/check-encoding.ps1` — text encoding checks.
- `scripts/check-duplicates.ps1` — repeated-declaration scan.

## 9. Recommended Follow-up

1. Capture and archive deployed response headers for representative pages.
2. Conduct a documented WCAG 2.1 AA assessment.
3. If a zero-JavaScript network claim is needed, collect reproducible browser
   network evidence and define whether third-party scripts are in scope.
4. Review duplicate CSS warnings individually before attempting deduplication.
5. Consider encoding normalization only as a separate, scoped change.

These follow-ups are not represented as completed by this report.

## 10. Completion Statement

The documentation alignment and repository validation steps are complete
within the stated scope. The report records the observed results, narrows
unsupported EX-002 claims, and identifies remaining unverified areas without
presenting them as confirmed vulnerabilities or conformance failures.

**Final status: COMPLETED WITH LIMITATIONS.**
