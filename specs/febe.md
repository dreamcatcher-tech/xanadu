# FeBe Protocol Specification

This document summarizes the FeBe Protocol used for communication between Udanax Green frontends and the backend. The complete historical description can be found in `md/green/febe/protocol.md`.

## Metasyntax

- Terminal symbols appear in `monospace`.
- Non-terminal symbols are _italicized_.
- Optional sequences are in `[ ]`.
- Repetition uses `*` or `+` after brackets.
- Exchanges follow `call -> result | error`.

## Lexical Components

- **newline** – ASCII 128 (A16).
- **delim** – `~` or newline.
- **digit** – `0`–`9`.
- **byte** – any 8‑bit value (data is count delimited and not escaped).
- **error** – a single `?` character returned by the backend.

## Identifiers and Addresses

- **tumbler** – ordered sequence of numbers.
- **id** – tumbler used as a global identifier.
- **vaddr** – tumbler relative to a document specifying space and location.

## Groups

- **span** – range of objects in global space.
- **vspan** – range within a document.
- **spec** – references a span or document-relative vspan.
- **spec-set** – list of specs.

## Document Contents

- **string** – `t` followed by a byte count and that many bytes.
- **contents** – a string or a link id.

## Command Codes

```
11 create-new-document
13 create-new-version
35 open
36 close
27 create-link
14 retrieve-doc-vspan
1  retrieve-doc-vspanset
5  retrieve-v
18 follow-link
28 retrieve-endsets
30 find-links-from-to-three
10 show-relations-of-2-versions
22 find-docs-containing
0  insert
2  copy
3  rearrange
12 delete-vspan
16 quit
34 x-account
38 create-node-or-account
```

Each command is issued by the frontend and returns the command number and any results on success, or `?` on failure.

## Frontend/Backend Usage

Frontends use these commands to store data, retrieve contents and manage versions. Multiple frontends may communicate with the backend simultaneously. Automatic version creation resolves editing conflicts when necessary.
