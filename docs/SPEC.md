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

### 2.3 Git branches
- `work` (current)

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

## 4. Proposed Information Architecture (initial)
**Goal**: Provide an archive-first browsing experience with multiple entry points (author, topic, era, medium) while preserving a simple, low-friction UI.

### 4.1 Primary entry points
- **Authors**: browse by author with works and metadata
- **Topics**: thematic taxonomies (e.g., political economy, constitutionalism, markets)
- **Periods**: historical eras and movements
- **Collections**: curated sets (e.g., “Foundational texts”, “Policy debates”)
- **Periodicals**: journals and magazines
- **eBooks**: packaged or compiled readings
- **Search**: global search across metadata and content
- **About / Contribute / Donate**: mission and sustainability

### 4.2 Navigation model
- Top-level nav with ~6–8 primary items
- Dense index pages for archives (author/topic/period)
- Secondary nav in sidebars or subheaders
- Deep cross-linking between author profiles, works, and topics

## 5. Content Model (initial)
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

### 5.3 Periodical
- Title, publication years, issues
- Issue list with links

## 6. Non-Functional Requirements
- **Static-first**: no server-side runtime required
- **Fast navigation**: index pages must be light and cacheable
- **Accessibility**: clear typography, keyboard navigation
- **Longevity**: content stored in plain text/markdown

## 7. Open Decisions (for interview)
- Whether to keep Beautiful Jekyll theme or replace UI
- Search approach (static client-side vs. external indexing)
- Content ingestion workflow (manual, scripted import, hybrid)
- Metadata granularity and schema

## 8. Risks & Tradeoffs (initial)
- **Static-only search**: simpler hosting but may limit scale
- **Dense index pages**: good for archival browsing but may overwhelm casual users
- **Theme constraints**: Beautiful Jekyll may resist heavy archival layouts

## 9. Next Steps
- Interview to define UX, IA, content workflow, and tooling
- Decide on taxonomy and metadata schema
- Propose minimum viable archive structure
