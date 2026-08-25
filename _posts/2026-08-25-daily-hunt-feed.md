---
title: "Daily Hunt Feed - 2026-08-25"
date: 2026-08-25 23:49:45 +0000
categories: [security, hunt]
tags: [threat-hunting, ttp, mitre-attack]
published: true
---

## Threat Hunt Feed (2026-08-25)

### Hacker News: Best

- [iCloud+ Hide My Email addresses will remain on icloud.com](https://developer.apple.com/news/?id=1ptvdtcm) — Mon, 24 Aug 2026 22:13:40 +0000
  - **Matched TTPs:** Email Addresses (T1589.002), Software (T1592.002)
- [IPFS Maintainers Winding Down](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) — Mon, 24 Aug 2026 15:48:45 +0000
  - **Matched TTPs:** Domains (T1584.001), Software (T1592.002), At (T1053.002)
- [OpenAI: GPT 5.6 Sol price reduction (until at least Nov 21)](https://developers.openai.com/api/docs/pricing) — Mon, 24 Aug 2026 15:22:43 +0000
  - **Matched TTPs:** Server (T1584.004), Tool (T1588.002), At (T1053.002)
- [Anna's Archive Owes $340 Million, Lost Several Domains, but It's Still Online](https://torrentfreak.com/annas-archive-owes-340-million-lost-several-domains-but-its-still-online/) — Mon, 24 Aug 2026 15:10:25 +0000
  - **Matched TTPs:** Domains (T1584.001), Phishing (T1566), Social Media (T1593.001), At (T1053.002)

### BleepingComputer

- [Hackers abuse npm mirrors to host phishing redirect pages](https://www.bleepingcomputer.com/news/security/hackers-abuse-npm-mirrors-to-host-phishing-redirect-pages/) — Tue, 25 Aug 2026 17:39:01 -0400
  - **Matched TTPs:** JavaScript (T1059.007), Malware (T1588.001), Hardware (T1592.001), Botnet (T1584.005), Domains (T1584.001), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001), At (T1053.002)
- [AnonyMousKIT PhaaS uses voice AI agents to phish iPhone passcodes](https://www.bleepingcomputer.com/news/security/anonymouskit-phaas-uses-voice-ai-agents-to-phish-iphone-passcodes/) — Tue, 25 Aug 2026 16:25:26 -0400
  - **Matched TTPs:** Keychain (T1555.001), Malware (T1588.001), Hardware (T1592.001), Botnet (T1584.005), Domains (T1584.001), Proxy (T1090), Tool (T1588.002), Phishing (T1566), Software (T1592.002), Credentials (T1589.001), At (T1053.002)

### Darkreading

- [Finding Nemo(Claw): Networking Issue Allows for LLM Poisoning in OpenClaw](https://www.darkreading.com/cyber-risk/nemo-claw-networking-llm-poisoning-openclaw) — Tue, 25 Aug 2026 19:50:16 GMT
  - **Matched TTPs:** DNS (T1071.004), Hardware (T1592.001), Vulnerabilities (T1588.006), Server (T1584.004), Tool (T1588.002), At (T1053.002)

### The Hacker News

- [WhatsApp Adds Multiple Passkeys for Phishing-Resistant Sign-Ins Across iOS and Android](https://thehackernews.com/2026/08/whatsapp-adds-multiple-passkeys-for.html) — Tue, 25 Aug 2026 18:49:41 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Botnet (T1584.005), Domains (T1584.001), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode](https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html) — Tue, 25 Aug 2026 18:13:51 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Artificial Intelligence (T1588.007), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Botnet (T1584.005), Domains (T1584.001), Server (T1584.004), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365 Login Flows](https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-eu.html) — Tue, 25 Aug 2026 17:26:15 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Botnet (T1584.005), Domains (T1584.001), Email Addresses (T1589.002), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), Impersonation (T1656), At (T1053.002)
- [24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages](https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html) — Tue, 25 Aug 2026 17:22:43 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), JavaScript (T1059.007), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Botnet (T1584.005), Domains (T1584.001), Server (T1584.004), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002), Dead Drop Resolver (T1102.001)
- [E4del and PINHOLE RATs Turn FTP Banners Into Dead Drops for Malware Commands](https://thehackernews.com/2026/08/e4del-and-pinhole-rats-turn-ftp-banners.html) — Tue, 25 Aug 2026 17:03:44 +0530
  - **Matched TTPs:** Rundll32 (T1218.011), Sharepoint (T1213.002), IP Addresses (T1590.005), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), DLL (T1574.001), Botnet (T1584.005), Domains (T1584.001), Masquerading (T1036), Server (T1584.004), Proxy (T1090), PowerShell (T1059.001), Phishing (T1566), Software (T1592.002), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access](https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html) — Tue, 25 Aug 2026 14:04:07 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), IP Addresses (T1590.005), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Botnet (T1584.005), Domains (T1584.001), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
- [Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data](https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html) — Tue, 25 Aug 2026 11:42:35 +0530
  - **Matched TTPs:** Sharepoint (T1213.002), Malware (T1588.001), Hardware (T1592.001), Vulnerabilities (T1588.006), Botnet (T1584.005), Domains (T1584.001), Server (T1584.004), Proxy (T1090), Phishing (T1566), Exploits (T1588.005), Social Media (T1593.001), Credentials (T1589.001), At (T1053.002)
