gh-pages:
	make -C master clean all
	rm -rf generated
	cp -a master/output generated
	rst2html master/README.rst > index.html
