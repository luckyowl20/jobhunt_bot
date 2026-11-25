# Document style rules — copy privately and customize during setup

Revision: starter-1 | Approval: pending | Reference preview: [path after approval]
This file controls future document runs. The starter values come from the supplied `resume_template.tex` and cover-letter examples; replace them with the user's approved choices and keep the TeX templates consistent.

## Resume visual contract

| Property | Starter value |
| --- | --- |
| Paper / length | US Letter / one page |
| Class / body size | article / 10pt |
| Typeface | Inria Sans, lining/light, T1 encoding |
| Margins | left/right 0.45in; top/bottom 0.4in |
| Line spread | 0.8 |
| Section style | large bold, horizontal rule |
| Section order | Education; Technical Skills; Experience; Projects |
| Bullets | 14 total; experience 5 + 3; projects 3 + 1 + 2 |
| Item spacing | itemsep 0.2em; topsep 0em |
| Header | centered large bold name; contact/links/location beneath |
| Links | dark blue RGB 0,102,180; retain actual verified URLs |
| Pagination | none |
| Density | detailed bullets, close vertical fill to approved sample; no clipping |

Baseline visible-text length: [measure after user content is approved]
Typical per-bullet length and line count: [measure]
Permitted section variations by role family: [list]

Preserve approximate length and bullet allocation during tailoring. Do not pad to hit a count or shrink type to fit unsupported content. Do not add decorative Unicode, arrows, new icons, or unsupported packages. The starter uses `\textbullet{}` for contact separators instead of raw Unicode. Exact character counts cannot predict font wrapping; inspect the PDF.

## Resume voice and factual rules

Use precise action, task, tools, scope, and supported result. Keep completed/in-progress distinctions. Label academic or personal work accurately. Prefer relevant technical detail over adjectives. Do not invent numbers, ownership, eligibility, or links. Keep dates and source facts consistent across versions.

## Cover-letter visual and voice contract

10pt article, Inria Sans, 0.85in margins, no paragraph indent, 0.7em paragraph spacing, no page number, one page. Contact block, date, hiring team/company, salutation, role-specific opening, evidence paragraphs, concise closing, signature. Use natural professional language; avoid generic flattery and unsubstantiated company claims. Preserve approved paragraph density and tone instead of copying a long example verbatim.

## Outreach voice

Short, warm, friendly, professional; normally two or three short paragraphs. Exact role, one or two fit points, modest review/routing request. No fabricated familiarity or false “already applied” claim.

## Change process

Discuss desired changes, edit this private file and corresponding template, compile a sample, review its full-page image, and record approval/revision in decisions.md. Existing runs retain their recorded style revision unless explicitly regenerated. New runs use the latest approved version. Employer-specific document requirements can override the baseline for that job; record the exception.
