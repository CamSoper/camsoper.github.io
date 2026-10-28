---
layout: default
nav: portfolio
title: "Docs AI review pipeline: how it works | Cam Soper"
description: "How a Pulumi docs pull request moves from open to a merge-gate decision through deterministic checks, Claude models, and a model-free Sentinel."
---

<div class="wrap">

  <header class="card band" style="padding:48px 64px;">
    <h1 style="font-size:40px;">AI docs review pipeline</h1>
    <p class="lead">A pre-merge review for docs pull requests in <code>pulumi/docs</code>: deterministic linting and claim checks, Claude models for finding, verifying, and editing, and a merge gate that no model controls.</p>
  </header>

  <article class="card prose portfolio project">

    <section>
      <h2>How it works</h2>
      <figure class="tall">
        <a href="{{ '/assets/img/diagrams/docs-pipeline.svg' | relative_url }}"><img src="{{ '/assets/img/diagrams/docs-pipeline.svg' | relative_url }}" alt="Flowchart: a docs PR is triaged by a shell classifier. Trivial PRs get a Haiku prose check. Others go through Vale on added lines, claim extraction with regex and two Sonnet passes, Opus verification of each claim, a script-drafted review that Opus edits, and a validator. If the reviewed commit is still the head, a publish job posts the review, then the Sentinel merge gate evaluates five gates without a model."></a>
        <figcaption>One docs PR, from open to gate decision. Click for full size.</figcaption>
      </figure>
      <p>When an author opens a ready docs PR, a triage workflow labels it with a shell classifier. Trivial or frontmatter-only PRs get a quick Claude Haiku prose check and skip the full review. Everything else gets the full review. Vale runs on changed files and keeps findings only on added lines. Claims are found three ways, a regex floor plus two Claude Sonnet passes, and each one is verified by a bounded Claude Opus agent loop, routed to a lane by plain rules (some claims settle with no model call at all). A script drafts the review, Opus edits it without cloud credentials, and a validator rejects any edit that demotes or drops a finding. A separate publish job posts the results, but only if the reviewed commit is still the PR head. Finally the Sentinel, a pure function of GitHub state with no model, evaluates five gates and posts one commit status. markdownlint runs separately as part of the PR build.</p>
    </section>

    <section>
      <h2>Notable engineering details</h2>
      <ul>
        <li><strong>Models never decide a merge.</strong> Model output enters only as files that scripts validate, and findings may move up toward blocking, never down.</li>
        <li><strong>Privilege split.</strong> The model job holds no cloud credentials, only the model key and a PR-scoped token, and runs only for authors with write access. The publish job runs only default-branch scripts and refuses to publish a review of a stale head.</li>
        <li><strong>Redundant claim extraction.</strong> Regex plus two differently framed passes feed a claim floor, and each claim is routed by rules to source, URL, or web-search verification. A verdict whose only evidence is the page under review gets re-checked.</li>
        <li><strong>The Sentinel fails closed.</strong> An evaluation error blocks the merge. The <code>review:waived</code> break-glass label is honored only from an active routing-team member, and the verdict summary names who applied it.</li>
        <li><strong>Safe on untrusted PRs.</strong> The Sentinel never checks out PR code, and a test asserts it. A repo setting runs it report-only before it enforces.</li>
        <li><strong>Models chosen by benchmark.</strong> Haiku for trivial PRs, Sonnet for extraction, Opus for verification and editing, with the benchmark results recorded next to the choices.</li>
      </ul>
    </section>

    <section>
      <h2>Code and write-up</h2>
      <ul>
        <li><a href="https://github.com/pulumi/docs/tree/master/scripts/review-v3">Review machinery and the Sentinel</a></li>
        <li><a href="https://github.com/pulumi/docs/blob/master/.github/workflows/claude-code-review.yml">Review workflow</a></li>
        <li><a href="https://github.com/pulumi/docs/blob/master/.github/workflows/review-sentinel.yml">Sentinel workflow</a></li>
        <li><a href="https://github.com/pulumi/docs/tree/master/.claude/commands">The docs skills (open source)</a></li>
        <li><a href="https://www.pulumi.com/blog/treating-prompts-like-code/">Treating Prompts Like Code</a></li>
      </ul>
      <h2>Code walkthrough</h2>
      <p><a href="https://claude.ai/artifact/XVUbiaM9o87AfmwiE7Ckay"><strong>Step through the code, chapter by chapter</strong></a></p>
      <p class="note">Built by <a href="https://github.com/CamSoper/adhd-ops/tree/main/code-walkthrough">code-walkthrough</a>, my Claude Code skill, from <code>pulumi/docs</code> at a pinned commit. Every line links to GitHub, so you can check its work.</p>
      <p class="back"><a href="{{ '/portfolio/' | relative_url }}">Back to the portfolio</a></p>
    </section>

  </article>

</div>
