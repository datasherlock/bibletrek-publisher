# Bible Trek Publisher — Global Sync & Publishing Guardrails

1. **Automatic GitHub Sync (`datasherlock/bibletrek-publisher`):**
   - This plugin directory (`~/.gemini/config/plugins/bibletrek`) is a live Git repository synced to `https://github.com/datasherlock/bibletrek-publisher.git`.
   - Whenever you create, edit, or update any file inside this plugin (`SKILL.md`, `references/*`, `scripts/*`, `rules/AGENTS.md`, `plugin.json`, or `README.md`), you **MUST** immediately commit and push the changes to `origin main` (or run `skills/bibletrek-publisher/scripts/sync_to_github.sh "<commit message>"`) in the same task so `github.com/datasherlock/bibletrek-publisher` is always 100% up to date across machines and agents.
   - Before modifying files in this plugin during a new session, run `git -C ~/.gemini/config/plugins/bibletrek pull --ff-only` (ignoring errors if offline) so you start from the latest remote state.

2. **Mandatory Skill Activation for `bibletrek4kids.com`:**
   - Whenever the user asks to create, publish, update, style, or audit any **Series Hub**, **Workshop**, **Craftivity**, **Object Lesson**, **Sunday School Game**, or **Page** on `bibletrek4kids.com`, ALWAYS read and follow `skills/bibletrek-publisher/SKILL.md` and the matching template in `skills/bibletrek-publisher/references/` before generating HTML or calling WordPress tools.
