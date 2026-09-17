---
title: "Daily Hunt Feed - 2026-09-17"
date: 2026-09-17 01:37:50 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-09-17)

### Hacker News: Best

- [Hackers Got Inside a Flock Camera](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) — Wed, 16 Sep 2026 13:18:47 +0000
  - **Matched TTPs:** Hardware (T1592.001), Vulnerabilities (T1588.006), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)

### Krebs on Security

- [Data Broker Radaris Loses Domains in Privacy Fight](https://krebsonsecurity.com/2026/09/data-broker-radaris-loses-domains-in-privacy-fight/) — Wed, 16 Sep 2026 18:14:22 +0000
  - **Matched TTPs:** Domains (T1584.001), Software (T1592.002), Social Media (T1593.001), At (T1053.002)

### BleepingComputer

- [Windows 11 KB5124008 update breaks domain trust for some users](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5124008-update-breaks-domain-trust-for-some-users/) — Wed, 16 Sep 2026 16:39:29 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), PowerShell (T1059.001), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Iranian hackers use CHOSEN BRICK Windows malware to spy on targets](https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/) — Wed, 16 Sep 2026 16:24:55 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Cloud Services (T1021.007), Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [Malware bypasses browser checks to force install Chrome, Edge extensions](https://www.bleepingcomputer.com/news/security/malware-bypasses-browser-checks-to-force-install-chrome-edge-extensions/) — Wed, 16 Sep 2026 14:50:53 -0400
  - **Matched TTPs:** Scheduled Task (T1053.005), JavaScript (T1059.007), Malware (T1588.001), Hardware (T1592.001), Databases (T1213.006), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Windows Server 2022 reaches end of mainstream support next month](https://www.bleepingcomputer.com/news/microsoft/windows-server-2022-reaches-end-of-mainstream-support-next-month/) — Wed, 16 Sep 2026 05:10:20 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [Google fixes actively exploited Android zero-day on Pixel devices](https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-android-zero-day-on-pixel-devices/) — Wed, 16 Sep 2026 03:00:19 -0400
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Server (T1584.004), Tool (T1588.002), Software (T1592.002), Exploits (T1588.005), At (T1053.002)

### Darkreading

- [Black Hat USA 2026 | OpenAI's Deep Dive Into Hugging Face Incident](https://www.darkreading.com/vulnerabilities-threats/bhusa26huggingfacetalk) — Tue, 15 Sep 2026 19:27:19 GMT
  - **Matched TTPs:** Vulnerabilities (T1588.006), At (T1053.002)

### The Hacker News

- [Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution](https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html) — Wed, 16 Sep 2026 21:20:59 +0530
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers](https://thehackernews.com/2026/09/three-threat-groups-target-russian.html) — Wed, 16 Sep 2026 20:57:49 +0530
  - **Matched TTPs:** Scheduled Task (T1053.005), IP Addresses (T1590.005), Malware (T1588.001), Local Account (T1136.001), Windows Service (T1543.003), Vulnerabilities (T1588.006), Web Shell (T1505.003), Server (T1584.004), Windows Remote Management (T1021.006), PowerShell (T1059.001), Phishing (T1566), Social Media (T1593.001), Credentials (T1589.001), Domain Accounts (T1078.002), DCSync (T1003.006), At (T1053.002), Inhibit System Recovery (T1490)
- [One Extension Could Hijack AI Assistants Across Chrome, Comet, Edge, Opera Neon and Claude](https://thehackernews.com/2026/09/one-extension-could-hijack-ai.html) — Wed, 16 Sep 2026 20:06:44 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories](https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html) — Wed, 16 Sep 2026 19:07:07 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Code Repositories (T1213.003), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Parallels Desktop Flaw Lets Non-Admin Mac Users Gain Root, but Intel Macs Can't Install Fix](https://thehackernews.com/2026/09/parallels-desktop-flaw-lets-non-admin.html) — Wed, 16 Sep 2026 18:44:05 +0530
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Local Account (T1136.001), Vulnerabilities (T1588.006), Web Shell (T1505.003), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [N0va Phishkit Targets US and EU Businesses: A New Challenge for Identity Security](https://thehackernews.com/2026/09/n0va-phishkit-targets-us-and-eu.html) — Wed, 16 Sep 2026 17:28:00 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Malware (T1588.001), Vulnerabilities (T1588.006), Domains (T1584.001), Web Shell (T1505.003), Device Registration (T1098.005), Cloud Services (T1021.007), Phishing (T1566), Valid Accounts (T1078), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)

### 데일리시큐 - 최근인기기사

- [브이엠웨어 vCenter 치명적 RCE 실제 악용…ESXi 랜섬웨어 공격까지 확인](https://www.dailysecu.com/news/articleView.html?idxno=208516) — 2026-09-16 22:31:16
  - **Matched TTPs:** SSH (T1021.004), Server (T1584.004)
