# Run individual stages

Attach AGENTS.md and the named procedure plus the saved context in a chat-only client. Replace bracketed paths. These are instructions, not product-specific slash commands or installed skills.

| Mode | Copyable request |
| --- | --- |
| source-review | Read docs/01-initialize.md and all indexed candidate sources. Refresh the evidence inventory, conflicts, and base-resume mapping. Do not search jobs. |
| jobs-only | Follow docs/02-discover-and-rank.md using saved preferences/history. Create the ranked workbook and validated history update. Leave contact fields blank. |
| contacts-only | Follow docs/03-research-contacts.md for [workbook]. Preserve the accepted job set and record the authoritative enriched workbook in the manifest. |
| resumes-only | Follow docs/04-tailor-documents.md for [workbook] using approved style/evidence. Produce one resume source per accepted job, then render and inspect with docs/05-render-and-verify.md. |
| cover-letters-only | Follow docs/04-tailor-documents.md for [workbook]. Research official employer context, write one letter per job, then render and inspect with docs/05-render-and-verify.md. |
| emails-only | Follow docs/06-draft-outreach.md using [workbook], verified contacts, document paths, and actual application status. Save unsent text drafts. |
| render-and-verify | Follow docs/05-render-and-verify.md on [source directory]. Preserve substantive content, use a new build directory, and record all automated and manual checks. |

For every mode also follow docs/07-quality-and-handoff.md. If inputs are missing/stale, run the minimum prerequisite or request the missing input; do not repeat valid stages merely because the session is new.
