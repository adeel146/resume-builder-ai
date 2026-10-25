# Deel application - coverage and verification

The targeted resume emphasizes the supplied job description's React.js, TypeScript,
Redux/state management, HTML/CSS, SaaS, automated testing, accessibility, cross-functional
delivery, remote collaboration, ownership, mentoring, and customer-workflow outcomes.
It uses the existing master records without introducing new employers, dates, skills,
or metrics. No gap-fill claims were added.

## Requirements not established by the source material

- **7+ / 8+ years:** the recorded employment history begins in 2021. It does not establish
  either tenure threshold as of October 2026. The resume does not assert a total.
- **React Hooks, Functional Components, Class Components:** React.js is documented,
  but these specific APIs/patterns are not explicitly confirmed in the master skills.
  Confirm hands-on experience before adding them.
- **Node.js:** not documented. Backend experience is C#/.NET and AWS serverless;
  do not relabel it as Node.js. The application can explain this transferable background.
- **FinTech, payroll, subscription management, and access auditing:** not documented.
  Approval workflows and authentication/authorization are adjacent, not equivalent.

## Candidate review before submission

Some source metrics are labeled "Added" or "interview-defensible," rather than independently
measured, in master/achievements.md. This draft reuses those existing figures, including
component/test counts, team sizes, test coverage, and several percentage improvements.
Confirm each retained figure against your own evidence, or replace it with qualitative
wording before submission. The resume is tailored, not an assurance of eligibility or an
ATS score.

## Output

Run `python scripts\build_deel_resume_pdf.py` from the workspace root.
The builder reads targeted-resume.md directly and writes the application PDF under
output/deel. It rejects output over two pages rather than silently producing a long resume.
