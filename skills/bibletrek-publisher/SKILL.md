---
name: bibletrek-publisher
description: >-
  Official end-to-end publishing system for bibletrek4kids.com. Transforms Google Drive folders, PDFs, docs, notes, and photos into mobile-first, wpautop-proof, Yoast-SEO-optimized WordPress pages and posts using the Bible Trek outdoor-adventure brand palette and Avada Fusion Builder layout. Use whenever creating, publishing, updating, or auditing a Bible Workshop, Workshop Series Hub, Printable Craftivity, Object Lesson, Sunday School Game, or Landing Page on bibletrek4kids.com.
---

# Bible Trek Publisher (`bibletrek4kids.com`)

This is the single authoritative publishing skill for **Bible Trek 4 Kids** (`https://bibletrek4kids.com`, WordPress/Jetpack site `bibletrek4kids.com`). Follow these rules on **every** publish or update across any session, agent, or machine to guarantee 100% consistent branding, layout, SEO, and navigation sync.

---

## 1. Route by Content Type (Progressive Disclosure)

Before building HTML, read `references/seo-and-site-registry.md` AND the specific reference file for what you are publishing:

| What the User Gives You | Read This Reference First | WordPress Type & Taxonomy | Hub Pages You Must Also Update |
| :--- | :--- | :--- | :--- |
| **New Workshop** (Google Drive folder with Teacher's Guides, Slide Decks, Craftivities, Activity Sheets) | [workshop-and-series.md](./references/workshop-and-series.md) | **Post** • Category `28` (`Workshop`) | Parent Series Hub Page (+ `/hindi-bible-crafts-for-kids/` `ID 4490` if bilingual `ENG \| HIN`) |
| **New Workshop Series** (Multiple workshops or new Series launch) | [workshop-and-series.md](./references/workshop-and-series.md) | **Page** (Series Hub) + **Posts** (`Cat 28`) | `/workshops/` (`ID 3324`) **AND** Homepage `/` (`ID 2038` `.bt-hm-grid4`) |
| **New Printable Craftivity** (PDF link + optional church kid photos / YouTube video / slider) | [craftivity-guide.md](./references/craftivity-guide.md) | **Post** • Category `31` (`Craftivity`), Tag `30` (`craftivity`) | `/craftivity/` (`ID 2743`) (+ `/hindi-bible-crafts-for-kids/` `ID 4490` if bilingual/Scripture-flexible) |
| **New Object Lesson** (Notes/doc + demonstration photo/prop) | [object-lesson-and-game.md](./references/object-lesson-and-game.md) | **Post** • Category `33` (`Object Lessons`), Tag `32` (`object lesson`) | `/object-lessons/` (`ID 3049`) |
| **New Sunday School Game** (Rules + objective + diagram/photo) | [object-lesson-and-game.md](./references/object-lesson-and-game.md) | **Post** • Category `34` (`Games`), Tag `36` (`games`) | `/games/` (`ID 3056`) |

Always check [seo-and-site-registry.md](./references/seo-and-site-registry.md) for exact Page IDs, Category/Tag IDs, Yoast SEO formulas, and Avada Page vs. Post `featured_media` rules.

---

## 2. Five Non-Negotiable Golden Rules

### Rule 1: Evergreen Copy Everywhere (Never Hardcode Counts)
* Bible Trek continuously publishes new series, workshops, crafts, object lessons, and games.
* **NEVER** write total site counts like `"8 Bible Workshop Series"`, `"75+ Workshops"`, or `"16 Craftivities"` on the Homepage (`/`), `/start/`, `/workshops/`, or hub headers. Use evergreen phrasing (*"Explore Our Bible Workshop Series"*, *"with new lessons added regularly"*).

### Rule 2: 100% `wpautop`-Proof HTML & Stretched-Link Cards
WordPress's `wpautop` filter runs inside `[fusion_text]` and `[fusion_tab]`:
1. **NEVER wrap block elements (`<div>`, `<h1>`–`<h6>`, `<p>`, `<ul>`) inside an inline `<a>` or `<span>` tag.** WordPress `wpautop` closes inline tags early around block elements, splitting cards into alternating empty "ghost" grid cells!
   * **Mandatory Card Pattern:** Make every clickable card a `<div class="...-card" style="position:relative">`, put the `<a>` strictly inside the heading (`<h3><a class="...-stretch" href="...">Title</a></h3>`), and style `.bt-*-stretch::after { content:""; position:absolute; inset:0; z-index:2; cursor:pointer; }`.
2. **NEVER mix raw inline tags (`<a>`, `<span>`, `<img>`, `<svg>`) as direct siblings of block tags (`<div>`, `<h2>`, `<p>`)** inside flex/grid headers—always wrap sibling buttons, eyebrows, or icons in a `<div>`.
3. **Minify all HTML into a single line** and place the `<style>` block **at the very end** of `[fusion_text]` (never at the top, so social/Pinterest/snippet scrapers never ingest raw CSS). Run [minify_wpautop.py](./scripts/minify_wpautop.py) to minify and validate every payload before publishing.
4. **Always include the anti-`wpautop` CSS guard** inside your scoped wrapper:
   ```css
   .bt-wrap br:not(.bt-br), .bt-wrap p:empty { display: none !important; }
   ```
   Use `<br class="bt-br" />` when an intentional line break is required.

### Rule 3: Content Fidelity & Depth
* **Workshops:** Preserve **100% verbatim text fidelity** from the family's source PDFs (`Teacher's Guide`, `Presentation Deck`, `Pick & Stick`, `Craftivity`, `Activity Sheet`). Never summarize, paraphrase, or omit teacher scripts, verses, chits, or supply items—structure and beautify them into Trail Stops.
* **Craftivities:** Expand PDF printables into complete **600–800-word Sunday School Craftivity Guides** (Memory Verse, Supplies + Download Box, Teacher Story Intro, Step-by-Step Cards, Church Kids Gallery if provided, Table-Talk Questions, and Related Workshop Banner).
* **Object Lessons & Games:** Preserve the family's authentic, warm conversational voice (`"Begin by saying..."`) while structuring Objective, Supplies, Setup/How to Play, Visual Illustration, and Scripture Application cleanly.

### Rule 4: Avada Page vs. Post Image & Titlebar Quirks
* **On Posts** (`Workshop`, `Craftivity`, `Object Lesson`, `Game`): **ALWAYS set `featured_media`** to the cover artwork attachment ID and set `"comment_status": "open"`.
* **On Avada Pages** (`Series Hubs`, `Resource Hubs`, `Landing Pages`): Set **`featured_media: 0`** (otherwise Avada injects a huge duplicate `.post-slideshow` image above your hero!) and include `.avada-page-titlebar-wrapper{display:none!important}` in `<style>` so Avada's default titlebar banner never duplicates your `<h1>`. Yoast SEO automatically pulls `og:image` from the first `<img>` inside the Page content.

### Rule 5: Complete Yoast SEO Metadata on Every Publish
Every single Post and Page must be published with:
* Clean URL `slug` (concise, lowercase, keyword-focused)
* `excerpt` (140–165 chars plain text—no HTML or shortcodes)
* Yoast `meta` fields (on Posts via `wpcom-mcp/posts-create` / `posts-update`):
  * `_yoast_wpseo_title` (`50–60 chars`, ending with `| Bible Trek`)
  * `_yoast_wpseo_metadesc` (`135–158 chars`, actionable summary mentioning free printables/ages)
  * `_yoast_wpseo_focuskw` (natural search phrase teachers/parents type into Google)
* Descriptive `alt` attributes on **every** `<img>` tag (`width`, `height`, and `loading="lazy"` on below-the-fold images).

---

## 3. Official Bible Trek Brand Palette & Typography

| Role | Hex | Usage |
| :--- | :--- | :--- |
| **Trek Forest Green** | `#427200` | Primary buttons, active tab gradient end, trail checkpoints, links |
| **Trail Lime Green** | `#86ba1f` | Beginners (4–6 yrs) accent, active tab gradient start, card hover borders |
| **Campfire Terracotta** | `#c45b19` | Primary (7–15 yrs) accent, eyebrows/kickers, Object Lesson & discussion accents |
| **Timber Wood Brown** | `#6d3c00` | Signpost borders (`2px–3px solid`), wooden trail framing |
| **Deep Espresso Bark** | `#3b220c` | Hero banner gradient start, top track switcher bar, dark headings (`#2b1d0e`) |
| **Warm Parchment Sand** | `#fbf6ef` / `#e7ccb6` | Subtle card surfaces, step boxes, soft borders |
| **Sunshine Compass Gold** | `#f9a513` / `#ffd57e` | Memory verse left border, hero pill text, active highlights |
| **Trek Sky Blue** | `#0284c7` / `#e0f2fe` | Prayer boxes, devotional/printable accents |

* **Typography:** Headings/Badges: `'KoHo', 'Work Sans', sans-serif` (`700`/`800`). Body copy: `'ABeeZee', 'Work Sans', sans-serif` (`16px`, `line-height: 1.7`, `#2b1d0e`).
* **Hosted Brand Icons (`bibletrek4kids.com`):**
  * Hike Flag: `https://bibletrek4kids.com/wp-content/uploads/2022/07/hike-flag-300x300.webp`
  * Bible Icon: `https://bibletrek4kids.com/wp-content/uploads/2024/12/bible-icon.png`
  * Goal Target Icon: `https://bibletrek4kids.com/wp-content/uploads/2024/12/blobid2.png`
  * Memory Verse Scroll: `https://bibletrek4kids.com/wp-content/uploads/2024/12/blobid3.png`
  * Duration Clock: `https://bibletrek4kids.com/wp-content/uploads/2024/12/blobid4.png`

---

## 4. Standard Publishing & Verification Workflow

1. **Ingest Source Assets:**
   * If given a Google Drive folder/file URL, use the `gdrive` CLI to list and download PDFs/images into a scratch folder.
   * Run `python3 scripts/extract_pdf_assets.py <pdf_or_dir> <output_dir>` (works on both **Linux** and **macOS**) to extract 100% verbatim PDF text and high-res PNG slide/printable previews.
2. **Upload Media to WordPress:**
   * Upload cover artwork and slide/printable preview PNGs via `wordpress_mcp` (`wpcom-mcp/media-upload`), recording each `id` and `source_url`.
3. **Build & Validate Payload:**
   * Construct the Avada `[fusion_builder_container]...[fusion_text]...[/fusion_text]...` HTML using the exact template in `references/`.
   * Run `python3 scripts/minify_wpautop.py <payload_file>` to minify into a single line and verify zero illegal `<a>`-wrapped blocks or unclosed tags.
4. **Publish & Cross-Link:**
   * Create/update the WordPress Post or Page via `wordpress_mcp` (`wpcom_site: "bibletrek4kids.com"`).
   * Update the corresponding parent Hub Page(s) (Series Hub, `/workshops/`, Homepage `/`, `/craftivity/`, `/object-lessons/`, `/games/`, and `/hindi-bible-crafts-for-kids/` if bilingual) so the new item is immediately discoverable—never orphaned!
5. **Live HTTP & DOM Verification:**
   * Fetch the live URL (`curl` or Python `urllib`) and verify: HTTP `200`, `<title>` & `<meta name="description">` populated, `og:image` valid, `0` empty `<p></p>` tags, `0` `<br>` tags inside buttons/pills, and always return both the **View Live URL** and **WP-Admin Edit link** (`https://bibletrek4kids.com/wp-admin/post.php?post={id}&action=edit`) to the user.
6. **Keep Skill Synced with GitHub:**
   * Whenever you refine or add anything to this skill/plugin, run `bash scripts/sync_to_github.sh "Describe update"` so `https://github.com/datasherlock/bibletrek-publisher` stays in sync.
