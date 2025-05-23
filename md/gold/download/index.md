Udanax Gold Download Page

[![](../../images/logo.gif)](../../index.html)

\*\*Download

Udanax Gold\*\*

---

# _Opening Date not yet set_

The files available for download from this page are covered
by [The Udanax Open-Source License](../../license.html), which
you may want to read before proceeding.

The two download files, [udanax-top.st](udanax-top.st)
and [udanax-spaces.st](udanax-spaces.st), are not yet usable
without heroic effort. They are in the form of Smalltalk fileouts from
a ParcPlace 2.5a Smalltalk system heavily modified by us. In particular,
we enhanced the system to automatically translate from a modified subset
of Smalltalk, which we called XTalk, to a corresponding heavily macro-ized
subset of C++ we called X++. This Smalltalk fileout came from this modified
system, and will not filein to a normal Smalltalk system without a lot
of work.

-

[udanax-top.st](udanax-top.st) contains all the Smalltalk
code for the backend which was shared by translation between the Smalltalk/XTalk
environment and C++/X++ environment. In particular, all the Ent data
structures and algorithms are here.

-

[udanax-spaces.st](udanax-spaces.st) contains the most
interesting self-contained subset of udanax-top.st -- the coordinate
space system. This set of abstractions should have wide applicability
outside of hypertext. Indeed, the IntegerSpaces from Udanax Gold have
already been incorporated into the [E](http://www.erights.org)
language.

-

[xugold.tar](xugold.tar) (33MB) contains the C++ backend
as a whole. This can be read and run without intellectual
property problems, or major technical problems. However, since
major portions of it are the result of automatic translation
from Smalltalk, this code is not maintainable. Think of
these portions as compiler output (though it's not quite
that bad).

Remaining pieces that will be posted soon:

-

The C++ macros, tools, and libraries for turning C++ into X++. This
includes

- A non-conservative incremental generational collector for C++

- A transactional persistent object system for C++ object groups

-

A proxy/stub generator for remote method invocation, with a message
pipelining of much influence on the [Joule](http://www.agorics.com/joule.html)
and [E](http://www.erights.org) languages.

-

Corresponding Smalltalk tools and libraries for turning Smalltalk
into the semantically matching XTalk, including

- A similar persistent object system

- A similar stub generator.

More difficult to extract and post, because of the intellectual property
entanglements explained [here](../index.html), is

-

The "Browser Hacks", an extensive set of enhancements
to the Smalltalk browsing environment, enabling one to manipulate
a large body of code with an ease none of us have experienced since.
Fortunately, none of the rest of the system depends on these browser
hacks.

- The Smalltalk-to-C++ (or XTalk-to-X++) translator itself. Most of
  this is un-entangled new code, but some crucial pieces are entangled.

---

[![](../../images/logo.gif)](../../index.html)

[green](../../green/index.html)
[gold](../index.html)
[FAQ](../../FAQ.html)
[discussion](../../discussion/index.html)

[download](../../green/download/index.html)
[download](index.html)
[history](../../history/index.html)
[Related Sites](../../related.html)

_[contact us](../../contact.html)_
or [![](../../images/cmn.gif)](http://www.blindpay.com/crit-me-now.cgi)

[![Golden Key](../../images/key.gif)](http://www.privacy.org/ipc/) [![Blue Ribbon](../../images/ribbon.gif)](http://mirrors.yahoo.com/eff/blueribbon.html)
