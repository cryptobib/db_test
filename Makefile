PYTHON=python3
BIBER=biber
BIBTEX=./bibtex8/bibtex
BIBTEX_FLAGS=--csfile bibtex8/csf/cp850lat.csf --wolfgang
PDFLATEX=./pplatex/bin/ppdflatex -q --

TEX_TESTS=test_abbrev0_bibtex.tex test_abbrev0_crossref_bibtex.tex test_abbrev1_bibtex.tex test_abbrev1_crossref_bibtex.tex test_abbrev2_bibtex.tex test_abbrev2_crossref_bibtex.tex test_abbrev3_bibtex.tex test_abbrev3_crossref_bibtex.tex test_abbrev0_biber.tex test_abbrev0_crossref_biber.tex test_abbrev1_biber.tex test_abbrev1_crossref_biber.tex test_abbrev2_biber.tex test_abbrev2_crossref_biber.tex test_abbrev3_biber.tex test_abbrev3_crossref_biber.tex
PDF_TESTS=$(TEX_TESTS:.tex=.pdf)

.PHONY: all clean mrproper FORCE

all: $(TEX_TESTS) $(PDF_TESTS)

%_biber.pdf: %_biber.tex clean FORCE
	@echo
	@echo "--- Test of $<"
	rm -f $(patsubst %.tex,%.aux,$<)
	$(PDFLATEX) $<
	$(BIBER) $(basename $<) 2>&1 | sed -e '/WARN - month field/d' | sed -e '/WARN - legacy month field/d' | sed -e '/cannot be null, deleting it/d' |  sed -e '/line 279/d' # remove the issues with the months and the empty fields + workaround for issue https://github.com/plk/biber/issues/174

%_bibtex.pdf: %_bibtex.tex clean FORCE
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
