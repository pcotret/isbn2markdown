#! /usr/bin/env python3
""" Import a list of books from their ISBN.
Author:  Pascal Cotret, https://github.com/pcotret/isbntools4markdown/
"""

# Import libraries
import sys
import isbnlib

# Main stuff
if __name__ == '__main__':
    # Part 1 - Get all infos from the ISBN list in a bibtex compliant format
    # Open file in read mode
    isbn_file = open("input.txt", 'r')
    md_file = open('markdown.md', 'w+')
    # Read everything and put it in a list
    mylist = isbn_file.read().splitlines()
    print(mylist)
    md_str = '|Title' + '|Author' + '|Publisher' + '|Year' + '|ISBN|\n' \
           + '|-----' + '|------' + '|---------' + '|----' + '|----|\n'
    md_file.write(md_str)
    # For each element of the list
    for index in range(len(mylist)):
        meta_dict = isbnlib.meta(str(mylist[index]))
        print(meta_dict)
        # Part 2 - Modify authors field from meta_dict to get lastname/firstname
        # of the 1st author. I would say something like:
        first_author = meta_dict['Authors'][0].split()
        md_str = '|' +  meta_dict['Title'] \
               + '|' +  first_author[1] + ", " + first_author[0] \
               + '|' +  meta_dict['Publisher'] \
               + '|' +  meta_dict['Year'] \
               + '|' +  '['+ meta_dict['ISBN-13'] + '](http://isbndb.com/book/' + meta_dict['ISBN-13'] + ')|\n'
        print(md_str)
        md_file.write(md_str)
    # Done, closes the files
    isbn_file.close()
    md_file.close()
