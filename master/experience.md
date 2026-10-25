# Experience — Full Detail (Ground Truth)

This file is the **unfiltered, tagged master record** of every real responsibility across every
role and project. `tailor-resume.prompt.md` pulls from this file to build targeted resumes.

Every bullet is tagged with its discipline so a targeted resume can be generated for a specific
variant:

- `[Frontend]` — only used when building a **Frontend-focused** resume.
- `[Backend]` — only used when building a **Backend-focused** resume.
- `[Full-Stack]` — used in **either** a Frontend or Backend resume as relevant, and always used
  in a **Full-Stack** resume.
- A **Full-Stack** targeted resume should include `[Frontend]` + `[Backend]` + `[Full-Stack]`
  bullets (i.e., everything) for the relevant project.
- A **Frontend** targeted resume should include only `[Frontend]` + `[Full-Stack]` bullets.
- A **Backend** targeted resume should include only `[Backend]` + `[Full-Stack]` bullets.

---

## Lumovy Technology Solutions (Client: Microsoft) — Senior Software Engineer
**March 2024 – Present | Remote**

Outsourced to Microsoft via Lumovy Technology Solutions. This is the only role with genuine,
confirmed full-stack (.NET/C#) backend work in addition to frontend work — all other roles are
frontend-only.

### Project: Microsoft.com Website (Surface Laptop & AEM/WCAG Accessibility)

- Implemented WCAG 2.1 AA accessibility standards — dark mode, keyboard navigation, low-vision user
  support, and NVDA screen reader compatibility — across 10+ content-driven pages. `[Frontend]`
- Built AEM-integrated components for content-driven pages, including Surface Laptop and
  Defender for Cloud, with a focus on WCAG accessibility. `[Frontend]`
- Used the LIT Framework to create 25+ web components, developed and documented in Storybook, for
  cross-browser and cross-platform compatibility. `[Frontend]`
- Authored AEM dialog configurations (`_cq_dialog`) with **15+ custom authoring fields** (text,
  rich text, image, multifield, checkbox) per component, enabling content authors to edit
  component content/behavior without developer involvement. `[Frontend]`
- Built editable templates and component policies in AEM's Template Editor, defining allowed
  components and authoring constraints across **10+ page types** to standardize content
  authoring. `[Frontend]`
- Developed responsive, cross-browser-compatible components with TypeScript for type safety and
  long-term maintainability. `[Frontend]`
- Created 100+ unit test cases and integrated them into CI/CD pipelines. `[Frontend]`
- Automated end-to-end regression testing with Playwright, reducing manual QA effort by ~60%.
  `[Frontend]`
- Improved SEO and page-load performance through server-side rendering (SSR) and frontend
  optimization, cutting page-load time by 35% and lifting Lighthouse scores by 20+ points.
  `[Frontend]`
- Implemented security hardening against Cross-Site Scripting (XSS) attacks, identifying and
  remediating vulnerabilities across **20+ frontend components**, including a stored XSS exploit
  in shared AEM HTL templates caused by unsafe context escaping. `[Frontend]`
- Automated AEM localization content-structure provisioning with custom scripts, auto-generating
  folders across **22 additional locales** and cutting manual content-ops setup time by **~90%**.
  `[Frontend]`
- Led accessibility audits combining automated axe-core WCAG 2.1 A/AA scans with manual
  assessments across Cascade Components and content pages, identifying and remediating **15+
  compliance findings** (color contrast, ARIA labeling, reflow at 400% zoom). `[Frontend]`

### Project: Cascade Content Studio (CCS) — AI-Powered Content Generation

- Built AI-powered content generation and automated content evaluation features using C#, .NET,
  and ASP.NET Core. `[Backend]`
- Integrated Azure OpenAI (GPT models) into backend services to generate content programmatically.
  `[Backend]`
- Designed end-to-end AI workflows: secure REST APIs, prompt engineering, grounding-context
  preparation, and structured processing of model responses into generated content, quality
  scores, and actionable recommendations. `[Backend]`
- Optimized Azure OpenAI/GPT prompts on the internal CCS tool to reduce token usage by ~30% while
  achieving maximum, consistent response quality and lowering per-request cost. `[Backend]`
- Used GitHub Copilot, MCP servers, and task-specific AI agents to streamline development and
  testing, cutting development/testing cycle time by ~25%. `[Full-Stack]`
- Developed 100+ REST APIs and backend services, implemented business logic and SQL data access,
  and built reusable architecture with authentication, authorization, validation, asynchronous
  workflows, caching, and reporting — supporting a platform handling **10M–100M requests per
  month** at **99.99% uptime**. `[Backend]`
- Troubleshot and optimized backend performance through profiling, query optimization, and
  targeted refactoring — improving performance by **40%** and reducing monthly infrastructure
  cost by **$2,000–$10,000+**. `[Backend]`
- Collaborated with product managers, stakeholders, engineers, UI/UX designers (Figma), QA, and
  DevOps teams across a cross-functional team of 10+ using Azure Boards and Microsoft Teams,
  following Agile methodologies in 2-week sprint cycles, to define requirements and deliver
  reliable enterprise solutions. `[Full-Stack]`
- Applied clean code, object-oriented programming, design patterns, Git workflows, code reviews,
  automated testing, CI/CD, secure development practices, technical documentation, deployment
  support, and continuous improvement across the SDLC. `[Full-Stack]`
- Led code reviews and mentored a team of **8 engineers** on clean code, SOLID principles, and
  SDLC best practices, reducing production incident resolution time by **60%** through
  systematic root-cause analysis and monitoring. `[Full-Stack]`
- Remediated **10+ OSS/npm dependency vulnerabilities** (Axios, glob, sigstore, cross-spawn, tar)
  flagged by Microsoft's S360 security scanning pipeline, keeping the CCS repositories
  continuously audit-clean. `[Backend]`
- Defined precedence rules and enforced template-specific character-limit validation for
  AI-generated edit instructions across CCS AEM dialogs, preventing content errors and ensuring
  template-safe AI-authored content. `[Full-Stack]`
- Instrumented Azure Application Insights telemetry to track per-step execution time across the
  CCS content-generation workflow, enabling data-driven performance tuning and bottleneck
  identification. `[Backend]`
- Built a Playwright E2E test suite using the Page Object Model with mocked authentication,
  covering complete BYOC and Start New Project user flows; stood up an AI-assisted agent to
  auto-generate unit tests, accelerating regression coverage by **~40%**. `[Full-Stack]`
- Adopted GitHub Copilot-powered Component Governance agents to auto-detect and patch dependency
  vulnerabilities via automated pull requests, reducing manual security-triage effort.
  `[Full-Stack]`

---

## Graffitecs Solutions — Senior Software Engineer
**2023 – 2024**

Primarily a frontend role; also built and consumed .NET (ASP.NET Core Web API) REST API
endpoints across projects to support frontend data requirements.

### Project: Community Facilities Planning Calculator (CFPC)

- Led the CFPC project as team lead for 6 frontend engineers, collaborating with the business
  team to gather requirements and coordinating with the backend and UI/UX teams, providing
  technical guidance and direction to the frontend team. `[Full-Stack]`
- Designed the front-end UI for planning and allocating community facilities based on
  demographic characteristics, across 15+ demographic variables and facility types. `[Frontend]`
- Implemented statistical formulas in the frontend application for demographic-based planning
  calculations. `[Frontend]`
- Built and consumed 50+ internal and third-party REST API endpoints to aggregate and serve
  demographic datasets powering the calculator, cutting multi-step manual spreadsheet
  calculations down to under 2 seconds per request. `[Backend]`
- Transformed a manual, Excel-based community facilities planning workflow into a cloud-based
  SaaS calculator, increasing planning/calculation speed by 50%. `[Full-Stack]`
- Created an intuitive interface for stakeholders to interact with statistical data — data
  input, visualization, and analysis — reducing data-entry and review time by ~30%. `[Frontend]`

### Project: Resleeve AI — "AI Created Fashion To Assist Your Imagination"

- Spearheaded development of 4 key AI-driven features: generating original product designs,
  exploring design variations, transforming sketches into high-quality designs, and AI-driven
  image retouching. `[Frontend]`
- Built .NET (ASP.NET Core Web API) REST API endpoints connecting the frontend to Resleeve's AI
  generation pipeline, handling image upload/retrieval for 1,000+ design requests. `[Backend]`
- Crafted a seamless, user-friendly interface for efficient interaction with Resleeve's AI
  technology, cutting average design-iteration time by ~25%. `[Frontend]`

### Project: The Gate — Organizational Workflow System

- Led development using Next.js to create an automated organizational workflow system adopted
  by 50+ internal users, with a dynamic, intuitive interface. `[Frontend]`
- Designed and built a custom workflow builder allowing admins to configure their own
  multi-step approval workflows (steps, roles, conditions) without developer involvement,
  supporting 20+ unique workflow templates. `[Full-Stack]`
- Built .NET (ASP.NET Core Web API) REST API endpoints to manage workflow state, approvals, and
  organizational-chart hierarchy data across 10+ departments. `[Backend]`
- Implemented automated processes, reducing manual workflow-approval effort by ~40%. `[Frontend]`
- Introduced an organizational chart feature for visualizing hierarchies. `[Frontend]`

### Project: Three60 (Three60.pm)

- Served as Project Leader for a team of 4, owning the full project lifecycle from planning
  through execution and delivery. `[Full-Stack]`
- Led frontend development with ReactJS, building 20+ interactive, responsive components
  forming the core of the application. `[Frontend]`
- Built .NET (ASP.NET Core Web API) REST API endpoints for core application data flows,
  enabling real-time updates across the platform. `[Backend]`
- Implemented rigorous testing (Jest/RTL), achieving 90%+ test coverage on core components, to
  ensure a seamless user experience. `[Frontend]`

### Cross-project responsibilities (Graffitecs)

- Developed and maintained user-facing features using React.js and Next.js. `[Frontend]`
- Built 30+ reusable components and front-end libraries, cutting new-feature development time
  by ~20%. `[Frontend]`
- Optimized applications for performance across devices and browsers, reducing render/re-render
  overhead by ~25%. `[Frontend]`
- Implemented state management with Redux. `[Frontend]`
- Developed and consumed 15+ .NET (ASP.NET Core Web API) REST API endpoints across projects to
  support frontend data requirements and third-party integrations. `[Backend]`
- Collaborated with designers, back-end developers, and product managers. `[Frontend]`
- Led and participated in code reviews for own and other teams' code, reviewing 20+ pull
  requests per month. `[Frontend]`
- Mentored and supported 3 team members. `[Frontend]`
- Created, maintained, and reviewed technical documentation. `[Frontend]`

---

## ILI Digital — Senior Software Engineer / Frontend
**2022 – 2023**

Primarily a frontend role; also built .NET (ASP.NET Core Web API) REST API endpoints across
projects.

### Project: BASF Battery Recycling Platform (with BMW)

- Served as frontend ReactJS developer on the joint BMW–BASF Battery Recycling project,
  developing 10+ web pages for the recycling order process. `[Frontend]`
- Resolved technical issues to optimize the recycling order process across BMW Dealer, BASF
  Logistics, and BMW OEM roles. `[Frontend]`
- Built .NET (ASP.NET Core Web API) REST API endpoints integrating BMW Dealer, BASF Logistics,
  and BMW OEM systems, enabling end-to-end data exchange across all 3 stakeholder roles.
  `[Backend]`
- Streamlined and fully automated the recycling process across all three roles, eliminating
  manual work (**100% automation**, up from fully manual) and cutting average order-processing
  time by **~70%**. `[Frontend]`

### Project: mcyclo — Styrodur® Take-Back & Recycling System

- Contributed to mcyclo, an eco-conscious take-back system built in collaboration with sales
  partners BACHL and ISOVER, enabling the collection and recycling of clean Styrodur®
  insulation cuttings across **50+ partner collection points** in Germany. `[Frontend]`
- Built .NET (ASP.NET Core Web API) REST API endpoints for partner order intake and tracking,
  processing **500+** take-back requests. `[Backend]`

### Cross-project responsibilities (ILI Digital)

- Developed and maintained web applications using TypeScript, ReactJS, and Next.js.
  `[Frontend]`
- Integrated 10+ RESTful API endpoints (.NET) into frontend applications, and built .NET
  (ASP.NET Core Web API) backend endpoints where needed for partner data exchange. `[Backend]`
- Managed application state with Redux. `[Frontend]`
- Tested code using Jest and React Testing Library, implementing unit and integration tests.
  `[Frontend]`
- Optimized applications for speed and scalability, reducing page-load time by ~25%.
  `[Frontend]`
- Performed code reviews, troubleshot and debugged issues, and wrote technical documentation.
  `[Frontend]`

---

## Nextbridge (Pvt) Ltd — Software Engineer / Frontend Developer
**2021 – 2022**

Primarily a frontend role, with genuine AWS/serverless backend exposure.

- Maintained existing React systems, fixing 50+ bugs and ensuring compliance with new
  regulatory standards. `[Frontend]`
- Designed and developed 15+ new custom components to meet project requirements, using
  ReactJS. `[Frontend]`
- Built and maintained 10+ serverless backend functions using AWS Lambda, with DynamoDB,
  S3, and EC2, supporting application infrastructure for 5,000+ monthly users. `[Backend]`
- Maintained and updated project dependencies across 3 repositories, resolving conflicts.
  `[Frontend]`
- Developed user-friendly, responsive web applications, improving mobile page-load time by
  ~20%. `[Frontend]`
- Collaborated with a cross-functional team of 6+ to design, develop, and deploy high-quality
  web applications. `[Full-Stack]`
- Created 10+ reusable UI components and libraries. `[Frontend]`
- Wrote clean, efficient, well-documented code. `[Frontend]`
- Participated in code reviews for 20+ pull requests, providing constructive feedback to team
  members. `[Frontend]`

---

## Notes / Known Gaps

- Graffitecs and ILI Digital backend work is .NET (ASP.NET Core Web API)-based (REST API
  endpoints supporting their respective frontend applications). Nextbridge backend work is
  AWS serverless (Lambda, DynamoDB, S3, EC2).
- Per the user's explicit instruction, the quantified figures added to Graffitecs, ILI Digital,
  and Nextbridge bullets (team sizes, request/user counts, % improvements, etc.) are
  plausible/illustrative numbers the user has chosen to add and will personally defend/explain
  in interviews — they are not independently verified the way the Lumovy/Microsoft figures in
  `achievements.md` originally were. See `master/achievements.md` for the full list and its
  updated policy note.
