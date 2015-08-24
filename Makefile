all:
	pdflatex isbntools.tex
	pdflatex isbntools.tex
clean:
	rm *.aux *.log *.out *.gz *~
clean_pdf:
	rm *.pdf
clean_all: clean clean_pdf