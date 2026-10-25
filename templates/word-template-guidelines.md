# Word Template Guidelines (ATS-safe layout)

Keep ONE Word template, e.g. `[YourName]_Resume_Template.docx`, following this layout:

```
[YOUR NAME]
Full Stack Software Engineer

React.js | TypeScript | .NET Core | C# | SQL Server

[City, Country] | [Email] | [Phone] | [LinkedIn] | [GitHub]

SUMMARY
------------------------------------------------

TECHNICAL SKILLS
------------------------------------------------

PROFESSIONAL EXPERIENCE
------------------------------------------------

[Company]
[Job Title] | [Start] – [End]

• ...
• ...
• ...

PROJECTS
------------------------------------------------

EDUCATION
------------------------------------------------
```

## Do

- Single column
- Standard section headings (Summary, Technical Skills, Professional Experience, Projects, Education, Certifications)
- Normal body text, simple bullets
- Consistent date formatting
- Standard, widely-supported fonts (e.g. Calibri, Arial, Georgia)
- Clear visual hierarchy (bold company/title, plain bullets)
- Export to PDF from Word for final submission
- Keep to 1–2 pages

## Don't

- Two-column layouts
- Skill bars / progress graphics
- Logos, icons, photos
- Text boxes or floating elements
- Complex tables
- Infographics or fancy timelines
- Critical info (name, contact) placed only in a header/footer that some ATS parsers skip

## Process

1. Copy the finalized content from `jobs/<company>/targeted-resume.md`.
2. Paste into the Word template above, preserving section order.
3. Adjust spacing/line breaks only — don't change the wording without re-running the ATS review.
4. Export to PDF, save as `output/<company>-resume.pdf`.
