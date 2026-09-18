---
title: "Daily Hunt Feed - 2026-09-18"
date: 2026-09-18 01:24:08 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-09-18)

### Hacker News: Best

- [Neovim have a ~$800k Bitcoin donation sitting untouched since 2023](https://news.ycombinator.com/item?id=49738879) — Thu, 17 Sep 2026 10:44:49 +0000
  - **Matched TTPs:** Hardware (T1592.001), Private Keys (T1552.004), Lua (T1059.011), Software (T1592.002), At (T1053.002)

### BleepingComputer

- [New RatHat Android malware uses AI to automate device control](https://www.bleepingcomputer.com/news/security/new-rathat-android-malware-uses-ai-to-automate-device-control/) — Thu, 17 Sep 2026 17:50:26 -0400
  - **Matched TTPs:** Keylogging (T1056.001), Artificial Intelligence (T1588.007), Malvertising (T1583.008), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Brevo supply-chain attack injected ClickFix scripts on customer sites](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/) — Thu, 17 Sep 2026 13:11:34 -0400
  - **Matched TTPs:** JavaScript (T1059.007), DNS (T1071.004), Malware (T1588.001), Hardware (T1592.001), Domains (T1584.001), Server (T1584.004), Email Addresses (T1589.002), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [US takes down NightmareStresser DDoS-for-hire platform](https://www.bleepingcomputer.com/news/security/fbi-seizes-nightmarestresser-service-linked-to-thousands-of-ddos-attacks/) — Thu, 17 Sep 2026 07:33:35 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Domains (T1584.001), Server (T1584.004), Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [Chinese hackers use SparroWocky malware in govt espionage attacks](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/) — Thu, 17 Sep 2026 05:00:00 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Windows Service (T1543.003), DLL (T1574.001), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [Microsoft shares workaround for Windows domain login issues](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-workaround-for-windows-domain-login-authentication-issues/) — Thu, 17 Sep 2026 04:24:48 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), At (T1053.002)

### Darkreading

- [CISA Ditches Weekly Vulnerability Roundups for Risk-Based Focus](https://www.darkreading.com/cyber-risk/cisa-ditches-weekly-vuln-roundups-risk-based-focus) — Thu, 17 Sep 2026 21:23:50 GMT
  - **Matched TTPs:** Vulnerabilities (T1588.006), Software (T1592.002), At (T1053.002)

### The Hacker News

- [Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html) — Thu, 17 Sep 2026 18:00:00 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002), Compression (T1027.015)
- [CISO's Expert Guide to Agentic Pentesting for Websites](https://thehackernews.com/2026/09/cisos-expert-guide-to-agentic.html) — Thu, 17 Sep 2026 16:20:53 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Email Addresses (T1589.002), Tool (T1588.002), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [China-Aligned FamousSparrow Deploys SparroWocky Backdoor Across Latin America](https://thehackernews.com/2026/09/china-aligned-famoussparrow-deploys.html) — Thu, 17 Sep 2026 15:35:45 +0530
  - **Matched TTPs:** IP Addresses (T1590.005), Malware (T1588.001), Vulnerabilities (T1588.006), DLL (T1574.001), Web Shell (T1505.003), Server (T1584.004), Proxy (T1090), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS](https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html) — Thu, 17 Sep 2026 13:30:29 +0530
  - **Matched TTPs:** DNS (T1071.004), DNS Server (T1584.002), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Gyazo Breach Exposes 23.62 Million User Records and 490 Million Image Metadata Records](https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html) — Thu, 17 Sep 2026 13:00:01 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Email Addresses (T1589.002), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [U.S. Seizes NightmareStresser Domains Linked to Hundreds of Thousands of DDoS Attacks](https://thehackernews.com/2026/09/us-seizes-nightmarestresser-domains.html) — Thu, 17 Sep 2026 10:43:46 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), Domains (T1584.001), Web Shell (T1505.003), Tool (T1588.002), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
