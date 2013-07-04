Overview of Challenges and Solutions
====================================

Target participants
-------------------
This workshop is specifically aimed at:

* ICT/Computer centre director
  * responsible for ICT policy development and implementation
* Other senior staff
  * responsible for the development and implementation of ICT policies
* Head librarians or senior library staff
  * involved in the development and implementation of ICT policies
  and should benefit from them

Introductions
-------------

Name, institution, role within your institution, questions:

* How many people in your IT department?
* How many computers on your network?
* How much bandwidth do you have?
* What is the biggest problem on your network?
* Any other areas that you would like us to cover?

.. class:: handout

If you are facilitating, you may wish to go round twice; once for the participants
to introduce themselves, and then again for them to answer the questions above.

Content outline
---------------

* The role of a supportive policy environment
* Why policies often fail (examples of unsuccessful policy development)
* User authentication requirements and features
* Developing appropriate policies
* Sample policy review and development
* Planning an effective policy development process
* Writing an effective policy
* Implementing policy
* Policy implications and applications

Outcomes
--------

* Examine the importance of a supportive policy environment for successful BMO
* Review key policies and an appropriate policy development framework
* Review BMO supportive policies
* Create an institutional level policy development action plan

Pre workshop task
-----------------

* Request participants to bring five printed copies of their organisations “acceptable use policy” (AUP) relating to computers and the Internet
  * http://en.wikipedia.org/wiki/Acceptable_use_policy 
  * These could include draft documents, working documents, implemented or planned policies, etc.
* Also include electronic copies if possible (e.g. MS Word, PDF, or website URL)
* Please send electronic copies to the organisers in advance if possible.
	http://en.wikipedia.org/wiki/Acceptable_use_policy 

The State of Nature Game
------------------------

Play the State of Nature Game described in the
`facilitators' notes <Unit_10_Facilitation.rst>`_, to learn about public
goods, free riding and collaboration vs. competition.

Rules of the game:

* The facilitator plays the role of Nature
* Each player begins the game with 100 Monetary Units (MU)
* In each round, each player must pay a survival cost of 10 MU
* Nature is bountiful and matches this amount
* The whole amount collected is auctioned off
* All bids are forfeit to the winner
* All agreements are permitted
* No agreements are binding
* No violence is permitted
* The object is to maximise your own outcome

Definition of a Public Good
---------------------------

A public good can be defined as:

* any good (resource or valuable thing)
* that the members of a community benefit from,
* irrespective of whether they have contributed to it, and
* which they can consume in arbitrary amounts (as much or as little as
  they wish to).

TCP/IP and Congestion
---------------------

Understanding basic TCP/IP issues is important in understanding problems of
overloaded and slow Internet connections:

* IP = Internet Protocol, basic protocol on which the Internet is built.
  * A "connectionless" and "unreliable" protocol.
* TCP = Transmission Control Protocol
  * A connection-oriented, reliable-transport protocol.
  * Adds (among other things) "flow control" to the IP layer.
  * When each TCP segments is received, an acknowledgement is sent back.
  * If a segment is not acknowledged then it is retransmitted by the sender.

TCP increases sending rate whenever no packets are lost. Thus it uses all the
available bandwidth and causes congestion (deliberately).

Multiple connections share bandwidth "fairly" between them.

Congestion causes network collapse for all users; see `Effect of Congestion
<https://github.com/aptivate/inaspmaterials/blob/master/src/Network_Management/Unit_6_Solving_Network_Problems/Unit_6_Presentation.rst#effect-of-congestion>`_ in Unit 6 for details.

Policy and Behaviour
--------------------

Technical measures alone fail to change behaviour. Why?

"5% of users use 50% of the traffic, so 95% should be on your side."
Discuss.

Policy and Behaviour
--------------------

* Who has authority to create policy?
* Who has authority to implement technical measures?
* Who do users fear more?
* Whose side are the users on? What do they want?

Policy-based solutions
----------------------

* Aim to bring about behavioral change
* Treat bandwidth just as any common good that needs policy management
* Can require or authorise use of technical solutions
  * distribute the bandwidth evenly between users
  * make sure that no one user can damage other users' experiences
  * can prioritise and restrict traffic flows or users but which ones and how?
  * do not automatically ensure that the traffic that flows is consistent
  with institutional purposes

Examples of policy based approaches
-----------------------------------

Some simple examples, that we can come back to later.

A policy that says something about:

Appropriate and inappropriate use
	Can be used to reward/punish such behaviour
Ability to limit traffic by volume
	Can be used to set quotas
Ability to shape traffic
	Can be used to throttle non-core online resources or speed up core ones
Virus protection and software standards
	Can be used to remove problem computers/users from the network who do not comply

