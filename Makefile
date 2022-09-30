
PROJECTPATH   = ./
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = notebook
SOURCEDIR     = docs
BUILDDIR      = docs/_build

all: html

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html: gallery
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

pdf:
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clear:
	@rm -rf "$(BUILDDIR)"

open: $(BUILDDIR)/html/index.html
	@open $<

gallery:
	@python scripts/generate_link_images.py

.PHONY: help html all clear open pdf gallery