# Agent Guidelines for xanadu Repository

## Repository Layout

- `udanax/` holds the original HTML website. Important subfolders include:
  - `green/`, `gold/`, `history/`, `discussion/` – sections of the site.
  - `images/` – referenced by both HTML and Markdown content.
  - `Templates/` and `CVS/` – template and legacy version-control files.
- `md/` mirrors the structure of `udanax/` but contains Markdown files extracted
  from the HTML.
  - Links inside the Markdown still point to `.html` files and rely on images in
    `udanax/images`.

## Tips

- Search across many files with `grep -r` or `find` since there are numerous
  pages.
- `md/` contains the primary text for edits; keep the parallel structure intact
  so paths remain consistent with the HTML originals.
- Some folders (e.g., `CVS`) are historical artifacts and can be ignored unless
  needed.
- The Markdown files in `md/` are the canonical source for project knowledge.
  Use them when answering questions or drafting documentation.
- Treat everything under `udanax/` as read-only; the HTML files and other
  resources are preserved solely for reference.
- Smalltalk source files in `udanax/gold/download/` are provided for historical
  context. There is no active environment to run them, so they generally do not
  need modification.
- When researching the repository, search within `md/` using `grep` or `find`
  to locate relevant information quickly.
