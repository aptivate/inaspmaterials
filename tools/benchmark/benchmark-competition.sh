#!/bin/bash

set -e 
# for competition in 0 100 200 300 400 500 600 700 800 900 \
# 910 920 930 940 950 960 970 980 990 1000 \
# for competition in 1010 1020 1030 1040 1050 1060 1070 1080 1090 1100 \
#	1200 1300 1400 1500 1600 1700 1800 1900 2000;
for competition in \
	`seq 500 100 799` \
	`seq 800  10 899` \
	`seq 900   5 1100`
do
	[ $competition -gt 0 ] && \
		iperf -c 10.0.156.214 -u -U -t 3600 -b ${competition}k \
		> iperf-${competition}k-competition.log &
	./benchmark-once.sh 100ms-1mbit-symmetric-${competition}k-competition
	[ $competition -gt 0 ] && killall iperf
done
