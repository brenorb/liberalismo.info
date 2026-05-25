---
version: alpha
name: Gadsden Archive
description: Signal-yellow editorial archive for a static library of liberal thought.
colors:
  ink: "#1F1A10"
  paper: "#FFF8DB"
  paperAlt: "#F3E4A5"
  signal: "#F2CB05"
  signalDeep: "#C8A102"
  olive: "#4C5B22"
  brass: "#8B6E00"
  border: "#2A2413"
  muted: "#6B6042"
  fog: "#F7F1D2"
typography:
  display-xl:
    fontFamily: IBM Plex Sans Condensed
    fontSize: 4.25rem
    fontWeight: 700
    lineHeight: 0.92
    letterSpacing: 0.02em
  h1:
    fontFamily: IBM Plex Sans Condensed
    fontSize: 3.2rem
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: 0.01em
  h2:
    fontFamily: IBM Plex Sans Condensed
    fontSize: 2rem
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: 0.01em
  body-md:
    fontFamily: Newsreader
    fontSize: 1.125rem
    fontWeight: 400
    lineHeight: 1.58
  meta-sm:
    fontFamily: IBM Plex Sans Condensed
    fontSize: 0.85rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
  mono-sm:
    fontFamily: IBM Plex Mono
    fontSize: 0.82rem
    fontWeight: 400
    lineHeight: 1.4
rounded:
  sm: 4px
  md: 12px
  lg: 20px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 72px
components:
  nav:
    backgroundColor: "{colors.signal}"
    textColor: "{colors.border}"
    accentColor: "{colors.olive}"
  archive-card:
    backgroundColor: "{colors.paper}"
    borderColor: "{colors.border}"
    titleColor: "{colors.ink}"
    metaColor: "{colors.muted}"
  chip:
    backgroundColor: "{colors.signal}"
    textColor: "{colors.border}"
    borderColor: "{colors.border}"
  search-input:
    backgroundColor: "#FFFDF4"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
  work-shell:
    backgroundColor: "{colors.paper}"
    borderColor: "{colors.paperAlt}"
    headingColor: "{colors.ink}"
---

## Overview

`liberalismo.info` should feel like an annotated political archive, not a startup landing page. The visual reference is the Gadsden flag translated into editorial infrastructure: signal yellow, dark ink, olive accents, dense navigation, and the feeling of opening a well-used reference desk.

The homepage should behave like a switchboard into the archive. Readers must quickly branch into works, authors, themes, schools, reading paths, and project documentation without being funneled through a single hero CTA.

## Colors

- **Ink (`#1F1A10`)** is the primary reading color and border color. It should dominate headings, metadata rules, and navigation text.
- **Paper (`#FFF8DB`)** and **Fog (`#F7F1D2`)** replace clean white. The archive should feel printed, not sterile.
- **Signal (`#F2CB05`)** is the main accent. Use it for navigation, chips, labels, and search affordances. It should read as deliberate warning energy, not playful lemon.
- **Olive (`#4C5B22`)** is the secondary accent for hover states and active emphasis.
- **Brass (`#8B6E00`)** and **Muted (`#6B6042`)** support metadata, dividers, and shelf labels.

## Typography

- **IBM Plex Sans Condensed** is for headings, nav labels, chips, and archive metadata. It brings compression and discipline, which suits a dense archive.
- **Newsreader** is for body copy and long editorial text. It carries the reading experience without feeling like generic web serif.
- **IBM Plex Mono** is reserved for slugs, structured metadata, and extraction/process references.

Hierarchy should feel editorial:

- big, compressed section headings
- readable body text with comfortable measure
- uppercase metadata labels with wider tracking

## Components

- **Nav**: a flat signal-yellow band with dark text. It should feel like a directory bar, not a floating app shell.
- **Archive card**: thick border, paper background, strong heading, concise explanatory copy, and one compact metadata line.
- **Chip**: used for themes and schools. These are navigation devices, not badges for decoration.
- **Search input**: wide, obvious, and archive-oriented. It should feel like querying a catalog.
- **Work shell**: work pages should privilege bibliographic context, source clarity, and chapter navigation when available.

## Page Patterns

- **Homepage**: dense switchboard. Multiple entry points visible above the fold, plus a shelf of representative works.
- **Library index**: list of works first, then browse affordances by theme and school.
- **Taxonomy index**: simple, scan-friendly chip clouds or lists that route into filtered search.
- **Work page**: bibliographic summary, editorial note, source statement, then the cleaned text.
- **Docs pages**: lighter treatment, but still inside the same archive language.

## Motion

Use motion sparingly. Prefer subtle hover lifts, border/ink transitions, and soft background shifts. The archive should feel alive but stable.

## Anti-Patterns

- no purple gradients
- no glassmorphism
- no rounded SaaS cards everywhere
- no oversized generic hero with one central button
- no pure white background unless a component explicitly needs contrast
