What is Performance Management?
-------------------------------

	Monitor and measure various aspects of performance so that overall
	performance can be maintained at an acceptable level.

How would you do it?

.. class:: handout

Some software tools return numerical information about services, or even
archive and graph it:

Smokeping
	collect and graph low-level packet loss and latency data from wireless
	and modulated Layer 2 links (quality of service/QoS).
Munin
	collect and graphing information from Unix servers, such
	as disk, memory and CPU usage, mail queue size, etc.
Windows Performance Counters
	collect and graphing information from multiple (newer) Windows servers
	across a network.
Nagios
	collect performance metrics as well as up/down decision data and
	from each service, can derive service uptime, can be graphed using
	add-ons.
Zenoss and Cacti
	collect performance metrics from devices with SNMP support and graph them.
pmacct, pmgraph, argus and nfsen
	collect network traffic information broken down by flow for analysis.
squid cache manager, webalizer and Google Analytics
	collect web traffic logs for analysis.

Why use Performance Management?
-------------------------------

* Forensic analysis of failures
* Predicting future failures

.. class:: handout

We most often use these graphs when a failure has occurred, or a problem is
detected by a monitoring system, such as:

* a server crashed
* a network connection is slow/congested/lossy
* Nagios detected a server running out of disk space or memory
* a server is/was running slowly (out of spec)

Nagios checks (yes/no answers) are our most important performance spec.
We set thresholds for things like:

* "too slow" page loading
* "too slow" email delivery
* "too much" packet loss
* "too little" disk space free

All these thresholds are arbitrary, *but* they often detect problems
before they occur. They also often create noise. Sometimes we have to
change the thresholds to reduce noise and keep the system useful.

By looking at the performance graphs we can establish correlations:

* The disk filled up suddently, overnight: someone left a job running?
* The network connection has been getting more congested for a while,
* Available bandwidth suddenly dropped two weeks ago when the ISP
  sent an engineer out to resolve another issue.
* The server's memory is nearly full every night: a scheduled cron job?

Usually these correlations either help us to create new hypotheses, or rule
out some hypotheses, to help us identify the cause. They rarely answer the
question by themselves.

Graphs are really useful for quickly analysing large quantities of performance
data that would otherwise be useless, to pick out correlations and trends
by engaging the brain's visual circuitry.

Careful with Performance Management!
------------------------------------

* It's possible to measure everything;
* Everything has a cost;
* The benefits are limited:

	* post-mortem analysis,
	* early warning of problems.

.. class:: handout

Performance data can require:

* a lot of CPU time and bandwidth to collect and aggregate;
* a lot of disk space to store;
* a lot of CPU to produce graphs.

For example, our monitoring system with 55 hosts, 650 services in Nagios
and 31 hosts, 1085 services in Munin, uses:

* 93% of one virtual CPU
* 5.7 GB disk space
* 1.8 GB per day bandwidth

