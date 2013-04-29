sources_mkd = $(wildcard */*.mkd)

all: html s5 slidy
clean:
	find output -type f | xargs -r rm

template_dir = templates
pandoc = pandoc --data-dir=.

remove_trailing_slash = $(patsubst %/,%,$(1))
invert_path = $(shell echo $(call remove_trailing_slash,$(1)) | sed -e 's|[^/]*|..|g')
# $(call base_path) inverts whatever target we are producing at the moment
base_path = $(call invert_path,$(dir $@))
base_template_dir = $(call base_path)/$(template_dir)

html_dstdir = output/html
html_files = $(sources_mkd:%.mkd=$(html_dstdir)/%.html)
html: $(html_files)
$(html_dstdir)/%.html: %.mkd
	mkdir -p $(dir $@)
	$(pandoc) -f markdown -t html -o $@ -s $<

s5_dstdir = output/s5
s5_files = $(sources_mkd:%.mkd=$(s5_dstdir)/%.html)
s5: $(s5_files)
$(s5_dstdir)/%.html: %.mkd
	mkdir -p $(dir $@)
	$(pandoc) -f markdown -t s5 --variable s5-url=$(base_template_dir)/s5 -o $@ -s $<

slidy_dstdir = output/slidy
slidy_files = $(sources_mkd:%.mkd=$(slidy_dstdir)/%.html)
slidy: $(slidy_files)
$(slidy_dstdir)/%.html: %.mkd
	mkdir -p $(dir $@)
	# $(pandoc) -f markdown -t slidy --variable slidy-url=$(base_template_dir)/slidy -o $@ -s $<
	$(pandoc) -f markdown -t slidy -o $@ -s $<
