#! /usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" Import a list of books from their ISBN.

- Date:    August 2016.
- Author:  Pascal Cotret, https://github.com/pcotret/isbntools4mediawiki/
- Licence: ?
"""

# from __future__ import print_function, absolute_import  # Python 2 compatibility if needed

# Import libraries
# os/sys for Unix, re for string manipulations
import os
import sys
import re

from isbntools.app import *  # ISBN metadata retrieval


# Define custom functions

def strmanip(x):
    """ Custom function to manipulate the string x."""
    idx = 0
    list1 = x.split()
    list2 = ['', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '']
    unwanted = ["[u\'", ",", "\']", "u\'", "\'"]
    for x in list1:
        # Remove unwanted characters
        for y in unwanted:
            x = x.encode('utf-8')
            x = x.replace(y, "")
        # Keep only words beginning with a capital letter
        if re.findall('[A-Z]', x) != []:
            # Remove words which length is under 3
            if len(x) >= 3:
                list2[idx] = x
                idx = idx + 1
    return list2


# Main stuff
if __name__ == '__main__':
    # Pre-define variables
    meta_str = "isbn_meta "
    opt_str = " bibtex"
    export_str = " >> output.bib"
    wiki_str = ""
    authors_str = ""
    # Part 1 - Get all infos from the ISBN list in a bibtex compliant format
    # Open file in read mode
    isbn_file = open("input.txt", 'r')
    wiki_file = open("mediawiki.txt", 'w')
    # Read everything and put it in a list
    mylist = isbn_file.read().splitlines()
    # For each element of the list
    for index, value in enumerate(mylist):
        # Build the command to run
        cmd_str = meta_str + mylist[index] + opt_str + export_str
        # Print its ISBN info and write to the bibfile
        os.system(cmd_str)
        meta_dict = meta(mylist[index])
        # Part 2 - Modify authors field from meta_dict to get lastname/firstname
        # of the 1st author. I would say something like:
        authors_str = strmanip(str(meta_dict['Authors']))
        wiki_str = '| ' + meta_dict['Title'].encode('utf-8')
        + ' || ' + authors_str[1] + ", " + authors_str[0]
        + ' || ' + meta_dict['Publisher'].encode('utf-8')
        + ' || ' + meta_dict['Year'].encode('utf-8')
        + ' || [http://isbndb.com/search/all?query=' + meta_dict['ISBN-13'].encode('utf-8') + ' ' + meta_dict['ISBN-13'].encode('utf-8')
        + '] || ' + sys.argv[1].encode('utf-8')
        + '\n |-\n'
        wiki_file.write(wiki_str)
    # Done, closes the files
    isbn_file.close()
    wiki_file.close()
