# Udanax Concept Dictionary

## account

An account is the system's representation of a user. The account includes that
users' [documents](#document). Users can have multiple accounts.
([source](green/febe/glossary.html))

## Be

Short for [backend](#backend). ([source](green/febe/glossary.html))

## backend

One of two high-level modules required for a Udanax Green hypertext system. The
backend is responsible for document and version storage, link management and
editing. In many installations it will run on a more powerful computer networked
to the individual workstation where users work. (See [frontend](#frontend).)
([source](green/febe/glossary.html))

## data-byte

The smallest addressable unit of storage in the Udanax Green FeBe Protocol. A
data-byte is an eight bit unsigned binary number.
([source](green/febe/glossary.html))

## data space

The part of a [document](#document) that contains arbitrary data, supplied by
the user or front-ends. The other space in [documents](#document) is the
[link space](#linkslink-space). ([source](green/febe/glossary.html))

## document

A block of information in a [hypermedia](#hypermedia) information pool that is
thematically unified. Such documents resemble contemporary paper documents
except that clips of animation, pictures, and sound tracks may also be
documents. Also, in fully integrated hypermedia systems, the typical document
will likely be smaller in size - closer to the length of an article in a
newspaper than to the length of a book. ([source](green/febe/glossary.html))

## docuverse

The abstract address space that contains all Udanax Green objects.
([source](green/febe/glossary.html))

## end-set

The sets that describe links. Each link has three end-sets: a
[from-set](#from-set), a [to-set](#to-set), and a [three-set](#three-set). The
three end-sets are operationally the same, but by convention, links start at the
[from-set](#from-set) and end at the [to-set](#to-set), and have a type as
defined by their [three-set](#three-set). Each link also has a
[home-set](#home-set). ([source](green/febe/glossary.html))

## Fe

Short for [frontend](#frontend). ([source](green/febe/glossary.html))

## FeBe Protocol

[Frontends](#frontend) communicate with the [backend](#backend) using a
standard, public protocol called FeBe (stands for &quot;Frontend Backend&quot;).
Other sections of this package describe the preliminary protocol used by the
current system. ([source](green/febe/glossary.html))

## from-set

The set of elements from which a link `starts'. (See [end-set](#end-set).)
([source](green/febe/glossary.html))

## frontend

One of the two high-level modules required for a multi-user Udanax Green
hypertext system. The frontend is responsible for presenting the information
from [the backend](#backend) to the user on his or hers workstation. (See
[backend](#backend).) It supports users in reading, creating, and editing
information. ([source](green/febe/glossary.html))

## home-set

The set of [documents](#document) that actually contain a given link in their
contents. Note that the home of a [document](#document) is independent from any
of its [end-sets](#end-set). ([source](green/febe/glossary.html))

## hypertext

Any form of non-linear writing. This includes paper mechanisms such as table of
contents and indexes. Computerized hypertext allows readers to navigate through
large quantities of information. ([source](green/febe/glossary.html))

## hypermedia

Everything that [hypertext](#hypertext) does, but NOW IMPROVED! NOW WITH
PICTURES, ANIMATION, AND SOUND! ([source](green/febe/glossary.html))

## ID

A global [tumbler](#tumbler) address of [a document](#document), link,
[data-byte](#data-byte), etc. The ordering of the addresses groups related
things. For example, the [documents](#document) of a single user have contiguous
addresses. ([source](green/febe/glossary.html))

## links:link space

The part of a [document](#document) in which links reside. The other space is
the [data space](#data-space). ([source](green/febe/glossary.html))

## node

A running Udanax Green [backend](#backend), and all information it contains.
([source](green/febe/glossary.html))

## span

An span specifies a range of [tumblers](#tumbler) with a starting
[tumbler](#tumbler) and a [tumbler width](#width). The span includes all
[tumblers](#tumbler) between the start inclusive and the start plus the width
exclusive. (See the chapter &quot;Tumbler Arithmetic&quot;.) Because of the
uniformity of addressing, spans can represent ranges of
[data-bytes](#data-byte), links, [documents](#document), and even users.
([source](green/febe/glossary.html))

## spec

Many of the FeBe operations use a set of specs to specify a set of arbitrary
Udanax Green objects. A spec is either a [span](#span) of globally addressed
elements like [documents](#document), or a [document identifier](#document) and
a set of [vspans](#vspan) (document local spans).
([source](green/febe/glossary.html))

## three-set

The [end-set](#end-set) which determines the type of a link, by convention.
([source](green/febe/glossary.html))

## to-set

The [end-set](#end-set) which a link points to, by convention.
([source](green/febe/glossary.html))

## tumbler

Tumblers are multi-part ordinal numbers similar to the Dewey Decimal System. For
example, 1.0.34.5 and 123.56.87.1.1.3.4 are both tumblers. Since they can expand
at any point, a numbering system based on them never runs out of precision.
Udanax Green uses tumblers for all address to allow any number of
[nodes](#node), users, [documents](#document), [data-bytes](#data-byte), and
links. (See the chapters &quot;Addressing&quot; and &quot;Tumbler
Arithmetic&quot;.) ([source](green/febe/glossary.html))

## vspan

A vspan describes a range of the contents of a single [document](#document).
Like a [span](#span), a vspan has a start and [width](#width)
[tumblers](#tumbler). The tumblers are relative to the [document](#document),
however. The vspan designates everything between the start tumbler inclusive and
the start plus the width exclusive. The width can cross the boundaries of space
within the [document](#document). (See the chapter &quot;Addressing&quot;.)
([source](green/febe/glossary.html))

## width

The size of a [span](#span); the sum of the origin [tumbler](#tumbler) and width
[tumbler](#tumbler) is the first thing past the end of the [span](#span).
([source](green/febe/glossary.html))

## Udanax Green

A [hypertext](#hypertext) [backend](#backend) designed to allow multiple
concurrent users to have fast retrieval and update of hypertext information
pools of unbounded size. ([source](green/febe/glossary.html))

## Udanax Green:Udanax Green objects

[Nodes](#node), [accounts](#account), [documents](#document), links, and
[data-bytes](#data-byte) are all objects in the Udanax Green address space (also
called &quot;the [docuverse](#docuverse)&quot;).
([source](green/febe/glossary.html))

## canopy

A balanced binary tree structure of CanopyCrums used in Udanax Gold to propagate
property changes and manage recorders. ([source](history/index.html))

## detector

An object clients register to receive callbacks when editions or range elements
change, such as when placeholders are filled. ([source](history/index.html))

## coordinate space system

A general framework defining positions, regions, mappings, and order
specifications that describe the domain of tables.
([source](gold/download/index.html))

## enfilade

The tree-based data structure underlying Xanadu storage, allowing efficient
versioned documents and [transclusion](#transclusion).
([source](history/index.html))

## The Ent

A more advanced implementation of [enfilade](#enfilade) concepts developed for
Udanax Gold. ([source](gold/index.html))

## transclusion

The reuse of content by reference to its original location so the same material
can appear in many contexts without duplication. ([source](green/index.html))
