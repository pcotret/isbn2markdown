# Introduction
This document is a tutorial to use a custom based on the wonderful isbntools package in order to import ISBN references in a Mediawiki-like syntax. Two short tutorials are given with related codes:
1. Importing a list of references from an input file.
2. Importing a single reference.

# Prerequisites
Tested on an Ubuntu machine
1. `sudo apt-get install python-pip`
2. `sudo pip install isbntools`

# Tutorials
## Importing from a list
### Prerequisites
* You have a Python script `listimport.py` (see code section below).
* You have a file `input.txt` with all your ISBNs (one per line).

### Example
#### Input file (input.txt):
```
9780470474242
9780201440997
```

#### Command (parameter after the Python script is books’ owner):
```bash
python listimport.py pascal
```

#### Output (mediawiki.txt):
```
| Cryptography Engineering : Design Principles And Practical Applications || Kohno, Tadayoshi || Wiley Pub., inc . || 2010 || [http://isbndb.com/search/all?query=9780470474242 9780470474242] || pascal
|-
| Computer Security: Art And Science || Bishop, Matt || Addison - Wesley || 2004 || [http://isbndb.com/search/all?query=9780201440997 9780201440997] || pascal
|-
```

## Importing a single book
### Prerequisites
* You have a Python script `singleimport.py` (see code section below).
* You have an ISBN number to add (10 or 13 digits).

### Example
#### Command:
```bash
python simpleimport.py pascal 9780470474242
```

#### Parameters:
1. Books' owner.
2. ISBN number.

#### Output (mediawiki.txt):
```
| Cryptography Engineering : Design Principles And Practical Applications || Kohno , Tadayoshi || Wiley Pub., inc . || 2010 || [http://isbndb.com/search/all?query=9780470474242 9780470474242] || pascal
|-
```

# References
* https://pypi.python.org/pypi/isbntools
* https://www.mediawiki.org/wiki/MediaWiki/fr
