---
layout: default
nav: portfolio
title: "Self-hosted MCP platform: how it works | Cam Soper"
description: "How an agent's tool call reaches a self-hosted MCP server, and how a new server ships as infrastructure as code."
---

<div class="wrap">

  <header class="card band" style="padding:48px 64px;">
    <h1 style="font-size:40px;">Self-hosted MCP platform</h1>
    <p class="lead">My own MCP servers run as containers in my home lab, reachable by Claude only through authentication, and every merge ships itself through GitHub Actions, Pulumi ESC, and a Pulumi C# deployment.</p>
  </header>

  <article class="card prose portfolio project">

    <section>
      <h2>How it works</h2>
      <figure>
        <a href="{{ '/assets/img/diagrams/mcp-platform.svg' | relative_url }}"><img src="{{ '/assets/img/diagrams/mcp-platform.svg' | relative_url }}" alt="Two flows. Shipping: a merge builds only changed images in GitHub Actions, pins each image digest in Pulumi ESC, and a Pulumi deployment replaces the container over SSH. A tool call: Claude signs in through Cloudflare Access, the call travels a Cloudflare Tunnel to the MCP container, which re-checks the token and a topic allowlist before touching home systems."></a>
        <figcaption>Left: how a change ships. Right: how a tool call arrives. Click for full size.</figcaption>
      </figure>
      <p>Two repos split the work. One holds a directory per MCP server: some wrap upstream packages, others are first-party TypeScript. GitHub Actions builds only the directories a push changed, pushes each image to GitHub Container Registry, writes its sha256 digest into a Pulumi ESC environment, and triggers a deployment. The other repo, a Pulumi C# program, reads those digests and deploys each container over SSH from a customer-managed Pulumi workflow agent. At runtime, Claude signs in through Cloudflare Access with OAuth, which forwards each call with a signed token down one Cloudflare Tunnel. The tunnel reaches each MCP container by its Docker network name, and no container publishes a port. The server re-verifies the token, then applies its own limits, such as the MQTT server's topic allowlist, before touching a home system.</p>
    </section>

    <section>
      <h2>Notable engineering details</h2>
      <ul>
        <li><strong>Two independent checks.</strong> Access at the edge, then origin-side verification of the signed token on the first-party servers that have one, against that server's own audience, which the Pulumi program pulls from the stack that owns the Access apps through a StackReference.</li>
        <li><strong>A narrow MQTT server.</strong> The broker is pinned from configuration and every subscribe and publish is checked against read and write allowlists. It replaced a third-party server whose tools accepted a host and credentials on every call.</li>
        <li><strong>Request and response over pub/sub.</strong> Subscribe before publishing, accept only the live echo (never a retained message), and re-check every delivered topic against the allowlist.</li>
        <li><strong>Merge ships it.</strong> CI maps each directory to its ESC key and writes every digest in one job, so parallel builds can't race on the environment. The only human step is a one-time switch to make a new server's image package public.</li>
        <li><strong>Digest-pinned images.</strong> Each container depends explicitly on its image resource, so a replacement never fails trying to delete an image that's still in use.</li>
        <li><strong>Stateless transport.</strong> A fresh MCP server per HTTP request, so no session has to survive the tunnel hop.</li>
      </ul>
      <p class="note">The source is private for security and privacy reasons, so the walkthrough quotes a redacted extract and its line numbers aren't linked to GitHub.</p>
      <h2>Code walkthrough</h2>
      <p><a href="https://claude.ai/artifact/3JbqPSV3DPa2DTxwK8ouNd"><strong>Step through the code, chapter by chapter</strong></a></p>
      <p class="note">Written by <a href="https://github.com/CamSoper/adhd-ops/tree/main/code-walkthrough">code-walkthrough</a>, a Claude Code skill I built so a private codebase can still be explained honestly, quoted verbatim from a redacted extract.</p>
      <p class="back"><a href="{{ '/portfolio/' | relative_url }}">Back to the portfolio</a></p>
    </section>

  </article>

</div>
