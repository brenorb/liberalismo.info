# Liberalismo.info — Initial Specification (Draft)

## 1. Purpose
Liberalismo.info aims to be a public, easily navigable library of liberal thought, mirroring the accessibility and archival sensibilities of Marxists.org while using a modern, maintainable static-site stack.

## 2. Current Codebase Snapshot
### 2.1 Tech stack
- **Static site generator**: Jekyll (Beautiful Jekyll theme)
- **Primary content format**: Markdown/HTML with YAML front matter
- **Hosting**: GitHub Pages-style static hosting (implied by theme and repo layout)

### 2.2 Repo structure (top-level)
- `_config.yml`: site configuration
- `_layouts/`, `_includes/`: page templates and shared UI
- `_posts/`: blog-style content
- `_data/`: structured data (YAML/JSON) used by templates
- `docs/`: project documentation (this spec lives here)
- `css/`, `js/`, `img/`: static assets
- `index.html`, `aboutme.md`, `tags.html`, `404.html`: primary pages

## 3. Inspiration: Marxists.org structure (high-level)
Marxists.org is a static-HTML, archive-first site with a strong emphasis on structured navigation and archival depth. Observed characteristics from the homepage:

- **Top navigation items**: Search, What’s New, Periodicals, eBooks, About, Donate, Buy books, Contact
- **Page layout**: static HTML, highly index-driven, link-dense
- **Navigation patterns**:
  - Category-like entry points (e.g., Periodicals, eBooks)
  - Informational/admin area (About, Donate, Contact)
  - Search as a primary entry
- **Mobile handling**: separate mobile page (`index-mobiles.htm`) with viewport-based redirect
- **Content model**: large archives of author works, historical materials, and themed collections (implied by site meta description)

## 4. Product Direction
**Goal**: Provide a neutral, archive-first browsing experience with multiple entry points (author, topic, era, medium) while preserving a simple, low-friction UI focused on helping visitors find ideas and answers to questions.

### 4.1 Primary entry points
- **Authors**: browse by author with works and metadata
- **Topics**: thematic taxonomies (e.g., political economy, constitutionalism, markets)
- **Periods**: historical eras and movements
- **Collections**: curated sets (e.g., “Foundational texts”, “Policy debates”)
- **Periodicals**: journals and magazines
- **eBooks**: packaged or compiled readings
- **Search**: global search across metadata and content (primary wayfinding)
- **About / Contribute / Donate**: mission and sustainability

### 4.2 Navigation model
- Top-level nav with ~6–8 primary items
- Global search present on every page; highlighted/central on the homepage
- Dense index pages for archives (author/topic/period) with clear wayfinding (no patronizing language)
- Secondary nav in sidebars or subheaders
- Deep cross-linking between author profiles, works, and topics
- Curated paths may exist for discovery, but are optional and should be tested

## 5. Content Model
### 5.1 Author
- Name, dates, short bio
- Affiliations/labels (schools of thought)
- Works list with publication year
- Related topics

### 5.2 Work
- Title, year, type (book/essay/speech), language
- Optional source/translation metadata
- Tags/topics
- Author reference(s)
- Full text is the default view when available
- Excerpts and commentary are allowed in specific sections (e.g., contextual notes, curated paths)
- Affiliate “buy” links can appear in multiple locations and should be clearly disclosed

### 5.3 Periodical
- Title, publication years, issues
- Issue list with links

## 6. Search & Discovery
- Global search is the primary entry point for idea/answer discovery
- Search should cover metadata (author/topic/period) and full text where feasible
- Hybrid search is desired: keyword/tags plus semantic matching (client-side embeddings if viable)
- Prefer static-site constraints over usability if the two conflict, at least initially

## 7. Visual & UX Notes
- Neutral archive tone; avoid editorial framing in primary content areas
- Gadsden flags are a light, fun recurring motif (subtle and/or explicit, potentially collectible)
- UX should be respectful and direct; avoid condescending “start here” language

## 8. Non-Functional Requirements
- **Static-first**: no server-side runtime required
- **Fast navigation**: index pages must be light and cacheable
- **Accessibility**: clear typography, keyboard navigation
- **Longevity**: content stored in plain text/markdown

## 9. Tradeoffs & Constraints
- Static-first and client-side search may limit scale/relevance; acceptable initially
- Dense index pages improve archival browsing but require careful UX to avoid overwhelm
- Theme constraints may limit how archival layouts evolve
