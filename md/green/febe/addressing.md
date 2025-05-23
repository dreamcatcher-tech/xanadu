Addressing



[![](../../images/logo.gif)](../../index.html)

**Addressing**

---

Every object in the Udanax Green
backend has a unique global address that functions as the object's identifier.
This chapter identifies the objects that can be addressed in the backend,
and describes the generation of their addresses.

**Tumbler

**All addresses in Udanax Green are *tumblers*. Tumblers
are multi-part ordinal numbers similar to Dewey Decimal numbers. For example,
2.4.23 and 45.6.72 are both tumblers. Each period separated number is
called a tumbler digit. The digits of a tumbler (leftmost first) exactly
describe the path to a specific point in a tree. Udanax Green address
tumblers use the zero tumbler digit only to separate concatenated fields
within the tumbler. This will be shown below.

Tumblers are
transmitted in a compressed format within the FeBe Protocol.
Example tumblers in this chapter do *not* use that representation.

**Node

**Each running backend is called a node in anticipation of an interconnected
network of Udanax Green backends. Each node has a unique tumbler that positions
it in an abstract global address space called the *docuverse*. Since
node addresses are tumblers, any node could give addresses to new nodes
by appending another tumbler digit to its own tumbler address. For example,
node 23.4 could create nodes 23.4.1, 23.4.2, 23.4.3, etc.

**Account

**Each node has account*s* for any number of users. Each account
on a single node is identified by a tumbler. Udanax Green currently makes
no use of the potential hierarchy of accounts. The global address of an
account is the concatenation of the node's address, the tumbler separator,
and the account's tumbler. The separator allows any number of tumbler digits
for the node address.

**Document

**Accounts contain any number of document*s*. New documents
are numbered sequentially for each account. Addresses for versions get allocated
like addresses for nodes: the first new version adds a tumbler digit. Each
successive version increments the last digit. Each of these new versions
can create versions of their own by adding more digits. The global address
of any document is created by concatenating the global address of the document's
account, the zero tumbler, and the document's address relative to its account.

**Data-Bytes and Links

**

The final level of addressing is for the contents of documents. Documents
have two spaces, the data space for storing raw data such as text and pictures,
and the link space for storing document interconnections. Characters and
links are addressed within a document by a two digit tumbler. The first
digit identifies the space (data=1, links=2); the second identifies the
position within that space. Thus, the thirty-ninth character has address
1.39 whereas the fourth link has the address 2.4. As above, global addresses
for characters and links are made by appending (with a separator) their
addresses to the global address of their home document - the document in
which they were created. The home document is unique, even though edit operations
and versioning can copy a link to many documents.

All addresses used in the FeBe Protocol are global except addresses used
in some commands that stay within the bounds of a single document. These
addresses, called vaddresses, are relative to the document, and so have
only two digits. The containing document is supplied as a separate argument.
For historical reasons, document relative terms are annotated with 'v'.

**Groups of Udanax Green Objects

**Groups of objects can be referred to with spans, vspans, and
spec-sets. A span represents a range of global tumbler addresses. A vspan
is a range of addresses relative to a single document. A spec-set is a list
of spans or vspans (with an associated document identifier). Spec-sets allow
specification of an arbitrarily complex set of Udanax Green objects.

Spans are represented with a start tumbler and a width tumbler. The start
tumbler is the address of the first thing in the span. The start tumbler
plus the width tumbler (see "[Tumbler Arithmetic](tumblers.html)")
is the address of the first thing *not* included in the span.

Vspans are built from document relative tumblers (vaddresses). Thus, the
entire data space of a document is in the vspan with a start of 1.1 and
a width of 1 . This vspan covers from the first data-byte data up to but
not including the first link.

**Tumbler Ordering

**Tumblers are ordered similar to real number fractions. For example,
4 < 4.23 < 4.23.7 < 4.24 < 5. Thus, a single span could cover
all the documents for a given account, all the accounts (and their documents)
for a given node, all the versions of a particular document, etc. Because
addresses at every level of the hierarchy are just tumblers, spans can cover
characters, links, documents, versions, or any other Udanax Green entities,
including the entire docuverse.







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
