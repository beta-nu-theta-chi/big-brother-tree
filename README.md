# Beta Nu Chapter of Theta Chi Fraternity #
## Big Brother Tree ##

This repository contains the markup describing the big brother tree for Beta Nu Chapter of Theta Chi Fraternity. It shows the relationships between big brothers and their little brothers. It has records back to the 60s (although the first 10 years or so are not known to be accurate).

The current maintainer of the tree is Eric Yarnot (ery12@case.edu).

## Markup Language ##

The big brother tree is described using the [dot language][dot]. Dot is a language that was developed by Bell labs in order to describe directed graphs. It is very good at making them and is also free. Since a tree is a directed graph, it made sense to use dot to create our tree.

[dot]: http://en.wikipedia.org/wiki/DOT_language

### Syntax ###

For a primer on the syntax of the language, see the [wiki page on the dot language][dot-wiki].

[dot-wiki]: https://github.com/beta-nu-theta-chi/big-brother-tree/wiki/Dot-Language

## Rendering the Tree ##

In order for the markup to be put into a usable form, it must first be rendered using the dot program.

### Install Dot/Graphviz ###

#### Linux ####

On Debian based systems:

```bash
sudo apt-get install graphviz
```

That is all you need!

On any `nix` supported system:

```bash
nix develop
```
To activate an graphviz environment.

To build:
```bash
nix build
```

#### OS X ####

For OS X, you will need to download the install for Graphviz from [their website][gviz-osx]. From there, you can just install like a normal application.

[gviz-osx]: http://www.graphviz.org/Download_macos.php

#### Windows ####

This is the least recommended platform for using dot, since it does not work as well, but if you must use Windows, please read on.

The Windows version of Graphviz is also available from [their website][gviz-windows]. It can be installed as a normal application. Make sure to pay attention to where you downloaded the application, since you will need to run dot from that directory.

[gviz-windows]: http://www.graphviz.org/Download_windows.php

### Running Dot ###

From the command line, just run:

```
dot -Tpdf brotherhood.gz > brotherhood.pdf
```

Note to Windows users: you may need to run this command from the location where the `dot` program is located (Try looking in `c:\program files (x86)\graphviz`). You will also need to use the full path to the dot file. As an example:

```
cd c:\program files (x86)\graphviz
dot -Tpdf c:\Users\john\desktop\brotherhood.gz > c:\Users\john\desktop\brotherhood.pdf
```

The `-T` flag tells dot which format to use for the output file. In this case, we are specifying PDF, but other formats like PNG may be used as well.
