Appendix C - Manual Pages



[![](../../images/logo.gif)](../../index.html)

**Appendix
C

Manual Pages**

---

BACKEND(L) LOCAL COMMANDS
BACKEND(L)



NAME

** backend** - single user Udanax Green backend

SYNOPSIS

backend

TYPICAL USAGE

intf **backend** fex

DESCRIPTION

** Backend** accepts requests from a frontend, such as **fex**(**L**),
through **stdin** and responds through **stdout** according to
the **FeBe Protocol** **88.1x** .

Metaprotocol

Initially **backend** conducts a dialogue with the frontend to establish
that both parties understand a common protocol. This "metaprotocol"
consists of one or more newline characters (i.e., byte value 0x0a) from
the frontend as synchronization; before the newlines, all input is ignored.
After the newlines **backend** expects to receive the string:

P0~

(i.e., byte values 0x50 0x30 0x7e). On seeing this, **backend **responds
with:

\nP0~

(0x0a 0x50 0x30 0x7e) meaning that **Udanax Green FeBe Protocol**
represented by "0" is understood. If **backend** sees any
other input after the last newline, it responds with:

\nP?~

(0x0a 0x50 0x3f 0x7e) meaning that it did not understand the frontend,
and then exits.

Error Redirection

After successful completion of the metaprotocol dialogue, **backend**
closes **stderr** and reopens it with the file **backenderror**
to avoid disrupting the frontend interaction.

Data Structure File

** Backend** then attempts to open the file **enf.enf** in the
current working directory. This file contains the data and links from
all sessions since it was created. If this file does not exist or has
been obviously corrupted, a new one is created.

Interactive Session

** Backend** is now ready to accept **Udanax Green FeBe Protocol
**requests. The session lasts until the frontend issues a quit request.
After **backend** responds with a quit code the frontend may exit.
After sending the quit code, **backend** updates **enf.enf** and
closes it before itself exiting.

Accounts

When **backend** starts accepting requests, the working user account
is set to the default account 1.1.0.1, under which new documents and
versions will be created until the working user account is changed with
the x-account request.

Note that if the session is using a new enfilade file, neither 1.1.0.1
nor any other account will exist, and must be created before any documents
may be created. To create the account 1.1.0.1, first create the node
1.1 with:

create-node-or-account 0.1.1

and then create account 1.1.0.1 with:

create-node-or-account 0.1.1.0.1

Edit Logging

** Backend** records all edit requests in a file called:

ln**m**.**d**.**h**:**m

** where **m**, **d**, **h**, and **m** are the month,
day, hour, and minute, respectively that the backend began execution.
Each line in this file is a single backend request. This format is possible
since the **Udanax Green FeBe Protocol** terminator character `~'
and a newline are accepted as identical by **backend**, and multiple
delimiters before a new request are ignored (treated as null requests).
The file is produced so that edit operations made during any session
may be reproduced later should **backend** fail, or for whatever
other reason may arise. If you want to redo the operations recorded
in an individual log file, edit that file so that it has at least one
blank line followed by "P0~" at the top, then invoke
**backend** as

backend <**logfile

** where **logfile** is the name of the appropriate edit log. The
edit described above is necessary since the metaprotocol does not appear
in the log.

For reconstructing entire enfilades from edit logs, it is useful to
concatenate the relevant logs into one file. To do this, first append
the files together with **cat**(**1**), or some other utility.
Then edit the resulting file to remove all quit requests (16~) except
at the last line of the file. This new file may then be used to execute
the contained requests in the manner described above.

FILES

** backenderror** - redirected stderr

** enf.enf** - the magic data structure file

** ln**?.?.?:? - the edit log file

SEE ALSO

fex(L), intf(L)

** Udanax Green FeBe Protocol Documentation**, Udanax.com, August
1988

BUGS

Virtually no sanity checking is performed on the input.

There are many possible requests, particularly edit operations on non-existent
addresses and creating documents in non-existent accounts that are likely
to corrupt the data structure.

Numeric inputs to the backend (i.e., tumbler digits, sizes and counts)
are currently limited to values representable by 32 bit unsigned integers.

Tumblers input to the backend are allowed a maximum depth of 11 tumbler
digits from the last leading zero digit.

Text items for insert may be no more than 950 bytes long; larger insertions
must be broken into multiple text items.

Longer items are likely to cause the program to fail (see previous bug).

Node numbers are meaningless other than as a prefix for account numbers.

The data file **enf.enf** has a size limit around 400K disk blocks
because of a kluged, fixed size allocation table.

etc...

NOTE

Since the data structure is easy to corrupt with invalid, but unchecked,
requests it is a good idea to occasionally copy **enf.enf** to a
backup file.



Last change: 25 August 1988



BACKENDDAEMON(L) LOCAL COMMANDS BACKENDDAEMON(L)



NAME

** backenddaemon** - multiple user Udanax Green backend daemon

TYPICAL USAGE

** backenddaemon** is usually spawned when necessary by **ints**(**L**)
or **intx**(**L**), which will be referred to as "glue"
programs.

DESCRIPTION

** Backenddaemon** accepts and responds to requests from up to five
frontends through **socket**(**2**) connections using the **Udanax
Green FeBe** **Protocol**.

Error Redirection

The first action by the **backenddaemon** process is to close **stderr**
and reopen it as the file **backenderror** to avoid disrupting the
frontend interaction.

Parameter and Data Structure Files

** Backenddaemon** attempts to open .**backendrc** in the working
directory inherited from the process that spawned it, either a glue
program or a shell. This file is used by **backenddaemon**, both
glue programs, and **xlog**(**L**) to set various run-time values
to other than their defaults with lines of the form

metaname = **word

** where each program uses a different set of metanames, although
since they all use the same routine to read the file, lines not used
by a particular program must still be correct. Lines in .**backendrc**
beginning with "#" are ignored.

** Backenddaemon** then tries to open **enf.enf** in the same
directory. **Enf.enf** contains the data and links from all sessions
since it was created. If this file does not exist or has been obviously
corrupted, a new one is created.

Connection to Frontend

After the data structure initialization, **backenddaemon** creates
a **socket**(**2**) with AF INET address format and SOCK_STREAM
communications semantics. This socket is then bound to either the default
port 55146 or the port given by

port = **port-number

** in .**backendrc**. The socket address is set to INADDR_ANY so
that connections will be accepted from any host in the domain. **Backenddaemon**
then waits for frontend connections with **select**(**2**). It
is up to a frontend or a glue program to attach to the socket with **connect**(**2**).

After a connection is established, **backenddaemon** reads a device
name from the socket. This name should be "SOCKET" if frontend
interaction is to be through the socket. **Ints**(**L**) uses
this mechanism. Otherwise, **backenddaemon** will communicate through
the named device; see **intx**(**L**) for an example of this method.

After the device name is acquired, but before it is used, **backenddaemon**
expects an x-account request over the socket to establish the initial
account to be used (see Accounts, below).

When the account is set, **backenddaemon** switches to the nonsocket
device if one was specified, otherwise communication continues to the
original socket connection.

Metaprotocol

Next, **backenddaemon** conducts a dialog with the frontend to establish
that both parties understand a common protocol. This "metaprotocol"
consists of one or more newline characters (i.e., byte value 0x0a) from
the frontend as synchronization; before the newlines, all input is ignored.
After the newlines, **backenddaemon** expects to receive the string:

P0~

(i.e., byte values 0x50 0x30 0x7e). On seeing this, **backenddaemon**
responds with:

\nP0~

(0x0a 0x50 0x30 0x7e) meaning that **Udanax Green FeBe Protocol **represented
by "0" is understood. If **backenddaemon** sees any other
input after the last newline, it responds with:

\nP?~

(0x0a 0x50 0x3f 0x7e) meaning that it did not understand the frontend,
and then closes the connection.

Interactive Session

** Backenddaemon** is now ready to accept **Udanax Green FeBe Protocol
** requests. The session lasts until the frontend issues a quit request.
After **backenddaemon** responds with a quit code the frontend may
exit. After the quit command, **Backend** closes the connection that
the frontend was using.

Accounts

See **backend**(**L**) for a description of account maintenance.

Edit Logging

** Backenddaemon** records all edit requests as **backend**(**L**)
does, with the added property that an x-account request is placed in
the log file whenever the requests that may follow are from a different
account than the previous requests.

FILES

.**backendrc** - run time switches

** backenderror** - redirected stderr

** enf.enf** - the magic data structure file

** ln**?.?.?:? - the edit log file

SEE ALSO

backend(L), fex(L), ints(L), intx(L), xlog(L), accept(2), bind(2), socket(2)

** Udanax Green FeBe Protocol Documentation**, Udanax.com, August
1988

BUGS

In .**backendrc**, whitespace is required on both sides of the "="
on each line.

When given a device name other than "SOCKET," **daemon**
does not read lines that are not terminated with a newline.

See **backend**(**L**) for more bugs.

NOTES

Since the data structure is easy to corrupt with invalid but unchecked
requests, it is a good idea to occasionally copy **enf.enf** to a
backup file.

The limit of 5 frontend connections is an arbitrary one, and does not
reflect any limitations in the internal structure of the backend. The
**socket**(**2**) facility was chosen because it was simple enough
to not distract from the development of the more intricate Udanax hypertext
functionality (i.e., it was a quick hack).



Last change: 25 August 1988



FEX(L) LOCAL COMMANDS FEX(L)



NAME

** fex** - experimental Udanax Green frontend

SYNOPSIS

fex **pipe-from-backend pipe-to-backend

** INVOCATION

** fex** is normally invoked by a "glue" program such as
**intf** that starts both the frontend and the backend and sets up
the pipes to allow them to communicate.

DESCRIPTION

** fex** is a screen-oriented program resembling a visual text editor
which provides a user interface to the Udanax Green backend **backend**(**L**).
There is no explicit insert mode: alphanumeric characters typed at any
time are inserted into the text under the cursor position. The DEL key
is used to delete characters before the cursor position.

When **fex** is invoked it automatically locates and places on the
screen a document (1.1.0.1.0.1) that serves as an entry point to the
system. This document contains a summary of frontend commands and a
link connecting it to another document that serves as a general index.
Additional commands are invoked through a pop-up menu.

TERMINOLOGY

** end-set** A region of text (possibly discontinuous
and possibly spanning more than one document) connected to
another such region by a link.

** link** A connection between two end-sets, modified by
a third end-set. These are respectively called the **from-set**,
**to-set**, and **three-set**, of the link. **From-sets**
are displayed as back-lit; **to-sets** as underlined (termcap
permitting) or as back-lit. **Three-sets** are used to
describe the intended meaning of the link, such as if it is
a jump link or a footnote link. The distinction between from-sets
and to-sets reflects the link author's intentions rather than
any functional difference. The from-sets and to-sets of a
link are really symmetrical.

** cut** A temporary mark made in the text to specify boundaries
of an end-set for a link to be created, or a section to be
rearranged or deleted.

** display style** When a link is followed, the text at
the destination is displayed in a window that can be a quarter-screen
(default), a horizontal half-screen, a vertical half-screen,
or an entire screen. The display style can be changed through
the menu (see below). If a window was created by following
a link, its display style is initially determined by the three-set
of that link.



COMMANDS

** cursor control**

^W or up arrow Move cursor up

^Z or down arrow Move cursor down

^A or left arrow Move cursor left

^S or right arrow Move cursor right

^Q Top of document

^F Down one page

** menu**

^N Show menu: current selection is back-lit. Up and
down cursor controls change current selection and SPACE
BAR executes it. Available menu selections are listed under
MENU OPTIONS below.

** link following**

^Y Follow the link indicated by the cursor. If the cursor
position is occupied by multiple, overlapping end-sets,
the first lines of each destination will be displayed in
a menu. When the link is selected the destination text will
appear in a new window whose size and position is determined
by the **display style**.

^U Return from link: the first lines of the windows to which
a return is possible are displayed in a menu.

** text editing**

^G Make cut. (For deletions see **MENU OPTIONS**
)

^P Delete block

^C Rearrange

** link creation**

^V Change from-set: text delimited by cuts is added
to a temporary from-set; then the cuts are cleared.

^B Change to-set: text delimited by cuts is added to a temporary
to-set; then the cuts are cleared.

^L Make link: a menu appears asking if the link is to be
a jump, quote, footnote, or marginal note. An appropriately
typed link is then created between the temporary from-set
and the temporary to-set; then the temporary end-sets are
cleared.

** miscellaneous**

^] Redraw screen

^T Exit program

MENU OPTIONS

set display style Select a **display style**, as
defined above

show key definitions (unimplemented)

compare Show corresponding portions of two documents

follow link = ^Y

create link = ^L

make cut = ^G

delete cuts Clear all cuts

delete block = ^P

rearrange = ^C

create document Create a new, empty document. NOTE: a link
to the new document must be made before leaving the document
or the frontend will be unable to retrieve the document
even though it still exists.

change from-set = ^V

change to-set = ^B

clearendsets Remove all temporary end-sets created by the
previous two commands.

create version Duplicate the current document as a new version.
NOTE: a link to the new document must be made before leaving
the document or the frontend will be unable to retrieve
the document even though it still exists.

BUGS

This is an experimental frontend. The following bugs are known to exist.
There are undoubtedly others.

1. Hitting DELETE with the cursor in the first position of a
window causes a fatal error.

2. Text cannot be inserted below the last line of a document. Attempts
to do so cause a fatal error. To append text to a document, place
the cursor at the end of the last line and hit RETURN. Blank lines
may be appended with repeated RETURNs.

3. Deletion of text in a newly-created document (i.e., one created
in the current invocation of **fex**) may result in a mispositioning
of the cursor. The actual document **should** be edited correctly.
However, it is recommended that editing of newly-created documents
be kept to a minimum.

Last change: 25 August 1988



INTF(L) LOCAL COMMANDS INTF(L)



NAME

** intf** - connect a frontend to the single-user Udanax Green backend

SYNOPSIS

intf **backend frontend

** DESCRIPTION

** Intf** uses the **pipe**(**2**) facility to connect a frontend
program to the standard I/O of a program such as **backend**(**L**).

Two pipes are created by **intf**, one from the frontend to the backend,
the other in the opposite direction. One end of each pipe is attached
to **stdin** and **stdout**. **Intf** then forks and executes
the backend program with these pipes as its standard I/O. The original
branch of the fork then executes the frontend program with the file
descriptor numbers for the other ends of the pipes passed as command
line arguments in the form

frontend **pipe-from-backend pipe-to-backend

** so that the frontend can communicate with the backend through them.
**Intf** does not exit if successful, turning into the frontend instead.

SEE ALSO

backend(L), frontend(L), execl(2), fork(2), pipe(2)

Last change: 25 August 1988



INTS(L) LOCAL COMMANDS INTS(L)



NAME

** ints** - connect a frontend to a Udanax Green backend daemon

SYNOPSIS

ints **frontend account

** DESCRIPTION

** Ints** uses the **socket**(**2**) facility to connect a
frontend program to **daemon**(**L**).

** Ints** first reads the file .**backendrc** in the current directory.
If the line

backenddir = **path

** is present, **ints** sets **path** as its working directory,
otherwise the directory is unchanged.

Next, **ints** acquires a socket with AF_INET address format and
SOCK_STREAM semantics-the same form as **daemon**(**L**). **Ints**
then binds the socket to a specific port and host. The default port
is 55146 and the default host is localhost, although these can be changed
in .**backendrc** with

port = **port-number

** and

host = **host-name

Connect**(**2**) is then called with this binding. If the connection
is not made, **ints** spawns a daemon on the local host machine with
**fork**(**2**) and **execl**(**2**). The default daemon
is **backenddaemon** in the directory set above, but this may be
changed with

backend = **daemon-name

** in .**backendrc**. **Ints** then makes a second attempt to
connect after a 15 second wait. A second failure results in termination.

Once the connection is acquired, **ints** sends the string "SOCKET"
to **daemon** to indicate that the socket connection will be used
by the frontend. **Ints** then sends an x-account request to **daemon**
with the account number from the command line.

Finally, **ints** executes the frontend program. The default frontend
is **fex** in the directory set above, but may be changed with

frontend = **frontend-name

** in .**backendrc**. The file descriptor numbers for the socket
are passed as command line arguments in the form

frontend **from-backend to-backend

** so that the frontend can communicate with the backend through them.
**Ints** does not exit if it is successful.

FILES

.**backendrc** - run time switches

** backenddaemon** - Udanax Green backend daemon program

** fex** - frontend program

SEE ALSO

daemon(L), fex(L), bind(2), connect(2), socket(2)

** Udanax Green FeBe Protocol Documentation**, Udanax.com, August
1988

BUGS

If you are trying to connect to a backend daemon on another machine,
it will not help for **ints** to spawn one on the local machine,
as the second connection attempt will still fail.

Last change: 25 August 1988



INTX(L) LOCAL COMMANDS INTX(L)



NAME

** intx** - connect a Udanax Green backend daemon to a terminal

SYNOPSIS

intx **backend account

** DESCRIPTION

** Intx** is almost identical to **ints**(**L**). Instead of
connecting to a frontend via a socket, however, **intx** connects
the backend to the terminal that is attached to **stdin**. The purpose
of this is to allow a frontend program running on a different machine
connected to a network host via a serial line to connect to a Udanax
Green backend.

FILES

.**backendrc** - run time switches

** backenddaemon** - Udanax Green backend daemon program

SEE ALSO

daemon(L), xlog(L), connect(2), socket(2), ttyname(3)

BUGS

Presently requests to the backend are line buffered with **intx**.

Last change: 25 August 1988



XLOG(L) LOCAL COMMANDS XLOG(L)



NAME

** xlog** - entry point for experimental multiple user Udanax Green
hypertext system

SYNOPSIS

xlog [ **user-name** ]

DESCRIPTION

** Xlog** attempts to find an Udanax Green account number based on
a user name, if any, and then invokes either **ints**(**L**) or
**intx**(**L**) with that account number. If no user name is given,
account 1.1.0.1 is used.

** Xlog** first reads .**backendrc** in the current directory.
If the line

backenddir = **path

** is present, **xlog** sets **path** as its working directory,
otherwise the directory is unchanged. **Xlog** then prompts for a
password (which is not checked), and looks for the account number for
**user-name** in either **accountfile** in the directory set above,
or in the file named by

accountfile = **file-name

** in .**backendrc**. This file contains lines with the format

user-name:password:account-number

for example,

albert:space-time:1.42.0.23

** Xlog** then asks if you want to run the standard frontend (through
**ints**(**L**)) or one running on a different machine (connected
via **intx**(**L**)). The appropriate program is then executed,
and **xlog** vanishes.

FILES

** accountfile** - file to map from user names to account numbers

.**backendrc** - run time switches

SEE ALSO

daemon(L), fex(L), ints(L), intx(L), execl(2)

BUGS

If the directory is changed by .**backendrc**, **ints**, **intx**,
and **daemon** will start with that directory, and attempt to read
.**backendrc** from there. For now, just keep a copy wherever it
may be used.

Last change: 25 August 1988



XUMAIN(L) LOCAL COMMANDS XUMAIN(L)



NAME

** xumain** - interactive stand alone Udanax Green backend with awful
numerical interface

SYNOPSIS

xumain [ < **setup-script** ]

DESCRIPTION

** Xumain** is a quasi-interactive stand alone version of **backend**(**L**),
which does not use the **Udanax Green FeBe Protocol ** syntax, instead
prompting for input to most requests. **Xumain** does, however, have
enough similarities to **Udanax Green FeBe Protocol ** for the protocol
document to be a useful reference.

** Xumain** is the original Udanax Green backend, written before
any frontend, and was intentionally left as a user-hostile program to
encourage us to really write a frontend. The program continues to exist
principally as a tool to create Udanax Green documents from text files
using the source-unix-command command, which should really be a function
of some

frontend.

Spec-sets

Spec-sets, spans, and v-spans are handled differently by **xumain**,
with prompts for yes/no responses to determine which type to use; some
of the prompts are context dependent. Tumblers are also different: **xumain**
requires that the leading zeros of a tumbler are explicitly given, rather
than with an exponent. All the prompts below that end with "=>"
require a tumbler according to the **Udanax Green FeBe Protocol**.
When a spec set is expected the user is prompted with

any spans or vspecs? (y/n)

where span has its usual meaning and vspec is a document number with
a set of v-spans. The spec set is terminated with a negative response
to this prompt. A positive response is followed by the prompt

a span? (y/n)

This is asking whether you want a span or a collection of v-spans within
a document. A `yes' answer elicits a prompt for a span:

enter span

start=>

width=>

If you respond with `no', then you will be prompted for a document number
with

document=>

and then for a v-span set with

any spans? (y/n)

except that this time, the span in question is a v-span. V-spans are
requested until a `no' answer, after which you will be prompted for
the next spec.

As an example consider this request to retrieve the first 10 characters
from the document 1.1.0.1. (The emphasized text is the user's response.):

request? **5

** any spans or vspecs? (y/n) **y

** a span? (y/n) **n

** document=> **1.1.0.1

** any spans? (y/n) **y

** enter span

start=> **1.1

** width=> **0.10

** any spans? (y/n) **n

** any spans of vspecs? (y/n) **n

**

Assuming they are present, **xumain** will then respond with those
10 characters.

Commands

There are four commands, x-account, create-node-or-account, open, and
close which do not prompt for their arguments. All these, however, accept
the same arguments as **Udanax Green FeBe Protocol**, but separated
by newlines rather than the **Udanax Green FeBe Protocol ** word
delimiter character.

The insert request in **xumain** has an important difference from
**Udanax Green FeBe Protocol.** Rather than giving a count of the
number of characters in the text item, the input text is terminated
with a blank line.

There is a request unique to **xumain** called source-unix-command,
which is request number 21. This asks for a command for execution by
**sh**(**1**) with the standard output directed to a file with
the name "xum" followed by **xumain's** process number.
A new document is created and the command output is placed there. The
new document number is printed for future use. Finally, the output file
is deleted.

FILES

** enf.enf** - the magic data structure file.

** xum**??? - command output for source-unix-command

SEE ALSO

backend(L), sh(1)

** Udanax Green FeBe Protocol Documentation**, Udanax.com, August
1988

BUGS

See **backend**(**L**).

NOTE

Since the data structure is easy to corrupt with invalid but unchecked
requests, it is a good idea to occasionally copy **enf.enf** to a
backup file.

** Xumain** will not appear in future releases.

Last change: 25 August 1988







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
