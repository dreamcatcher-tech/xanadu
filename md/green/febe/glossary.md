Appendix D - Glossary

[![](../../images/logo.gif)](../../index.html)

\*\*Appendix
D

Glossary\*\*

---

** account** An account is the system's representation
of a user. The account includes that users' documents. Users
can have multiple accounts.

** Be** Short for backend.

** backend** One of two high-level modules required for
a Udanax Green hypertext system. The backend is responsible
for document and version storage, link management and editing.
In many installations it will run on a more powerful computer
networked to the individual workstation where users work.
(See "frontend".)

** data-byte** The smallest addressable unit of storage
in the Udanax Green FeBe Protocol. A data-byte is an eight
bit unsigned binary number.

** data** **space** The part of a document that contains
arbitrary data, supplied by the user or front-ends. The
other space in documents is the link space.

** document** A block of information in a hypermedia
information pool that is thematically unified. Such documents
resemble contemporary paper documents except that clips
of animation, pictures, and sound tracks may also be documents.
Also, in fully integrated hypermedia systems, the typical
document will likely be smaller in size - closer to the
length of an article in a newspaper than to the length of
a book.

** docuverse** The abstract address space that contains
all Udanax Green objects.

** end-set** The sets that describe links. Each link
has three end-sets: a from-set, a to-set, and a three-set.
The three end-sets are operationally the same, but by convention,
links start at the from-set and end at the to-set, and have
a type as defined by their three-set. Each link also has
a home-set.

** Fe** Short for frontend.

** FeBe Protocol** Frontends communicate with the backend
using a standard, public protocol called FeBe (stands for
"**F**ront**e**nd **B**ack**e**nd").
Other sections of this package describe the preliminary
protocol used by the current system.

** from-set** The set of elements from which a link `starts'.
(See "end-set".)

** frontend** One of the two high-level modules required
for a multi-user Udanax Green hypertext system. The frontend
is responsible for presenting the information from the backend
to the user on his or hers workstation. (See "backend".)
It supports users in reading, creating, and editing information.

** home-set** The set of documents that actually contain
a given link in their contents. Note that the home of a
document is independent from any of its end-sets.

** hypertext** Any form of non-linear writing. This includes
paper mechanisms such as table of contents and indexes.
Computerized hypertext allows readers to navigate through
large quantities of information.

** hypermedia** Everything that hypertext does, but NOW
IMPROVED! NOW WITH PICTURES, ANIMATION, AND SOUND!

** ID** A global tumbler address of a document, link,
data-byte, etc. The ordering of the addresses groups related
things. For example, the documents of a single user have
contiguous addresses.

The component of a hypertext document that describes and
maintains interconnections between blocks of information.
In Udanax Green a link has three parts. (For a complete
explanation, please read the chapter "Links and Link
Types".) Frequently, however, the pieces have the following
usage: the from-set describes the block of information from
which the link originates, the to-set describes the block
of text to which the origin is linked, and the three-set
describes the link's type.

** links:link space** The part of a document in which
links reside. The other space is the data space.

** node** A running Udanax Green backend, and all information
it contains.

** span** An span specifies a range of tumblers with
a starting tumbler and a tumbler width. The span includes
all tumblers between the start inclusive and the start plus
the width exclusive. (See the chapter "Tumbler Arithmetic".)
Because of the uniformity of addressing, spans can represent
ranges of data-bytes, links, documents, and even users.

** spec** Many of the FeBe operations use a set of specs
to specify a set of arbitrary Udanax Green objects. A spec
is either a span of globally addressed elements like documents,
or a document identifier and a set of vspans (document local
spans).

** three-set** The end-set which determines the type
of a link, by convention.

** to-set** The end-set which a link points to, by convention.

** tumbler** Tumblers are multi-part ordinal numbers
similar to the Dewey Decimal System. For example, 1.0.34.5
and 123.56.87.1.1.3.4 are both tumblers. Since they can
expand at any point, a numbering system based on them never
runs out of precision. Udanax Green uses tumblers for all
address to allow any number of nodes, users, documents,
data-bytes, and links. (See the chapters "Addressing"
and "Tumbler Arithmetic".)

A document initially created as a virtual copy of some other
document.

** vspan** A vspan describes a range of the contents
of a single document. Like a span, a vspan has a start and
width tumblers. The tumblers are relative to the document,
however. The vspan designates everything between the start
tumbler inclusive and the start plus the width exclusive.
The width can cross the boundaries of space within the document.
(See the chapter "Addressing".)

** width** The size of a span; the sum of the origin
tumbler and width tumbler is the first thing past the end
of the span.

** Udanax Green** A hypertext backend designed to allow
multiple concurrent users to have fast retrieval and update
of hypertext information pools of unbounded size.

** Udanax Green:Udanax Green objects** Nodes, accounts,
documents, links, and data-bytes are all objects in the
Udanax Green address space (also called "the docuverse").

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
