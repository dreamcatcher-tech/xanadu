# Udanax Concept Dictionary

## account

An account is the system's representation of a user. The account includes that
users' [documents](#document). Users can have multiple accounts.
([source](../md/green/febe/glossary.md))

## Be

Short for [backend](#backend). ([source](../md/green/febe/glossary.md))

## backend

One of two high-level modules required for a Udanax Green hypertext system. The
backend is responsible for document and version storage, link management and
editing. In many installations it will run on a more powerful computer networked
to the individual workstation where users work. (See [frontend](#frontend).)
([source](../md/green/febe/glossary.md))

## data-byte

The smallest addressable unit of storage in the Udanax Green FeBe Protocol. A
data-byte is an eight bit unsigned binary number.
([source](../md/green/febe/glossary.md))

## data space

The part of a [document](#document) that contains arbitrary data, supplied by
the user or front-ends. The other space in [documents](#document) is the
[link space](#linkslink-space). ([source](../md/green/febe/glossary.md))

## document

A block of information in a [hypermedia](#hypermedia) information pool that is
thematically unified. Such documents resemble contemporary paper documents
except that clips of animation, pictures, and sound tracks may also be
documents. Also, in fully integrated hypermedia systems, the typical document
will likely be smaller in size - closer to the length of an article in a
newspaper than to the length of a book. ([source](../md/green/febe/glossary.md))

## docuverse

The abstract address space that contains all Udanax Green objects.
([source](../md/green/febe/glossary.md))

## end-set

The sets that describe links. Each link has three end-sets: a
[from-set](#from-set), a [to-set](#to-set), and a [three-set](#three-set). The
three end-sets are operationally the same, but by convention, links start at the
[from-set](#from-set) and end at the [to-set](#to-set), and have a type as
defined by their [three-set](#three-set). Each link also has a
[home-set](#home-set). ([source](../md/green/febe/glossary.md))

## Fe

Short for [frontend](#frontend). ([source](../md/green/febe/glossary.md))

## FeBe Protocol

[Frontends](#frontend) communicate with the [backend](#backend) using a
standard, public protocol called FeBe (stands for &quot;Frontend Backend&quot;).
Other sections of this package describe the preliminary protocol used by the
current system. ([source](../md/green/febe/glossary.md))

## from-set

The set of elements from which a link `starts'. (See [end-set](#end-set).)
([source](../md/green/febe/glossary.md))

## frontend

One of the two high-level modules required for a multi-user Udanax Green
hypertext system. The frontend is responsible for presenting the information
from [the backend](#backend) to the user on his or hers workstation. (See
[backend](#backend).) It supports users in reading, creating, and editing
information. ([source](../md/green/febe/glossary.md))

## home-set

The set of [documents](#document) that actually contain a given link in their
contents. Note that the home of a [document](#document) is independent from any
of its [end-sets](#end-set). ([source](../md/green/febe/glossary.md))

## hypertext

Any form of non-linear writing. This includes paper mechanisms such as table of
contents and indexes. Computerized hypertext allows readers to navigate through
large quantities of information. ([source](../md/green/febe/glossary.md))

## hypermedia

Everything that [hypertext](#hypertext) does, but NOW IMPROVED! NOW WITH
PICTURES, ANIMATION, AND SOUND! ([source](../md/green/febe/glossary.md))

## ID

A global [tumbler](#tumbler) address of [a document](#document), link,
[data-byte](#data-byte), etc. The ordering of the addresses groups related
things. For example, the [documents](#document) of a single user have contiguous
addresses. ([source](../md/green/febe/glossary.md))

## links:link space

The part of a [document](#document) in which links reside. The other space is
the [data space](#data-space). ([source](../md/green/febe/glossary.md))

## node

A running Udanax Green [backend](#backend), and all information it contains.
([source](../md/green/febe/glossary.md))

## span

An span specifies a range of [tumblers](#tumbler) with a starting
[tumbler](#tumbler) and a [tumbler width](#width). The span includes all
[tumblers](#tumbler) between the start inclusive and the start plus the width
exclusive. (See the chapter &quot;Tumbler Arithmetic&quot;.) Because of the
uniformity of addressing, spans can represent ranges of
[data-bytes](#data-byte), links, [documents](#document), and even users.
([source](../md/green/febe/glossary.md))

## spec

Many of the FeBe operations use a set of specs to specify a set of arbitrary
Udanax Green objects. A spec is either a [span](#span) of globally addressed
elements like [documents](#document), or a [document identifier](#document) and
a set of [vspans](#vspan) (document local spans).
([source](../md/green/febe/glossary.md))

## three-set

The [end-set](#end-set) which determines the type of a link, by convention.
([source](../md/green/febe/glossary.md))

## to-set

The [end-set](#end-set) which a link points to, by convention.
([source](../md/green/febe/glossary.md))

## tumbler

Tumblers are multi-part ordinal numbers similar to the Dewey Decimal System. For
example, 1.0.34.5 and 123.56.87.1.1.3.4 are both tumblers. Since they can expand
at any point, a numbering system based on them never runs out of precision.
Udanax Green uses tumblers for all address to allow any number of
[nodes](#node), users, [documents](#document), [data-bytes](#data-byte), and
links. (See the chapters &quot;Addressing&quot; and &quot;Tumbler
Arithmetic&quot;.) ([source](../md/green/febe/glossary.md))

## vspan

A vspan describes a range of the contents of a single [document](#document).
Like a [span](#span), a vspan has a start and [width](#width)
[tumblers](#tumbler). The tumblers are relative to the [document](#document),
however. The vspan designates everything between the start tumbler inclusive and
the start plus the width exclusive. The width can cross the boundaries of space
within the [document](#document). (See the chapter &quot;Addressing&quot;.)
([source](../md/green/febe/glossary.md))

## width

The size of a [span](#span); the sum of the origin [tumbler](#tumbler) and width
[tumbler](#tumbler) is the first thing past the end of the [span](#span).
([source](../md/green/febe/glossary.md))

## Udanax Green

A [hypertext](#hypertext) [backend](#backend) designed to allow multiple
concurrent users to have fast retrieval and update of hypertext information
pools of unbounded size. ([source](../md/green/febe/glossary.md))

## Udanax Green:Udanax Green objects

[Nodes](#node), [accounts](#account), [documents](#document), links, and
[data-bytes](#data-byte) are all objects in the Udanax Green address space (also
called &quot;the [docuverse](#docuverse)&quot;).
([source](../md/green/febe/glossary.md))

## canopy

A balanced binary tree structure of CanopyCrums used in Udanax Gold to propagate
property changes and manage recorders. ([source](../md/history/index.md))

## detector

An object clients register to receive callbacks when editions or range elements
change, such as when placeholders are filled. ([source](../md/history/index.md))

## coordinate space system

A general framework defining positions, regions, mappings, and order
specifications that describe the domain of tables.
([source](../md/gold/download/index.md))

## enfilade

The tree-based data structure underlying Xanadu storage, allowing efficient
versioned documents and [transclusion](#transclusion).
([source](../md/history/index.md))

## The Ent

A more advanced implementation of [enfilade](#enfilade) concepts developed for
Udanax Gold. ([source](../md/gold/index.md))

## transclusion

The reuse of content by reference to its original location so the same material
can appear in many contexts without duplication. ([source](../md/green/index.md))

## FAQ

A compilation of "Frequently Asked Questions" about the Xanadu Project that
collects answers for new readers. ([source](../md/FAQ.md#1-what-is-xanadu))

## The Information Future

An overview of Xanadu's vision for the future of
[hypermedia](#hypermedia) publishing and how authors, readers and
publishers might interact. ([source](../md/future.md#transpublication))

## The Xanadu Ideal

Ted Nelson's statement of principles describing how Xanadu differs from other
[hypertext](#hypertext) systems. ([source](../md/ideal.md#why-do-they-call-us-a-cult))


## Inforights

Also known as the "Bill of Information Rights," this text proposes a framework
for open [hypermedia](#hypermedia) publishing through contractual
agreements. ([source](../md/inforights.md#bill-of-information-rights))

## automatic royalty

The policy that each byte delivered from a publication triggers a small
royalty payment to the original publisher. ([source](external/future.html))

## connected literature

An interconnected network of documents enabled by
[transclusion](#transclusion), allowing readers to traverse a shared
[docuverse](#docuverse). ([source](external/future.html))

## context relinquishment

The practice of permitting a work to appear in unpredictable contexts in
exchange for royalty and credit. ([source](external/transcopy.html))

## hypernaut

A reader exploring the Xanadu universe through following links from document to
document. ([source](external/inforights.html))

## open hypermedia publishing

Xanadu's approach where anyone may link to and re-use materials across the
network, combining all media forms. ([source](external/future.html))

## receipt token

A record provided to users so they can prove what material they have purchased
and stored. ([source](external/inforights.html))

## repository network

The networked storage and delivery system planned for Xanadu to distribute
copyrighted media on demand. ([source](external/future.html))

## transpublication

Publishing by reference so quoted material is fetched from its original
publisher, who receives the royalty. ([source](external/future.html))

## virtual republication

Republishing digital material by transmitting a purchase address instead of the
bytes themselves. ([source](external/transcopy.html))

## World Publishing Repository

Ted Nelson's term for the Xanadu system envisioned as a universal bookstore
built around links rather than text search. ([source](external/ideal.html))

## Xanadu paradigm

The overarching model for computing based on sideways connections among
documents, enabling open electronic publishing. ([source](external/faq.html))

## transcopyright

A permission system proposed by Ted Nelson that allows republication of digital
materials while tracking ownership and crediting authors. ([source](../md/transcopy.md#summary))

