What is Security Management?
----------------------------

Provide access to network devices and corporate resources to authorized
individuals.

Why use Security Management?
----------------------------

* detect intrusions
* identify culprits
* ease account/password management
* prevent access by untrusted individuals

.. class:: handout

Security stops people from doing things they want to do:

* plugging their computer into the network
* downloading large files, videos and pornography
* installing unauthorised software on your computers
* accessing the network without authorization

Therefore it's important to sensibly balance security and ease of use,
and to be flexible (willing to change if necessary).

Sometimes good security makes life hard for legitimate users:

* having to remember many user accounts and passwords
* having to use long passwords which are hard to remember
* having to change their passwords regularly or if compromised
* not being able to access the network from the Internet
* not being able to access the network using any socket they want
* requiring the use of antivirus software that slows their computer down
* blocking legitimate traffic based on keywords
* installing security updates regularly creates downtime

These can be balanced by improved security technology:

having to remember many user accounts and passwords:
	provide a directory service integrated with most or all services, such
	as RADIUS, LDAP, Active Directory, Kerberos, FreeIPA, Samba4 or GoSa.
having to use long passwords which are hard to remember:
	Provide two-factor authentication such as hardware tokens to reduce
	password strength and change requirements while maintaining security.
having to change their passwords regularly or if compromised:
	provide a directory service as above.
not being able to access the network from the Internet:
	provide a VPN service such as OpenVPN, Cisco IPsec or IPsec/L2TP.
not being able to access the network using any socket they want:
	use 802.1x and RADIUS for network authentication instead of
	MAC address locking, to maintain identity and access control.
requiring the use of antivirus software that slows their computer down:
	choose antivirus software with lower performance impact, or use
	systems which are less vulnerable, such as tablets, phones and Linux
	machines.
blocking legitimate traffic based on keywords:
	slow down traffic, or monitor and investigate, instead of blocking
	traffic outright if it appears to breach acceptable use policy.
installing security updates regularly creates downtime:
	schedule and automate installation of security updates at quiet times
	such as during the night. Test security updates on some canary servers
	before applying to others, or using one of a redundant group.

What are good security practices?
---------------------------------

.. class:: handout

Too many to list! Some examples are:

* strong passwords, regularly changed, or two-factor authentication
* single sign on
* every password has an expiry date
* monitor attempts to log in using expired accounts
* run an intrusion detection system and tune it
* practise penetration testing, security bypass and intrusion response at least
  annually
* monitor web access for unusual/banned sites and protocols
* encrypt where possible: passwords, disks, emails, backups
* restrict access to certain IP addresses where possible
* use VPNs to provide additional protection on public services where possible
* install security updates regularly, on a schedule
* monitor security and antivirus status and alert if not updated
* lock down computers and user accounts to prevent unauthorised software
  installation
* ensure that computers use is always associated with a user account
* ensure that security protocols are written down and staff trained in them
* protect yourselves against social engineering and dumpster diving
* monitor blacklists to alert you if your IP addresses appear on them
* store system logs, especially security logs, on a write-only server
* physically secure network equipment, servers, desktops and laptops
* keep backups of servers and configurations to restore quickly after an
  intrusion

What is Accounting Management?
------------------------------

Usage information of network resources, for:

* detecting and tracing excessive use
* predicting future capacity needs
* auditing and forensics
* billing for usage or enforcing quotas (in some cases)

Detecting, tracing, billing and quotas are covered in the Bandwidth
Management unit.
