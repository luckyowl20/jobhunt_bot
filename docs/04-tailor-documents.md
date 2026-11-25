# 04 — Tailor resumes and cover letters from the workbook

**Inputs:** the accepted workbook, live exact postings, evidence inventory, chosen base resumes, approved private LaTeX templates, and style rules. **Outputs:** one resume and one cover-letter source per accepted job, plus a claim map. Partial modes create only the requested document type.

## Resume procedure

1. Read the full approved template and style rules. Read the row's tailoring notes and chosen resume base, then the full official posting. Revalidate activity and unresolved gates. If closed, mark it skipped and reconcile counts; do not silently substitute a different role.
2. Build `research/<job-key>-claim-map.md`: requirement, evidence ID, source location, intended wording, and caveat. Select the strongest truthful evidence across all bases; the chosen base controls emphasis, not which facts exist.
3. Preserve chronology, dates, employment type, project maturity, and links. Reorder emphasis and compress or expand existing evidence to foreground relevant duties. Use exact job terminology only when it describes genuine experience. Do not upgrade coursework to professional experience, familiarity to production ownership, or a design goal to a measured outcome.
4. Keep section hierarchy, typography, margins, approximate per-bullet and total length, bullet count, and vertical fill close to the approved template. The historical baseline had 14 bullets (5 + 3 + 3 + 1 + 2); a new user's approved template may differ. Dense means useful detail, not filler, unreadable type, clipping, or fabricated scope.
5. Use supported LaTeX commands and escape reserved characters (`&`, `%`, `_`, `#`, `$`, braces). Avoid decorative Unicode arrows or new icons/packages. Preserve documented project URLs. Do not introduce a summary section or redesign during routine tailoring unless the approved style calls for it.
6. Save `tailored_resumes/company_position_YYYY-MM-DD.tex`. Use lowercase ASCII-safe filename tokens. Add requisition or job-key suffix when names collide. Record the exact job-key-to-file mapping in the manifest.
7. Compile and inspect with procedure 05. Repair wording before shrinking layout. Recheck facts after each repair. Do not edit the approved master template to fix one job's overflow.

## Cover-letter procedure

Read all user-approved examples in full. Preserve their voice and LaTeX structure; do not treat their old factual claims as newly verified. Research the employer's mission, products, or public-service function using official pages and record URL/check date in the job research record.

Write a specific opening naming the exact role and a concrete reason for interest. Connect two or three relevant pieces of evidence to the role's central work. Show adaptability, learning, and work under pressure through supported examples or honest statements of intent. Close with a concise invitation to discuss fit. Avoid generic praise, invented initiatives, unsupported company culture claims, and a prose copy of every resume bullet.

Use `tailored_cover_letters/company_position_cover_letter_YYYY-MM-DD.tex`, with the same collision suffix convention. Follow the saved paragraph structure, contact block, signature, font, margins, and page limit. The original examples used 10-point Inria Sans, 0.85-inch margins, no paragraph indentation, and 0.7em paragraph spacing. The private approved version is authoritative.

Review candidate claims against evidence IDs and company facts against official sources. Render every letter using the same QA process as resumes. Keep placeholders and unresolved claims out of employer-ready files. Save unsupported details as questions in the manifest while continuing with supported content.
