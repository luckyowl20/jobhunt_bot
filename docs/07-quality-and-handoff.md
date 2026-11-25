# 07 — Quality gates, resumability, and delivery

Create `run-manifest.json` from the template at run start and update it after every stage. Save exact inputs, context/style revisions, timestamps/timezone, resolved paths, requested and accepted counts, job keys, source URLs/check times, stage statuses, output mapping, history append state, application status, and unresolved questions. Hash key inputs when possible. A stage is `pending`, `in_progress`, `passed`, `blocked`, or `skipped`; preserve the reason for blocked/skipped work.

Suggested layout:

```text
private/
  context/{SESSION_CONTEXT,profile,search-preferences,evidence-inventory,input-index,style-rules,decisions}.md
  sources/...
  templates/{resume_template,cover_letter_template}.tex
  templates/jobs_template.xlsx
  history/previously_considered_jobs.xlsx
outputs/<run-id>/
  run-manifest.json
  workbooks/{new_jobs,jobs_with_contacts}.xlsx
  research/...
  tailored_resumes/*.tex
  tailored_resumes/pdfs/*.pdf
  tailored_cover_letters/*.tex
  tailored_cover_letters/pdfs/*.pdf
  recruiter_email_drafts/*.txt
  qa/{verification.md,history-backup.xlsx,...}
  HANDOFF.md
```

For each accepted job key, reconcile exactly one source/PDF pair for each requested document type and one draft when outreach is requested. Check keys, not just file counts. Record explicitly excluded or expired jobs and adjust expected counts transparently. No missing PDF can be hidden by a duplicate for another job.

Workbook QA: reopen all sheets, inspect full content and display, check official clickable URLs, activity evidence, exclusions, ranking, qualifications, deduplication, formula errors, stable IDs, blank contact fields before research, and contact evidence afterward. Preserve template formatting and the history's prior rows. If XLSX authoring is unavailable, a CSV can be an interim export, but it does not satisfy the requested formatted workbook deliverable.

Document QA: exact filename mapping; current source/PDF pair; successful compilation; page limit; log review; every rendered page visually checked; density consistent with approved style; candidate and company claims supported; no placeholders or unsupported eligibility claims. Email QA: recipient provenance, truthful status, correct attachments, unsent state.

Use `templates/qa-checklist.md` to record results. Automated compilation does not establish factual or visual correctness. Do not mark a batch complete until all requested checks pass; preserve partial files and explain the exact remaining work.

## Resume an interrupted run

Read the manifest and HANDOFF first, then verify existing files and recorded statuses. Reuse passed stages if inputs remain unchanged and posting evidence is current. Revalidate changed facts/postings before dependent work. If style changes, rerender affected documents; if an evidence claim changes, recheck every document that cites its ID. Use a new build revision, not silent replacement of prior build evidence. Do not reappend history for an already committed run.

At session end, update `private/context/SESSION_CONTEXT.md` with the latest context revisions, active run, completed stages, unresolved questions, and next concrete command/prompt. Save `outputs/<run-id>/HANDOFF.md` even if blocked. In a chat-only client, deliver downloadable copies and have the user retain them.

Final response: link workbooks, document folders or ZIPs if requested, manifest, and QA report; state verified counts, shortfalls, unresolved fields, and what was not completed. Optional ZIPs contain only intended deliverables, never private source documents or unrelated prior runs. Application submission and email sending remain separate tasks requiring explicit instructions.
