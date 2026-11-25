# Jobs workbook and history schema

Create a real XLSX using the user's workbook template if supplied. For a fresh workbook use a `Jobs` sheet, one job per row, bold readable headers, frozen header row, filters, wrapped long text, sensible widths, and clickable official URLs. Preserve the 11-column historical structure first; append verification/ranking fields as needed. Rename the original location-specific header generically.

| Primary column | Meaning |
| --- | --- |
| Priority | Integer rank, 1 strongest |
| Organization and position | Exact employer and official title |
| Location | City/region and remote/hybrid terms |
| Match | Concise supported rationale; no hiring-probability claims |
| Resume base | Actual source-resume path/version |
| Suggested resume tailoring | Specific evidence-backed projects/skills/bullet changes |
| Official source | Exact official posting hyperlink |
| Recruiter / hiring contact | Blank until contact research |
| Email | Published address or blank |
| Contact type / relevance | Direct recruiter/manager, secondary, or inbox route |
| Contact source | Supporting URL(s) |

Append: `Job key`, `Job ID`, `Verification date`, `Employment lane`, `Active evidence`, `Work arrangement`, `Required qualifications / evidence IDs`, `Eligibility / risk note`, `Closing date`, `Start date`, `Salary as published`, `Score`, component scores/reasons, `Status`, `Applied?`, `Application date`. Unknown facts remain blank with explanatory notes where material. Store actual date cells with visible date formats.

For contacts append: `Contact title`, `Attention`, `Contact checked`, `Email source`, `Role / relevance source`, `LinkedIn / professional profile`, `Confidence`, and `Routing notes`. A person's role and email can require separate evidence.

The source workbooks used qualitative `Match` and ordinal `Priority`; optional weighted scores are this repository's reproducibility addition. If using formulas, place editable weights in labeled cells, recalculate and verify results; if using assessed numeric values, identify them as assessments and include the method. Do not fabricate formula caches.

## Stable keys

Prefer `normalized-employer:requisition-id`. Without an ID, use employer + normalized title + location and store canonical URL for a second duplicate check. Record the exact key in manifest mappings. Rankings may change; keys must not. Distinguish distinct locations only when the posting represents a distinct opening.

## Previously considered history

Minimum legacy columns: `Organization and position`, `Official source`. Preserve every existing row and order. For a new history add `Job key`, `Job ID`, `Run ID`, `Date added`, and `Status`. Store extra audit metadata in a sidecar when extending an existing layout would be disruptive. History means selected/considered, not submitted.

First use: an empty header-only XLSX is valid. Later runs must read all rows/sheets. Append only validated accepted jobs, exactly once, following the transaction in procedure 02. Keep rejected/conditional leads in run research notes with reasons and dates, so a changed posting can be reconsidered deliberately later.
