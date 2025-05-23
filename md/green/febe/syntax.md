Appendix A - FeBe Protocol Syntax

[![](../../images/logo.gif)](../../index.html)

\*\*Appendix
A

FeBe Protocol Syntax\*\*

---

\*\*Metasyntax

\*\*This document specifies the FeBe Protocol in an
extended Backus

- Naur Form (BNF) strongly influenced by [Harbison&Steele
  84].

Terminal symbols are printed using a fixed
typeface, while non-terminal symbols are written in _cursive_
style.
All terminal symbols refers to ASCII characters to be sent exactly
as defined
within the open and close quotes (` ').

All non-terminal symbols are defined by a production. The vertical
bar (|)
designates an exclusive-or choice between options. The production:

- non-terminal* ::=
  `terminal'
  | *also-non-terminal\*

defines the symbol _non-terminal_ as either the terminal
symbol terminal
or the non-terminal symbol _also-non-terminal_. The symbol
`|' has
lower precedence than all operators except `::=' and `'.

\*\*Sequences

\*\*The brackets `[' and `]' are used as meta-syntactical
symbols
to designate optional and/or repeating sequences.

[ *symbol* ]? zero or
one occurrence
of \*symbol

- [ *symbol *]* zero or more
  occurrences of
  *symbol

- [ *symbol* ]+ one or more
  occurrences of
  _symbol_

The FeBe Protocol also uses a sequence construct difficult to
model in BNF:
a count delimited sequence. We introduce an extension to the
syntax:

- count\* * [
  *element\*
  ]

to designate the number _count_ followed by _count_
repetitions
of \*element.

\*\*\*Calls

\*\*The arrow `' specifies a
protocol
call:

- call \*
  _result_ | _error_

Although this looks like a production it is in reality an action. The above
example is a call from Fe (_call_) with a reply from the Be (_result_)
or possibly an error (_error_).

\*\*

Lexical Definitions

\***\* Special Characters**

- newline\* ::= This
  is the
  character 128
  or A16 often
  represented as '\n'
  in C.

- delim* ::= `~'
  | *newline

digit\* ::= `0'
| `1'
| `2'
| `3'
| `4'
| `5'
| `6'
| `7'
| `8'
| `9'

- char\* ::= Any 8 bit ASCII character

**Errors**

- error\* ::= `?'

**Tumblers**

- number* ::= [ *digit* ]+
  *delim

exponent* ::= [ *digit\* ]+

- tumbler* ::= exponent [ `.'
  [ *digit* ]+ ]* \*delim

id* ::= *tumbler

vaddr* ::= *exponent* `.'
[ *digit* ]+ [ `.'
[ *digit* ]+ ]? *delim\*

**Groups**

- span* ::= *tumblerstart
  tumblerwidth

vspan*
::= *vaddr\*\*start
vaddrwidth

spec*
::= `s'
*delim span

- | `v'
  _delim doc-id number_ * [ *vspan
  \*]

- spec-set* ::= *number\* * [
  *spec\*
  ]

- shared-span* ::= *tumblerstart-1
  tumblerstart
  -2
  tumblerwidth

- **Document contents**

- string* ::=
  `t'
  *number\* * [ *char\* ]

- contents* ::= *string* |
  *idlink\*

**Command codes**

- create-new-document*
  ::= `11'
  *delim

create-new-version* ::= `13'
*delim

open* ::= `35'
*delim

close* ::= `36'
*delim

create-link* ::= `27'
*delim

retrieve-doc-vspan* ::= `14'
*delim

retrieve-doc-vspanset* ::= `1'
*delim

retrieve-v* ::= `5'
*delim

follow-link* ::= `18'
*delim

retrieve-endsets* ::= `28'
*delim

find-links-from-to-three* ::= `30'
*delim

show-relations-of-2-versions* ::= `10'
*delim

find-docs-containing *::= `22'
*delim

insert* ::= `0'
*delim

copy* ::= `2'
*delim

rearrange* ::= `3'
*delim

delete-vspan* ::= `12'
*delim

quit* ::= `16'
*delim

x-account* ::= `34'
*delim

create-node-or-account* ::= `38'
*delim

**\*   **

\*\*Requests

\***\* create-new-document 11**

- create-new-document\*
  _create-new-document iddoc_|
  _error_

  **create-new-version 13**

- create-new-version
  id\*_old-doc_

_create-new-version
idnew-doc_| _error_

**open 35**

- mode* ::=
  `1'*read-only
  **delim
  *|
  `2'*read-write
  **delim

copy-switch* ::=
`1'*fail-on-conflict \*_delim
_|
`2'*copy-on-conflict*
*delim* | `3'\*always-copy

\*_ open
iddoc_
_mode copy-switch_
_open idnew-doc
_|
_error_

**close 36**

- close
  id\*_doc_

_close_
| _error_

**create-link 27**

- create-link iddoc\*
  \*spec-set\*\*from
  spec-setto
  spec-setthree

- _create-link
  idlink_
  | _error_

  **retrieve-doc-vspan 14**

- retrieve-doc-vspan
  id\*_doc_

_retrieve-doc-vspan
vspan_ | _error_

**retrieve-doc-vspanset 1**

- retrieve-doc-vspanset iddoc\*

_retrieve-doc-vspanset
number_ * [ *vspan\* ]

| _error_

**retrieve-v 5**

- retrieve-v spec-set\*
  _retrieve-v number_ * [ *contents*
  ] | *error\*

**follow-link 18**

- end-switch* ::= `1'*from\*
  _delim _| `2'*to
**delim
*|
`3'\*three
  \*\*delim

follow-link end-switch idlink\*

_follow-link
spec-setend_ |
_error_

**retrieve-endsets 28**

- retrieve-endsets
  spec-set\*_contents_

\*retrieve-endsets
spec-setfrom spec-setto

spec-setthree
*| *error\*

**find-links-from-to-three 30**

- home-spec* ::=
  *number\*
- [ *id**doc*]

- find-links-from-to-three
  spec-set**from
  spec-setto\*
  \*spec-set**three
  home-spec\*

- find-links-from-to-three
  number\* * [
  *idlink\* ]

| _error_

**show-relations-of-2-versions 10**

- show-relations-of-2-versions
  spec-set\*_1
  spec-set2_

- show-relations-of-2-versions
  number\*
- [ *shared-span* ]

| _error_

**find-docs-containing 22**

- find-docs-containing spec-set\*

_find-docs-containing number_ * [
*iddoc\*
]

| _error_

**insert 0**

- insert
  id\*_doc_
  _vaddr number_ * [ *string\* ]

_insert_ | _error_

**copy 2**

- copy iddoc\*
  _vaddr spec-set_
  _copy_ | _error_

**ii.rearrange; 3**

- cut-count* ::= `2'
  *delim *| `3'
  *delim *| `4'
  *delim

rearrange iddoc\*
_cut-count_ * [ *vaddr\* ]

_rearrange_ | _error_

**delete-vspan 12**

- delete-vspan iddoc\*
  _vspan_
  _delete-vspan_ | _error_

**quit 16**

- quit \*
  _quit_ (The _quit_ call can't
  return error.)

**x-account 34**

- x-account idaccount\*

_x-account_
| _error_

**create-node-or-account 38**

- create-node-or-account idaccount\*
  \*create-node-or-account idaccount

- | \*error
- ***

[![](../../images/logo.gif)](../../index.html)

[green](../index.html)
[gold](../../gold/index.html)
[FAQ](../../FAQ.html)
[discussion](../../discussion/index.html)

[download](../download/index.html)
[download](../../gold/download/index.html)
[history](../../history/index.html)
[Related Sites](../../related.html)

_[contact us](../../contact.html)_
or [![](../../images/cmn.gif)](http://www.blindpay.com/crit-me-now.cgi)

[![Golden Key](../../images/key.gif)](http://www.privacy.org/ipc/) [![Blue Ribbon](../../images/ribbon.gif)](http://mirrors.yahoo.com/eff/blueribbon.html)
