.. include:: <s5defs.txt>

.. include:: Series.rst.inc

Unit 2: Why Monitor
===============================

INASP Network Monitoring Workshops
----------------------------------

:Authors:
	- Dick Elleray, AfriConnect (delleray@africonnect.com);
	- Chris Wilson, Aptivate (chris+inaspbmo2013@aptivate.org)
:Date:   2013-04-29

.. class:: handout

  Everything that is in this block will only be in the notes.
  You can put these on each slide.

Objectives
----------

On completion of this session, we hope you will:

* Understand why congestion happens, and causes slow page loading.

* Understand how to change users behaviour by providing the right
  incentives.
  
* Understand how monitoring helps you to create those incentives.

* Understand how monitoring can help you to improve and repair your
  network and Internet connection.
  
Advice on how to carry out monitoring is given in Unit 3.
  
Why Monitor
-----------

How else do you know if:

* You are getting what you paid for
* It is being used for the purpose intended
* It is being used efficiently
* Anything is going wrong
* You are making the most of what you have
* You know what you need for the future

Bandwidth Questions
-------------------

Questions you might want to answer:

* What is the biggest problem on your network?

    * What do users complain about?

* What are response times (latency) for loading external sites?

   -  Latency causes most perceived network slowness
   -  If it's overloaded, response time increases, so reduce the load

* How is your connection currently being used?

   -  What websites are people visiting, how much?
   -  Who are the heaviest users, how much?
   -  When is the connection fully utilised/overloaded?

* Do you actually get all the bandwidth you pay for?

Troubleshooting Questions
-------------------------

* Is the connection working at all?

   -  When did it break, how long ago?
   -  Where is the break? On my side or the ISP?

* How fast is the connection right now?

   -  If a user says it's slow, can I confirm or refute that claim?

* Can you detect and fix problems before users complain?

   -  How quickly do you respond to automated alerts?

* How quickly and effectively are user complaints resolved?

   -  How do you reduce the chances of the same problem reoccuring?

* How can you track down and stop malicious/unwanted activity?

   -  Identify the user and talk to them?
   -  Firewalls, web proxies, content filtering?

Well managed bandwidth
----------------------

.. figure:: images/traffic-graph-good.png

   Traffic graph of a well-managed busy network. Green = incoming, Blue = Outgoing.

What does this graph tell you?

.. class:: handout

On this graph you can see that:

* Maximum traffic load of 12.4 Mbps
* The circuit is symmetric
* The connection is not overloaded (~95% full)

Badly managed bandwidth
-----------------------

.. figure:: images/traffic-graph-bad.png

   Traffic graph of a badly-managed busy network. Green = incoming, Blue = Outgoing.

By contrast, on this graph:

* Maximum traffic load of 10 Mbps
* Symmetric circuit
* Completely saturated (100%) during office hours

A small change to bandwidth use (95% to 100%) makes a huge difference to
user experience. But how and why?

What causes congestion
----------------------

IP (the Internet protocol standard) includes TCP (Transmission Control
Protocol):

* provides reliable delivery of large data streams
* used by most Internet traffic, including web pages, downloads and videos
* tries to use maximum possible bandwidth
* therefore it creates congestion

Latency, queues and delays
--------------------------

Why does latency matter? Imagine a shop that serves one customer per minute:

- If customers arrive at 0.99 per minute:

   - no queue, and each customer gets immediate attention.

- If customers arrive at 1.01 per minute:

   - a queue builds up, customers wait longer and longer, some get
     bored and leave.

In the second case, the shop makes 2% more money, but the customers
experience is completely different!

Congestion and internet speed
-----------------------------

What effect does congestion have on page loading speed?

.. figure:: images/congestion-vs-latency.png

* Web page loads very fast (~0.25 seconds) until connection is 98% full.
* At 100% full it takes 1 second
* At 105% full (5% packet loss) it takes 6 seconds

Is congestion affecting your network?

* If browsing is fast when nobody is using the network, then probably.

.. class:: handout

  It may be that your Internet provider has congestion on their side as
  well/instead. You can apply monitoring and diagnostic techniques to 
  understand where the problem is.

What can you do?
----------------

You need to increase *supply* and/or reduce *demand*:

-  Buy more bandwidth (expensive)
-  Optimise the efficiency of the circuit (2-5% increase? not much)

   -  Major problems such as packet loss or high latency have a bigger
      impact, and are worth fixing.
   -  Sometimes can find and fix completely unwanted traffic such as
      viruses and spam.

-  Provide an incentive for good behaviour

   -  Charge, block, limit, inform, shame or punish users

Monetary Options
----------------

Buy more bandwidth
~~~~~~~~~~~~~~~~~~

-  Expensive
-  Often only a short-term solution
-  Can make things worse (encourage bad behaviour)
-  Important to benchmark costs

Charge for bandwidth used
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Very effective at dampening demand
-  Can fund growth of the circuit
-  *Highly damaging* to educational and research objectives

Other incentives for good behaviour
-----------------------------------

-  Give users feedback about how much bandwidth they're using.
-  Give each users a limited bandwidth quota.
-  Ensure that abusive users hurt themselves, not others.
-  Engage with highest bandwidth users.

   -  "Have a chat" with them
   -  Name and shame them

-  Block access to some resources.

   -  Unpopular with users - they want Facebook and Youtube!
   -  Least preferred option! But technically easiest.
   -  How much impact will it have? Is it worth the cost?
   -  Reduce bandwidth available at peak times instead of blocking?

All of these require monitoring to implement them

-  Except "Ensure that abusive users hurt themselves, not others" which
   can be automatic.

Changing user behaviour
-----------------------

Change in behaviour must be *voluntary*:

-  You have an Acceptable Use Policy (AUP);
-  It allows you to take action (including monitoring);
-  All users have read it, and agreed to follow it.

   -  That means they have to understand how and why it benefits them.

Otherwise, the users will be fighting against you instead of for you.
And there are more of them.

Choose your path
----------------

Which one do you prefer?

-  Buy more bandwidth

   -  Can you afford it? Good value for money?

-  Pass on bandwidth costs

   -  How do you measure individual use?
   -  Highly damaging to educational and research objectives.

-  Change user behaviour

   -  Hard work, but better than the other options?
   -  Good network management includes changing user behaviour.

We assume that you want to change user behaviour. Then you need
monitoring.

Group Discussion
----------------

-  What sorts/aspects of traffic could be monitored?
-  Why are those sorts/aspects of traffic monitoring important?
-  Which does your institution monitor?
-  Have you found it of use? How and why?

.. slide-layout:: 2column

Monitor/measure – Example
-------------------------

-  Protocols
-  Dropped packets
-  IPs in use on LAN
-  P2P
-  Virus traffic
-  Hackers spoofing
-  SMTP (illegitimate mail)
-  Usage (who, what)

.. column:: 2

-  Applications using high bandwidth
-  Movies
-  Music
-  telnet
-  Voip/sip
-  Microsoft ds
-  Non business browsing
-  Amount of bandwidth (per user if poss)
