---
title: "Daily Hunt Feed - 2026-06-16"
date: 2026-06-16 02:08:49 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-06-16)

### Hacker News: Best

- [Ask HN: Has anyone replaced Claude/GPT with a local model for daily coding?](https://news.ycombinator.com/item?id=48542100) — Mon, 15 Jun 2026 14:46:53 +0000
  - **Matched TTPs:** DNS (T1071.004), Hardware (T1592.001), SSH (T1021.004), Domains (T1584.001), Cloud API (T1059.009), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [Hetzner increased dedicated server prices 3-4x](https://news.ycombinator.com/item?id=48542064) — Mon, 15 Jun 2026 14:44:02 +0000
  - **Matched TTPs:** Server (T1584.004)
- [Hetzner Price Adjustment](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) — Mon, 15 Jun 2026 13:19:39 +0000
  - **Matched TTPs:** Hardware (T1592.001), Server (T1584.004)
- [Even more batteries included with Emacs](https://karthinks.com/software/even-more-batteries-included-with-emacs/) — Mon, 15 Jun 2026 02:30:25 +0000
  - **Matched TTPs:** Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [Formal methods and the future of programming](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) — Sun, 14 Jun 2026 12:35:27 +0000
  - **Matched TTPs:** Hardware (T1592.001), Vulnerabilities (T1588.006), Tool (T1588.002), Software (T1592.002), At (T1053.002)

### BleepingComputer

- [SimpleHelp bug lets hackers create rogue remote support accounts](https://www.bleepingcomputer.com/news/security/simplehelp-bug-lets-hackers-create-rogue-remote-support-accounts/) — Mon, 15 Jun 2026 16:06:52 -0400
  - **Matched TTPs:** Rootkit (T1014), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Email Addresses (T1589.002), Tool (T1588.002), Multi-Factor Authentication (T1556.006), Software (T1592.002), At (T1053.002)
- [Chinese hackers breach REDCap servers, steal medical research](https://www.bleepingcomputer.com/news/security/chinese-hackers-breach-redcap-servers-steal-medical-research/) — Mon, 15 Jun 2026 10:00:00 -0400
  - **Matched TTPs:** Rootkit (T1014), Malware (T1588.001), Hardware (T1592.001), Databases (T1213.006), Botnet (T1584.005), Server (T1584.004), Email Addresses (T1589.002), Proxy (T1090), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001)
- [New attack turned Microsoft 365 Copilot into 1-click data theft tool](https://www.bleepingcomputer.com/news/security/new-attack-turned-microsoft-365-copilot-into-1-click-data-theft-tool/) — Mon, 15 Jun 2026 09:00:00 -0400
  - **Matched TTPs:** Sharepoint (T1213.002), Artificial Intelligence (T1588.007), Rootkit (T1014), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), At (T1053.002)
- [Webinar: How behavioral AI stops phishing and account takeovers](https://www.bleepingcomputer.com/news/security/webinar-how-behavioral-ai-stops-phishing-and-account-takeovers/) — Mon, 15 Jun 2026 08:12:20 -0400
  - **Matched TTPs:** Rootkit (T1014), Malware (T1588.001), Hardware (T1592.001), Tool (T1588.002), Phishing (T1566), Software (T1592.002), At (T1053.002)

### Darkreading

- [China-Nexus Actor Spy on US Researchers Undetected for a Year](https://www.darkreading.com/threat-intelligence/china-nexus-actor-us-researchers-undetected) — Mon, 15 Jun 2026 17:00:45 GMT
  - **Matched TTPs:** IP Addresses (T1590.005), Malware (T1588.001), Vulnerabilities (T1588.006), Server (T1584.004), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Credentials (T1589.001), At (T1053.002)

### The Hacker News

- [Chinese Hackers Abused Google Workspace Rules to Steal Research and Defense Emails](https://thehackernews.com/2026/06/chinese-hackers-abused-google-workspace.html) — Tue, 16 Jun 2026 01:14:06 +0530
  - **Matched TTPs:** Rootkit (T1014), Malware (T1588.001), Databases (T1213.006), Vulnerabilities (T1588.006), Server (T1584.004), Email Addresses (T1589.002), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [North Korean Hackers Are Turning Developer Tools Into Malware Delivery Channels](https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html) — Tue, 16 Jun 2026 01:02:52 +0530
  - **Matched TTPs:** Keylogging (T1056.001), Sharepoint (T1213.002), Artificial Intelligence (T1588.007), Rootkit (T1014), JavaScript (T1059.007), Malware (T1588.001), Browser Extensions (T1176.001), Vulnerabilities (T1588.006), SSH (T1021.004), AppleScript (T1059.002), Masquerading (T1036), Server (T1584.004), PowerShell (T1059.001), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers](https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html) — Mon, 15 Jun 2026 22:09:01 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Rootkit (T1014), Vulnerabilities (T1588.006), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html) — Mon, 15 Jun 2026 20:39:05 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Rootkit (T1014), Vulnerabilities (T1588.006), Domains (T1584.001), Server (T1584.004), Proxy (T1090), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), At (T1053.002)
- [⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More](https://thehackernews.com/2026/06/weekly-recap-chrome-0-day-unifi.html) — Mon, 15 Jun 2026 19:19:29 +0530
  - **Matched TTPs:** Scheduled Task (T1053.005), Artificial Intelligence (T1588.007), Rootkit (T1014), JavaScript (T1059.007), DNS (T1071.004), Malvertising (T1583.008), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), DLL (T1574.001), Domains (T1584.001), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Multi-Factor Authentication (T1556.006), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Bidirectional Communication (T1102.002), Python (T1059.006), Malicious Link (T1204.001), At (T1053.002)
- [Popular WordPress Plugin Scripts Tampered to Plant Hidden Backdoors on Sites](https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html) — Mon, 15 Jun 2026 15:29:38 +0530
  - **Matched TTPs:** Rootkit (T1014), JavaScript (T1059.007), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect VPN Flaw](https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html) — Mon, 15 Jun 2026 11:47:32 +0530
  - **Matched TTPs:** IP Addresses (T1590.005), Rootkit (T1014), Vulnerabilities (T1588.006), Software (T1592.002), Social Media (T1593.001), At (T1053.002)
