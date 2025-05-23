Links & Link Types



[![](../../images/logo.gif)](../../index.html)

**Links
and

Link Types**

---

The connection that
a link represents is defined by spec-sets called end-sets. Each link has
three end-sets: a from-set, a to-set, and a three-set. These three end-sets
are operationally the same, but by convention, links start at the from-set
and end at the to-set, and have a type as defined by their three-set.

Frontends create links by specifying the three end-sets and a document in
which to store the link. This document is the link's home document. The
address of the link within its home document is the link's global identifier.
Note that the home document and end-sets of a link are completely independent.
A link in a document could connect from the contents of another document
to the contents of still other documents.

Each link has a final, virtual property called its home-set. It is the set
of all documents that store the link in their link space. This initially
contains just the home document of the link, but editing and version creation
operations can cause a link to exist in more than one document.

**Link Types

**The current, unimaginative scheme for link typing simply associates
each type with a tumbler address. The three-set for a quote link, for example,
just contains the tumbler address associated with type "quote".
Below are listed the values used for the example Udanax Green system:



jump 1.1.0.1.0.2.0.2.1

quote 1.1.0.1.0.2.0.2.2

footnote 1.1.0.1.0.2.0.2.3

marginal note 1.1.0.1.0.2.0.2.4

Much more powerful conventions will completely replace this in the product
release.

The end-set used to designate a link's type is deliberately misnamed to
escape the assumption that a type is just a symbol. The simplest improvement
makes each type a document that stores a description of the uses and conventions
for the given type. In a more interesting example, type "quote"
refers to a set of documents with programs for presenting the link on a
variety of displays. Thus, a frontend could present a mathematical equation
as a graph, a musical score as sheet music, and digital audio as sound played
on a stereo.

**Link Matching

**Udanax Green supplies a very powerful operation for finding links.
The operation takes four spec-sets as arguments: one for each end-set and
one for the home-set. The arguments specify the contents within which the
appropriate end-set must attach. The operation returns all links whose from-set
intersects the first argument, whose to-set intersects the second argument,
whose three-set intersect the third argument, and whose home-set intersects
the fourth argument. The example shows the arguments used to find all the
places at which author A quotes other authors (or himself):



from-set: span of author A's documents

to-set the docuverse

three-set: the ID that specifies the `quote' type.

home-set: span of author A's documents

This returns all links of type `quote' that author A made from his documents
to anywhere within the docuverse. In the example, links were matched based
on their owner using the tumbler addressing architecture. The docuverse
(i.e., no restriction) can also be expressed with an empty spec-set. By
restricting the to-set to author B's documents rather than the entire docuverse,
the operation would return all the places at which author A quoted author
B.

Note that the link matching is an operation on the Udanax Green enfiladic
data structures and does NOT search through all the links in the docuverse!

**Link Interaction with Edits and Versions

**Links interact with edit operations and versions by staying attached
to the same contents, independent of their location. The chapter "Addressing"
described the derivation of a unique identity for each byte and link in
Udanax Green. Links connect to these objects rather than to the positions
of the objects within documents. A consequence of this is that inserted
bytes remain unconnected to links, even when inserted amidst a connected
group of bytes. The end-set of the link effectively splits to only include
the original characters. In the examples below, the italicized characters
are in the end-set of a link.



initial text *This text was already here...

* insert text *This text was al*inserted text *ready here...

* rearrange text *This text al*inserted *was *text *ready
here...*

Consistent interaction between links and editing operations requires that
the backend perform the editing operations. Frontends might be unaware of
all links attached to a particular span of bytes.







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
