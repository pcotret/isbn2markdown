# Introduction
Scripts to import ISBN references in a Markdown-like syntax. Two short tutorials are given with related codes:
1. Importing a list of references from an input file.
2. Importing a single reference.

# Prerequisites
Tested on an Ubuntu machine
1. `sudo apt-get install python3-pip`
2. `sudo pip3 install isbnlib`

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

#### Command (parameter after the Python script is the input file):
```bash
python3 listimport.py input.txt
```
## Importing a single book
### Prerequisites
* You have a Python script `singleimport.py` (see code section below).
* You have an ISBN number to add (10 or 13 digits).

### Example
#### Command:
```bash
python3 simpleimport.py 9780470474242
```

#### Parameters:
1. ISBN number.

# References
* https://pypi.org/project/isbnlib/
