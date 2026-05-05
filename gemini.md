# Yash Anand — Portfolio Website

## Project Overview

This is a single-page personal portfolio website for **Yash Anand**, a B.Tech Data Science student at Manipal University Jaipur (2024–2028), based in Delhi, India. The site showcases his skills, projects, freelance experience, and leadership roles. He is actively seeking internships in data science, ML engineering, or full-stack development.

- **Contact:** yashanand2755@gmail.com | +91 8076839293
- **GitHub:** [github.com/yashanand969-max](https://github.com/yashanand969-max)
- **Live Project:** [i4uinvoice.netlify.app](https://i4uinvoice.netlify.app)

---

## File Structure

```
index.html   # Entire site — single self-contained HTML file (CSS + JS inline)
gemini.md    # This file
```

No build system, no frameworks, no dependencies. Everything is in `index.html`.

---

## Tech Stack

- **Pure HTML/CSS/JS** — no bundler, no framework
- **Google Fonts** — Playfair Display (serif), Inter (sans), IBM Plex Mono
- **Vanilla JS** — IntersectionObserver for scroll-triggered fade-up animations
- **CSS custom properties** — full design token system via `:root` variables
- **CSS Grid & Flexbox** — all layout
- **Responsive** — breakpoint at `max-width: 900px`

---

## Design System

### Color Tokens (CSS Variables)

| Token       | Value                        | Usage                        |
|-------------|------------------------------|------------------------------|
| `--bg`      | `#0d1117`                    | Page background (GitHub dark)|
| `--bg2`     | `#161b22`                    | Card/section backgrounds     |
| `--bg3`     | `#1c2128`                    | Hover states, headers        |
| `--bg4`     | `#21262d`                    | Chip backgrounds             |
| `--border`  | `rgba(139,148,158,0.12)`     | Subtle dividers              |
| `--border2` | `rgba(139,148,158,0.24)`     | Default borders              |
| `--border3` | `rgba(139,148,158,0.40)`     | Hover borders                |
| `--text`    | `#e6edf3`                    | Primary text                 |
| `--text2`   | `#c9d1d9`                    | Secondary text               |
| `--muted`   | `#7d8590`                    | Subdued text, labels         |
| `--accent`  | `#3b82f6`                    | Blue accent (Tailwind 500)   |
| `--accent2` | `#60a5fa`                    | Blue accent light (400)      |
| `--gold`    | `#d4a853`                    | Gold accent (unused visually)|

### Typography

| Variable   | Font                         | Usage                        |
|------------|------------------------------|------------------------------|
| `--serif`  | Playfair Display             | Headings, names, project titles |
| `--sans`   | Inter                        | Body text, buttons, labels   |
| `--mono`   | IBM Plex Mono                | Tags, badges, nav logo, dates |

### Spacing & Shape
- `--radius: 6px` — small elements (buttons, tags)
- `--radius2: 10px` — cards, panels

---

## Page Sections

### `#hero`
Two-column grid layout. Left: name, tagline, CTA buttons. Right: photo placeholder + stat cards (GPA `8.9/10`, `1` live project, `3` years coding).

### `#about` — Section 01
Two-column: bio text on left, sidebar info card on right. Sidebar lists: degree, institution, location, graduation year, status (`Open to Work`).

### `#skills` — Section 02
Full-width section with dark `--bg2` background. 4-column skill grid, hoverable with blue accent on tags.

**Skill categories:**
- **Data & ML** — Python, Pandas, NumPy, Scikit-Learn, Matplotlib, SQL
- **AI & NLP** — Machine Learning, NLP, LangChain, Prompt Engineering, RAG
- **Web Dev** — HTML/CSS, JavaScript, React, Node.js, REST APIs
- **Tools** — Git, VS Code, Excel, Jupyter, Netlify, GitHub

### `#projects` — Section 03
Stacked card list. Cards have a left blue accent bar on hover.

| Project | Type | Stack | Link |
|---------|------|-------|------|
| I4U Invoice Generator | Freelance · Full-Stack | Python, JavaScript, HTML/CSS, Excel API | [i4uinvoice.netlify.app](https://i4uinvoice.netlify.app) |
| AI-Managed Traffic Control System | Hackathon · Smart India Hackathon | Python, ML, Scikit-Learn, Computer Vision | — |

The I4U project card uses a `.showcase` layout variant with a 2-column screenshot grid inside it.

### `#experience` — Section 04
Single experience card for **Freelance Developer** at I4U Engineering Services (2024, Delhi Remote). Contains achievement list and deliverables grid.

### `#leadership` — Section 05
3-column leadership card grid + hackathon banner.

| Role | Org | Period |
|------|-----|--------|
| Vice President | MUJ Origins | 2026–2027 |
| Head of Events | Unstop Igniters | 2025–2026 |
| Core Committee Member | Aperture & Oneiros Festival | 2026 |
| Hackathon Participant | Smart India Hackathon (National Level) | — |

### `#contact`
Two-column: headline + CTA email button on left, contact links panel on right (Email, Phone, GitHub, Live Project).

---

## Component Patterns

### Buttons
- `.btn-primary` — filled blue, used for primary CTAs
- `.btn-ghost` — outlined, used for secondary CTAs

### Cards
- `.stat-card` / `.stat-card.accent-card` — hero stats
- `.skill-category` — skill grid cells, hover reveals blue tags
- `.project-card` — left-border accent on hover; `.showcase` variant spans full width
- `.leadership-card` — simple bordered card with emoji icon
- `.experience-card` — header + body layout with achievement list

### Animations
- `.fade-up` + `.visible` — scroll-triggered via `IntersectionObserver` (threshold `0.1`, 80ms stagger)
- `.live-dot` — pulsing green dot (CSS keyframe animation)
- `.marquee-track` — infinite horizontal scroll marquee (25s linear)

---

## Known Gaps / TODO

- Hero photo `<img>` has no `src` set — needs a real photo path
- No `<meta>` OG tags for social sharing
- No `favicon`
- Screenshot images in the I4U project card have no `src` — placeholder frames only
- No form handling on the contact section (email link only)
- No analytics

---

## Common Tasks for AI Assistance

- **Add a new project card:** Copy an existing `.project-card` block in Section 03, update text and stack pills. Use `.showcase` class if you want to include screenshots.
- **Change accent color:** Update `--accent` and `--accent2` in `:root`.
- **Add a new nav link:** Add an `<li><a href="#section-id">Label</a></li>` inside `.nav-links`.
- **Add a new skill tag:** Add a `<span class="tag">Name</span>` inside the relevant `.skill-tags` div.
- **Update contact info:** Search for `yashanand2755@gmail.com` and `+91 8076839293` — they appear in multiple places.
- **Responsive tweaks:** All responsive overrides are in a single `@media (max-width: 900px)` block near the bottom of the `<style>` tag.
