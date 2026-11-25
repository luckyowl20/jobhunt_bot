# Use with a desktop assistant

The procedure is portable Markdown. A local folder path typed into a chat does not itself grant file access. At session start, ask the assistant to report whether it can read/write the working folder, browse current websites, create/edit XLSX, run local commands, and inspect images/PDFs. Plan availability and app features vary; use the capability check rather than assuming a particular subscription.

## ChatGPT Desktop

Create a project for the job search, add the procedure files and candidate documents, and put the contents of `AGENTS.md` in the project instructions or explicitly attach it at session start. Projects can hold chats, reference files, and custom instructions. See [OpenAI's project guide](https://help.openai.com/en/articles/10169521-using-projects-in-chatgp).

For a folder-capable Work/Codex session, select the local repository as the project folder and provide access to the private context location. Verify access by having the agent list the input index. Local project behavior is described in [Projects and chats](https://learn.chatgpt.com/docs/projects). This repository does not depend on a globally installed `$job-application-campaign` skill; its instructions are self-contained.

## Claude Desktop

Create a project, upload the shared instructions and relevant files to its knowledge, and start the initialization conversation there. See [Claude projects](https://support.claude.com/en/articles/9517075-what-are-projects). If your available desktop mode supports working in a local folder, select this repository and verify which local tools it can use. See [Claude Cowork projects](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork). Do not assume a chat project can run the computer's LaTeX installation.

## Reliable upload/download fallback for either client

1. Attach `AGENTS.md`, the current stage guide, the private context files, and required source documents. If `.tex` is unsupported, attach a UTF-8 `.txt` copy labeled with the intended `.tex` filename.
2. Ask the assistant to enumerate the files it can actually read. If attachments are too large, supply the input index and work through complete sources in batches, recording review status.
3. Have it return named files for download. Save them to the paths specified by the guide. A chat reply saying something was saved is insufficient: verify the actual files exist.
4. If live browsing is unavailable, supply exact official postings and their dates as research inputs. Mark active status unverified until someone checks the live page; do not call the discovery stage complete.
5. Download generated TeX, run the local rendering helper, then upload its JSON summary, logs, and full-page previews. Have the assistant inspect every preview; if it cannot view images, the user performs and records this check.
6. At the end, download the updated context/handoff and replace stale project attachments with current versions. Do not depend on conversational memory to retain edits.

## First-session folder preparation

Create `private/context`, `private/sources`, `private/templates`, and `private/history`. Copy the Markdown templates into `private/context` (renaming `profile.template.md` to `profile.md`, and `search-preferences.template.md` to `search-preferences.md`). Copy the two LaTeX templates into `private/templates`. Let the initialization conversation fill them. Leave originals under `templates/` generic.

After setup, keep `SESSION_CONTEXT.md` small enough to attach in every new session. It points to detailed evidence and files; it does not replace reading the evidence used for a claim.

Documentation links checked 2026-11-24. UI labels may change; the upload/download path is the baseline workflow.
