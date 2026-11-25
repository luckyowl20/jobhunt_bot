# 01 — Initialize and review sources

**Inputs:** the user's answers, existing career documents, and generic templates. **Outputs:** approved private context and rendered user-specific templates. Do not start discovery until search scope is usable; do not generate a batch until document style is approved.

## Interview in short rounds

1. Establish role families and priorities, career stage, industries, desired responsibilities, and explicit exclusions. Offer the historical three lanes (government, government contractors, commercial) as options, not mandatory quotas.
2. Establish country/region, preferred cities or radius, excluded places, remote eligibility, hybrid office requirements, relocation/travel, start date, employment type, and compensation constraints. Distinguish must-haves from preferences. Ask what “remote” means for the user's actual residence.
3. Establish relevant employment, education, projects, dates, tools, responsibilities, outcomes, and links. Ask which work was academic, personal, volunteer, or paid. Record completed work separately from plans and design targets.
4. Ask only relevant eligibility questions: work authorization, sponsorship, required licenses, citizenship or clearance where a target role makes it material. Permit `unknown` or `not provided`; do not put unconfirmed sensitive facts into documents.
5. Collect examples and preferences for visual style and writing voice: section order, font, page count, density, bullet length, link placement, cover-letter tone. Ask what the user likes/dislikes in existing documents. Offer the generic template as a starting point.

Use `templates/input-checklist.md`, `profile.template.md`, and `search-preferences.template.md` to make the interview complete. Ask targeted follow-ups after reading the sources, rather than asking the user to retype facts already documented.

## Review and establish evidence

Inventory all relevant files with relative path, type, version/date, purpose, and review status in `private/context/input-index.md`. Read each relevant source in full, including PDF links and relevant diagrams; inspect all worksheets of input workbooks. Exclude dependency folders, temporary renders, and old output batches from candidate authority unless specifically designated.

Populate `evidence-inventory.md` with stable evidence IDs, exact source locations, bounded claims, dates, tools, metrics, and caveats. Build a project/link index and a base-resume mapping by role family. Generated prior resumes can suggest phrasing but are not independent proof. A recommendation supports attributed assessments, not invented first-person accomplishments.

Where documents disagree, record both values and ask for clarification. Until resolved, omit the disputed claim or use a supported narrower statement. Do not turn conflicting measurements into a made-up range. Distinguish designed, prototyped, tested, deployed, and achieved. Optionally provide exactly three evidence-backed strengths and three gaps, as in the original workflow.

## Calibrate the user-specific document style

1. Copy the generic LaTeX templates into `private/templates/`; do not overwrite the public templates.
2. Replace all placeholder text with verified user facts. Initially preserve the resume's 10-point Inria Sans, compact Letter layout, four sections, and 5/3/3/1/2 bullet allocation. Change these deliberately with the user where their experience requires it.
3. Create one representative resume and cover-letter sample. Use a user-supplied representative role or clearly label the sample as general. Never invent a live posting.
4. Render using procedure 05 and show full-page previews to the user. Ask about readability, density, emphasis, tone, and what feels unlike them. Iterate on both content and style.
5. Save approved `resume_template.tex`, `cover_letter_template.tex`, optional alternative base resumes, and `private/context/style-rules.md`. Record actual bullet count, typical bullet length, page count, margins, font, section order, line spacing, and a reference preview path. Character counts are diagnostics; the PDF is the layout authority.
6. Record approval date and template/style revision in `decisions.md`. Do not mark a placeholder scaffold as an approved candidate template.

## Persist setup

Save the profile, preferences, evidence, input index, style rules, decisions, and `SESSION_CONTEXT.md`. Create an empty `private/history/previously_considered_jobs.xlsx` using the schema in `workbook-schema.md`, or import the user's existing workbook preserving its rows/styles. Create a blank user workbook template from that schema if none was supplied.

The handoff must list resolved paths, approved versions, unresolved facts, available tools, and the next action. Let the user review the factual profile and search scope. Initialization is complete when another agent can identify the authoritative files, reproduce the approved layout, and start discovery without needing this chat's memory. Missing optional documents must be recorded, not silently assumed.
