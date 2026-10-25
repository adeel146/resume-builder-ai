---
mode: agent
description: Review a targeted resume against its job description as an ATS and senior technical recruiter.
---

Review the targeted resume against the job description.

Act as an ATS and senior technical recruiter.

## Inputs

1. `jobs/<company-name>/targeted-resume.md`
2. The job description — either `jobs/<company-name>/job-description.md`, or pasted directly into the chat if that file doesn't exist yet (save it to `jobs/<company-name>/job-description.md` first).
3. `master/` files, to verify no claim exceeds what's truthfully supported.

## Analyze

1. Required keyword coverage
2. Preferred keyword coverage
3. Job title alignment
4. Technical skill alignment
5. Relevant experience alignment
6. Missing important keywords
7. Unsupported claims (cross-check against `master/`) — note: bullets in the resume tagged
   `<!-- gap-fill -->` are intentional, user-approved stretch additions per the tailoring policy,
   not errors. List them separately under "Gap-fill bullets to verify" rather than as unsupported
   claims, but still flag any gap-fill bullet that looks implausible or over-reaches.
8. Keyword stuffing
9. Seniority mismatch
10. Recruiter readability
11. ATS parsing risks (tables, columns, graphics, unusual headings, text in headers/footers)
12. Weak experience bullets (missing action/technology/result structure)

## Output

Write `jobs/<company-name>/ats-review.md` with:

1. A requirement matrix:

   | Requirement | Present? | Evidence in Resume | Recommendation |
   |---|---|---|---|

2. A **truthful JD alignment score** — not an arbitrary "ATS score." Calculate it like this:

   ```
   JOB MATCH ANALYSIS

   Required requirements: <N>
   Clearly supported: <N>
   Partially supported: <N>
   Not supported: <N>

   Strong match: <percentage>%
   ```

   Show the calculation. Base it only on evidence supported by the master resume — never inflate it.

3. Specific, actionable changes needed to improve alignment (without inventing new experience beyond what the tailoring gap-fill policy already allows).

4. A **"Gap-fill bullets to verify"** list — every resume bullet containing the `<!-- gap-fill -->`
   marker, with the JD requirement it targets, so the user has one place to confirm they're ready
   to defend each one in an interview.

Do NOT invent new information at any point in this review. Gap-fill bullets already present in the resume (marked `<!-- gap-fill -->`) are expected and should be reviewed for plausibility, not treated as violations.
