# Reference: Bible Object Lessons & Sunday School Games

Use this guide whenever publishing or updating an **Object Lesson** (`Post`, Category `33`, Tag `32`) or a **Sunday School Game** (`Post`, Category `34`, Tag `36`).

---

## 1. Taxonomy & Media Settings

| Content Type | Category ID | Tag ID | `featured_media` | Hub Page to Update |
| :--- | :--- | :--- | :--- | :--- |
| **Object Lesson** | `[33]` (`Object Lessons`) | `[32]` (`object lesson`) | Required (illustration / prop photo ID) | `/object-lessons/` (`ID 3049`) |
| **Sunday School Game** | `[34]` (`Games`) | `[36]` (`games`) | Required (game diagram / photo ID) | `/games/` (`ID 3056`) |

Always pass `"comment_status": "open"`.

---

## 2. Layout & Voice Guidelines

Object Lessons and Games on `bibletrek4kids.com` have a warm, conversational, teacher-to-class voice (`"Begin by saying..."`, `"Ask a volunteer to come forward..."`). Keep 100% of the family's authentic script and humor while structuring the post cleanly inside the `.bt-cf-wrap` outdoor-adventure design system (reusing the same `.bt-cf-*` classes from `craftivity-guide.md`, swapping the hero gradient accent to Terracotta `#c45b19` for Object Lessons or Sky Blue `#0369a1` for Games):

1. **Top Navigation Bar (`.bt-cf-topbar`):**
   * Left pill: `← All Object Lessons` (`https://bibletrek4kids.com/object-lessons/`) or `← All Sunday School Games` (`https://bibletrek4kids.com/games/`).
   * Right pill: Link to the most relevant Bible Trek Workshop or Series Hub!
2. **Hero Banner (`.bt-cf-hero`):**
   * Eyebrow pill (`5-Minute Gospel Object Lesson` or `Interactive Sunday School Game`).
   * Semantic `<h1 class="bt-cf-h1">` Title + **Objective** subtitle + quick pills (`Time: 5–10 Mins` / `10–15 Mins`, `Ages: 4–15`, `Prep: Low / Zero-Prep`, `Scripture`).
3. **Key Scripture Callout (`.bt-cf-verse`):**
   * Highlight the anchor Bible verse (e.g., *Proverbs 16:18*, *Romans 5:17–19*, *Ephesians 2:10*).
4. **Supplies & Setup / How to Play Card (`.bt-cf-card`):**
   * Clean `<ul>` for **What You Will Need** (never leave trailing spaces or empty `<strong> </strong>` tags).
   * Clean, flat `<ol>` for **Setup / How to Play** rounds (never nest `<ol><ol>`).
   * Center or float the demonstration diagram/photo (`<img>` hosted on `https://bibletrek4kids.com/wp-content/uploads/...` — **never** `localhost` URLs — with descriptive `alt`, `width`, and `height`).
5. **Teacher Script & Gospel Explanation Card (`.bt-cf-card`):**
   * Preserve the teacher's spoken dialogue (`"Begin by saying..."`), volunteer prompts, and discussion questions (`1.`, `2.`) clearly.
6. **Related Workshop Callout Banner (`.bt-cf-rel`) + Scoped `<style>` at End:**
   * Cross-link to the matching full 60-minute Workshop or Series so teachers who discover a quick Object Lesson/Game via Google or Instagram Reels naturally explore your full curriculum.

---

## 3. Hub Page Sync After Publishing

1. **For an Object Lesson:** Fetch `/object-lessons/` (`ID 3049`) via `wpcom-mcp/pages-get`, inspect how existing Object Lesson cards/posts are displayed (Note: if `/object-lessons/` uses an Avada `[fusion_blog]` dynamic grid pulling Category `33`, verify via `curl https://bibletrek4kids.com/object-lessons/` that the new post appears automatically with its `featured_media` and `excerpt`; if static cards exist, append a matching card!).
2. **For a Sunday School Game:** Fetch `/games/` (`ID 3056`) and verify `https://bibletrek4kids.com/games/` renders the new Game post cleanly with cover art, title, and excerpt.
