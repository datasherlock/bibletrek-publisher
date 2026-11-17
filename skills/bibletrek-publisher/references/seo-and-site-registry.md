# Reference: Yoast SEO Formulas & `bibletrek4kids.com` Site Registry

Always check this registry for exact WordPress IDs, URLs, and Yoast SEO metadata formulas on `bibletrek4kids.com` (`wpcom_site: "bibletrek4kids.com"`, Jetpack `blog_id: 258558883`).

---

## 1. Yoast SEO Formulas (Required on 100% of Posts & Pages)

Teachers and Christian parents rarely search internal lesson titles alone (e.g., `"Puffed Up"` or `"The Big Reveal"`). Always engineer `_yoast_wpseo_title`, `_yoast_wpseo_metadesc`, `_yoast_wpseo_focuskw`, and `excerpt` around real search intent:

| Content Type | `_yoast_wpseo_title` Formula (`50–60 chars`) | `_yoast_wpseo_metadesc` & `excerpt` Formula (`135–158 chars`) |
| :--- | :--- | :--- |
| **Workshop (`Cat 28`)** | `[Topic/Bible Story] ([Verse]): Free Kids Bible Lesson & Craft \| Bible Trek` | `Teach kids [core truth] ([Scripture]) with this free 60-min Sunday school workshop for ages 4–15—includes Teacher's Guides, slides, games & printables.` *(mention English & Hindi if bilingual!)* |
| **Series Hub (`Page`)** | `[Series Name] — Free Kids Sunday School Curriculum Series \| Bible Trek` | `Explore our free [Series Name] Bible workshop series for kids (ages 4–15), complete with interactive stories, slide decks, memory verse games & printable crafts.` |
| **Craftivity (`Cat 31`)** | `[Craft Name] ([Verse]) Free Printable Bible Craft for Kids \| Bible Trek` | `Download our free [Craft Name] printable Bible craft ([Scripture]) for kids ages 4–12—with step-by-step instructions, supplies list & discussion prompts.` |
| **Object Lesson (`Cat 33`)** | `[Title]: [Topic] Bible Object Lesson for Kids ([Verse]) \| Bible Trek` | `Teach kids about [topic] ([Scripture]) in 5 minutes using [everyday object]! Free step-by-step Sunday school & family devotional object lesson.` |
| **Game (`Cat 34`)** | `[Title]: [Zero-Prep / Team] Sunday School Bible Game \| Bible Trek` | `Play [Title]—a fun, high-energy Sunday school Bible game teaching kids [lesson truth] ([Scripture]), with easy rules and discussion takeaways.` |

### Avada `featured_media` Rule (Critical!)
* **Posts (`Workshop`, `Craftivity`, `Object Lesson`, `Game`):** **ALWAYS** pass `"featured_media": <attachment_id>`. Category archives and `[fusion_blog]` grids require it.
* **Pages (`Series Hubs`, `Resource Hubs`, `Landing Pages`):** **ALWAYS** pass `"featured_media": 0` and include `.avada-page-titlebar-wrapper{display:none!important}` in `<style>`. On Pages, setting `featured_media > 0` causes Avada to inject an unwanted duplicate `.post-slideshow` banner above your hero, whereas Yoast SEO automatically sets `<meta property="og:image">` from the first `<img>` inside your Page content!

---

## 2. Official Taxonomies (Categories & Tags)

| Taxonomy | Name | Slug | ID |
| :--- | :--- | :--- | :--- |
| **Category** | Workshop | `workshop` | **`28`** |
| **Category** | Craftivity | `craftivity` | **`31`** |
| **Category** | Object Lessons | `object-lessons` | **`33`** |
| **Category** | Games | `games` | **`34`** |
| **Tag** | craftivity | `craftivity` | **`30`** |
| **Tag** | object lesson | `object-lesson` | **`32`** |
| **Tag** | games | `games` | **`36`** |

---

## 3. Core Hub & Landing Pages Registry

| Page Role | Page ID | Live URL | Notes |
| :--- | :--- | :--- | :--- |
| **Homepage** | **`2038`** | `https://bibletrek4kids.com/` | Keep Slider Container 1 intact (`margin_bottom_small="0px"`), and preserve `#SR7_20_1-40-0` CSS in Container 2 `<style>` (`PixarKatieClimbing.png`, Media ID `4512`). Series grid is `.bt-hm-grid4` inside Container 2. **100% evergreen—no counts!** |
| **Instagram Link-in-Bio Hub** | **`4489`** | `https://bibletrek4kids.com/start/` | Mobile-first GA4-tracked social landing page for `@bibletrek`. |
| **Hindi & English Hub** | **`4490`** | `https://bibletrek4kids.com/hindi-bible-crafts-for-kids/` | Update `.bt-hi-grid2` whenever a new bilingual `(ENG \| HIN)` Workshop is added; `.bt-hi-grid3` for crafts. |
| **Workshops Library** | **`3324`** | `https://bibletrek4kids.com/workshops/` | Master directory of all Workshop Series—add a Series card whenever launching a new Series. |
| **Craftivity Hub** | **`2743`** | `https://bibletrek4kids.com/craftivity/` | Master Printable Craftivity hub—update when adding a new Craftivity. |
| **Object Lessons Hub** | **`3049`** | `https://bibletrek4kids.com/object-lessons/` | Object Lessons directory (`Cat 33`). |
| **Games Hub** | **`3056`** | `https://bibletrek4kids.com/games/` | Sunday School Games directory (`Cat 34`). |
| **Letters from God** | **`2782`** | `https://bibletrek4kids.com/letters-from-god/` | Top-nav devotional letters page. |
| **About Us** | **`2732`** | `https://bibletrek4kids.com/about-us/` | Family mission page (Jerome, Sandra & Katie). |

---

## 4. Existing Workshop Series Hub Pages Registry

| Series Title | Page ID | Live URL |
| :--- | :--- | :--- |
| **God – From A To Z** | **`3232`** | `https://bibletrek4kids.com/god-from-a-to-z/` |
| **The New You** | **`3716`** | `https://bibletrek4kids.com/the-new-you/` |
| **Fruit of the Spirit** | **`2568`** | `https://bibletrek4kids.com/the-fruit-of-the-spirit/` |
| **The Genesis** | **`2098`** | `https://bibletrek4kids.com/the-genesis/` |
| **Walking With God** | **`3134`** | `https://bibletrek4kids.com/walking-with-god/` |
| **Salvation** | **`2677`** | `https://bibletrek4kids.com/salvation/` |
| **Giving** | **`3207`** | `https://bibletrek4kids.com/giving/` |
| **Thanksgiving** | **`3178`** | `https://bibletrek4kids.com/thanksgiving/` |

---

## 5. Active Custom Site Tweaks Plugin (`bibletrek-site-tweaks`)

* **Source Path:** `wp-plugin/bibletrek-site-tweaks/bibletrek-site-tweaks.php`
* **Installed Slug on `bibletrek4kids.com`:** `bibletrek-site-tweaks/bibletrek-site-tweaks.php` (deployed via `wordpress_mcp` `wpcom/plugin-upload-request` -> `wpcom/plugin-upload` with `overwrite: true` -> `wpcom/plugin-activate`)
* **What It Controls:**
  1. Filters Avada's frontend `option_fusion_options` (`post_meta_author = '0'`) so `"By Jerome Rajan |"` is never output on single posts or category/blog archives.
  2. Outputs `#bibletrek-site-tweaks-css` in `wp_head` to cleanly left-align all comment form checkboxes (`#respond p.comment-form-cookies-consent` and `#respond p.comment-subscription-form`, overriding Avada's input `min-width`).
