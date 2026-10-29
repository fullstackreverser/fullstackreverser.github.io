---
title: "Daily Hunt Feed - 2026-10-29"
date: 2026-10-29 02:42:25 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-10-29)

### Hacker News: Best

- [Code-execution flaw in UEFI firmware threatens most servers on planet Earth](https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/) — Tue, 27 Oct 2026 20:35:09 +0000
  - **Matched TTPs:** Bootkit (T1542.003), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Server (T1584.004), Firmware (T1592.003), Exploits (T1588.005), At (T1053.002)
- [Tailscale SSH: Investigation and remediation update](https://tailscale.com/ssh-investigation-update) — Tue, 27 Oct 2026 19:55:21 +0000
  - **Matched TTPs:** Vulnerabilities (T1588.006), SSH (T1021.004), At (T1053.002)
- [Discord will soon let anyone find public server messages through Google](https://discord.com/blog/making-content-from-discoverable-servers-easier-to-discover) — Tue, 27 Oct 2026 18:44:17 +0000
  - **Matched TTPs:** Server (T1584.004), At (T1053.002)

### BleepingComputer

- [Discord to let search engines index public server messages](https://www.bleepingcomputer.com/news/security/discord-to-let-search-engines-index-public-server-messages/) — Wed, 28 Oct 2026 14:44:16 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Search Engines (T1593.002), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Microsoft urges Entra ID admins to migrate users to passkeys](https://www.bleepingcomputer.com/news/microsoft/microsoft-reminds-entra-id-admins-to-migrate-users-to-passkeys/) — Wed, 28 Oct 2026 10:48:32 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Search Engines (T1593.002), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001)
- [InfraTrust report warns of exploited flaws in critical network infrastructure](https://www.bleepingcomputer.com/news/security/infratrust-report-warns-of-exploited-flaws-in-critical-network-infrastructure/) — Wed, 28 Oct 2026 10:00:00 -0400
  - **Matched TTPs:** Network Devices (T1584.008), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Server (T1584.004), Search Engines (T1593.002), Tool (T1588.002), Firmware (T1592.003), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Even after PHP2Shell, blast radius matters more than a CVSS score](https://www.bleepingcomputer.com/news/security/even-after-php2shell-blast-radius-matters-more-than-a-cvss-score/) — Wed, 28 Oct 2026 09:50:59 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Server (T1584.004), Search Engines (T1593.002), Tool (T1588.002), Software (T1592.002), Exploits (T1588.005), Credentials (T1589.001), At (T1053.002)

### Darkreading

- [Attacker Relentlessly Scans for Credentials by Impersonating AI Bots](https://www.darkreading.com/cyber-risk/attacker-impersonates-ai-bots-scans-credentials) — Wed, 28 Oct 2026 14:37:52 GMT
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Software (T1592.002), Credentials (T1589.001), Impersonation (T1656), At (T1053.002)

### The Hacker News

- [Google to Allow One-Tap Android App Installs From Approved Third-Party Stores Outside U.S.](https://thehackernews.com/2026/10/google-to-allow-one-tap-android-app.html) — Wed, 28 Oct 2026 22:38:09 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [Researcher Reveals How Logic Bugs Alone Cracked Microsoft Edge in $175,000 Pwn2Own Win](https://thehackernews.com/2026/10/researcher-reveals-how-logic-bugs-alone.html) — Wed, 28 Oct 2026 21:53:34 +0530
  - **Matched TTPs:** JavaScript (T1059.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [PHP2Shell Attack Roots 25 Servers, Breaches U.S. Government-Affiliated Network](https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html) — Wed, 28 Oct 2026 21:32:45 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Web Shell (T1505.003), Server (T1584.004), Proxy (T1090), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [Critical 16-Year-Old UEFI Flaw Can Run Code Before Secure Boot on Network-Booting Servers](https://thehackernews.com/2026/10/critical-16-year-old-uefi-flaw-can-run.html) — Wed, 28 Oct 2026 17:20:00 +0530
  - **Matched TTPs:** Network Devices (T1584.008), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), SSH (T1021.004), Server (T1584.004), Proxy (T1090), Firmware (T1592.003), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [Wazuh and AI for Enhanced SOC Workflows](https://thehackernews.com/2026/10/wazuh-and-ai-for-enhanced-soc-workflows.html) — Wed, 28 Oct 2026 17:00:00 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Network Devices (T1584.008), Malware (T1588.001), Databases (T1213.006), Vulnerabilities (T1588.006), SSH (T1021.004), Server (T1584.004), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [Adobe Fixes 8 Critical Campaign Classic Flaws Allowing Code Execution and Security Bypass](https://thehackernews.com/2026/10/adobe-fixes-8-critical-campaign-classic.html) — Wed, 28 Oct 2026 16:45:51 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [American Organizations Under Attack: Skyw4lker Device Code Phishing Campaign Exposed](https://thehackernews.com/2026/10/american-organizations-under-attack.html) — Wed, 28 Oct 2026 16:00:00 +0530
  - **Matched TTPs:** IP Addresses (T1590.005), JavaScript (T1059.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Domains (T1584.001), Proxy (T1090), Compromise Accounts (T1586), Cloud Services (T1021.007), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [Anthropic's Unreleased AI Model Chains Flaws Into Working Chrome, Safari, Windows and Linux Exploits](https://thehackernews.com/2026/10/anthropics-unreleased-ai-model-chains.html) — Wed, 28 Oct 2026 13:45:07 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), JavaScript (T1059.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Server (T1584.004), Proxy (T1090), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers](https://thehackernews.com/2026/10/tailscale-patches-ssh-flaws-that-could.html) — Wed, 28 Oct 2026 11:50:37 +0530
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), SSH (T1021.004), Server (T1584.004), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html) — Wed, 28 Oct 2026 11:34:58 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Web Shell (T1505.003), Server (T1584.004), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [Adobe Commerce PolyShell Attacks Breach Hundreds of Stores as Brotli Exploit Traffic Emerges](https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html) — Wed, 28 Oct 2026 11:12:26 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
