---
layout: default
nav: portfolio
title: "AI driveway intelligence: how it works | Cam Soper"
description: "How one Gemini vision call and a template rule turn driveway motion into an event timeline and package reminders."
---

<div class="wrap">

  <header class="card band" style="padding:48px 64px;">
    <h1 style="font-size:40px;">AI driveway intelligence</h1>
    <p class="lead">One Gemini vision call per driveway visit turns two front-of-house cameras into a timestamped, typed record. A Home Assistant template rule, with no second model call, decides what happens next.</p>
  </header>

  <article class="card prose portfolio project">

    <section>
      <h2>How it works</h2>
      <figure class="tall">
        <a href="{{ '/assets/img/diagrams/driveway.svg' | relative_url }}"><img src="{{ '/assets/img/diagrams/driveway.svg' | relative_url }}" alt="Flowchart in three stages: a free gate that skips the model when the door just opened or Doorbot is busy, one Gemini call that returns a timestamped event sequence and typed labels, and a template rule that logs the event and starts a package reminder until the front door opens."></a>
        <figcaption>Three stages: a free gate, one model call, a deterministic rule. Click for full size.</figcaption>
      </figure>
      <p>A motion sensor on the driveway starts the run. Two free state checks stop it first if the front door just opened or Doorbot is already handling a visit. The automation seeds a fail-closed answer, then makes one call to Gemini with frames from the yard camera and the doorbell camera, capped at 10 frames, 1024 px wide, and low media resolution. A JSON schema makes the model write a timestamped event sequence first, reading the time burned into each frame so both cameras merge into one timeline. Then it fills fixed-list labels for origin, last action, item, and role, each with an "unclear" option. A Jinja template reads those labels: real activity goes on the event timeline, and a delivery pattern with the door still closed starts a reminder. After a 90-second grace period it announces once, then nags every two hours until the front door opens.</p>
    </section>

    <section>
      <h2>Notable engineering details</h2>
      <ul>
        <li><strong>Evidence before verdict.</strong> The schema puts the event sequence first, so every label rests on a written, timestamped list of observations. On-frame timestamps, rather than frame order, merge the two cameras.</li>
        <li><strong>The decision is a rule.</strong> Dispatch is a deterministic template over the model's labels: a uniform plus a set-down, or a visitor who arrived from the street and left. No second model call, so it's free and auditable.</li>
        <li><strong>Fail-closed by construction.</strong> A seeded "no activity, all unclear" answer survives a failed call, the prompt tells the model to prefer "unclear", and truncated replies are logged for review.</li>
        <li><strong>Cost and noise controls.</strong> Single-run mode plus a 45-second cooldown, capped frames and resolution, and a cheaper pre-screen model running in a logged shadow trial before it's trusted to skip calls.</li>
        <li><strong>Plays well with Doorbot.</strong> A shared flag keeps a package from being announced twice, and opening the front door is the one off switch for the whole reminder cycle.</li>
      </ul>
      <p class="note">The source is private for security and privacy reasons, so this page describes it without linking to code.</p>
      <p class="back"><a href="{{ '/portfolio/' | relative_url }}">Back to the portfolio</a></p>
    </section>

  </article>

</div>
