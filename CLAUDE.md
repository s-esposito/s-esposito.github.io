# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A static personal academic homepage hosted on GitHub Pages at `s-esposito.github.io`. The site is generated from Python: [build.py](build.py) reads BibTeX files and emits a single [index.html](index.html). The repo is a fork of [m-niemeyer/m-niemeyer.github.io](https://github.com/m-niemeyer/m-niemeyer.github.io) — keep the footer credit to Michael Niemeyer intact.

## Build

```bash
pip install -r requirements.txt   # pybtex, black
python build.py                    # regenerates index.html in place
```

`index.html` is a committed build artifact, not source — regenerate and commit it whenever [build.py](build.py), [publication_list.bib](publication_list.bib), [apps_list.bib](apps_list.bib), or [talk_list.bib](talk_list.bib) change. There is no test suite, linter config, or CI build step; GitHub Pages serves the committed `index.html` directly.

## Architecture

[build.py](build.py) is a flat module of pure functions that compose strings of HTML. The entrypoint `write_index_html` calls `get_index_html`, which stitches together:

- `get_personal_data()` — name, bio HTML, footer HTML. **Edit this function to update bio/links/CV path**, not the rendered `index.html`.
- `get_author_dict()` — map of `"First Last"` → personal homepage URL. Names matched here become hyperlinked in author lists. Names must match the BibTeX `author` field exactly (after pybtex's "First Last" reassembly).
- `get_publications_html()` / `get_apps_html()` / `get_talks_html()` — pybtex parses the corresponding `.bib` files and each entry is rendered by `get_paper_entry` / `get_app_entry` / `get_talk_entry`. Entries appear in the order they're written in the `.bib` file (top = top of page).

The talks section is currently commented out inside the HTML template in `get_index_html` — uncomment that block to re-enable it.

### BibTeX entry fields

`get_paper_entry` (publications) reads these non-standard fields beyond the usual BibTeX ones:
- `img` (required) — path to thumbnail under `assets/img/publications/`. All other link fields are optional and silently skipped if absent.
- `html`, `pdf`, `supp`, `video`, `poster`, `code` — render as icon-link buttons in a `.publication-links` row.
- `award` — renders in `.award` (accent color) next to the title.
- `note` — used in place of `booktitle` for non-conference items (e.g. arXiv, GitHub).

`get_app_entry` (software in [apps_list.bib](apps_list.bib)) reads `img`, `title`, `year`, and supports `html` / `code` / `video` as link buttons plus `note` as an italic description line. No authors or BibTeX expand button.

`get_talk_entry` reads `img`, `title`, `booktitle`, `year`, plus optional `slides` and `video`.

### Author highlighting

`generate_person_html` italicizes the name passed as `highlight_name`, which defaults to `"Stefano Esposito"`. The comparison runs against the *plain* name (before any author-dict link wrapping), so an author with both a link and a highlight will get both. Pass `highlight=False` when rendering the BibTeX preview to suppress it.

## Styling

[assets/css/style.css](assets/css/style.css) drives the visual design. Bootstrap 4 is still loaded from CDN for grid/collapse, but most paint properties (colors, type, card hover, spacing) are overridden via custom rules. Theme tokens are CSS variables in `:root`, with a `@media (prefers-color-scheme: dark)` block scoped `:not([data-theme="light"])` and a `[data-theme="dark"]` rule that re-define them. The fixed top-right `.theme-toggle` button cycles `auto → light → dark → auto`; choice is persisted in `localStorage['theme']` (absent = auto = follow OS). A pre-paint inline script in `<head>` reads it before paint to avoid FOUC. Key class hooks added in [build.py](build.py): `.publication-card` (outer paper/app/talk wrapper, shared across all three entry types), `.publication-links` (icon-link row + optional Bibtex button), `.social-links` (bio social row), `.profile-photo` (bio photo, replaces the old hardcoded `width="280px"`), `.award`, `.footer-credits`.

Publication cards use a `col-4 col-sm-3` / `col-8 col-sm-9` grid so the thumbnail stays beside the text on phones at a smaller ratio (Bootstrap 4's bare `col-sm-*` would have stacked them into oversized full-width blocks below 576px).

## Assets

- `assets/img/profile.jpg` — main profile photo
- `assets/img/publications/*` — publication thumbnails referenced by `img` fields in [publication_list.bib](publication_list.bib)
- `assets/img/apps/*` — software/app thumbnails referenced by `img` fields in [apps_list.bib](apps_list.bib)
- `assets/pdf/` — CV and other linked PDFs
- `assets/css/style.css` — custom styles layered on top of Bootstrap 4 (loaded from CDN in the template)
