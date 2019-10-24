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
    md_file = open('markdown.md', 'w+')
    # Read everything and put it in a list
    isbn_number = sys.argv[1]
    # Print its ISBN info and write to the bibfile
    print('Searching a book with ISBN ' + str(isbn_number)+'...')
    try:
        meta_dict = isbnlib.meta(str(isbn_number))
        print('Adding the book ' + meta_dict['Title'] + ' by ' + meta_dict['Authors'][0].split()[1])
        # Part 2 - Modify authors field from meta_dict to get lastname/firstname
        # of the 1st author. I would say something like:
        first_author = meta_dict['Authors'][0].split()
        md_str = '|Title' + '|Author' + '|Publisher' + '|Year' + '|ISBN|\n' \
               + '|-----' + '|------' + '|---------' + '|----' + '|----|\n' \
               + '|' +  meta_dict['Title'] \
               + '|' +  first_author[1] + ", " + first_author[0] \
               + '|' +  meta_dict['Publisher'] \
               + '|' +  meta_dict['Year'] \
               + '|' +  '['+ meta_dict['ISBN-13'] + '](http://isbndb.com/book/' + meta_dict['ISBN-13'] + ')|'
        md_file.write(md_str)
    except Exception:
        print('Book not found!')
    # Done, closes the files
    md_file.close()