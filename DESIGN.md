---
version: alpha
name: Soft Archive Shell
description: Warm editorial archive with restrained yellow accents and a calmer research-surface feel.
colors:
  ink: "#1E1912"
  paper: "#FFFCF7"
  paperAlt: "#F6F2EA"
  shell: "#EFE9DE"
  signal: "#F3BF17"
  signalDeep: "#C38D00"
  border: "rgba(32,25,15,0.12)"
  muted: "#6D675B"
  soft: "#908879"
typography:
  display-xl:
    fontFamily: Instrument Sans
    fontSize: 4.75rem
    fontWeight: 700
    lineHeight: 0.92
    letterSpacing: -0.04em
  h1:
    fontFamily: Instrument Sans
    fontSize: 3.4rem
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.04em
  h2:
    fontFamily: Instrument Sans
    fontSize: 2rem
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.03em
  body-md:
    fontFamily: Instrument Sans
    fontSize: 1.0625rem
    fontWeight: 400
    lineHeight: 1.68
  serif-accent:
    fontFamily: Cormorant Garamond
    fontSize: 1em
    fontWeight: 700
    fontStyle: italic
  meta-sm:
    fontFamily: Instrument Sans
    fontSize: 0.72rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.18em
  mono-sm:
    fontFamily: IBM Plex Mono
    fontSize: 0.82rem
    fontWeight: 400
    lineHeight: 1.4
rounded:
  sm: 8px
  md: 18px
  lg: 28px
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
    backgroundColor: "rgba(251,248,242,0.78)"
    textColor: "{colors.ink}"
    accentColor: "{colors.signal}"
  archive-card:
    backgroundColor: "rgba(255,252,247,0.82)"
    borderColor: "{colors.border}"
    titleColor: "{colors.ink}"
    metaColor: "{colors.muted}"
  chip:
    backgroundColor: "rgba(255,255,255,0.74)"
    textColor: "{colors.muted}"
    borderColor: "{colors.border}"
  search-input:
    backgroundColor: "rgba(255,255,255,0.84)"
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
  work-shell:
    backgroundColor: "{colors.paper}"
    borderColor: "{colors.border}"
    headingColor: "{colors.ink}"
---

## Overview

`liberalismo.info` should feel like an annotated political archive, not a startup landing page. The current direction is closer to a calm editorial product surface: warm paper, floating shells, restrained signal-yellow accents, and a softer sense of depth inspired by premium landing pages rather than blog templates.

The homepage should behave like a switchboard into the archive. Readers must quickly branch into works, authors, themes, schools, reading paths, and project documentation without being funneled through a single hero CTA.

## Colors

- **Ink (`#1E1912`)** remains the main reading and heading color.
- **Paper (`#FFFCF7`)**, **Paper Alt (`#F6F2EA`)**, and **Shell (`#EFE9DE`)** create a warm, high-end background without turning the site into a yellow poster.
- **Signal (`#F3BF17`)** is now an accent, not the dominant field color. Use it for the brand mark, footer base, and selected emphasis.
- **Muted (`#6D675B`)** and **Soft (`#908879`)** handle metadata, dividers, and secondary labels.

## Typography

- **Instrument Sans** carries the main interface: headings, body text, nav labels, and metadata. It gives the site a cleaner product cadence than the earlier condensed type.
- **Cormorant Garamond italic** is the accent voice inside major headings. Use it selectively to create editorial lift.
- **IBM Plex Mono** is reserved for slugs, structured metadata, and extraction/process references.

Hierarchy should feel editorial:

- big, precise section headings with occasional italic serif interruption
- readable body text with comfortable measure and lighter visual pressure
- uppercase metadata labels with wider tracking

## Components

- **Nav**: floating warm shell with a compact brand block, quiet links, and a subtle dropdown. It should feel precise and expensive, not loud.
- **Archive card**: rounded warm panel with soft shadow, tight metadata label, strong heading, and concise explanatory copy.
- **Chip**: quiet rounded filter handle rather than a loud badge.
- **Search input**: wide, obvious, and catalog-oriented. It should feel like querying an index rather than posting into a feed.
- **Work shell**: work pages should privilege bibliographic context, source clarity, and chapter navigation when available.

## Page Patterns

- **Homepage**: airy switchboard. Multiple entry points stay visible above the fold, but the composition should breathe.
- **Library index**: large intro panel, compact metrics, dense work list, then browse affordances by theme and school.
- **Taxonomy index**: simple, scan-friendly chip clouds or lists that route into filtered search.
- **Work page**: bibliographic summary, editorial note, source statement, then the cleaned text.
- **Docs pages**: lighter treatment, but still inside the same archive language.

## Motion

Use motion sparingly. Prefer hover lifts, subtle shell transitions, and soft background shifts. The archive should feel alive but stable.

## Anti-Patterns

- no purple gradients
- no heavy opaque yellow slabs across the whole page
- no oversized generic hero with one central button
- no pure white background unless a component explicitly needs contrast
