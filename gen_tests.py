#!/bin/env python2

from string import Template

test_template_bibtex = r"""\documentclass[a4paper,10pt]{article}
\usepackage{url}
\usepackage{amscd,amsmath}
\usepackage{amsfonts}
\usepackage[cm]{fullpage}

\begin{document}

\nocite{*}
\bibliographystyle{alpha}
\bibliography{../db/abbrev${short},../db/crypto${crossref}}

\end{document}
"""

test_template_biber = r"""\documentclass[a4paper,10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{url}
\usepackage{amscd,amsmath}
\usepackage{amsfonts}
\usepackage[cm]{fullpage}

\usepackage{biblatex}

\bibliography{../db/abbrev${short},../db/crypto${crossref}}

\begin{document}

\nocite{*}
\printbibliography{}

\end{document}
"""

def main():
    for crossref in ["","_crossref"]:
        for short in range(4):
            out = file("test_abbrev{}{}_bibtex.tex".format(short, crossref), "w")
            out.write(Template(test_template_bibtex).substitute(short=short, crossref=crossref))
            out.close()
    for crossref in ["","_crossref"]:
        for short in range(4):
            out = file("test_abbrev{}{}_biber.tex".format(short, crossref), "w")
            out.write(Template(test_template_biber).substitute(short=short, crossref=crossref))
            out.close()

if __name__ == "__main__":
    main()
