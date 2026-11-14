# Reference: Bible Workshops & Series Hub Pages

Use this guide whenever publishing a **new Workshop** (`Post`, Category `28`) or launching a **new Workshop Series** (`Page` + Homepage & Workshops Hub card updates).

---

## 1. Workshop Architecture (`Post`, Category `28`)

### Non-Negotiable Content Rule
* **100% Verbatim PDF Fidelity:** Extract every word from `Teacher's Guide` (Beginners & Primary), `Presentation Deck`, `Pick & Stick`, `Craftivity`, and `Activity Sheet` using `scripts/extract_pdf_assets.py`. Never omit, summarize, or paraphrase any story paragraph, discussion question, verse, prayer, or supply item.
* **Post Settings:**
  * `categories`: `[28]` (`Workshop`)
  * `comment_status`: `"open"`
  * `featured_media`: Upload/assign the Workshop's official cover artwork attachment ID (required for post archives and social cards).

### 4-Part Layout Inside `[fusion_builder_container]...[fusion_builder_column]`
1. **Part 1 — Expedition Trailhead Hero (`.bt-hero` inside `[fusion_text]`):**
   * Top breadcrumb pill (`← Back to [Series Name] Series` linking to the Series Hub URL + `Series Name • Workshop`).
   * Workshop `<h1>` title, subtitle, and cover illustration (`<img>` with descriptive `alt`, `width`, `height`).
   * Quick-glance Trail Stats Bar (`Beginners 4–6 & Primary 7–15`, `60 Mins`, Core Theme, `Free Printables` — include `(ENG | HIN)` badge if Hindi Teacher's Guides exist in the Drive folder!).
   * Secondary link button: `Open Full Google Drive Workshop Folder ↗`.

2. **Part 2 — Mobile-First Top Track Switcher (`[fusion_tabs class="bt-tabs" mobile_mode="tabs"]`):**
   * Signpost prompt above tabs: `🧭 CHOOSE YOUR TREK TRAIL:`
   * **3 Tabs:**
     * Tab 1: `🌱 Beginners (4–6 Yrs)`
     * Tab 2: `🎯 Primary (7–15 Yrs)`
     * Tab 3: `📥 Printables & Slides`
   * **CRITICAL MOBILE CSS OVERRIDE:** Avada's default mobile accordion hides `.nav` at `<=640px` and pushes Primary below Beginners. Always include this CSS so all 3 track buttons remain side-by-side at the top on mobile, tablet, and desktop:
     ```css
     .bt-workshop br:not(.bt-br),.bt-workshop p:empty{display:none!important}
     .fusion-tabs.bt-tabs .nav{display:block!important;width:100%!important}
     .fusion-tabs.bt-tabs .fusion-mobile-tab-nav{display:none!important}
     .fusion-tabs.bt-tabs .nav-tabs{display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;gap:10px!important;justify-content:center!important;background:#3b220c!important;padding:10px!important;border-radius:20px!important;border:3px solid #6d3c00!important;box-shadow:0 10px 24px rgba(59,34,12,0.22)!important;margin-bottom:28px!important;list-style:none!important}
     .fusion-tabs.bt-tabs .nav-tabs>li{flex:1 1 0!important;float:none!important;margin:0!important;border:none!important}
     .fusion-tabs.bt-tabs .nav-tabs>li>a.tab-link{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;padding:14px 10px!important;border-radius:14px!important;background:rgba(255,255,255,0.08)!important;color:#f7ede2!important;font-family:'KoHo','Work Sans',sans-serif!important;font-weight:700!important;font-size:16px!important;line-height:1.25!important;border:2px solid transparent!important;text-decoration:none!important;min-height:64px!important}
     .fusion-tabs.bt-tabs .nav-tabs>li.active>a.tab-link{background:linear-gradient(135deg,#86ba1f 0%,#427200 100%)!important;color:#ffffff!important;border-color:#f9f900!important;box-shadow:0 6px 16px rgba(66,114,0,0.45)!important}
     @media(max-width:640px){.fusion-tabs.bt-tabs .nav-tabs{gap:6px!important;padding:7px!important;border-radius:16px!important}.fusion-tabs.bt-tabs .nav-tabs>li>a.tab-link{padding:10px 6px!important;font-size:13px!important;min-height:58px!important;border-radius:11px!important}}
     ```

3. **Part 3 — Age-Track Lesson Trail (Inside Tab 1 & Tab 2):**
   * **Trail Overview Dashboard:** Lesson Title, Theme, Goal (`blobid2.png`), Memory Verse (`blobid3.png`), Key Scriptures (`bible-icon.png`), Duration (`blobid4.png`), 60-minute visual time breakdown bar, and track-specific PDF quick-download buttons.
   * **Numbered Trail Stops (`TRAIL STOP 1` – `TRAIL STOP 6`):**
     1. *Worship Time* (duration badge, song suggestions, teacher guidance)
     2. *Story Time & Presentation Deck* (Opening Question, Object Lesson / Opening Story, verbatim Bible Story paired side-by-side with rendered Slide PNGs uploaded to WordPress Media, Discussion Questions)
     3. *Memory Verse & Activity* (Highlighted verse banner + verbatim Pick & Stick chits / memory game)
     4. *Craftivity* (Supplies checklist + verbatim step-by-step instructions + template preview PNG)
     5. *Prayer Time* (Guided teacher/student prayer card)
     6. *Lesson Summary & Takeaway* (Summary table/cards + Activity Sheet preview PNG)

4. **Part 4 — Printable Resource Hub (Inside Tab 3):**
   * Clean grid separated into **Beginners Printables** and **Primary Printables** (plus **Hindi `HIN` Teacher's Guides** clearly badged when present in the Google Drive folder) with direct `View / Download PDF ↗` links.

---

## 2. Launching or Updating a Series Hub Page (`Page`)

### When Adding a Workshop to an Existing Series
1. Fetch the parent Series Hub Page (`wpcom-mcp/pages-get`, see ID table in `seo-and-site-registry.md`).
2. Add or update the Workshop card so its button links directly to the new WordPress post permalink (`https://bibletrek4kids.com/<slug>/` — **never** leave Series Hub cards pointing only to raw Google Drive folders once the interactive WordPress workshop post is live!).
3. If the new Workshop includes Hindi (`HIN`) Teacher's Guides in its Drive folder, also append a bilingual card to `/hindi-bible-crafts-for-kids/` (`ID 4490`) inside `.bt-hi-grid2`!

### When Creating a Brand-New Series Hub Page
1. **Create the Series Page** (`wpcom-mcp/pages-create`, `status: "publish"`, `featured_media: 0`):
   * Include `.avada-page-titlebar-wrapper{display:none!important}` in `<style>`.
   * Include a semantic `<h1>` in the Series hero banner, Series overview description, and `wpautop`-proof stretched-link cards (`<div class="...">` + `<h3><a class="...-stretch">`) for each Workshop in the series.
2. **Add the New Series Card to `/workshops/` (`ID 3324`):**
   * Fetch Page `3324`, add the new Series cover banner (`1024×379` full-res URL, never `300×111` thumbnail!) and description linking to the new Series Page URL.
3. **Add the New Series Card to Homepage `/` (`ID 2038`):**
   * Fetch Page `2038`, locate `<div class="bt-hm-grid4">` inside the Series panel, and append a `wpautop`-proof card:
     ```html
     <div class="bt-hm-card"><div class="bt-hm-thumb"><img src="SERIES_BANNER_URL" alt="SERIES_ALT" width="1024" height="379" loading="lazy" /></div><div class="bt-hm-body"><div class="bt-hm-tag">SERIES_THEME_TAG</div><h3 class="bt-hm-h3"><a class="bt-hm-stretch" href="https://bibletrek4kids.com/SERIES_SLUG/">SERIES_TITLE</a></h3><p class="bt-hm-p">SERIES_DESCRIPTION</p><div class="bt-hm-cta">Explore Series &#8594;</div></div></div>
     ```
   * **Remember Evergreen Rule:** Never add `"9 Bible Workshop Series"` or `"X Workshops"` badges!
