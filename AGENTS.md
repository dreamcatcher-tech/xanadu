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

## Purpose

- the purpose of this repository is to create and curate the documents in the
  specs/ folder, to ensure clear definitions and specifications using the files
  in the md/ folder as reference, and as a final backstop, the files in the
  udanax folder.

## Rules

- whenever you use a novel term, it must be in the dictionary. you can only add
  novel terms if they are mentioned somewhere in the reference md/ or udanax/
  folders.
- any time you use a term in the dictionary, you must link the usage of the word
  to the definition of the word using a markdown link, so that users can easily
  navigate to the dictionary definition.

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
- When researching the repository, search within `md/` using `grep` or `find` to
  locate relevant information quickly.
