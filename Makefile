presentations_dir = src/presentations
guides_dir        = src/guides

presentations_sources = $(wildcard $(presentations_dir)/*/*.rst)
guides_sources        = $(wildcard $(guides_dir)/*.rst)

all: html s5 slidy epub odp pdf
clean:
	find output -type f | xargs -r rm

template_dir = templates
pandoc = pandoc
pandoc_cmd = $(pandoc) --data-dir=. --smart \
	--variable static-url=$(base_path)/static \
	--variable static-dir="$(shell pwd)"/static
rst2odp_dir = tools/rst2odp
rst2odp = PYTHONPATH=$(rst2odp_dir) $(rst2odp_dir)/bin/rst2odp --traceback --template-file=templates/presentation.odp

remove_trailing_slash = $(patsubst %/,%,$(1))
invert_path = $(shell echo $(call remove_trailing_slash,$(1)) | sed -e 's|[^/]*|..|g')
# $(call base_path) inverts whatever target we are producing at the moment
base_path = $(call invert_path,$(dir $@))
base_template_dir = $(call base_path)/$(template_dir)

# one_output_file_per_input_file is called with three parameters:
#
# $(1): the list of sources, for example $(presentation_sources) and/or
#   $(guide_sources)
#   removed from the input filename by pattern matching;
# $(2): the source base directory, often $(presentations_dir), which is
#   removed from the input filename by pattern matching;
# $(3): the output directory, often a $(something_dstdir), which is
#   added to the input filename by pattern matching;
# $(4): the extension to be added to the destination filename, for
#   example .html.
# 
# so for example $(call one_output_file_per_input_file,$(presentations_dir),$(html_dstdir),.html)
# converts each input file $(presentations_dir)/a/b.rst to
# $(html_dstdir)/a/b.rst.html.

one_output_file_per_input_file = $(1:$(2)/%=$(3)/%.$(4))
one_output_file_per_presentation = $(call one_output_file_per_input_file,$(presentations_sources),$(presentations_dir),$(1),$(2))
one_output_file_per_guide        = $(call one_output_file_per_input_file,$(guides_sources),$(guides_dir),$(1),$(2))

html_dstdir = output/html
html_files = \
	$(call one_output_file_per_presentation,$(html_dstdir),html) \
	$(call one_output_file_per_guide,$(html_dstdir),html)
html: $(html_files)
$(html_dstdir)/%.html: $(presentations_dir)/%
	mkdir -p $(dir $@)
	$(pandoc_cmd) -t html -o $@ -s $<
$(html_dstdir)/%.html: $(guides_dir)/%
	mkdir -p $(dir $@)
	$(pandoc_cmd) -t html -o $@ -s $<

s5_dstdir = output/s5
s5_files = $(call one_output_file_per_presentation,$(s5_dstdir),html)
s5: $(s5_files)
$(s5_dstdir)/%.html: $(presentations_dir)/%
	mkdir -p $(dir $@)
	$(pandoc_cmd) -t s5 --variable s5-url=$(base_template_dir)/s5 -o $@ -s $<

slidy_dstdir = output/slidy
slidy_files = $(call one_output_file_per_presentation,$(slidy_dstdir),html)
slidy: $(slidy_files)
$(slidy_dstdir)/%.html: $(presentations_dir)/% $(template_dir)/default.slidy
	mkdir -p $(dir $@)
	# $(pandoc_cmd) -f markdown -t slidy --variable slidy-url=$(base_template_dir)/slidy -o $@ -s $<
	$(pandoc_cmd) -t slidy -o $@ -s $<

epub_dstdir = output/epub
epub: $(call one_output_file_per_guide,$(html_dstdir),html)
$(epub_dstdir)/%.epub: $(presentations_dir)/%/*.rst
	mkdir -p $(dir $@)
	$(pandoc_cmd) -o $@ -s $^

# TEXINPUTS="$(shell pwd)/templates/beamer"
# TEXMFHOME="$(shell pwd)/templates/beamer"

pdf_dstdir = output/pdf
pdf_guides = $(call one_output_file_per_guide,$(pdf_dstdir)/guides,pdf)
pdf_presentations = $(pdf_dstdir)/presentations/Network_Traffic_Monitoring.pdf
pdf_files = $(pdf_guides) $(pdf_presentations)
pdf_clean:
	rm -f $(pdf_files)
pdf_force: pdf_clean pdf
pdf: $(pdf_files)
pandoc_beamer = $(pandoc_cmd) -t beamer --latex-engine=xelatex --toc \
	--variable handout=1 --toc-depth=4 --template=templates/beamer.tex
$(pdf_dstdir)/presentations/%.pdf: $(presentations_dir)/%/*.rst
	mkdir -p $(dir $@)
	ln -sf static images
	# $(pandoc_cmd) -t beamer -V theme:foo -o $@ $^
	echo ${TEXINPUTS}
	$(pandoc_beamer) -o $@ $^
	rm images
$(pdf_dstdir)/guides/%.pdf: $(guides_dir)/%
	mkdir -p $(dir $@)
	$(pandoc_cmd) -o $@ $^

test:
	echo $(odp_files)

odp_dstdir = output/odp
odp_files = $(call one_output_file_per_presentation,$(odp_dstdir),odp)
odp_clean:
	rm -f $(odp_files)
odp_force: odp_clean odp
odp: $(odp_files) templates/presentation.odp
$(odp_dstdir)/%.odp: $(presentations_dir)/%
	mkdir -p $(dir $@)
	ln -sf $(call invert_path,$(dir $<))/static $(dir $<)/images
	$(rst2odp) $< $@

rst_files = $(sources_mkd:%.mkd=%.rst)
rst_dangerous: $(rst_files)
$(rst_files): %.rst: %.mkd
	$(pandoc_cmd) -f markdown -t rst -o $@ $^
	
