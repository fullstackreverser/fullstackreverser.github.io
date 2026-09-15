---
title: "Daily Hunt Feed - 2026-09-15"
date: 2026-09-15 01:46:48 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-09-15)

### Hacker News: Best

- [iOS 27, iPadOS 27, and macOS 27](https://www.apple.com/newsroom/2026/09/major-updates-for-apples-software-platforms-are-now-available/) — Mon, 14 Sep 2026 17:50:29 +0000
  - **Matched TTPs:** Server (T1584.004), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), At (T1053.002), Wi-Fi Networks (T1669)
- [Steam Frame starts at $1059](https://store.steampowered.com/hardware/steamframe) — Mon, 14 Sep 2026 17:27:55 +0000
  - **Matched TTPs:** Hardware (T1592.001), At (T1053.002)
- [How to write an effective software design document](https://refactoringenglish.com/excerpts/write-an-effective-design-doc/) — Mon, 14 Sep 2026 13:00:46 +0000
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Domains (T1584.001), Server (T1584.004), Tool (T1588.002), Software (T1592.002), At (T1053.002)

### BleepingComputer

- [Hackers hijack HBO Max Reddit account to push malware in ClickFix ads](https://www.bleepingcomputer.com/news/security/hackers-hijack-hbo-max-reddit-account-to-push-malware-in-clickfix-ads/) — Mon, 14 Sep 2026 14:34:16 -0400
  - **Matched TTPs:** Scheduled Task (T1053.005), Malware (T1588.001), Hardware (T1592.001), Mshta (T1218.005), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Hackers target exposed Vite dev servers to steal AWS, Azure secrets](https://www.bleepingcomputer.com/news/security/hackers-target-exposed-vite-dev-servers-to-steal-aws-azure-secrets/) — Mon, 14 Sep 2026 12:15:58 -0400
  - **Matched TTPs:** Serverless (T1584.007), IP Addresses (T1590.005), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Microsoft: September updates cause RDS failures on Windows Server](https://www.bleepingcomputer.com/news/microsoft/microsoft-september-updates-cause-rds-failures-on-windows-server/) — Mon, 14 Sep 2026 05:50:25 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Tool (T1588.002), Phishing (T1566), Software (T1592.002), At (T1053.002), MMC (T1218.014)

### Darkreading

- ['Sandworm' Chains Cisco Vulnerabilities to Deploy Cyclops Blink](https://www.darkreading.com/cyberattacks-data-breaches/sandworm-chains-cisco-vulnerabilities-cyclops-blink) — Mon, 14 Sep 2026 21:37:28 GMT
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), Botnet (T1584.005), Proxy (T1090), Tool (T1588.002), Firmware (T1592.003), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Maximum Severity GitLab Flaw Puts Supply Chains at Risk](https://www.darkreading.com/cyberattacks-data-breaches/maximum-severity-gitlab-flaw-supply-chains-risk) — Mon, 14 Sep 2026 20:19:22 GMT
  - **Matched TTPs:** Malvertising (T1583.008), Hardware (T1592.001), Vulnerabilities (T1588.006), SSH (T1021.004), Server (T1584.004), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [SpiderSilk Hunts External Threats With AI-Based Scanner](https://www.darkreading.com/endpoint-security/spidersilk-hunts-external-threats-ai-scanning) — Fri, 11 Sep 2026 18:27:28 GMT
  - **Matched TTPs:** Artificial Intelligence (T1588.007), IP Addresses (T1590.005), Hardware (T1592.001), Databases (T1213.006), Vulnerabilities (T1588.006), Domains (T1584.001), Server (T1584.004), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)

### The Hacker News

- [New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing](https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html) — Mon, 14 Sep 2026 23:32:13 +0530
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Cloud Services (T1021.007), Phishing (T1566), Firmware (T1592.003), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [3BB Attacker Used MeshCentral Backdoor for Root Access, Targeted Subscriber Credentials](https://thehackernews.com/2026/09/3bb-attacker-used-meshcentral-backdoor.html) — Mon, 14 Sep 2026 23:31:49 +0530
  - **Matched TTPs:** Malware (T1588.001), Databases (T1213.006), Vulnerabilities (T1588.006), SSH (T1021.004), Web Shell (T1505.003), Server (T1584.004), Tool (T1588.002), Phishing (T1566), Firmware (T1592.003), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports](https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html) — Mon, 14 Sep 2026 23:28:16 +0530
  - **Matched TTPs:** JavaScript (T1059.007), Malware (T1588.001), Databases (T1213.006), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Red Heron Exploits Gitea RCE to Compromise 13 Organizations Across Six Countries](https://thehackernews.com/2026/09/red-heron-exploits-gitea-rce-to.html) — Mon, 14 Sep 2026 22:26:30 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Rootkit (T1014), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Web Shell (T1505.003), Server (T1584.004), Tool (T1588.002), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [⚡ Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits](https://thehackernews.com/2026/09/weekly-recap-rogue-ai-agents-wechat.html) — Mon, 14 Sep 2026 20:10:34 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Rootkit (T1014), DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), DLL (T1574.001), Password Managers (T1555.005), Masquerading (T1036), Web Shell (T1505.003), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [AI Changed the Exposure Problem. Validation Needs to Change With It.](https://thehackernews.com/2026/09/ai-changed-exposure-problem-validation.html) — Mon, 14 Sep 2026 17:28:00 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Malicious Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users](https://thehackernews.com/2026/09/malicious-twitch-browser-extension.html) — Mon, 14 Sep 2026 12:54:39 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
