---
title: "Daily Hunt Feed - 2026-09-24"
date: 2026-09-24 01:36:06 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-09-24)

### Hacker News: Best

- [Jev in 25 Lines of Python](https://www.nobodywho.ai/posts/jev-in-25-lines/) — Wed, 23 Sep 2026 07:26:23 +0000
  - **Matched TTPs:** Phishing (T1566), Python (T1059.006)
- [Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived](https://foxscript.org/) — Tue, 22 Sep 2026 21:00:30 +0000
  - **Matched TTPs:** Databases (T1213.006), DLL (T1574.001), Add-ins (T1137.006), Server (T1584.004), At (T1053.002)

### BleepingComputer

- [Placeholder domain used in dev docs now serves ClickFix attacks](https://www.bleepingcomputer.com/news/security/placeholder-domain-used-in-dev-docs-now-serves-clickfix-attacks/) — Wed, 23 Sep 2026 18:46:01 -0400
  - **Matched TTPs:** JavaScript (T1059.007), Malware (T1588.001), Hardware (T1592.001), Domains (T1584.001), Server (T1584.004), PowerShell (T1059.001), Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [New RemControl Android banking malware targets users in Europe and Canada](https://www.bleepingcomputer.com/news/security/new-remcontrol-android-banking-malware-targets-users-in-europe-and-canada/) — Wed, 23 Sep 2026 17:25:13 -0400
  - **Matched TTPs:** Malvertising (T1583.008), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Malicious AI agents steal 600K credit cards, infect 100+ sites with skimmers](https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/) — Wed, 23 Sep 2026 12:20:54 -0400
  - **Matched TTPs:** Artificial Intelligence (T1588.007), JavaScript (T1059.007), Malware (T1588.001), Hardware (T1592.001), Databases (T1213.006), Cron (T1053.003), Vulnerabilities (T1588.006), Server (T1584.004), Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [InfraTrust report warns network management systems under attack](https://www.bleepingcomputer.com/news/security/infratrust-report-warns-network-management-systems-under-attack/) — Wed, 23 Sep 2026 10:35:26 -0400
  - **Matched TTPs:** Network Devices (T1584.008), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Server (T1584.004), Tool (T1588.002), Firmware (T1592.003), Software (T1592.002), Credentials (T1589.001), At (T1053.002)

### Darkreading

- [EDR Evasion Stack Helps Process Injection Slip Past Defenses](https://www.darkreading.com/endpoint-security/edr-evasion-stack-helps-process-injection-slip-past-defenses) — Wed, 23 Sep 2026 21:03:01 GMT
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), DLL (T1574.001), Thread Execution Hijacking (T1055.003), Process Injection (T1055), Email Addresses (T1589.002), Phishing (T1566), Software (T1592.002), At (T1053.002)
- [GitLab Email Addresses Can Be Weaponized for Supply Chain Attacks](https://www.darkreading.com/application-security/gitlab-email-addresses-supply-chain-attacks) — Wed, 23 Sep 2026 20:53:38 GMT
  - **Matched TTPs:** Malvertising (T1583.008), Hardware (T1592.001), Vulnerabilities (T1588.006), Email Account (T1087.003), Email Addresses (T1589.002), Tool (T1588.002), Phishing (T1566), Software (T1592.002), At (T1053.002)
- [Attackers Manipulate AI Chatbots in Mass Disinformation, Phishing Campaign](https://www.darkreading.com/threat-intelligence/attackers-manipulate-ai-chatbots-mass-disinformation-phishing-campaign) — Wed, 23 Sep 2026 14:47:09 GMT
  - **Matched TTPs:** Vulnerabilities (T1588.006), Domains (T1584.001), Email Addresses (T1589.002), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), SEO Poisoning (T1608.006), At (T1053.002)

### The Hacker News

- [Attackers Use Malicious Terraform Providers to Deliver Go Malware via HashiCorp Registry](https://thehackernews.com/2026/09/attackers-use-malicious-terraform.html) — Wed, 23 Sep 2026 23:36:30 +0530
  - **Matched TTPs:** JavaScript (T1059.007), DNS (T1071.004), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Server (T1584.004), Phishing (T1566), Multi-Factor Authentication (T1556.006), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Bidirectional Communication (T1102.002), Asymmetric Cryptography (T1573.002), At (T1053.002)
- [MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key](https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html) — Wed, 23 Sep 2026 21:36:41 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Cloud Accounts (T1078.004), Server (T1584.004), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [This Windows Malware is Built to Let Up to Four AI Models Vote on Its Next Move](https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html) — Wed, 23 Sep 2026 19:47:58 +0530
  - **Matched TTPs:** Scheduled Task (T1053.005), Artificial Intelligence (T1588.007), DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Domains (T1584.001), Process Injection (T1055), Server (T1584.004), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Process Hollowing (T1055.012), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI](https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html) — Wed, 23 Sep 2026 19:22:46 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Cloud Accounts (T1078.004), Private Keys (T1552.004), Server (T1584.004), Cloud Services (T1021.007), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002)
- [New cPanel Flaw Lets a Hosting Account Run Code as Root, Take Full Server Control](https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html) — Wed, 23 Sep 2026 17:46:00 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Databases (T1213.006), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Control Panel (T1218.002), Server (T1584.004), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [545 Hackers Tested It First. Now XRanges for AI Scores Your Security Agent](https://thehackernews.com/2026/09/545-hackers-tested-it-first-now-xranges.html) — Wed, 23 Sep 2026 17:17:19 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Server (T1584.004), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Anthropic and OpenAI Models Still Attempt Restricted Actions in Safety Tests](https://thehackernews.com/2026/09/anthropic-and-openai-models-still.html) — Wed, 23 Sep 2026 17:17:13 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Domains (T1584.001), Server (T1584.004), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [F5 Patches Critical BIG-IP APM Zero-Day Exploited for Unauthenticated RCE on OAuth Servers](https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html) — Wed, 23 Sep 2026 13:59:48 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Server (T1584.004), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Chinese Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy CLEANGULP Malware](https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html) — Wed, 23 Sep 2026 13:59:24 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Server (T1584.004), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Critical Next.js ImageResponse Flaw Can Lead to Server Code Execution via Crafted SVG Input](https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html) — Wed, 23 Sep 2026 12:34:40 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Server (T1584.004), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [ShinyHunters Claims FBI Breach, Says It Stole Data on Agents and Job Applicants](https://thehackernews.com/2026/09/shinyhunters-claims-fbi-breach-says-it.html) — Wed, 23 Sep 2026 11:00:09 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Server (T1584.004), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
