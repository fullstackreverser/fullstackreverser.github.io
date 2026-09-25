---
title: "Daily Hunt Feed - 2026-09-25"
date: 2026-09-25 01:45:40 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-09-25)

### Hacker News: Best

- [Owners mourn spoiled food after firmware update bricks Samsung smart fridges](https://arstechnica.com/gadgets/2026/09/owners-mourn-spoiled-food-after-firmware-update-bricks-samsung-smart-fridges/) — Thu, 24 Sep 2026 12:58:08 +0000
  - **Matched TTPs:** Hardware (T1592.001), Firmware (T1592.003), Software (T1592.002), At (T1053.002)
- [Meta takes down a critical video about meta AI Glasses after filming at Meta](https://www.reddit.com/r/facebook/comments/1wotwrk/meta_takes_down_a_critical_video_about_meta_ai/) — Thu, 24 Sep 2026 08:23:03 +0000
  - **Matched TTPs:** At (T1053.002)
- [Show HN: Make cursed fonts like Times New Bastard](https://bastardica.mitpit.com) — Wed, 23 Sep 2026 22:53:28 +0000
  - **Matched TTPs:** Tool (T1588.002), Python (T1059.006), At (T1053.002)
- [VSCode's SSH Agent Is Bananas (2025)](https://fly.io/blog/vscode-ssh-wtf/) — Wed, 23 Sep 2026 21:01:48 +0000
  - **Matched TTPs:** SSH (T1021.004)

### BleepingComputer

- [MacSync malware uses public iCloud calendars to deliver new payloads](https://www.bleepingcomputer.com/news/security/macsync-malware-uses-public-icloud-calendars-to-deliver-new-payloads/) — Thu, 24 Sep 2026 16:53:35 -0400
  - **Matched TTPs:** Keychain (T1555.001), Malware (T1588.001), Hardware (T1592.001), SSH (T1021.004), AppleScript (T1059.002), Server (T1584.004), Email Addresses (T1589.002), Tool (T1588.002), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [New Carbonato malware uses AI agents to hijack exposed Docker hosts](https://www.bleepingcomputer.com/news/security/new-carbonato-malware-uses-ai-agents-to-hijack-exposed-docker-hosts/) — Thu, 24 Sep 2026 16:10:48 -0400
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Hardware (T1592.001), Cron (T1053.003), SSH (T1021.004), Botnet (T1584.005), Server (T1584.004), Email Addresses (T1589.002), Tool (T1588.002), Systemd Timers (T1053.006), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [Exposed GitLab project email addresses let attackers push code](https://www.bleepingcomputer.com/news/security/exposed-gitlab-project-email-addresses-let-attackers-push-code/) — Thu, 24 Sep 2026 13:47:44 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), Email Addresses (T1589.002), Tool (T1588.002), Software (T1592.002), At (T1053.002)
- [OpenAI hacked Australian Medicare govt site, probed data providers](https://www.bleepingcomputer.com/news/security/openai-hacked-australian-medicare-govt-site-probed-data-providers/) — Thu, 24 Sep 2026 05:38:53 -0400
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Server (T1584.004), Email Addresses (T1589.002), Tool (T1588.002), Software (T1592.002), At (T1053.002)

### Darkreading

- ['Salesbleed' Exploits Salesforce Agents to Enable Slack Phishing](https://www.darkreading.com/application-security/salesbleed-exploits-salesforce-agents-slack-phishing) — Thu, 24 Sep 2026 21:04:03 GMT
  - **Matched TTPs:** Vulnerabilities (T1588.006), Domains (T1584.001), Email Addresses (T1589.002), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), At (T1053.002)

### The Hacker News

- [Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions](https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html) — Thu, 24 Sep 2026 23:40:18 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Server (T1584.004), Tool (T1588.002), Phishing (T1566), Firmware (T1592.003), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [ThreatsDay: AI Search Poisoning, AI Coding Tool Leaking Repos, One-Click Code Execution and 13 More Stories](https://thehackernews.com/2026/09/threatsday-ai-search-poisoning-ai.html) — Thu, 24 Sep 2026 23:22:43 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), JavaScript (T1059.007), DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Botnet (T1584.005), Cloud Accounts (T1078.004), Thread Execution Hijacking (T1055.003), Web Shell (T1505.003), Server (T1584.004), Trap (T1546.005), Email Addresses (T1589.002), Code Repositories (T1213.003), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Impersonation (T1656), Python (T1059.006), Visual Basic (T1059.005), At (T1053.002)
- [Secrets Sprawl Is an Identity Problem That AI Just Made Impossible to Ignore](https://thehackernews.com/2026/09/secrets-sprawl-is-identity-problem-that.html) — Thu, 24 Sep 2026 16:30:00 +0530
  - **Matched TTPs:** Artificial Intelligence (T1588.007), DNS (T1071.004), Malware (T1588.001), Databases (T1213.006), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Server (T1584.004), Code Repositories (T1213.003), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [17,000 URLs Reveal How ClickFix Turns Trusted Websites Into Malware Traps: Report by CTM360](https://thehackernews.com/2026/09/17000-urls-reveal-how-clickfix-turns.html) — Thu, 24 Sep 2026 14:44:21 +0530
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), DLL (T1574.001), Cloud Accounts (T1078.004), Domains (T1584.001), Server (T1584.004), Proxy (T1090), User Execution (T1204), PowerShell (T1059.001), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Malicious Copy and Paste (T1204.004), At (T1053.002)
- [TeamFiltration Campaign Compromises Seven Microsoft 365 Accounts Using Default Passwords](https://thehackernews.com/2026/09/teamfiltration-compromises-seven.html) — Thu, 24 Sep 2026 12:02:03 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), IP Addresses (T1590.005), DNS (T1071.004), Malware (T1588.001), Vulnerabilities (T1588.006), Cloud Accounts (T1078.004), Email Accounts (T1585.002), Server (T1584.004), Phishing (T1566), Credential Stuffing (T1110.004), Multi-Factor Authentication (T1556.006), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
