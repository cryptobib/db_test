#!/bin/env python2

from string import Template

test_template = r"""\documentclass[a4paper,10pt]{article}
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

def main():
    for crossref in ["","_crossref"]:
        for short in range(4):
            out = file("test_abbrev{}{}.tex".format(short, crossref), "w")
            out.write(Template(test_template).substitute(short=short, crossref=crossref))
            out.close()

if __name__ == "__main__":
    main()
