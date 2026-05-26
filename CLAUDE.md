# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A static personal academic homepage hosted on GitHub Pages at `s-esposito.github.io`. The site is generated from Python: [build.py](build.py) reads BibTeX files and emits a single [index.html](index.html). The repo is a fork of [m-niemeyer/m-niemeyer.github.io](https://github.com/m-niemeyer/m-niemeyer.github.io) — keep the footer credit to Michael Niemeyer intact.

## Build

```bash
pip install -r requirements.txt   # pybtex, black
python build.py                    # regenerates index.html in place
```

`index.html` is a committed build artifact, not source — regenerate and commit it whenever [build.py](build.py), [publication_list.bib](publication_list.bib), or [talk_list.bib](talk_list.bib) change. There is no test suite, linter config, or CI build step; GitHub Pages serves the committed `index.html` directly.

## Architecture

[build.py](build.py) is a flat module of pure functions that compose strings of HTML. The entrypoint `write_index_html` calls `get_index_html`, which stitches together:

- `get_personal_data()` — name, bio HTML, footer HTML. **Edit this function to update bio/links/CV path**, not the rendered `index.html`.
- `get_author_dict()` — map of `"First Last"` → personal homepage URL. Names matched here become hyperlinked in author lists. Names must match the BibTeX `author` field exactly (after pybtex's "First Last" reassembly).
- `get_publications_html()` / `get_talks_html()` — pybtex parses the `.bib` files and each entry is rendered by `get_paper_entry` / `get_talk_entry`. Entries appear in the order they're written in the `.bib` file (top = top of page).

The talks section is currently commented out inside the HTML template in `get_index_html` — uncomment that block to re-enable it.

### BibTeX entry fields

`get_paper_entry` reads these non-standard fields beyond the usual BibTeX ones:
- `img` (required) — path to thumbnail under `assets/img/publications/`
- `html`, `pdf`, `supp`, `video`, `poster`, `code` — link buttons. Missing fields print a warning at build time but do not fail; the warning is informational.
- `award` — renders a red parenthetical next to the title.
- `note` — used in place of `booktitle` for non-conference items (e.g. arXiv, GitHub).

`get_talk_entry` reads `img`, `title`, `booktitle`, `year`, plus optional `slides` and `video`.

### Author bolding

`generate_person_html` bolds the name passed as `make_bold_name`, which defaults to `"Michael Niemeyer"` from the upstream template. The site owner's name (`"Stefano Esposito"`) is **not** currently bolded because of this default — if changing the author rendering, update the default in [build.py:88](build.py#L88) rather than passing the name at every call site.

## Assets

- `assets/img/profile.jpg` — main profile photo
- `assets/img/publications/*` — publication thumbnails referenced by `img` fields in the `.bib`
- `assets/pdf/` — CV and other linked PDFs
- `assets/css/style.css` — custom styles layered on top of Bootstrap 4 (loaded from CDN in the template)
