---
layout: resume
nav: resume
title: "Résumé — Cam Soper"
description: "Software engineer, developer advocate, and educator. I build AI agent systems, ship the code, write the docs, and get on stage to explain them."
---

I build AI agent systems and teach developers to build them. I don't stay in one lane: I write the code, run the platform, write the docs, and get on stage or on stream to explain it. At Pulumi I build automated quality analysis for pull requests written by people or coding agents, and I own the docs platform I built, including making it readable by agents. Before that, 13 years at Microsoft in .NET and Azure field engineering, then Microsoft Learn training, video series, conference talks, and co-hosting On .NET Live. Coding since 1991.

## Key Skills

- **AI Systems & Agents** — design multi-model LLM pipelines, agent workflows, and reusable skills for code and content review, fact-checking, and quality analysis.
- **Developer Advocacy & Education** — talks, livestreams, video series, docs, and training that developers actually use.
- **Platform Ownership & CI/CD** — repositories, build pipelines, information architecture, GitHub Actions, and automated quality gates, end to end.
- **Polyglot Engineering** — .NET/C#, Go, Python, and TypeScript; I pick up new languages fast because the fundamentals carry over.
- **Cloud & Infrastructure** — deep Azure background plus infrastructure as code with Pulumi, containers, and dev containers.

## Talks, Streams & Writing

- **Speaking:** 15+ conference sessions at .NET Conf, KCDC, CodeMash, DevUp, TechBash, Code PaLOUsa, Music City Tech, Beer City Code, Cream City Code, Little Rock Tech Fest, and local user groups. Selected talks:
  - "Infrastructure as (Actual) Code with C# 15 and .NET 11" (.NET Conf 2026 Community Days, Nov 13, upcoming)
  - "Have Your Pi and Eat It Too: .NET Core on Raspberry Pi" (.NET Conf 2018; CodeMash, Beer City Code, Code PaLOUsa, DevUp, TechBash 2019)
  - "My House Runs .NET: Smart Home Automation with .NET Core and Azure" (.NET Conf, Code PaLOUsa, Music City Tech, DevUp 2019)
  - "How Insightful! Grok Your ASP.NET Core Web Apps with Application Insights" (KCDC, DevUp, TechBash 2019)
  - "Smokin' .NET to Perfection: Building a smart wood pellet smoker with Raspberry Pi and .NET" (KCDC 2021)
- **Streaming and events:** co-founded and co-hosted [On .NET Live](https://www.youtube.com/playlist?list=PLdo4fOcmZ0oV2fcY7wsQHx4RNWXEDKgm4), the weekly community stream on the official .NET channels, from launch until the show wrapped; helped plan and host .NET Conf; ran hands-on training labs at Microsoft Build; taught Let's Learn .NET and Learn Live workshops.
- **Video:** wrote and recorded the Entity Framework Core for Beginners (120K+ views) and .NET IoT for Beginners series on the official .NET YouTube channel.
- **Writing:** the .NET IoT documentation, most of Microsoft Learn's .NET training modules, a 467-article Azure and .NET docs portfolio, Pulumi's documentation platform, and "[Treating Prompts Like Code](https://www.pulumi.com/blog/treating-prompts-like-code/)" on the Pulumi blog.

## Work Experience

### Senior Software Engineer

**Pulumi · Remote** — *Oct 2026 – Present*

Internal systems engineering team, focused on accelerating Pulumi's automated development workflows. My piece is QA: once a pull request is open, whether a human or an agent wrote it, how do we know it's good, and how fast can it merge safely?

- Building **automated quality analysis and merge gates** that apply one quality bar to human- and agent-authored pull requests.
- Still own the **Pulumi docs platform** I built as a content engineer, run as an engineering system.

### Senior Technical Content Engineer

**Pulumi · Remote** — *Jul 2025 – Oct 2026*

Joined to write docs; within a month I was Pulumi's sole docs engineer. Turned that into a one-person docs-ops practice for Pulumi's infrastructure-as-code product: the `pulumi/docs` repository, the build pipeline, the information architecture, and the quality gate every change ships through. Treated the docs as two products: one for humans, and one for the AI agents that increasingly read them first.

- Built an **AI-powered PR review pipeline**: Vale on changed lines, markdownlint as a build gate, and multi-model LLM fact-checking (Claude Haiku, Sonnet, and Opus) wired into CI/CD, behind a merge gate no model controls. The [skills behind it](https://github.com/pulumi/docs/tree/master/.claude/commands) are public in the docs repo.
- Designed a modular **"prompts as code"** skill system: reusable, version-controlled AI skills that share a single source of truth for style and review criteria, adopted and extended by engineering and marketing.
- Built the **agent-consumable knowledge layer**: every page served as Markdown, a curated `llms.txt`, a JSON sitemap, and Context7 onboarding, so coding agents retrieve current docs instead of stale training data.
- Partnered with marketing on **SEO/AEO**, tuning content so AI answer engines cite it accurately.
- Pushed for a **launch-docs standard** so new Pulumi Cloud features ship with complete documentation.
- Wrote docs and runnable examples in **.NET, Go, Python, and TypeScript**.

### Senior Content Developer

**Microsoft · Remote** — *Jun 2015 – May 2025*

Developer education and tooling across .NET and Azure, with a growing focus on automation.

- Primary author of **.NET training on Microsoft Learn** (fundamentals, ASP.NET Core, EF Core, microservices, Azure SDKs).
- Owned **467 Azure and .NET documentation and training topics** driving **1.1M+ annual pageviews**.
- Wrote the entire **.NET IoT documentation** set, bridging hardware integration with .NET development.
- Designed and implemented **AI-driven documentation tooling**, integrating GitHub Copilot into authoring and content automation.
- Built developer environments with **Dev Containers, Codespaces, and WSL** for Linux-first and cross-platform developers.

### Premier Field Engineer

**Microsoft · Various Locations, Remote** — *Feb 2012 – Jun 2015*

Consulted on mission-critical .NET and Azure systems for federal agencies and Fortune 500 companies, diagnosing scalability and performance issues, guiding enterprise architecture, and delivering hands-on developer training.

- Launched Microsoft's **first fully online Premier workshops**, proving virtual technical education could match in-person delivery.
- Notable customers: White House Communications Agency, US Air Force, US Government Printing Office, Orange County (CA), Toshiba of America.

## Selected Projects

- **[Pulumi docs AI review pipeline](https://camsoper.github.io/projects/docs-pipeline/):** every docs PR gets Vale on changed lines, claims verified by Claude agents (Haiku, Sonnet, Opus), and a merge gate no model controls. Open source in `pulumi/docs`.
- **[code-walkthrough](https://github.com/CamSoper/adhd-ops/tree/main/code-walkthrough):** a Claude Code skill that turns a repo or pull request into a guided, paged walkthrough pinned to a commit, with code copied from git so line numbers can't be invented, linked diagrams, and answer-first checks. Open source.
- **[Doorbot, an AI doorman](https://camsoper.github.io/projects/doorbot/):** Gemini reads the doorbell camera and Claude talks with the visitor, classifies intent, dismisses solicitors, and routes legitimate callers to a human. The agent has no tools, so prompt injection has nothing to reach.
- **Open source:** [`puppet`](https://github.com/CamSoper/puppet), a .NET home-automation framework (110+ stars); [`Inferno`](https://github.com/CamSoper/Inferno), a .NET-powered smart smoker; and [`shark2mqtt`](https://github.com/CamSoper/shark2mqtt), a Home Assistant device bridge in Python.

## Earlier Experience

### Sr. Software Engineer / Professional Services Tech Lead

**Fiserv · Remote** — *Sep 2007 – Feb 2012*

Originally hired at Corillian (acquired by CheckFree, then Fiserv). Designed and deployed secure, scalable online banking solutions for major financial institutions.

### Web Developer III

**Commerce Bank · Kansas City, MO** — *Nov 2000 – Jul 2007*

Started as a senior programmer analyst on in-house CRM and became the lead developer for the online banking system.

### Professional Education Instructor

**Missouri State University · Springfield, MO** — *May 1999 – Nov 2000*

Taught Microsoft Office and Windows in a professional education setting.

### Programmer / Consultant

**KMB Technical Group · Lake of the Ozarks, MO** — *May 1991 – Oct 2000*

Started as an eighth-grade apprentice with the area's only computer consultant: building computers, training users, and writing software.

## Education

### Missouri State University

**B.S. Communication — Cum Laude, Honors College** — *1995 – 1999 · Springfield, MO*

A humanities education building strong analytical, communication, and problem-solving skills, complemented by a minor in Computer Information Systems.

**Activities & Honors:** Golden Key National Honor Society · Lambda Pi Eta (communication honor society) · Jazz Band & Marching Band

## Certifications

- Microsoft Certified Solutions Developer: Azure Solutions Architect
- Microsoft Certified Solutions Expert: Cloud Platform & Infrastructure
- Microsoft Certified Solution Developer: .NET (Legacy)
