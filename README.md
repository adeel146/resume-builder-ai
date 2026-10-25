# Resume AI System

A reusable, version-controlled system for tailoring your resume to specific job descriptions using **VS Code + GitHub Copilot** as the intelligence layer, with **Microsoft Word** as the final formatting layer.

## Philosophy

- Your **Master Resume** (`master/`) is the single source of truth. Never invent new employers, job titles, dates, degrees, or certifications.
- For every job application, create a dedicated folder under `jobs/<company-name>/` containing the job description, Copilot's analysis, the targeted resume draft, and an ATS review.
- Don't chase an artificial "95% ATS score." Optimize for **truthful requirement coverage, exact relevant terminology, and strong achievement bullets**.
- When a job description requires something `master/` doesn't directly show, Copilot will **gap-fill**: reframe real, adjacent experience with the JD's terminology (or add a modest bullet using technologies you've genuinely used elsewhere), tag it inline as `<!-- gap-fill -->`, and list it separately in the output so you always know exactly what you'll need to defend in the interview.

## Folder structure

```
resume-builder/
├── master/                 # Source of truth — your complete career history
│   ├── master-resume.md
│   ├── experience.md
│   ├── projects.md
│   ├── skills.md
│   └── achievements.md
├── jobs/                   # One subfolder per application
│   └── <company-name>/
│       ├── job-description.md
│       ├── analysis.md
│       ├── targeted-resume.md
│       └── ats-review.md
├── output/                 # Final exported resumes (PDF/DOCX) per application
├── templates/
│   └── word-template-guidelines.md
└── .github/
    └── prompts/
        ├── analyze-job.prompt.md
        ├── tailor-resume.prompt.md
        └── ats-review.prompt.md
```

## Workflow

1. **Fill in `master/`** with your real, complete career history (summary, skills, experience, projects, achievements, education).
2. **New application**: paste the full job description directly into VS Code Copilot Chat — no need to create a file first. (If you prefer, you can still create `jobs/<company-name>/job-description.md` and paste it there yourself.)
3. In VS Code Copilot Chat, run the **analyze-job** prompt against the JD. If no `jobs/<company-name>/` folder exists yet, Copilot creates it and saves the pasted JD to `job-description.md` before generating `jobs/<company-name>/analysis.md`.
4. Run the **tailor-resume** prompt (references `master/` + the JD) to generate `jobs/<company-name>/targeted-resume.md`. Any JD requirement not directly covered by `master/` gets gap-filled (reframed real experience or a modest, plausible bullet), tagged inline with `<!-- gap-fill -->`, and listed in a "Gap-fill additions" section for your review.
5. Run the **ats-review** prompt to generate `jobs/<company-name>/ats-review.md`, check the "Gap-fill bullets to verify" list, and fix any remaining gaps.
6. Paste the final targeted content into your Word template (`templates/word-template-guidelines.md` has the layout rules), export to PDF, and save it in `output/`.

## Rules Copilot must always follow (baked into the prompt files)

- Never invent new employers, job titles, dates, degrees, or certifications.
- Build every bullet from real technologies, projects, and responsibilities in `master/` — including gap-fill bullets, which must reframe genuine adjacent experience or use technologies already listed in `master/skills.md`, never a technology or domain the candidate has never touched.
- Analyze the job description thoroughly before writing anything.
- Use exact JD terminology only when it truthfully matches real experience — no keyword stuffing.
- Keep the resume ATS-friendly: single column, standard headings, no tables/graphics/icons/text boxes.
- Keep the final resume to 1–2 pages.
- Tag every gap-fill bullet inline with `<!-- gap-fill -->` and list it explicitly in the output so nothing is silently blended in as verified fact.
- Flag requirements that are too far outside real experience to honestly gap-fill, so you can decide how to handle them directly.
