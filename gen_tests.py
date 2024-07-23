#!/bin/env python3

from string import Template

test_template_bibtex = r"""\documentclass[a4paper,10pt]{article}
\usepackage[T1]{fontenc}
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

test_templates = {
    "bibtex": test_template_bibtex,
    "biber": test_template_biber,
}


def main():
    for bib_software in ["bibtex", "biber"]:
        for crossref in ["", "_crossref"]:
            for short in range(4):
                with open("test_abbrev{}{}_{}.tex".format(short, crossref, bib_software), "w") as out:
                    out.write(
                        Template(test_templates[bib_software])
                        .substitute(short=short, crossref=crossref))


if __name__ == "__main__":
    main()
