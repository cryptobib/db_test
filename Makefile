PYTHON=python2
BIBTEX=./bibtex8/bibtex
BIBTEX_FLAGS=--csfile bibtex8/csf/cp850lat.csf --wolfgang
PDFLATEX=./pplatex/bin/ppdflatex -q --

TEX_TESTS=test_abbrev0.tex test_abbrev0_crossref.tex test_abbrev1.tex test_abbrev1_crossref.tex test_abbrev2.tex test_abbrev2_crossref.tex test_abbrev3.tex  test_abbrev3_crossref.tex
PDF_TESTS=$(TEX_TESTS:.tex=.pdf)

.PHONY: all clean mrproper FORCE

all: $(TEX_TESTS) $(PDF_TESTS)

%.pdf: %.tex clean FORCE
	@echo
	@echo "--- Test of $<"
	$(PDFLATEX) $<
	$(BIBTEX) $(BIBTEX_FLAGS) $(basename $<)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

test_abbrev%.tex: gen_tests.py
	$(PYTHON) gen_tests.py

clean:
	rm -f *.aux *.bbl *.blg *.log *.pdf

mrproper: clean
	rm -f *.tex
