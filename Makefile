presentation_dir = src/presentations

sources = $(wildcard $(presentation_dir)/*/*.rst)

all: html s5 slidy epub odp # pdf
clean:
	find output -type f | xargs -r rm

template_dir = templates
pandoc = pandoc --data-dir=. --variable static-url=$(base_path)/static
rst2odp_dir = tools/rst2odp
rst2odp = PYTHONPATH=$(rst2odp_dir) $(rst2odp_dir)/bin/rst2odp --traceback --template-file=templates/presentation.odp

remove_trailing_slash = $(patsubst %/,%,$(1))
invert_path = $(shell echo $(call remove_trailing_slash,$(1)) | sed -e 's|[^/]*|..|g')
# $(call base_path) inverts whatever target we are producing at the moment
base_path = $(call invert_path,$(dir $@))
base_template_dir = $(call base_path)/$(template_dir)

# one_output_file_per_input_file is called with three parameters:
#
# $(1): the source base directory, often $(presentation_dir), which is
#   removed from the input filename by pattern matching;
# $(2): the output directory, often a $(something_dstdir), which is
#   added to the input filename by pattern matching;
# $(3): the extension to be added to the destination filename, for
#   example .html.
# 
# so for example $(call one_output_file_per_input_file,$(presentation_dir),$(html_dstdir),.html)
# converts each input file $(presentation_dir)/a/b.rst to
# $(html_dstdir)/a/b.rst.html.

one_output_file_per_input_file = $(sources:$(1)/%=$(2)/%.$(3))

html_dstdir = output/html
html_files = $(call one_output_file_per_input_file,$(presentation_dir),$(html_dstdir),html)
html: $(html_files)
$(html_dstdir)/%.html: $(presentation_dir)/%
	mkdir -p $(dir $@)
	$(pandoc) -t html -o $@ -s $<

s5_dstdir = output/s5
s5_files = $(call one_output_file_per_input_file,$(presentation_dir),$(s5_dstdir),html)
s5: $(s5_files)
$(s5_dstdir)/%.html: $(presentation_dir)/%
	mkdir -p $(dir $@)
	$(pandoc) -t s5 --variable s5-url=$(base_template_dir)/s5 -o $@ -s $<

slidy_dstdir = output/slidy
slidy_files = $(call one_output_file_per_input_file,$(presentation_dir),$(slidy_dstdir),html)
slidy: $(slidy_files)
$(slidy_dstdir)/%.html: $(presentation_dir)/% $(template_dir)/default.slidy
	mkdir -p $(dir $@)
	# $(pandoc) -f markdown -t slidy --variable slidy-url=$(base_template_dir)/slidy -o $@ -s $<
	$(pandoc) -t slidy -o $@ -s $<

epub_dstdir = output/epub
epub: $(epub_dstdir)/Network_Traffic_Monitoring.epub
$(epub_dstdir)/%.epub: $(presentation_dir)/%/*.rst
	echo search for $(presentation_dir)/%/*.rst yielded: $^
	mkdir -p $(dir $@)
	$(pandoc) -o $@ -s $^

pdf_dstdir = output/pdf
pdf: $(pdf_dstdir)/Network_Traffic_Monitoring.pdf
$(pdf_dstdir)/%.pdf: $(presentation_dir)/%/*.rst
	mkdir -p $(dir $@)
	$(pandoc) -t beamer -o $@ $^

odp_dstdir = output/odp
odp_files = $(call one_output_file_per_input_file,$(presentation_dir),$(odp_dstdir),odp)
odp: $(odp_files) templates/presentation.odp
$(odp_dstdir)/%.odp: $(presentation_dir)/%
	mkdir -p $(dir $@)
	ln -sf $(call invert_path,$(dir $<))/static $(dir $<)/images
	$(rst2odp) $< $@

rst_files = $(sources_mkd:%.mkd=%.rst)
rst_dangerous: $(rst_files)
$(rst_files): %.rst: %.mkd
	$(pandoc) -f markdown -t rst -o $@ $^
	
