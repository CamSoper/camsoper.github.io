---
layout: resume
nav: resume
title: "Résumé — Cam Soper"
description: "Software engineer, developer advocate, and educator. I build AI agent systems, ship the code, write the docs, and get on stage to explain them."
---

I build AI agent systems, and I've been teaching developers for over a decade. I don't stay in one lane: I write the code, run the platform, write the docs, and get on stage or on stream to explain it. At Pulumi I build automated quality analysis for pull requests written by people or coding agents, and I own the docs platform I built, including making it readable by agents. Before that, 13 years at Microsoft: Premier Field Engineering for .NET and Azure, then Microsoft Learn training, video series, conference talks, and co-hosting On .NET Live. Coding since 1991.

## Key Skills

- **AI Systems & Agents** — design multi-model LLM pipelines, agent workflows, and reusable skills for code and content review, fact-checking, and quality analysis.
- **Developer Advocacy & Education** — talks, livestreams, video series, docs, and training that developers actually use.
- **Platform Ownership & CI/CD** — repositories, build pipelines, information architecture, GitHub Actions, and automated quality gates, end to end.
- **Polyglot Engineering** — C#/.NET is home; runnable Pulumi docs examples in Go, Python, and TypeScript, TypeScript MCP servers, and a Python Home Assistant bridge.
- **Cloud & Infrastructure** — deep Azure background, plus a [self-hosted MCP platform](https://camsoper.github.io/projects/mcp-platform/): containers behind Cloudflare Access and one tunnel, shipped by CI that pins image digests in Pulumi ESC and deploys with a Pulumi C# program.

## Selected Projects

- **[Pulumi docs AI review pipeline](https://camsoper.github.io/projects/docs-pipeline/):** every docs PR gets Vale on changed lines, claims extracted by Claude Sonnet and verified by Claude Opus (Haiku screens trivial PRs), and a merge gate no model controls. Open source in `pulumi/docs`.
- **[.NET IoT documentation](https://learn.microsoft.com/dotnet/iot/):** wrote the whole set on Microsoft Learn, from the overview and quickstart to six hands-on hardware tutorials (GPIO, I²C sensors, LCDs, ADCs) and the deployment and debugging guides, with all the samples and wiring diagrams.
- **[Doorbot, an AI doorman](https://camsoper.github.io/projects/doorbot/):** Gemini reads the doorbell camera and Claude talks with the visitor, classifies intent, dismisses solicitors, and routes legitimate callers to a human. The agent has no tools and code acts on only four intent words, so the worst a prompt injection can do is pick the wrong one. [Watch it run](https://youtu.be/KKPevcH1WuE).
- **Open source:** [`shark2mqtt`](https://github.com/CamSoper/shark2mqtt), a Python Home Assistant bridge for Shark robot vacuums (35+ stars, with a community-maintained Home Assistant OS add-on); [`Inferno`](https://github.com/CamSoper/Inferno), a .NET-powered smart smoker; and [`puppet`](https://github.com/CamSoper/puppet), a .NET home-automation framework (110+ stars, retired after my move to Home Assistant).

## Talks, Streams & Writing

- **Speaking:** 15+ conference sessions at .NET Conf, KCDC, CodeMash, DevUp, TechBash, Code PaLOUsa, Music City Tech, Beer City Code, Cream City Code, Little Rock Tech Fest, and local user groups. Selected talks:
  - "Infrastructure as (Actual) Code with C# 15 and .NET 11" (.NET Conf 2026 Community Days, Nov 13, upcoming)
  - "Have Your Pi and Eat It Too: .NET Core on Raspberry Pi" (.NET Conf 2018; CodeMash, Beer City Code, Code PaLOUsa, DevUp, TechBash 2019)
  - "My House Runs .NET: Smart Home Automation with .NET Core and Azure" (.NET Conf, Code PaLOUsa, Music City Tech, DevUp 2019)
  - "How Insightful! Grok Your ASP.NET Core Web Apps with Application Insights" (KCDC, DevUp, TechBash 2019)
  - "Smokin' .NET to Perfection: Building a smart wood pellet smoker with Raspberry Pi and .NET" (KCDC 2021)
- **Streaming and events:** co-founded The .NET Docs Show in 2020, which became [On .NET Live](https://www.youtube.com/playlist?list=PLdo4fOcmZ0oV2fcY7wsQHx4RNWXEDKgm4), the weekly community stream on the official .NET channels, and co-hosted it until 2026; helped plan and host .NET Conf; ran hands-on training labs at Microsoft Build; taught Let's Learn .NET and Learn Live workshops.
- **Video:** wrote and recorded the Entity Framework Core for Beginners (120K+ views) and .NET IoT for Beginners series on the official .NET YouTube channel.
- **Writing:** most of Microsoft Learn's .NET training modules, and "[Treating Prompts Like Code](https://www.pulumi.com/blog/treating-prompts-like-code/)" on the Pulumi blog.

## Work Experience

### Senior Software Engineer

**Pulumi · Remote** — *Oct 2026 – Present*

Internal systems engineering team, focused on accelerating Pulumi's automated development workflows. My piece is QA: once a pull request is open, whether a human or an agent wrote it, how do we know it's good, and how fast can it merge safely?

- Building **automated quality analysis and merge gates** that apply one quality bar to human- and agent-authored pull requests.
- Still own the **Pulumi docs platform** I built as a content engineer, run as an engineering system.

### Senior Technical Content Engineer

**Pulumi · Remote** — *Jul 2025 – Oct 2026*

Joined to write docs; within a month I was Pulumi's sole docs engineer. Turned that into a one-person docs-ops practice for Pulumi's infrastructure-as-code product: the `pulumi/docs` repository, the build pipeline, the information architecture, and the quality gate every change ships through. Treated the docs as two products: one for humans, and one for the AI agents that increasingly read them first.

- Built an **[AI-powered PR review pipeline](https://camsoper.github.io/projects/docs-pipeline/)**: Vale and markdownlint gates plus LLM claim verification in CI/CD, with models chosen by recorded benchmarks. The [skills behind it](https://github.com/pulumi/docs/tree/master/.claude/commands) are public in the docs repo.
- Designed a modular **"prompts as code"** skill system: reusable, version-controlled AI skills that share a single source of truth for style and review criteria, adopted and extended by engineering and marketing.
- Built the **agent-consumable knowledge layer**: every page served as Markdown, a curated `llms.txt`, a JSON sitemap, and Context7 onboarding, so coding agents retrieve current docs instead of stale training data.
- Partnered with marketing on **SEO/AEO**, tuning content so AI answer engines cite it accurately.
- Wrote docs and runnable examples in **.NET, Go, Python, and TypeScript**.

### Senior Content Developer

**Microsoft · Remote** — *Jun 2015 – May 2025*

Developer education for .NET and Azure: docs, training, video, and live shows, plus the authoring tooling behind them.

- Primary author of **.NET training on Microsoft Learn** (fundamentals, ASP.NET Core, EF Core, microservices, Azure SDKs).
- Owned **467 Azure and .NET documentation and training topics** driving **1.1M+ annual pageviews**.
- Wrote the entire **.NET IoT documentation** set, bridging hardware integration with .NET development.
- Built an early **AI authoring skill** on GitHub Copilot that turned structured model output into the .NET docs' standard "What's new" pages.
- Built developer environments with **Dev Containers, Codespaces, and WSL** for Linux-first and cross-platform developers.

### Premier Field Engineer

**Microsoft · Various Locations, Remote** — *Feb 2012 – Jun 2015*

Consulted on mission-critical .NET and Azure systems for federal agencies and Fortune 500 companies, diagnosing scalability and performance issues, guiding enterprise architecture, and delivering hands-on developer training.

- Launched Microsoft's **first fully online Premier workshops**, proving virtual technical education could match in-person delivery.
- Notable customers: White House Communications Agency, US Air Force, US Government Printing Office, Orange County (CA), Toshiba of America.

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
