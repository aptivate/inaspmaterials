#!/bin/sh

for i in benchmark-100ms-1mbit-symmetric-*-competition-n20.out; do
	echo $i | sed -e 's/.*symmetric-//' -e 's/-.*//'
done | sort -g | uniq > bandwidths.txt

for i in `cat bandwidths.txt`; do 
	time=`grep '^Time per request:' benchmark-100ms-1mbit-symmetric-$i-competition-n20.out \
		| grep -v 'mean,' \
		| tail -1 \
		| sed -e 's/.*: //' -e 's/ \[ms\].*//'` 
	echo $i $time | sed -e 's/ /,/g'
done > results.csv
