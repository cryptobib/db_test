# CryptoBib Test Repository for Developers

**WARNING**: This is probably not the repository your are interested in. This repository is only for *cryptobib* developers. The repositories containing the public *bib* files are [cryptobib/export](https://github.com/cryptobib/export) and  [cryptobib/export_crossref](https://github.com/cryptobib/export_crossref).

**WARNING**: This project shall only be used as a subfolder of the main project [cryptobib/cryptobib](https://github.com/cryptobib/cryptobib). Please read the documentation of the main project.

## Getting started

### Requirements

See `README.md` from the main project.

### Run all tests

Just launch `make` and check output (and *.pdf files).

## Troubleshoothing

### Clean tests

Just launch `make clean`.

## Under the hood

### bibtex8

`bibtex`/`bibtex8` (<http://www.ctan.org/tex-archive/biblio/bibtex/8-bit>) cannot support by default such a big bibliography.
We needed to modify `bibtex8` (more precisely the file `bibtex8/utils.c` - the original file is `bibtex8/utils.c.orig`).
