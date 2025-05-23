Fe vs. Be

[![](../../images/logo.gif)](../../index.html)

**Fe
_vs._ Be**

---

\*\* Introduction

\*\*The frontend/backend distinction has several aspects: why is
there a distinction, how was the distinction made, and what is the distinction?

The frontend and backend separation supports multiple users and single users
with multiple applications. Supporting multiple users requires either that
they all communicate with the same hypertext engine (the backend) or that
they exercise some system dependent database locking scheme. Neither the
system dependence nor the clumsiness of locking schemes were acceptable.
Even the single user will require multiple applications. Imagine creating
pictures with one frontend, while annotating the pictures with textual descriptions
and background music, all in the same document! No single frontend can cope
with all the possibilities of multi-media.

In terms of clients and servers, the backend is a hypertext server and the
frontends are clients. This emphasizes the anonymity of the frontends to
the backend. We use the term "frontend" rather than "client"
to stress the user interaction and data generation supplied by frontends.

\*\*Separation of Functionality

\*\*The separation between the frontend and backend allows them to
run on the same or different machines. Thus, low-end computers can use the
full power of the Udanax Green backend over a network. More powerful computers
can run both frontend and backend concurrently.

The backend supports as much generality as possible, with as few concepts
as possible. For example, because the backend avoids all operations that
interpret the stored data, it can store and interconnect _any_ kind
of data, from text to PostScript, RenderMan protocol to digital video.

The backend avoids all operations that can be done equally well outside
of the backend. Searching operations are an example. The special retrieval
operations in the backend which seem like searching operations actually
derive their results from the proprietary data-structures, without searching.
Since the FeBe Protocol follows a remote procedure call style, a frontend
and backend on the same machine can easily transfer massive amounts of data.
With the addition of application specific knowledge, frontends can search
faster than the backend possibly could.

\*\*Avoiding Premature Rules

\*\*Finally, the backend encourages the evolution of conventions,
rather than entrenching premature rules. Link types, for example are quite
general. Most existing hypertext type systems declare a fixed set of link
types. The Udanax Green system does not even specify the nature of a link
type, let alone the specific set of possible types. No solution by fiat
could possibly cope with the newly available and continually evolving media,
market needs, etc. The current list of areas for evolution are:

- frontend interaction conventions - what metaphors will present
  a document most intuitively?

- the nature of link types - will they be constants, pieces of code,
  etc.?

- specific link types - quote, reference, retraction, refutation?

- document topologies - how will documents typically be structured?

\*\*Where Do We Go From Here?

\*\*The chapter "Technical Overview" discusses the concepts
implemented by the backend. Only operations to support versions, links,
multi-user access, and comparison are included in the backend. The current
facilities will evolve, both in capability and in generality. Below is a
partial list of planned extensions.

- generalized data-space: two, three, and n dimensional

- time, timestamps, etc in the versions system

- editable links

- sophisticated access control

- historical trace documents which contain the edit and version
  history of other documents

- mechanism for charging royalties for access to links or documents.

This list will rapidly grow as we receive customer suggestions.

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
