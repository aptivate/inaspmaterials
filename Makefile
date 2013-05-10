gh-pages:
	make -C master clean all
	rm -rf generated
	cp -a master/output generated
	cp -a master/README.rst .
