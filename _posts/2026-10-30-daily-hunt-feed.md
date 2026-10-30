---
title: "Daily Hunt Feed - 2026-10-30"
date: 2026-10-30 02:49:11 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-10-30)

### BleepingComputer

- [Hugging Face malware campaign returns to hijack GPUs for crypto mining](https://www.bleepingcomputer.com/news/security/hugging-face-malware-campaign-returns-to-hijack-gpus-for-crypto-mining/) — Thu, 29 Oct 2026 18:09:24 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), PowerShell (T1059.001), Tool (T1588.002), Software (T1592.002), Exploits (T1588.005), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [Japan Airlines suffers third-party data breach exposing passenger info](https://www.bleepingcomputer.com/news/security/japan-airlines-suffers-third-party-data-breach-exposing-passenger-info/) — Thu, 29 Oct 2026 18:08:04 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Email Addresses (T1589.002), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Polymarket halts trading after crypto-draining script breach, $2.5M traced](https://www.bleepingcomputer.com/news/security/polymarket-halts-trading-after-crypto-draining-script-breach-25m-traced/) — Thu, 29 Oct 2026 17:47:25 -0400
  - **Matched TTPs:** JavaScript (T1059.007), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Hackers exploit Cisco SD-WAN flaw to deploy custom KeyDrift malware](https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/) — Thu, 29 Oct 2026 14:38:26 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Automated Exfiltration (T1020), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), Impersonation (T1656), At (T1053.002)
- [New Cisco firewall zero-day exploited to crash SSL VPN devices](https://www.bleepingcomputer.com/news/security/cisco-warns-of-firewall-zero-day-exploited-to-crash-ssl-vpn-devices/) — Thu, 29 Oct 2026 07:10:13 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), SSH (T1021.004), Web Services (T1584.006), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), At (T1053.002)

### Darkreading

- [Anthropic-Themed Phishing Emails Bypass Top Security Tools](https://www.darkreading.com/cyberattacks-data-breaches/anthropic-phishing-emails-bypass-security-tools) — Thu, 29 Oct 2026 21:21:56 GMT
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Vulnerabilities (T1588.006), Domains (T1584.001), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Impersonation (T1656), At (T1053.002)
- [Claude Model Builds Exploits Across Major Browsers &amp; OSes](https://www.darkreading.com/application-security/claude-model-exploits-major-browsers-oses) — Thu, 29 Oct 2026 18:15:59 GMT
  - **Matched TTPs:** JavaScript (T1059.007), Vulnerabilities (T1588.006), Email Account (T1087.003), Server (T1584.004), Firmware (T1592.003), Software (T1592.002), Exploits (T1588.005), At (T1053.002)
- [Cyber Vulnerabilities Besiege Italy, Absent Clear Cause](https://www.darkreading.com/cybersecurity-analytics/cyber-vulnerabilities-besiege-italy) — Thu, 29 Oct 2026 08:00:00 GMT
  - **Matched TTPs:** Vulnerabilities (T1588.006), Firmware (T1592.003), Exploits (T1588.005), Credentials (T1589.001), At (T1053.002)
- [AI Takes Root in Hospital Corridors, Raises Security Stakes](https://www.darkreading.com/cybersecurity-operations/ai-root-hospital-corridors-raised-security-stakes) — Wed, 28 Oct 2026 15:29:06 GMT
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Browser Extensions (T1176.001), Vulnerabilities (T1588.006), Tool (T1588.002), Phishing (T1566), Exploits (T1588.005), Impersonation (T1656), At (T1053.002)

### The Hacker News

- [ThreatsDay: Critical Firewall Flaws, Banking Trojans Rented, Weaponized PDF, Token Theft + 26 More Stories](https://thehackernews.com/2026/10/threatsday-critical-firewall-flaws.html) — Fri, 30 Oct 2026 00:41:58 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), IP Addresses (T1590.005), DNS (T1071.004), Malware (T1588.001), Malicious File (T1204.002), Vulnerabilities (T1588.006), SSH (T1021.004), Password Managers (T1555.005), Domains (T1584.001), Control Panel (T1218.002), Server (T1584.004), Search Engines (T1593.002), Proxy (T1090), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Process Hollowing (T1055.012), Credential Stuffing (T1110.004), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), MSBuild (T1127.001), Impersonation (T1656), Python (T1059.006), At (T1053.002)
- [Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions](https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html) — Thu, 29 Oct 2026 21:27:05 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [Fake ChatGPT and Claude Apps Abuse Signed Executables to Deploy Crypto Miners](https://thehackernews.com/2026/10/fake-chatgpt-and-claude-apps-abuse.html) — Thu, 29 Oct 2026 20:50:29 +0530
  - **Matched TTPs:** Scheduled Task (T1053.005), Artificial Intelligence (T1588.007), DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), DLL (T1574.001), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), SEO Poisoning (T1608.006), At (T1053.002)
- [Google's Gemini 4 Carbon Leads Benchmarks for Finding, Exploiting, and Patching Vulnerabilities](https://thehackernews.com/2026/10/googles-gemini-4-carbon-leads.html) — Thu, 29 Oct 2026 19:12:40 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [Webinar: How to Build AI Threat Readiness Into Your Security Operations](https://thehackernews.com/2026/08/learn-how-to-build-security-operations.html) — Thu, 29 Oct 2026 17:09:41 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [26,400 Valid Cloud and AI Credentials Found Exposed in Public Gitee Repositories](https://thehackernews.com/2026/10/26400-valid-cloud-and-ai-credentials.html) — Thu, 29 Oct 2026 17:03:15 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Cloud API (T1059.009), Proxy (T1090), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html) — Thu, 29 Oct 2026 16:14:46 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Server (T1584.004), Proxy (T1090), Automated Exfiltration (T1020), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [Attacker Tried to Exploit Alpine Linux’s GitLab via CVSS 10.0 Flaw Its Ruby Left Open](https://thehackernews.com/2026/10/attacker-tried-to-exploit-alpine-linuxs.html) — Thu, 29 Oct 2026 14:35:39 +0530
  - **Matched TTPs:** IP Addresses (T1590.005), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Server (T1584.004), Email Addresses (T1589.002), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [Hackers Exploited Cisco SD-WAN Flaw to Plant Malware Built to Steal Encryption Keys](https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html) — Thu, 29 Oct 2026 13:54:22 +0530
  - **Matched TTPs:** IP Addresses (T1590.005), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Domains (T1584.001), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility](https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html) — Thu, 29 Oct 2026 11:52:33 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Cloud Services (T1021.007), Multi-Factor Authentication (T1556.006), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
- [Attackers Exploit PHP2Shell Flaws in Internet-Exposed Palo Alto Networks Management Interfaces](https://thehackernews.com/2026/10/attackers-exploit-php2shell-flaws-in.html) — Thu, 29 Oct 2026 11:20:17 +0530
  - **Matched TTPs:** IP Addresses (T1590.005), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Proxy (T1090), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), At (T1053.002)
