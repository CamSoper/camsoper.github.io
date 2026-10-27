---
layout: resume
nav: resume
title: "Résumé — Cam Soper"
description: "Senior software engineer and AI systems builder. I automate code quality analysis at Pulumi and own its docs platform."
---

Senior software engineer and systems builder who automates complex technical work with AI. On Pulumi's internal systems engineering team I build automated quality analysis for pull requests, whether a person or an agent wrote them: is the change any good, and how fast can it merge safely? I also own Pulumi's documentation platform, which I built as a one-person docs-ops practice: the repository, the build pipeline, the information architecture, and an AI-driven review system that checks every change before it ships. Coding since 1991, across software engineering, cloud infrastructure (Azure, .NET), and developer education. I build the system, not just the content.

## Key Skills

- **AI Systems & Automation** — design modular, multi-model LLM pipelines for code and content review, fact-checking, and quality analysis that let one person operate like a team.
- **Solution Architecture & Platform Ownership** — own repositories, build pipelines, information architecture, and quality gates end to end.
- **DevOps, CI/CD & QA Automation** — GitHub Actions, automated PR quality analysis and gates, dev containers, and infrastructure as code with Pulumi.
- **Polyglot Engineering** — .NET/C#, Go, Python, and TypeScript; ramp on new languages through fundamentals, not syntax.
- **Cloud & Infrastructure** — deep Azure background plus multi-cloud IaC, containers, and scalable architectures.
- **Technical Education & Communication** — turn complex systems into documentation, talks, and training developers actually use.

## Work Experience

### Senior Software Engineer

**Pulumi · Remote** — *Oct 2026 – Present*

Internal systems engineering team, focused on accelerating Pulumi's automated development workflows. My piece is QA: once a pull request is open, whether a human or an agent wrote it, how do we know it's good, and how fast can it merge safely?

- Build **automated quality analysis** for open pull requests, so engineers (and coding agents) spend less time waiting on review and more time shipping.
- Continue to own the **Pulumi docs platform** I built as a content engineer, run as an engineering system: same quality gates, more automation, less manual review.

#### Skills & Technologies

QA Automation · AI Code Review · Agentic Workflows · Anthropic Claude · LLM Orchestration · CI/CD · GitHub Actions · TypeScript · Go · Python

### Senior Technical Content Engineer

**Pulumi · Remote** — *Jul 2025 – Oct 2026*

Joined to write docs; a month in, the only other docs person left and I became the docs team. Turned that into a one-person docs-ops practice for Pulumi's infrastructure-as-code product: the `pulumi/docs` repository, the site and docs build pipeline, the information architecture, and the quality gate every change ships through. Treated the docs as two products: one for humans, and one for the AI agents that increasingly read them first.

- Built an **AI-powered PR review pipeline** that pairs deterministic linting (Vale, markdownlint) with multi-model LLM fact-checking (Claude Opus and Sonnet), scoped to changed lines and wired into CI/CD. It is cited internally as the reference implementation for the company's content-quality model.
- Designed a modular **"prompts as code"** skill system: reusable, version-controlled AI skills that share a single source of truth for style and review criteria, adopted and extended by engineering and marketing. Wrote it up on the [Pulumi blog](https://www.pulumi.com/blog/treating-prompts-like-code/).
- Partner with marketing on **SEO/AEO**, tuning content to be accurately cited by AI answer engines (Google AI Overviews, LLM assistants) without resorting to spam.
- Built the **agent-consumable knowledge layer** (clean `.md` URLs, a curated `llms.txt`, and a JSON sitemap) so coding agents retrieve current, authoritative documentation instead of stale training data.
- Pushed for a **launch-docs standard** so new Pulumi Cloud features ship with complete documentation, not docs that show up three sprints later.
- Work polyglot across documentation and runnable examples in **.NET, Go, Python, and TypeScript**.

#### Skills & Technologies

AI Systems · Anthropic Claude · OpenAI · LLM Orchestration · Prompt Engineering · CI/CD · GitHub Actions · Docs-Ops · Vale · Hugo · Infrastructure as Code · Pulumi · Python · Go · TypeScript · .NET

### Senior Content Developer

**Microsoft · Remote** — *Jun 2015 – May 2025*

Developer education and tooling across .NET and Azure, with a growing focus on automation. Built and maintained learning systems used by millions of developers.

- Designed and implemented **AI-driven documentation tooling**, integrating GitHub Copilot to streamline authoring and content automation.
- Owned a portfolio of **467 Azure and .NET documentation and training topics** driving **1.1M+ annual pageviews**.
- Built developer environments with **Dev Containers, Codespaces, and WSL**, streamlining onboarding for Linux-first and cross-platform developers.
- Wrote the entire **.NET IoT documentation** set, bridging hardware integration with .NET development.
- Primary author of .NET training on Microsoft Learn (fundamentals, ASP.NET Core, EF Core, microservices, Azure SDKs); wrote and recorded instructional video series (.NET IoT for Beginners, Entity Framework Core for Beginners).
- Co-founded and co-hosted **On .NET Live**, the weekly community stream on the official .NET channels; kept co-hosting after Microsoft until the show wrapped, hundreds of episodes in.

#### Skills & Technologies

.NET · ASP.NET Core · Azure · AI Tooling · GitHub Copilot · Technical Documentation · Dev Containers · Codespaces · WSL · Microservices · Solution Architecture

### Premier Field Engineer

**Microsoft · Various Locations, Remote** — *Feb 2012 – Jun 2015*

Consulted on mission-critical .NET and Azure systems for federal agencies and Fortune 500 companies, diagnosing scalability and performance issues, guiding enterprise architecture, and delivering hands-on developer training.

- Launched Microsoft's **first fully online Premier workshops**, proving virtual technical education could match in-person delivery.
- Notable customers: White House Communications Agency, US Air Force, US Government Printing Office, Orange County (CA), Toshiba of America.

#### Skills & Technologies

.NET · Azure · Consulting · Enterprise Architecture · Performance Optimization · Developer Education

## Selected Projects

- **Doorbot — AI doorman** — a Claude-powered door agent that reads the doorbell camera, holds a conversation with visitors, classifies intent (delivery, solicitor, law enforcement, emergency), dismisses solicitors, and routes legitimate callers to a human. Resists prompt-injection attempts.
- **AI driveway intelligence** — a multi-camera vision pipeline (Gemini, structured-JSON output) that reconstructs an event timeline, classifies deliveries vs. solicitors vs. residents, and triggers package reminders, with model-cost controls and false-positive guards built in.
- **Open source** — [`puppet`](https://github.com/CamSoper/puppet), a home-automation framework (100+ stars); [`shark2mqtt`](https://github.com/CamSoper/shark2mqtt), a Home Assistant device bridge in Python; and [`Inferno`](https://github.com/CamSoper/Inferno), a .NET-powered smart smoker.

---

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
