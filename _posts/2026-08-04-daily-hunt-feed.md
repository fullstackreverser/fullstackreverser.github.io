---
title: "Daily Hunt Feed - 2026-08-04"
date: 2026-08-04 01:00:17 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-08-04)

### Hacker News: Best

- [Taylor Farms has rewritten its cyclospora statement four times in sixteen days](https://www.marlerblog.com/case-news/taylor-farms-has-rewritten-its-cyclospora-statement-four-times-in-sixteen-days-it-still-has-not-said-what-changed-at-that-plant-after-2013-or-why-two-thousand-negative-tests-should-mean-an/) — Mon, 03 Aug 2026 15:31:32 +0000
  - **Matched TTPs:** Proxy (T1090), At (T1053.002)
- [Don't be a meat proxy](https://gruhn.me/blog/2026-08-03/) — Mon, 03 Aug 2026 06:28:01 +0000
  - **Matched TTPs:** Proxy (T1090), At (T1053.002)
- [OpenAI's super PAC is funding AI-generated news site attacking industry critics](https://www.modelrepublic.org/articles/the-reporters-at-this-news-site-are-ai-bots.-openai%E2%80%99s-super-pac-appears-to-be-using-it-to-advance-its-political-agenda) — Mon, 03 Aug 2026 02:30:30 +0000
  - **Matched TTPs:** Artificial Intelligence (T1588.007), JavaScript (T1059.007), Software (T1592.002), Social Media (T1593.001), At (T1053.002)
- [EU Age Verification Project Mandates Hardware-Bound Attestation](https://linuxiac.com/eu-age-verification-project-mandates-hardware-bound-attestation/) — Sun, 02 Aug 2026 20:44:24 +0000
  - **Matched TTPs:** Hardware (T1592.001), Server (T1584.004), Firmware (T1592.003), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Show HN: Bor – Open-source policy management for Linux desktops](https://getbor.dev/blog/2026-08-02-bor-v080-release/) — Sun, 02 Aug 2026 09:06:33 +0000
  - **Matched TTPs:** Server (T1584.004)

### BleepingComputer

- [Hotel Wi-Fi attacks use custom malware to breach Microsoft 365 accounts](https://www.bleepingcomputer.com/news/security/hotel-wi-fi-attacks-use-custom-malware-to-breach-microsoft-365-accounts/) — Mon, 03 Aug 2026 20:17:15 -0400
  - **Matched TTPs:** Keylogging (T1056.001), DNS (T1071.004), Malware (T1588.001), Hardware (T1592.001), Windows Service (T1543.003), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001), At (T1053.002), Wi-Fi Networks (T1669)
- [New Pass-ta-key attacks let malware hijack Google-synced passkeys](https://www.bleepingcomputer.com/news/security/new-pass-ta-key-attacks-let-malware-hijack-google-synced-passkeys/) — Mon, 03 Aug 2026 19:58:01 -0400
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Hardware (T1592.001), Private Keys (T1552.004), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001)
- [New DOUBLECUP ClickFix service hides malware in browser cache images](https://www.bleepingcomputer.com/news/security/new-doublecup-clickfix-service-hides-malware-in-browser-cache-images/) — Mon, 03 Aug 2026 16:01:22 -0400
  - **Matched TTPs:** DNS (T1071.004), Malware (T1588.001), Hardware (T1592.001), Browser Extensions (T1176.001), Server (T1584.004), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Steganography (T1001.002), Python (T1059.006), At (T1053.002)
- [Fake Roblox Xeno script launcher pushes infostealer, RAT malware](https://www.bleepingcomputer.com/news/security/fake-roblox-xeno-script-launcher-pushes-infostealer-rat-malware/) — Mon, 03 Aug 2026 15:25:10 -0400
  - **Matched TTPs:** Keylogging (T1056.001), Malware (T1588.001), Hardware (T1592.001), Server (T1584.004), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Lua (T1059.011), Software (T1592.002)
- [Inside the Underground Business of the Android BTMOB RAT malware](https://www.bleepingcomputer.com/news/security/inside-the-underground-business-of-btmob-rat/) — Mon, 03 Aug 2026 10:45:55 -0400
  - **Matched TTPs:** Malware (T1588.001), Hardware (T1592.001), Control Panel (T1218.002), Server (T1584.004), Tool (T1588.002), Phishing (T1566), Software (T1592.002), At (T1053.002)

### Darkreading

- [New Tool Traces AI Videos Back to Their Source](https://www.darkreading.com/cyber-risk/new-tool-advances-ai-generated-video-detection) — Mon, 03 Aug 2026 20:42:28 GMT
  - **Matched TTPs:** Artificial Intelligence (T1588.007), Vulnerabilities (T1588.006), Tool (T1588.002), Social Media (T1593.001), Impersonation (T1656), At (T1053.002)
- [Cybersecurity, Then &amp; Now](https://www.darkreading.com/cyber-risk/cybersecurity-then-now) — Wed, 29 Jul 2026 23:26:46 GMT
  - **Matched TTPs:** Malware (T1588.001), Vulnerabilities (T1588.006), Social Media (T1593.001), At (T1053.002)

### The Hacker News

- [18 Malicious npm Packages Deliver Cross-Platform RAT to Alibaba Tool Users](https://thehackernews.com/2026/08/18-malicious-npm-packages-deliver-cross.html) — Tue, 04 Aug 2026 00:13:53 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), JavaScript (T1059.007), Malvertising (T1583.008), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Private Keys (T1552.004), Server (T1584.004), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), Launch Agent (T1543.001), At (T1053.002)
- [Google Password Manager Attacks Could Let Malware Hijack Passkey-Protected Accounts](https://thehackernews.com/2026/08/google-password-manager-attacks-could.html) — Mon, 03 Aug 2026 21:54:47 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Malvertising (T1583.008), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Private Keys (T1552.004), Server (T1584.004), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), At (T1053.002)
- [⚡ Weekly Recap: Rogue AI Models, $88M Bitcoin Theft, Water-System Attacks and Dangling DNS Hijacks](https://thehackernews.com/2026/08/weekly-recap-rogue-ai-models-88m.html) — Mon, 03 Aug 2026 19:33:11 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Artificial Intelligence (T1588.007), IP Addresses (T1590.005), JavaScript (T1059.007), DNS (T1071.004), Malvertising (T1583.008), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), SSH (T1021.004), Password Managers (T1555.005), Domains (T1584.001), Server (T1584.004), Proxy (T1090), Shell History (T1552.003), PowerShell (T1059.001), Tool (T1588.002), Phishing (T1566), Firmware (T1592.003), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Python (T1059.006), At (T1053.002), Wi-Fi Networks (T1669)
- [Chinese Threat Actor Uses Leaked DarkSword Kit to Deploy GHOSTBLADE on iOS](https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html) — Mon, 03 Aug 2026 16:19:06 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), IP Addresses (T1590.005), JavaScript (T1059.007), Malvertising (T1583.008), Keychain (T1555.001), Malware (T1588.001), Vulnerabilities (T1588.006), SSH (T1021.004), Domains (T1584.001), Control Panel (T1218.002), Web Services (T1584.006), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Impersonation (T1656), At (T1053.002)
- [PNLD Breach Exposes U.K. Police and Government Contact Details on Dark Web](https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html) — Mon, 03 Aug 2026 14:43:56 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Malvertising (T1583.008), Malware (T1588.001), Vulnerabilities (T1588.006), Email Addresses (T1589.002), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable](https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html) — Mon, 03 Aug 2026 13:35:30 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Malvertising (T1583.008), Malware (T1588.001), Vulnerabilities (T1588.006), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), At (T1053.002)
- [Hugging Face Diffusers Flaws Could Let Model Repositories Execute Arbitrary Code](https://thehackernews.com/2026/08/hugging-face-diffusers-flaws-could-let.html) — Mon, 03 Aug 2026 12:10:31 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Artificial Intelligence (T1588.007), Malvertising (T1583.008), Malware (T1588.001), Vulnerabilities (T1588.006), Phishing (T1566), Software (T1592.002), Social Media (T1593.001), Python (T1059.006), At (T1053.002)

### 보안뉴스 > SECURITY

- [유럽 진출 위해 꼭 알아야 할 사이버 보안법 ‘EU CRA’ 톺아보기](http://www.boannews.com/media/view.asp?idx=144902&kind=&sub_kind=) — Mon, 3 Aug 2026 17:00:00 +0900
  - **Matched TTPs:** Botnet (T1584.005)
