.. include:: <s5defs.txt>

.. include:: ../includes/Series.rst

Unit 8: Hands-on Practical Experience
=====================================

.. include:: ../includes/Authors.rst

Objectives
----------

On completion of this session, we hope you will be able to:

* Use common inbuilt network monitoring tools for simple network checks
* Install / use the Wireshark software packet probe on PC and Linux systems
* Install / use a typical more complex monitoring tool on a Linux system.
* Explore the facilities available on a Linux-based self-contained monitoring toolkit.

.. class:: handout

If you are the facilitator, please tell the group: 

	At the end of session I will ask if we have met the objectives – if not,
	we will discuss again.

Linux networking primer
-----------------------

Try out the following commands on a Linux command line:

* ip link list
* ip address show
* ip route show
* route –n
* ip neigh show
* ping anotherip –c 5
* ip neigh show
* ip neigh delete anotherip dev eth0
* ip neigh show
* ping 224.0.0.1 –c 5
* nmap -sO 127.0.0.1
* nmap -sS 127.0.0.1
* ping 224.0.0.1 -c 5
* traceroute www.bbc.co.uk
* netstat –I
* netstat –Mn
* netstat -an

If in doubt, try the manuals!

Install software packages on Linux
----------------------------------

Installation (or watch installation) and usage of the following packages:

* Webmin
	* See handout for installation instructions, watch live demo
* Ethereal
	* You should try to install package then deinstall using WebMin during
	  the course (only one person at a time !)
* Nagios
	* Watch demonstration
	* Try using it (see url on board)
	* Install yourself when you get back.
* MRTG
* Cacti
* Webalizer
* AWStats
* SawMill (if available)

.. class:: handout

TODO: complete instructions, walkthroughs and screenshots for these.




