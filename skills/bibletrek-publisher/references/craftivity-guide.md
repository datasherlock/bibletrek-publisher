# Reference: Printable Craftivity Guides (`.bt-cf-*`)

Use this guide whenever publishing or updating a **Printable Craftivity** (`Post`, Category `31`, Tag `30`).

---

## 1. Taxonomy, Media & Word Count Standards

* **WordPress Post Settings:**
  * `categories`: `[31]` (`Craftivity`)
  * `tags`: `[30]` (`craftivity`)
  * `comment_status`: `"open"`
  * `featured_media`: Upload/assign the finished craft photo or Craftivity cover graphic attachment ID.
* **Depth Target (`600–800 words`):** Never publish a thin ~120-word wrapper around a PDF button—Google will treat it as thin content. Expand every Craftivity into a complete, practical Sunday school guide while keeping **100% of any user-provided photos (`[fusion_images]`), YouTube videos (`[fusion_youtube]`), before/after sliders (`[fusion_image_before_after]`), and English/Hindi Google Drive PDF buttons**.

---

## 2. Standard Craftivity HTML & Scoped CSS Template

Wrap inside `[fusion_builder_container ...][fusion_builder_row][fusion_builder_column ...][fusion_text ...]` with **minified single-line HTML** and **place `<style>` at the very end of `[fusion_text]`** (so Pinterest/social scrapers never pull raw CSS into snippets):

### HTML Skeleton (Minify via `scripts/minify_wpautop.py` Before Publishing)
```html
<div class="bt-cf-wrap">
  <div class="bt-cf-topbar">
    <a class="bt-cf-back" href="https://bibletrek4kids.com/craftivity/">&#8592; All Bible Craftivities</a>
    <a class="bt-cf-back" href="RELATED_WORKSHOP_OR_SERIES_URL">&#129517; Related Workshop: RELATED_TITLE &#8594;</a>
  </div>
  <div class="bt-cf-hero">
    <span class="bt-cf-pill">EYEBROW_SCRIPTURE_AND_TOPIC</span>
    <h1 class="bt-cf-h1">CRAFTIVITY_H1_TITLE</h1>
    <p class="bt-cf-obj"><strong>Objective:</strong> CLEAR_ONE_SENTENCE_OBJECTIVE</p>
    <div class="bt-cf-meta">
      <span class="bt-cf-mpill">&#127919; <strong>Theme:</strong> THEME_NAME</span>
      <span class="bt-cf-mpill">&#9201;&#65039; <strong>Time:</strong> 20–25 Minutes</span>
      <span class="bt-cf-mpill">&#128103; <strong>Ages:</strong> 4–12 Years</span>
      <span class="bt-cf-mpill">&#128214; <strong>Scripture:</strong> SCRIPTURE_REF</span>
    </div>
  </div>
  <div class="bt-cf-verse">
    <span class="bt-cf-vlbl">&#128220; Key Memory Verse &amp; Scripture Truth</span>
    <p class="bt-cf-vq">&ldquo;FULL_MEMORY_VERSE_TEXT&rdquo; — SCRIPTURE_REF</p>
    <p class="bt-cf-vnote">KID_FRIENDLY_ONE_LINE_EXPLANATION</p>
  </div>
  <div class="bt-cf-grid2">
    <div class="bt-cf-card-in">
      <h3 class="bt-cf-h3">&#128230; What You Will Need</h3>
      <ul class="bt-cf-ul">
        <li>Printable template (or A4/cardstock paper)</li>
        <li>Child-safe scissors, glue stick &amp; crayons/markers</li>
      </ul>
      <div class="bt-cf-dlbox">
        <div style="font-weight:700;color:#3f6212;font-size:14.5px;margin-bottom:10px;">100% Free Printable PDF Template</div>
        <a class="bt-cf-dlbtn" href="GOOGLE_DRIVE_PDF_OR_FOLDER_URL" target="_blank" rel="noopener">&#128229; Download Free Craftivity PDF</a>
      </div>
    </div>
    <div class="bt-cf-card-in" style="border-top-color:#c45b19;">
      <h3 class="bt-cf-h3" style="color:#c45b19!important;">&#128161; Prep Tips for Teachers &amp; Parents</h3>
      <ul class="bt-cf-ul">
        <li><strong>Beginners (Ages 4–6):</strong> Pre-cut intricate shapes before class so little hands focus on coloring, folding, and retelling the verse.</li>
        <li><strong>Primary (Ages 7–12):</strong> Let older kids cut, assemble, look up the passage in their Bibles, and write a personal takeaway on the back.</li>
      </ul>
    </div>
  </div>
  <div class="bt-cf-card">
    <h2 class="bt-cf-h2">&#128214; Teacher Introduction &amp; Bible Story Connection</h2>
    <p class="bt-cf-p">WARM_STORY_AND_GOSPEL_CONNECTION_PARAGRAPH_1</p>
    <p class="bt-cf-p">WARM_STORY_AND_GOSPEL_CONNECTION_PARAGRAPH_2</p>
  </div>
  <div class="bt-cf-card">
    <h2 class="bt-cf-h2">&#9986;&#65039; Step-by-Step Activity Instructions</h2>
    <p class="bt-cf-p">Follow these simple steps together with your class or family:</p>
    <div class="bt-cf-steps">
      <div class="bt-cf-step"><span class="bt-cf-snum">1</span><h4 class="bt-cf-sh4">STEP_1_TITLE</h4><p class="bt-cf-sp">STEP_1_DESC</p></div>
      <div class="bt-cf-step"><span class="bt-cf-snum">2</span><h4 class="bt-cf-sh4">STEP_2_TITLE</h4><p class="bt-cf-sp">STEP_2_DESC</p></div>
      <div class="bt-cf-step"><span class="bt-cf-snum">3</span><h4 class="bt-cf-sh4">STEP_3_TITLE</h4><p class="bt-cf-sp">STEP_3_DESC</p></div>
      <div class="bt-cf-step"><span class="bt-cf-snum">4</span><h4 class="bt-cf-sh4">STEP_4_TITLE</h4><p class="bt-cf-sp">STEP_4_DESC</p></div>
    </div>
    <!-- Optional preview image, [fusion_youtube], or [fusion_image_before_after] goes here -->
  </div>
  <!-- Optional Church Kids [fusion_images] carousel card goes here -->
  <div class="bt-cf-qbox">
    <h2 class="bt-cf-h2">&#128172; Table-Talk &amp; Reflection Questions</h2>
    <p class="bt-cf-p">Ask these conversation starters while children work on their craft or share their finished creations:</p>
    <div class="bt-cf-qitem"><strong style="color:#3b220c;">1. QUESTION_1</strong></div>
    <div class="bt-cf-qitem"><strong style="color:#3b220c;">2. QUESTION_2</strong></div>
    <div class="bt-cf-qitem"><strong style="color:#3b220c;">3. QUESTION_3</strong></div>
  </div>
  <div class="bt-cf-rel">
    <div style="flex:1 1 320px;">
      <div style="font-family:'KoHo',sans-serif;font-weight:800;font-size:13px;text-transform:uppercase;letter-spacing:1px;color:#ffd57e;margin-bottom:4px;">Teach A Complete 60-Minute Sunday School Lesson</div>
      <div style="font-family:'KoHo',sans-serif;font-weight:800;font-size:21px;color:#ffffff;margin-bottom:4px;">RELATED_CALLOUT_HEADING</div>
      <div style="font-size:14.5px;color:#f5e9dc;">RELATED_CALLOUT_DESCRIPTION</div>
    </div>
    <a class="bt-cf-relbtn" href="RELATED_WORKSHOP_OR_SERIES_URL">Explore RELATED_TITLE &#8594;</a>
  </div>
</div>
```

### Scoped Craftivity CSS (Append Right Before `[/fusion_text]`)
```html
<style>.bt-cf-wrap br:not(.bt-br),.bt-cf-wrap p:empty{display:none!important}.bt-cf-wrap{max-width:980px;margin:0 auto;font-family:'ABeeZee','Work Sans',sans-serif;color:#2b1d0e;line-height:1.7;font-size:16px}.bt-cf-topbar{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:10px;margin-bottom:16px}.bt-cf-back{display:inline-flex;align-items:center;gap:6px;background:#fbf6ef;border:1.5px solid #dcc0a1;color:#481f01!important;text-decoration:none!important;font-family:'KoHo','Work Sans',sans-serif;font-weight:700;font-size:14px;padding:7px 15px;border-radius:999px}.bt-cf-back:hover{background:#427200;border-color:#427200;color:#ffffff!important}.bt-cf-hero{background:linear-gradient(135deg,#3b220c 0%,#427200 100%);border:3px solid #6d3c00;border-radius:20px;padding:34px 26px;text-align:center;color:#ffffff;box-shadow:0 10px 26px rgba(59,34,12,0.18);margin-bottom:26px}.bt-cf-pill{display:inline-block;background:rgba(249,165,19,0.22);border:1px solid rgba(249,165,19,0.65);color:#ffe08a;text-transform:uppercase;font-family:'KoHo','Work Sans',sans-serif;font-size:12.5px;font-weight:800;letter-spacing:1.2px;padding:5px 16px;border-radius:999px;margin-bottom:12px}.bt-cf-h1{font-family:'KoHo','Work Sans',sans-serif!important;font-weight:800!important;font-size:clamp(26px,3.5vw,38px)!important;line-height:1.2!important;color:#ffffff!important;margin:0 0 12px!important}.bt-cf-obj{font-size:17px;max-width:740px;margin:0 auto!important;color:#f5f9ee;line-height:1.6}.bt-cf-meta{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:20px}.bt-cf-mpill{background:rgba(0,0,0,0.24);border:1px solid rgba(255,255,255,0.18);padding:7px 14px;border-radius:10px;font-size:13.5px;color:#ffffff}.bt-cf-verse{background:#fbf6ef;border:2px solid #e7ccb6;border-left:6px solid #f9a513;border-radius:16px;padding:20px 22px;margin-bottom:26px;box-shadow:0 4px 14px rgba(59,34,12,0.05)}.bt-cf-vlbl{font-family:'KoHo','Work Sans',sans-serif;font-weight:800;font-size:14px;text-transform:uppercase;letter-spacing:0.8px;color:#b45309;margin-bottom:6px;display:block}.bt-cf-vq{font-size:17px;font-style:italic;font-weight:700;color:#3b220c;margin:0 0 6px!important}.bt-cf-vnote{font-size:14.5px;color:#5c4028;margin:0!important}.bt-cf-grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px;margin-bottom:26px}.bt-cf-card{background:#ffffff;border:1.5px solid #e7ccb6;border-radius:16px;padding:24px;margin-bottom:26px;box-shadow:0 4px 16px rgba(59,34,12,0.05)}.bt-cf-card-in{background:#ffffff;border:1.5px solid #e7ccb6;border-top:5px solid #427200;border-radius:16px;padding:22px;box-shadow:0 4px 16px rgba(59,34,12,0.05)}.bt-cf-h2{font-family:'KoHo','Work Sans',sans-serif!important;font-weight:800!important;font-size:23px!important;line-height:1.28!important;color:#3b220c!important;margin:0 0 14px!important;border-bottom:2px solid #86ba1f;padding-bottom:6px;display:inline-block}.bt-cf-h3{font-family:'KoHo','Work Sans',sans-serif!important;font-weight:800!important;font-size:19px!important;color:#427200!important;margin:0 0 12px!important}.bt-cf-ul{margin:0 0 14px!important;padding-left:20px;color:#2b1d0e}.bt-cf-ul li{margin-bottom:7px;line-height:1.65}.bt-cf-dlbox{background:#f7fee7;border:2px dashed #86ba1f;border-radius:14px;padding:18px;text-align:center;margin-top:14px}.bt-cf-dlbtn{display:inline-block;background:linear-gradient(135deg,#86ba1f 0%,#427200 100%);color:#ffffff!important;text-decoration:none!important;font-family:'KoHo','Work Sans',sans-serif;font-weight:800;font-size:15.5px;padding:11px 24px;border-radius:999px;box-shadow:0 5px 14px rgba(66,114,0,0.3)}.bt-cf-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:16px}.bt-cf-step{background:#fbf6ef;border:1px solid #e7ccb6;border-radius:12px;padding:16px}.bt-cf-snum{width:30px;height:30px;background:#427200;color:#ffffff;font-family:'KoHo','Work Sans',sans-serif;font-weight:800;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;margin-bottom:8px;font-size:15px}.bt-cf-sh4{font-family:'KoHo','Work Sans',sans-serif!important;font-weight:800!important;font-size:16.5px!important;color:#3b220c!important;margin:0 0 6px!important}.bt-cf-sp{margin:0!important;font-size:14.5px;line-height:1.58;color:#4a3723}.bt-cf-p{margin:0 0 14px!important;color:#2b1d0e;line-height:1.72}.bt-cf-qbox{background:#fdfbf7;border:1.5px solid #ead7c3;border-radius:16px;padding:24px;margin-bottom:26px}.bt-cf-qitem{background:#ffffff;border-left:4px solid #c45b19;border-radius:10px;padding:13px 16px;margin-bottom:10px;box-shadow:0 2px 6px rgba(0,0,0,0.03)}.bt-cf-rel{background:linear-gradient(135deg,#3b220c 0%,#5a3210 100%);border:2px solid #f9a513;border-radius:18px;padding:22px 24px;color:#ffffff;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px}.bt-cf-relbtn{display:inline-block;background:#f9a513;color:#2b1d0e!important;text-decoration:none!important;font-family:'KoHo','Work Sans',sans-serif;font-weight:800;font-size:15px;padding:10px 22px;border-radius:999px}.bt-cf-imgwrap{text-align:center;margin:18px 0}.bt-cf-imgwrap img{max-width:100%;height:auto;border-radius:12px;border:2px solid #e7ccb6;box-shadow:0 6px 18px rgba(59,34,12,0.08)}.bt-cf-imgcap{display:block;font-size:13px;color:#6d3c00;margin-top:6px;font-style:italic}@media(max-width:600px){.bt-cf-hero{padding:24px 16px}.bt-cf-card,.bt-cf-qbox{padding:18px 15px}}</style>
```

---

## 3. Hub Page Sync After Publishing a Craftivity

1. **Update `/craftivity/` (`ID 2743`):**
   * Fetch Page `2743` (`wpcom-mcp/pages-get`), inspect its category tab/grid structure, and add the new Craftivity card (full-resolution image URL, title, objective, and direct link to `https://bibletrek4kids.com/<slug>/`).
2. **If Bilingual `(ENG | HIN)` or Language-Flexible:**
   * Also add a card to `/hindi-bible-crafts-for-kids/` (`ID 4490`) inside `.bt-hi-grid3` using `<div class="bt-hi-ccard">` + `<h3 class="bt-hi-ch3"><a class="bt-hi-stretch" href="...">`.
