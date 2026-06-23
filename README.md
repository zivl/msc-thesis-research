# msc-thesis-research

My MSc thesis research final work — **"Is This Safe or Not? Mobile Apps Classification on
Android"** (Ziv Levy, under the supervision of Dr. David Movshovitz, IDC Herzliya, 2014) — as a
digital, explorable static website.

The site is built with [Astro](https://astro.build) + the
[Starlight](https://starlight.astro.build) documentation theme and deploys to GitHub Pages.

---

## Prerequisites

- [Node.js](https://nodejs.org) 18+ (developed on Node 24)
- [Yarn](https://classic.yarnpkg.com) 1.x

## Install

```bash
yarn install
```

## Preview locally

```bash
yarn dev
```

Then open the URL printed in the terminal (the site is served under the
`/msc-thesis-research` base path, e.g. <http://localhost:4321/msc-thesis-research/>).

## Build (production output)

```bash
yarn build      # output written to ./dist
yarn preview    # preview the built site locally
```

## Deploy to GitHub Pages

Deployment is automated by [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml):

1. In the GitHub repository, go to **Settings → Pages** and set **Source = GitHub Actions**.
2. Push to the `master` branch (or run the workflow manually from the **Actions** tab).
3. The workflow builds the site with Astro and publishes it to
   <https://zivl.github.io/msc-thesis-research/>.

The production URL is configured in [`astro.config.mjs`](astro.config.mjs) via `site` +
`base`. If you fork/rename the repo, update those two values.

---

## Switching the visual theme

The site ships **three swappable themes**, implemented as CSS-variable override files in
[`src/styles/`](src/styles):

| File | Look |
| --- | --- |
| `theme-classic.css` | **Default.** Clean academic white, Georgia serif body, minimal colour |
| `theme-modern.css` | Inter sans-serif, subtle navy accent, generous whitespace |
| `theme-dark.css` | Dark background, high contrast, easy on the eyes for long reading |

To switch, edit the `customCss` array in [`astro.config.mjs`](astro.config.mjs) so that exactly
**one** theme file is uncommented (keep `base.css` first, always on), then restart `yarn dev`:

```js
customCss: [
  "./src/styles/base.css",            // shared (always on)
  "./src/styles/theme-classic.css",   // ← active theme
  // "./src/styles/theme-modern.css",
  // "./src/styles/theme-dark.css",
],
```

(`theme-classic` and `theme-modern` also honour Starlight's light/dark toggle; `theme-dark`
forces the dark scheme regardless of the toggle.)

---

## Project layout

```text
astro.config.mjs            site config: base path, sidebar nav, math, active theme
src/content/docs/*.md       the thesis content, one file per chapter (verbatim)
src/styles/                 base.css + the three theme override files
public/images/              all figures (see "How the content was produced")
.github/workflows/deploy.yml  GitHub Pages CI
scripts/                    one-off tooling used to produce the content (see below)
```

## How the content was produced (reproducibility)

The source document is `Final Work - Ziv Levy_david_comments.docx`. The thesis prose was
transcribed **verbatim** — no wording, punctuation or ordering was changed; reviewer comments
were ignored.

- **Text & tables** were extracted with [`pandoc`](https://pandoc.org):
  ```bash
  pandoc "Final Work - Ziv Levy_david_comments.docx" -f docx -t gfm+pipe_tables \
    --wrap=none --extract-media=./_pandoc_media -o _full.md
  ```
  then split into per-chapter pages by [`scripts/migrate_content.py`](scripts/migrate_content.py).
- **5 figures were EMF** (a Windows vector format browsers can't display). They were converted
  to PNG with [Inkscape](https://inkscape.org): `inkscape in.emf --export-type=png --export-dpi=200 ...`.
- **8 figures were native Microsoft Word charts** that pandoc cannot extract. They were
  regenerated from the data embedded in the `.docx` by
  [`scripts/generate_charts.py`](scripts/generate_charts.py) (matplotlib). The data is exact;
  only the visual styling differs from the original Word charts.
- **LaTeX math** is rendered with KaTeX (`remark-math` + `rehype-katex`).

These scripts are kept for provenance; they are not needed to build or run the site.
