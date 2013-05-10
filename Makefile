.PHONY: default clean gh-pages

default: gh-pages

clean:
	make -C master clean
	rm -rf generated

gh-pages:
	make -C master all
	rsync -a --delete master/output/ generated/
	rst2html master/README.rst > index.html \
		--stylesheet-path=styles/html4css1.css,master/static/CharisSIL-4.112-web/web/CharisSIL-webfont-example.css \
		--link-stylesheet
