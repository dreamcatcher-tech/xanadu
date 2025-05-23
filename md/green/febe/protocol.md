FeBe Protocol

[![](../../images/logo.gif)](../../index.html)

**FeBe
Protocol**

---

\*\*Metasyntax

\*\*To be able to discuss the syntax and semantics of the FeBe Protocol,
we need a metasyntax.

Terminal symbols are printed using a fixed typeface. Non-terminal symbols are written in _cursive_
style. Subscripted labels are only for documentation. Descriptions of commands
refer to arguments using these labels.

The brackets `[' and `]' are meta-syntactic symbols. They designate optional
and/or repeating sequences.

[ *symbol* ]? zero or one occurrence of \*symbol

*[ *symbol* ]* zero or more occurrences of \*symbol

*[ *symbol* ]+ one or more occurrences of *symbol \*

- number\* * [ *symbol* ] *number* followed
  by *number* occurrences of *symbol\*

The arrow `' specifies a call and return sequence
in the protocol:

- call\* _result_ | _error_

For a more detailed discussion, please refer to the introduction of "Appendix
A - FeBe Protocol Syntax".

\*\* Lexical Components

\***\* Special Characters**

- newline\* ::= This is the
  character 128 or A16, often represented as '\n' in C.

- delim* ::= `~' | *newline

digit\* ::= `0' | `1' | `2' | `3' | `4' | `5' | `6' | `7' | `8' | `9'

- byte\* ::= Any 8 bit value

The FeBe Protocol uses 8 bit ASCII characters without parity. Commands that
transfer data-bytes transfer count delimited sequences of bytes. The protocol
does not reserve any escape codes within data transmissions.

**Errors**

- error\* ::= `?'

Calls to the backend that succeed return their command number followed by
any return values. Calls that fail for any reason return only the single
character `?'.

**Tumblers**

- number* ::= [ *digit*
  ]+ *delim

exponent* ::= [ *digit\* ]+

- tumbler* ::= *exponent* [ `.'
  [ *digit* ]+ ]* _delim_

A tumbler is an ordered sequence of numbers; for example, "123.45.0.89.1"
or "32.17".

Each number within a tumbler is called a "tumbler digit".

In the tumbler "_123_._45_._0_._89_._1_" the
underlined parts of the tumbler are "tumbler digits". The zero
(`.0.') tumbler digit (when not in
the exponent position) is only used as a separator in address tumblers.

- In the 88.1x
  implementation of the FeBe protocol each tumbler digit has to
  be in the range of 0 to 4,294,967,295 (232-1).

Comparison and arithmetic operations on tumblers align tumbler-digits from
the left. Since tumblers used as widths for spans often start with many
zeroes, FeBe uses a compact representation for tumblers. The first tumbler
digit in the representation is the number of zero tumbler digits at the
beginning of the tumbler. Thus, the tumblers "32.2" and "0.0.0.14.5"
are represented by "0.32.2" and "3.14.5."
This leading tumbler digit is referred to as the exponent of the tumbler.

- In the 88.1x
  implementation of the FeBe protocol there may be a maximum of
  11 non-zero tumbler digits plus exponent in any one tumbler.
  This restriction will be eliminated in a later release.

*   \*

* id* ::= *tumbler\*

These tumblers are global identifiers. IDs can refer to any Udanax Green
objects. (See the chapter "Addressing" for more details.)

- vaddr* ::= *exponent*
  `.' [ *digit* ]+ [ `.' [ *digit* ]+ ]? *delim\*

These tumblers are relative to a given document, so they only have one or
two digits. The first digit determines the space (1=text, 2=link). The second
digit determines the location within that space.

**Groups**

- span* ::= *tumbler\*_start
  tumblerwidth_

A span specifies a range of Udanax Green objects in the global address space.
Spans include all objects between *tumblerstart *inclusive
and *tumblerstart *plus *tumblerwidth *exclusive. (See the chapters "Tumbler Arithmetic"
and "Addressing".)

- vspan* ::= *vaddr\*_start
  vaddrwidth_

A vspan specifies a range of data-bytes and/or links within a given document.

- spec* ::= `s'
  *delim span

- | `v' _delim doc-id number_ * [ *vspan\*
  ]

- spec-set* ::= *number\* * [ *spec\*
  ]

A spec-set specifies a possibly discontinuous set of Udanax Green objects.

- shared-span* ::= *tumbler\*_start-1
  tumblerstart -2
  tumblerwidth_

A shared-span indicates that the span specified by *tumblerstart-1 *and *tumblerwidth *represents
the same Udanax Green objects as the span specified by *tumblerstart
-2 *and _tumblerwidth_. Only the version
comparison operation returns shared-spans.

**Document Contents**

- string* ::= `t'
  *number\* * [ *byte\* ]

Strings wrap data-bytes for transmission between the frontend and the backend.

- In the current
  implementation (88.1x) there is a maximum of 950 data-bytes
  in a single string. This limitation will be removed in future
  releases. It is _not_ recommended to even try to write
  longer strings to the backend.

*   \*

* contents* ::= *string*
  | *id\*_link_

Documents contain data-bytes and links. A frontend can retrieve a span that
contains both.

** Command Codes**

- create-new-document* ::= `11' *delim

create-new-version* ::= `13' *delim

open* ::= `35' *delim

close* ::= `36' *delim

create-link* ::= `27' *delim

retrieve-doc-vspan* ::= `14' *delim

retrieve-doc-vspanset* ::= `1' *delim

retrieve-v* ::= `5' *delim

follow-link* ::= `18' *delim

retrieve-endsets* ::= `28' *delim

find-links-from-to-three* ::= `30' *delim

show-relations-of-2-versions* ::= `10' *delim

find-docs-containing *::= `22' *delim

insert* ::= `0' *delim

copy* ::= `2' *delim

rearrange* ::= `3' *delim

delete-vspan* ::= `12' *delim

quit* ::= `16' *delim

x-account* ::= `34' *delim

create-node-or-account* ::= `38' *delim\*

\*\* Creation and Access

\***\* create-new-document 11**

- create-new-document\*
  _create-new-document iddoc_| _error_

Create a new document under the account and node of the user who issued
the request. Return the global identifier for the document.

This request creates the document but does not open it for access; you must
issue an open request (see below) to access the data in the new document.

**create-new-version 13**

- create-new-version id\*_old-doc_
  _create-new-version
  idnew-doc_| _error_

Return the identifier of a new copy of _idold-doc_. *idnew-doc *contains
the same data and links as _idold-doc_. Links to
those contents are visible from either document.

This request creates the document but does not open it for access; you must
issue an open request (see below) to access the data in the new document.

**open 35**

- mode* ::= `1'*read-only **delim
  *| `2'*read-write **delim

copy-switch* ::= `1'*fail-on-conflict **delim
*| `2'*copy-on-conflict\*
_delim_ | `3'\*always-copy
**delim

open iddoc\* _mode copy-switch_
_open idnew-doc
_| _error_

Open _iddoc_ for access using _mode_. *Mode
*can be _read-only_ or _read-write_. Read-only capability for
a document can be shared. Read-write capability is exclusive. Two situations
cause conflict: a request for write access on an already open document,
or a request for read access to a document already open _read-write_.
When contention arises, the backend can return a copy of the document or
fail. The _copy-switch_ determines the circumstances in which the backend
makes a copy. _iddoc_ and *idnew-doc *differ only if open makes a copy. Command descriptions
which require already open documents for their arguments will be so noted.
Open for read-write satisfies the requirement "Must be open for reading".

**close 36**

- close id\*_doc_
  _close_
  | _error_

Close _iddoc_. All opened documents must be closed.
Multiple opens of a document must balanced by the same number of close calls.
A loss of connection between the frontend and backend or a quit command
is the same as closing all documents and then doing a quit.

**create-link 27**

- create-link id**doc\*
  \*spec-set**from spec-setto spec-setthree\*

_create-link
idlink_ | _error_

Create a link with the specified end-sets and return its identifier. The
new link is appended to the link space of _iddoc_ . _iddoc_ is the home for
the _idlink_ . _iddoc_ must already be
open for writing.

\*\* Content Retrieval

\***\* retrieve-doc-vspan 14**

- retrieve-doc-vspan id\*_doc_
  _retrieve-doc-vspan
  vspan_ | _error_

Return the vspan describing the contents of _iddoc_ , including its links. The width of the span reflects
either the number of links or the number of data-bytes if there are no links.
_iddoc_ must already be open for reading.

**retrieve-doc-vspanset 1**

- retrieve-doc-vspanset id\*_doc_
  _retrieve-doc-vspanset
  number_ * [ *vspan\* ]

| _error_

Return a vspan describing each space in _iddoc_ . If either the data or link space is empty, its vspan
is left out. _iddoc_ must already be open for writing.

**retrieve-v 5**

- retrieve-v spec-set\*
  _retrieve-v number_ * [ *contents* ] | *error\*

Retrieve data and links from the backend. The spec-set can include document
identifiers, text ranges, and link identifiers. The information returned
follows the order of the spec-set. All the documents in *spec-set *must
be open for reading.

**follow-link 18**

- end-switch* ::= `1'*from\* _delim _|
  `2'*to **delim
*| `3'\*three \*\*delim

follow-link end-switch idlink\*
_follow-link spec-setend_ | _error_

Return an end-set of _idlink_ . *end-switch *determines
the end-set returned.

**retrieve-endsets 28**

- retrieve-endsets spec-set\*_contents_

\*retrieve-endsets
spec-setfrom spec-setto

spec-setthree *| *error\*

Describes where links attach to _contents_. Each returned spec-set
describes the union of all end-sets of the given type that attach to the
supplied _spec-setcontents_.

\*\* Connection Retrieval

\***\* find-links-from-to-three 30**

- home-spec* ::= *number\*
- [ *id**doc*]

- find-links-from-to-three spec-set**from
  spec-setto\* \*spec-set**three
  home-spec\*

- find-links-from-to-three number\* * [
  *idlink\* ]

| _error_

Return the IDs of all links whose end-sets overlap the given from, to, three,
and home set restrictions. All end-sets must satisfy their respective constraints.
A set containing the entire docuverse places no restriction.

**show-relations-of-2-versions 10**

- show-relations-of-2-versions
  spec-set\*_1 spec-set2_

- show-relations-of-2-versions number\*
- [ *shared-span* ]

| _error_

Structurally compare the two sets of contents. Return a list describing
the shared contents; i.e., contents derived from the same source through
versioning or edit operations. Identical sections entered independently
are not considered shared because they came from different sources. (See
the chapter "Versions".) All documents mentioned in the _spec-sets_
must be open for reading

**find-docs-containing 22**

- find-docs-containing spec-set\*

- find-docs-containing number\* * [ *iddoc\*
  ]

| _error_

Return identifiers for all documents that include any of the contents specified
by the argument. All documents with contents in _spec-set_ must be
open for reading.

\*\* Editing

\*\*Editing must be done within the backend to allow structural comparison
and proper interaction of editing operations and link connections.

**insert 0**

- insert id\*_doc_
  _vaddr number_ * [ *string* ]
  *insert* | *error\*

Insert text at *vaddr *in _iddoc_ . _iddoc_
must be open for writing.

**copy 2**

- copy id\*_doc_
  _vaddr spec-set_ _copy_ | _error_

Virtually copy the contents specified by the spec-set to _vaddr_ in
_iddoc_ . _iddoc_ must be open for writing. All documents with contents
in _spec-set_ must be open for reading.

**rearrange 3**

- cut-count* ::= `2'
  *delim *| `3' *delim *| `4' *delim

rearrange iddoc\* _cut-count_ * [ *vaddr* ]
*rearrange* | *error\*

Transpose large blocks of characters within _doc_. The number of vaddrs
(_cut-count_) determines the operation. If _cut-count_ equals
2, delete the contents from _vaddr1_ to _vaddr2_.
If _cut-count_ equals 3, swap the contents from _vaddr1_ to _vaddr2_ with the contents
from _vaddr2_ to _vaddr3_.
If cut-count equals 4, swap the contents from _vaddr1_
to _vaddr2_ with the contents from _vaddr3_
to _vaddr4_. The first vaddr specifying a range
must be less than or equal to the second vaddr for that range. _iddoc_
must be open for writing.

**delete-vspan 12**

- delete-vspan id\*_doc_
  _vspan_ _delete-vspan_ | _error_

Remove the bytes specified by _vspan_ from _iddoc_ . _iddoc_ must be open for
writing.

\*\* Session Control

\*\*Frontends and backends initially negotiate about the protocol
they will use. (The protocol negotiation for a session and some of the FeBe
commands are demonstrated in the chapter "FeBe Example".)

**quit 16**

- quit\* _quit_

Terminate the connection between the frontend and the backend. If appropriate,
the backend saves and terminates. Quit never returns an error.

**x-account 34**

- x-account id\*_account_
  _x-account_
  | _error_

The backend associates _account_ with the current connection and frontend.
It causes the current user to be considered the owner of _account_.
The multi-user backend requires that this command be sent from within the
standard login sequence. You can only login once per session.

\*\* Administration

\***\* create-node-or-account 38**

- create-node-or-account id\*_account_ \*create-node-or-account idaccount

- | _error_

Declare that _account_ is a legal account or node. If _account_
is an account tumbler, then the backend creates the account. If it is a
node tumbler, then the backend reassigns its own address to _account_.

\*\* Null Command

\***\* null-command -**

- delim \*

A delimiter sent by the frontend when the backend expects a command is ignored
by the backend.

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

_[contact us](../../contact.html)_
or [![](../../images/cmn.gif)](http://www.blindpay.com/crit-me-now.cgi)

[![Golden Key](../../images/key.gif)](http://www.privacy.org/ipc/) [![Blue Ribbon](../../images/ribbon.gif)](http://mirrors.yahoo.com/eff/blueribbon.html)
