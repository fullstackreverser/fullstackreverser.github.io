---
title: "Daily Hunt Feed - 2026-09-19"
date: 2026-09-19 01:27:37 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-09-19)

### Hacker News: Best

- [Bend 2 and the Vibe-Coding Trap](https://blog.liampwll.com/posts/bend_vibe_coding/) — Fri, 18 Sep 2026 12:03:55 +0000
  - **Matched TTPs:** Trap (T1546.005), At (T1053.002)
- [Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint](https://prismml.com/news/bonsai-2-27b) — Thu, 17 Sep 2026 21:13:31 +0000
  - **Matched TTPs:** Hardware (T1592.001), Tool (T1588.002), At (T1053.002), Compression (T1027.015)

### BleepingComputer

- [Gyazo server flaw exploited to steal 23.6 million user records](https://www.bleepingcomputer.com/news/security/gyazo-server-flaw-exploited-to-steal-236-million-user-records/) — Fri, 18 Sep 2026 12:00:38 -0400
  - **Matched TTPs:** IP Addresses (T1590.005), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Email Addresses (T1589.002), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Fake LastPass Authenticator GitHub repos push new Rapuncel infostealer](https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/) — Fri, 18 Sep 2026 11:19:06 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Windows Service (T1543.003), DLL (T1574.001), Server (T1584.004), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), Impersonation (T1656), Windows Credential Manager (T1555.004), At (T1053.002)
- [Secure enterprise sharing with access reviews for Microsoft 365](https://www.bleepingcomputer.com/news/security/secure-enterprise-sharing-with-access-reviews-for-microsoft-365/) — Fri, 18 Sep 2026 10:00:10 -0400
  - **Matched TTPs:** Sharepoint (T1213.002), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [New Check Point flaw lets hackers execute code with root privileges](https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/) — Fri, 18 Sep 2026 05:34:33 -0400
  - **Matched TTPs:** IP Addresses (T1590.005), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Server (T1584.004), Tool (T1588.002), Software (T1592.002), At (T1053.002)

### The Hacker News

- [Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root](https://thehackernews.com/2026/09/public-exploits-released-for-four-linux.html) — Fri, 18 Sep 2026 23:32:24 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Network Devices (T1584.008), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html) — Fri, 18 Sep 2026 22:26:19 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.](https://thehackernews.com/2026/09/an-abandoned-cdn-domain-was-re.html) — Fri, 18 Sep 2026 16:31:16 +0530
  - **Matched TTPs:** Scheduled Task (T1053.005), JavaScript (T1059.007), DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Domains (T1584.001), Web Shell (T1505.003), Server (T1584.004), Code Repositories (T1213.003), PowerShell (T1059.001), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage](https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html) — Fri, 18 Sep 2026 16:10:06 +0530
  - **Matched TTPs:** JavaScript (T1059.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Web Shell (T1505.003), Server (T1584.004), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer](https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html) — Fri, 18 Sep 2026 14:48:03 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), JavaScript (T1059.007), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Email Addresses (T1589.002), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [RatHat Android Malware Abuses ADB to Retain Shell Access After Uninstall](https://thehackernews.com/2026/09/rathat-android-malware-abuses-adb-to.html) — Fri, 18 Sep 2026 11:47:25 +0530
  - **Matched TTPs:** Keylogging (T1056.001), Artificial Intelligence (T1588.007), Malvertising (T1583.008), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Proxy (T1090), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root](https://thehackernews.com/2026/09/critical-check-point-management-server.html) — Thu, 17 Sep 2026 23:38:28 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories](https://thehackernews.com/2026/09/threatsday-self-rewriting-agents-800.html) — Thu, 17 Sep 2026 23:02:22 +0530
  - **Matched TTPs:** Keylogging (T1056.001), Artificial Intelligence (T1588.007), Malware (T1588.001), Hardware (T1592.001), Databases (T1213.006), Vulnerabilities (T1588.006), DLL (T1574.001), Botnet (T1584.005), Web Shell (T1505.003), Server (T1584.004), Proxy (T1090), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Firmware (T1592.003), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Hidden Window (T1564.003), At (T1053.002)
- [Iran-Linked Handala Hack Tied to HEAVYGRAM Telegram Backdoor That Can Steal Passwords](https://thehackernews.com/2026/09/iran-linked-handala-hack-tied-to.html) — Thu, 17 Sep 2026 19:33:13 +0530
  - **Matched TTPs:** WHOIS (T1596.002), Malware (T1588.001), Vulnerabilities (T1588.006), DLL (T1574.001), Masquerading (T1036), Web Shell (T1505.003), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
