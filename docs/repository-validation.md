# Repository validation

Checked 2026-11-24 on Windows with local MiKTeX and Poppler.

- Both generic LaTeX templates compiled with two passes using the included Python helper.
- Each generated PDF had exactly one page, with no recorded overfull or underfull warnings.
- Both full-page previews were visually inspected for clipping, overlap, glyphs, and wrapping. The resume retains 14 instructional bullet slots; the letter is an intentionally shorter scaffold to be filled and approved during initialization.
- The helper correctly rejected a wrong source count, a missing compiler, and an existing output directory.
- Relative Markdown links and the JSON manifest template were checked.
- Public text was scanned for the original candidate's name, username, contact details, and machine-specific paths; private materials were not packaged.

The generic previews under `examples/` demonstrate the starter layout. They are not candidate applications or an approved personalized style. A real user's initialization still requires factual review and template calibration. No new job campaign was run, and the desktop upload/download instructions were documented rather than exercised in separate ChatGPT and Claude accounts.
