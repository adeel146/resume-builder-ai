# Senior .NET Software Engineer - healthcare role review

No employer name was supplied; healthcare-dotnet is an application label, not a claimed
employer or healthcare work history. The draft emphasizes documented C#/.NET Core,
ASP.NET Core, SQL, REST APIs, architecture, security, testing, cloud operations,
reporting, troubleshooting, mentoring, and stakeholder collaboration.

## Important qualification gaps

- **6+ professional years:** the recorded career begins in 2021. Exact starting months
  are not available, and six years are not established as of October 2026.
- **6+ years of C#/.NET Core:** confirmed full-stack C#/.NET experience is documented
  at Lumovy/Microsoft from March 2024. Do not extend that tenure across earlier roles.
- **5+ years of C:** C is a different programming language from C#. No C experience
  is documented. Ask the recruiter whether this screening requirement was intentional;
  do not answer it as though it meant C#.
- **Healthcare/EHR integrations and HIPAA, HL7, X12, DICOM:** not documented. General
  secure APIs, authentication, authorization, reporting, and workflow experience are
  transferable skills, not evidence of patient-data or healthcare-standard expertise.
- **Degree:** the actual qualification is a Bachelor of Business and Information
  Technology. Retain that title; the employer determines whether it is a related field.
- **English fluency:** not explicitly confirmed in the master materials; omitted.
- **Regulated-industry experience:** not established. Security engineering experience
  is included without asserting healthcare or financial compliance.

## Source caveats and candidate verification

The opening note in master/experience.md says Lumovy/Microsoft is the only confirmed
full-stack C#/.NET role, while later entries describe .NET endpoints at Graffitecs
and ILI Digital. Until that inconsistency is resolved by the candidate, this resume
uses frontend/project-delivery achievements for those earlier roles and does not
claim additional .NET tenure.

The master achievements file distinguishes verified metrics from previously added,
interview-defensible figures. This draft reuses existing numbers without adding new
metrics. Before submission, confirm API counts, team sizes, test coverage, and
percentage improvements against evidence; otherwise replace them with qualitative
wording. No gap-fill claims were introduced, and no ATS score is asserted.

## Build

From the workspace root:

`python scripts\build_healthcare_dotnet_resume_pdf.py`

The PDF is generated from targeted-resume.md, uses an extractable single-column
layout, and is limited to two pages. The existing Deel build remains available:

`python scripts\build_deel_resume_pdf.py`
