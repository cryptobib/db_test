# CryptoBib Test Repository for Developers

**WARNING**: This is probably not the repository your are interested in. This repository is only for *cryptobib* developers. The repositories containing the public *bib* files are [cryptobib/export](https://github.com/cryptobib/export) and  [cryptobib/export_crossref](https://github.com/cryptobib/export_crossref).

**WARNING**: This project shall only be used as a subfolder of the main project [cryptobib/cryptobib](https://github.com/cryptobib/cryptobib). Please read the documentation of the main project.

## Getting started

### Requirements

- see `README.md` from the main project
- compile bibtex8:

		cd bibtex8
		make -f unix.mak linux-gcc

- scons (can be installed via `python -m pip install scons`)
- compile pplatex

		cd pplatex
		scons

Note: If pplatex compilation fails with `src/regex.h:12:10: fatal error: 'pcreposix.h' file not found`, on macOS do:

```
brew install pcre
scons PCREPATH="$(brew --prefix pcre)"
```

### Run all tests

Just launch `make` and check output (and *.pdf files).

## Troubleshoothing

### Clean tests

Just launch `make clean`.

## Under the hood

### bibtex8

`bibtex`/`bibtex8` (<http://www.ctan.org/tex-archive/biblio/bibtex/8-bit>) cannot support by default such a big bibliography.
We needed to modify `bibtex8` (more precisely the file `bibtex8/utils.c` - the original file is `bibtex8/utils.c.orig`).
