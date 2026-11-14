# Bible Trek Publisher (`bibletrek-publisher`)

Official, cross-platform AI agent plugin & skill bundle for publishing **Bible Workshop Series**, **Interactive Workshops**, **Printable Craftivities**, **Object Lessons**, and **Sunday School Games** to **[bibletrek4kids.com](https://bibletrek4kids.com)** with 100% consistent branding, `wpautop`-proof Avada layouts, Yoast SEO metadata, and automatic hub cross-linking.

---

## What's Inside

```text
bibletrek-publisher/
├── plugin.json                                     # Antigravity Plugin manifest
├── assets/logo.svg                                 # Plugin icon
├── rules/AGENTS.md                                 # Always-on rule: auto-syncs skill updates back to GitHub
└── skills/
    └── bibletrek-publisher/
        ├── SKILL.md                                # Core design tokens, 5 Golden Rules & content router
        ├── references/
        │   ├── workshop-and-series.md              # 3-tab mobile-first Workshop + Series Hub + Homepage sync
        │   ├── craftivity-guide.md                 # 600–800w Craftivity Guide (.bt-cf-*) + Craftivity/Hindi hub sync
        │   ├── object-lesson-and-game.md           # Object Lesson & Sunday School Game templates + hub sync
        │   └── seo-and-site-registry.md            # Yoast SEO formulas & complete Page/Category/Tag ID registry
        └── scripts/
            ├── extract_pdf_assets.py               # Cross-OS (Linux + macOS) PDF verbatim text & PNG extractor
            ├── minify_wpautop.py                   # Validates & minifies HTML (blocks ghost-grid <a> bugs)
            └── sync_to_github.sh                   # One-command commit + rebase + push to datasherlock/bibletrek-publisher
```

---

## 1-Command Setup on Any Machine or Agent

### 1. Google Antigravity (Recommended — Global Plugin across all workspaces & sessions)
```bash
git clone https://github.com/datasherlock/bibletrek-publisher.git ~/.gemini/config/plugins/bibletrek
```
*(Loads automatically across every session—includes both the `bibletrek-publisher` skill and the always-on `rules/AGENTS.md` rule that keeps this GitHub repo synced whenever you refine the skill!)*

### 2. Workspace-Local (Antigravity, Cursor, Codex, Gemini CLI)
Inside any project workspace directory:
```bash
mkdir -p .agents/skills
git clone https://github.com/datasherlock/bibletrek-publisher.git .agents/bibletrek-repo
ln -s ../bibletrek-repo/skills/bibletrek-publisher .agents/skills/bibletrek-publisher
```

### 3. Claude Code (Global Skill)
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/datasherlock/bibletrek-publisher.git ~/.claude/bibletrek-repo
ln -s ../bibletrek-repo/skills/bibletrek-publisher ~/.claude/skills/bibletrek-publisher
```

---

## Everyday Usage Prompts

Once installed (with WordPress and Google Drive connected), just drop your raw material in chat:

* **New Workshop:** *"Publish this new Workshop to the [Series Name] series from Google Drive: `<folder-link>`"*
* **New Series:** *"Create a new Bible Trek Series called `[Title]` using this Google Drive folder `<folder-link>` and add it to the Homepage and Workshops page."*
* **New Craftivity:** *"Publish this new Printable Craftivity from `<drive-pdf-link>` (here are photos from Sunday school: `...`)."*
* **New Object Lesson / Game:** *"Publish this new Object Lesson / Sunday School Game: `[notes or doc link]`."*
