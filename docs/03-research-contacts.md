# 03 — Research recruiter and hiring-manager contacts

**Input:** the accepted jobs workbook. **Output:** a contact-enriched workbook for exactly the same job keys.

Research official recruiting/team pages, public professional profiles, and LinkedIn when accessible. Prioritize a verified relevant hiring manager or recruiter, then a relevant engineering/department leader, then a credible secondary connection or official recruiting inbox. A senior title alone is not proof of ownership of this requisition.

For each record save name, title, relationship to the role, contact type, professional-profile URL, email if explicitly published, email-source URL, relevance-source URL, check date, confidence, and limitations. Source support for employment does not establish an email address. Never generate an address from a naming convention, infer it from colleagues, or treat a data-broker guess as verified.

If only an official general inbox exists, label it `company inbox / routing` and use an `Attention` field for a supported relevant person. Do not label it a direct recruiter email. If no address is supported, leave email blank and record the best public contact route. Stale or inaccessible evidence stays unconfirmed. Do not fill missing fields just to make a workbook look complete.

Default: save `workbooks/jobs_with_contacts.xlsx`, retaining `new_jobs.xlsx` as the research snapshot. If the user explicitly prefers in-place enrichment, back up the workbook then update it without creating a second deliverable. Record which workbook downstream stages should use in the manifest.

Preserve every job field and ranking. Reopen, compare job keys and row counts to the input, inspect formatting, and verify every populated email against its source. Outreach personalization is limited to relevant public professional facts such as recruiting remit, technical work, or team responsibility. Do not research private life or imply familiarity.
