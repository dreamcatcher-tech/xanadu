Appendix A - FeBe Protocol Syntax



[![](../../images/logo.gif)](../../index.html)

**Appendix
A

FeBe Protocol Syntax**

---

**Metasyntax

**This document specifies the FeBe Protocol in an
extended Backus
- Naur Form (BNF) strongly influenced by [Harbison&Steele
84].

Terminal symbols are printed using a fixed
typeface, while non-terminal symbols are written in *cursive*
style.
All terminal symbols refers to ASCII characters to be sent exactly
as defined
within the open and close quotes (` ').

All non-terminal symbols are defined by a production. The vertical
bar (|)
designates an exclusive-or choice between options. The production:

* non-terminal* ::=
`terminal'
| *also-non-terminal*

defines the symbol *non-terminal* as either the terminal
symbol terminal
or the non-terminal symbol *also-non-terminal*. The symbol
`|' has
lower precedence than all operators except `::=' and `'.

**Sequences

**The brackets `[' and `]' are used as meta-syntactical
symbols
to designate optional and/or repeating sequences.

[ *symbol* ]? zero or
one occurrence
of *symbol

* [ *symbol *]* zero or more
occurrences of
*symbol

* [ *symbol* ]+ one or more
occurrences of
*symbol*

The FeBe Protocol also uses a sequence construct difficult to
model in BNF:
a count delimited sequence. We introduce an extension to the
syntax:

* count* * [
*element*
]

to designate the number *count* followed by *count*
repetitions
of *element.

***Calls

**The arrow `' specifies a
protocol
call:

* call *
*result* | *error*

Although this looks like a production it is in reality an action. The above
example is a call from Fe (*call*) with a reply from the Be (*result*)
or possibly an error (*error*).

**

Lexical Definitions

**** Special Characters**

* newline* ::= This
is the
character 128
or A16 often
represented as '\n'
in C.

* delim* ::= `~'
| *newline

digit* ::= `0'
| `1'
| `2'
| `3'
| `4'
| `5'
| `6'
| `7'
| `8'
| `9'

* char* ::= Any 8 bit ASCII character

**Errors**

* error* ::= `?'

**Tumblers**

* number* ::= [ *digit* ]+
*delim

exponent* ::= [ *digit* ]+

* tumbler* ::= exponent [ `.'
[ *digit* ]+ ]* *delim

id* ::= *tumbler

vaddr* ::= *exponent* `.'
[ *digit* ]+ [ `.'
[ *digit* ]+ ]? *delim*

**Groups**

* span* ::= *tumblerstart
tumblerwidth

vspan*
::= *vaddr**start
vaddrwidth

spec*
::= `s'
*delim span

* | `v'
*delim doc-id number* * [ *vspan
*]

* spec-set* ::= *number* * [
*spec*
]

* shared-span* ::= *tumblerstart-1
tumblerstart
-2
tumblerwidth

*

**Document contents**

* string* ::=
`t'
*number* * [ *char* ]

* contents* ::= *string* |
*idlink*

**Command codes**

* create-new-document*
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

***   **

**Requests

**** create-new-document 11**

*
create-new-document*
*create-new-document iddoc*|
*error*

**create-new-version 13**

* create-new-version
id**old-doc*

*create-new-version
idnew-doc*| *error*

**open 35**

* mode* ::=
`1'*read-only
**delim
*|
`2'*read-write
**delim

copy-switch* ::=
`1'*fail-on-conflict
**delim
*|
`2'*copy-on-conflict*
*delim* | `3'*always-copy

** open
iddoc*
*mode copy-switch*
*open idnew-doc
*|
*error*

**close 36**

* close
id**doc*

*close*
| *error*

**create-link 27**

* create-link iddoc*
*spec-set**from
spec-setto
spec-setthree

*
*create-link
idlink*
| *error*

**retrieve-doc-vspan 14**

* retrieve-doc-vspan
id**doc*

*retrieve-doc-vspan
vspan* | *error*

**retrieve-doc-vspanset 1**

* retrieve-doc-vspanset iddoc*

*retrieve-doc-vspanset
number* * [ *vspan* ]

| *error*

**retrieve-v 5**

* retrieve-v spec-set*
*retrieve-v number* * [ *contents*
] | *error*

**follow-link 18**

* end-switch* ::= `1'*from*
*delim *| `2'*to
**delim
*|
`3'*three
**delim

follow-link end-switch idlink*

*follow-link
spec-setend* |
*error*

**retrieve-endsets 28**

* retrieve-endsets
spec-set**contents*

*retrieve-endsets
spec-setfrom spec-setto

spec-setthree
*| *error*

**find-links-from-to-three 30**

* home-spec* ::=
*number*
* [ *id**doc*]

* find-links-from-to-three
spec-set**from
spec-setto*
*spec-set**three
home-spec*

* find-links-from-to-three
number* * [
*idlink* ]

| *error*

**show-relations-of-2-versions 10**

*
show-relations-of-2-versions
spec-set**1
spec-set2*

* show-relations-of-2-versions
number*
* [ *shared-span* ]

| *error*

**find-docs-containing 22**

* find-docs-containing spec-set*

*find-docs-containing number* * [
*iddoc*
]

| *error*

**insert 0**

* insert
id**doc*
*vaddr number* * [ *string* ]

*insert* | *error*

**copy 2**

* copy iddoc*
*vaddr spec-set*
*copy* | *error*

**ii.rearrange; 3**

* cut-count* ::= `2'
*delim *| `3'
*delim *| `4'
*delim

rearrange iddoc*
*cut-count* * [ *vaddr* ]

*rearrange* | *error*

**delete-vspan 12**

* delete-vspan iddoc*
*vspan*
*delete-vspan* | *error*

**quit 16**

* quit *
*quit* (The *quit* call can't
return error.)

**x-account 34**

* x-account idaccount*

*x-account*
| *error*

**create-node-or-account 38**

* create-node-or-account idaccount*
*create-node-or-account idaccount

* | *error
*







---

[![](../../images/logo.gif)](../../index.html)

[green](../index.html)
[gold](../../gold/index.html)
[FAQ](../../FAQ.html)
[discussion](../../discussion/index.html)

[download](../download/index.html)
[download](../../gold/download/index.html)
[history](../../history/index.html)
[Related Sites](../../related.html)

*[contact us](../../contact.html)*
or [![](../../images/cmn.gif)](http://www.blindpay.com/crit-me-now.cgi)

[![Golden Key](../../images/key.gif)](http://www.privacy.org/ipc/) [![Blue Ribbon](../../images/ribbon.gif)](http://mirrors.yahoo.com/eff/blueribbon.html)
