Implementation



[![](../../images/logo.gif)](../../index.html)

**Implementation**

---

How does our implementation fit
the demands
of the philosophy and motivation? The major elements of the
implementation
are:

* Links

* Versions

* Unbounded information pools

* Support for cooperating users

**Links

**Links, more than any other feature, build and maintain
the web
of context.

We decided that the essential features were:

* The ability to do extremely fine-grained linking

* The ability to do complex linking

* Allowing the frontend to define and interpret the
meaning of links

* The ability to follow links bidirectionally. The ability
to enter
and exit documents quickly when following links.

* The preservation of links across edits.

**Fine-grained Linking

**

In literature, footnotes and quotes may specify a single word.
Hypertext
should provide similar or superior fine-grain linking: linking to
a particular
word or to a single number. "Chunky" hypertext only
allows you
to link to larger collections of data (such as "cards"
in HyperCard).
The reader must then try to find the one relevant piece of
information within
the "chunk".

Clearly the writer must be able to link to individual bytes. Such
linking
should be at the writer's discretion. Rather than forcing linking
according
to some predefined hierarchy the writer should decide exactly what
is included
as the end of a link.

**Complex Linking

** Letting the writer decide exactly what is included as
the end
of a link means providing as much flexibility as possible. The
ability to
freely and flexibly construct links means being able to:

* link within documents.

* link between documents. Example: a scholar writes a new
interpretation
of ancient Greek society, with numerous quotations from
the writings
of those times. The scholar could draw links from those
quotes to
the original texts, allowing the reader to follow the link
and see
the quote in situ.

* link to other links. Text itself or whole documents are
not the
only things to be linked. Links themselves have
information content
on which people might wish to comment.

* group disjoint sets of text, i.e., select a span of
text, a span
of links or a span of documents and define them as a
single unit
to form one end of a link. (The set of objects that form
one end
of a link is known as an "end-set".) On a small
scale,
this gives the same capability as when an ellipsis links
disjoint
text: "She said...that she would do it." On a
larger scale,
there could be a link whose end-set would be the span of
all the
documents written by Brian Kernighan. Or, you could
assemble a link
that had a set of disjoint spans as an end-set, such as
everything
written by Brian Kernighan and everything written by Doug
Engelbart.

**Identifying the Meaning of Links

** As the amount of connected material begins to grow, we
need
ways to clarify and identify links to avoid being lost in the
webbed information.
Where is a link from? Where is the link to? What type of link is
it: a quotation,
a refutation, a footnote, a bibliographic reference, a
bibliographic collection,
etc.? We gave the frontend the ability to choose whether to answer
these
questions and what meaning to give the answers.

Why didn't we define a series of link types ourselves? It would
make things
simpler if Udanax itself decided on a fixed set of link types. But
we also
realize that we couldn't possibly know or conceive of every kind
of connection
people would want to make. We will advocate certain conventions so
things
written by one system are readable by another, but we will not
enforce any
policies.

**

Bidirectional Links

** Links need to be at least bidirectional. In other
words, when
a link is created, the reader can go in either direction. Of
course you'd
want to be able to go from a document to a critique of that
document. But
imagine the person stumbling by chance into an ongoing heated
technical
debate. He'd want to follow links backward along the chain of
creation to
read source documents or trace the line of debate.

Bidirectional links fulfill the scholar's greatest fantasy: if an
author
creates references pointing backward to earlier works, the readers
of those
earlier works can follow the reference forward and find the later
writings.

Udanax links are actually more powerful than bidirectional links.
This greater
power is discussed later in this document.

**Stability Across Changes

** Information is dynamic. Documents have to be editable,
and you
want the links to survive the editing process still connected to
their material.
You do not want the user to be referred back to some previous
generation
of document when the link was first made, or referred to whatever
text happens
to be at the link's original location in the document.

Maintaining connectivity across edits is a very difficult
technical problem.
Its difficulty has led others to resort to "chunky"
hypertext
in which all you can do is link to an entire document or to a
point in a
hierarchy. This means that links can't represent the real
semantics of desired
connections.

In Udanax Green, the links survive editing, rearranging, and
changing. They
stay connected to the material they were connected to originally.
The link
will show where rearranged material is now appearing in the
document.

**Versions
**

Besides links, there are three
other key
features of the Udanax Green implementation: versions, unbounded
information
pools, and support for multiple users.

Versioning gives us context on material over time and through
changes. Even
relatively stable forms such as books go through drafts, versions,
editions,
modifications for publication in different formats. Versions arise
and are
maintained when several possible plans or variants of designs are
created
to suit different needs or eventualities.

In its most mundane form, version control is a frustrating
problem: what
do you name this backup copy? where do you put it? how do you know
which
version had the information this way or that way? But often, our
need for
versions is acute, as when we desperately wish to be able to go
back in
time and restore a document to an earlier state.

Our "version compare" differs from the heuristic-driven
content
comparison such as the Unix command "diff". Version
compare traces
the lineage of the actual bytes and tells how two versions differ
according
to the edits that resulted in two documents.

**Unbounded Information Pools

**Udanax's motivation is to allow users to construct and
use information
pools of unlimited size. Much software fails because it doesn't
scale. Many
systems that are obviously just too small are still 10 times the
maximum
size that the system creator imagined anyone would ever possibly
want. We
knew we weren't creative enough to imagine the largest thing
someone might
want to do with the Udanax software. So we did a design that would
keep
working as things scaled beyond our imaginations.

This decision had interesting implications for edits: what if
someone wants
to insert an extra word at the front of a document the size of
*War and
Peace* - how would we handle the overhead of moving everything
that followed?
So in our system, unlike in traditional systems, when you edit by
inserting,
deleting or rearranging, the rest of the document is left in
place.

Tumbler addressing is an example of how we have designed Udanax
Green to
allow maximal scaling. Each document in the system has a unique
address.
If some years from now many Udanax Green systems were to be
interconnected,
no confusion would result.

**Cooperating Users**

Existing and planned features are
designed
to make Udanax Green good at enhancing the diversity that results
from "social"
computing: collaborative editing, electronic mail, and computer
conferencing.

We support collaboration by forking versions of documents. As in a traditional
file system, the frontend opens a document and reserves a consistent view
of that document. Traditional systems can't resolve the conflict of two
users writing to the same document at the same time. Udanax Green simply
creates a version for each writer, and then provides the facilities to resolve
any conflicts.







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
