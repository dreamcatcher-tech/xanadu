Versions

[![](../../images/logo.gif)](../../index.html)

**Versions**

---

\*\* Introduction

\*\*This chapter starts with a simple scenario that highlights the
need for a document open operation. It then develops the operation, adding
capability. The examples demonstrate the relation between the document open
operation and version creation. Finally, the version comparison operation
is discussed.

\*\*Why Versions?

\*\*The simplest example to show the need for an open operation is
simultaneous editing of a document by two authors. If they both edit the
same copy of the document, their conflicting changes could destroy it. The
first frontend to open the document edits the existing copy. Later frontends
must either fail or open a new virtual copy of the document (determined
by an argument to open). The virtual copy is equivalent to a new version
of the document, so later efforts to recombine the independent changes of
the two documents have the full support of the version comparison mechanism
(described below).

When the open operation makes a copy for the second writer, it copies the
state of the document as of the moment of the copy operation. This includes
all the changes made by the first author. This means that locks `created'
by the open operation are transparent to readers. The current transparency
of locking is acceptable because it only allows the owner of a document
to change the original version. Other users can make and edit their own
versions, but they cannot edit the original.

\*\*Read-only and Read-write

\*\*Since documents will often be opened just for reading, the open
operation supports two modes: read-only and read-write. The above example
uses read-write capability for both authors. Reading a document does not
modify the contents of a document, so multiple users can read a single copy
at the same time. If the document is opened for reading, writing to the
document is prevented. Otherwise a user could be trying to read a constantly
changing document.

The experimental frontend supports even more complex behavior. The frontend
initially opens documents for read-only. It assumes the typical case in
which users only wish to browse the information. Any user can start editing
the contents of a document, however. The frontend then closes the read-only
connection and opens the document again for writing. The reopening of the
document will fail if any other users were reading the same document, or
if any open operations on that document happened between the close and the
open operations. If the open fails, the frontend can open a new version
and redisplay the possibly modified contents.

\*\*Parallel Versions

\*\*When two authors separately edit different versions of the same
document, they create parallel versions. To recombine these into one version,
the authors must compare their versions to discover conflicting changes,
and regions unchanged by either author. Udanax Green's version comparison
operation describes the data shared by two documents due to operations which
explicitly copy contents. It describes the contents retained by parallel
versions from their mutual ancestor, the data retained by a sequential version
from its ancestor, or the contents copied from one document to another.

\*\*Comparison

\*\*The comparison operation does not compare the contents directly.
The version comparison operation must apply to ANY byte representable data.
Content comparison algorithms such as Unix diff use data-specific heuristics,
so they cannot possibly work for all types of data. Also, the topological
nature of connections in Udanax Green add differences to apparently identical
contents. For example, imagine a document which describes a particular database
record structure. The document contains enough spaces for every character
of every field. The frontend defines each field by attaching a link to the
characters in the field. The frontend can now rearrange the fields in a
record simply by swapping the contents. Like any editing process, the user
might want to compare alternatives, undo changes, or check differences between
the current and past versions. Content comparison reveals nothing. The Udanax
Green comparison operation shows the actual field differences.

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
