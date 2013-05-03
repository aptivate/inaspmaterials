#!/bin/sh

if [ -z "$1" ]; then
	echo "Usage: $0 <unique-test-id>" >&2
	exit 2
fi

# ab -c 20 -n 200 -e benchmark-$1-n20.csv -g benchmark-$1-n20.gnuplot http://10.0.156.214/ \
# 	| tee -a benchmark-$1-n20.out
httperf --server 10.0.156.214 --num-conns 200 --verbose | tee httperf-$1-200.out
