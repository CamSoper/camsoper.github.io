---
layout: default
nav: portfolio
title: "Inferno: how it works | Cam Soper"
description: "How a .NET pellet-smoker controller turns a temperature reading into auger, blower, and igniter actions that hold a setpoint."
---

<div class="wrap">

  <header class="card band" style="padding:48px 64px;">
    <h1 style="font-size:40px;">Inferno: a .NET smart smoker</h1>
    <p class="lead">A Raspberry Pi running .NET 8 replaces a pellet grill's stock controller, holds a set temperature with a PID loop, keeps the fire alive on its own, and plugs into Home Assistant over MQTT.</p>
  </header>

  <article class="card prose portfolio project">

    <section>
      <h2>How it works</h2>
      <figure>
        <a href="{{ '/assets/img/diagrams/inferno.svg' | relative_url }}"><img src="{{ '/assets/img/diagrams/inferno.svg' | relative_url }}" alt="Flowchart: Home Assistant and a CLI reach the web API on the Raspberry Pi through an MQTT bridge or HTTP. The smoker mode loop runs a PID controller in Hold mode that sets seconds of auger feed per 20-second cycle, while a fire minder handles ignition, lid detection, and fail-safes. Relays drive the auger, blower, and igniter, and an RTD probe feeds temperature back."></a>
        <figcaption>The control loop in the middle, everything else hanging off the web API. Click for full size.</figcaption>
      </figure>
      <p>Inferno.Api runs on a Raspberry Pi inside the grill and is the only process that touches hardware. An RTD probe, read through an ADC, gives a smoothed grill temperature. In Hold mode a PID controller compares that reading to the setpoint and answers with a fraction, which becomes seconds of auger feed in each 20-second cycle. It works like cruise control, with pellets as the gas pedal, and it never feeds below a floor because a starved fire goes out. Beside that loop, a fire minder ticks every second. It lights the igniter on a cold start, tells an opened lid (a sudden cliff) from a dying fire (a slow slope), relights a struggling fire, and fails safe if the probe goes blind. Home Assistant, the CLI, and an MQTT bridge only change mode and setpoint, through the web API.</p>
    </section>

    <section>
      <h2>Notable engineering details</h2>
      <ul>
        <li><strong>PID with anti-windup.</strong> The integral is clamped so the I term alone never exceeds half a cycle, and the controller re-seeds after a sensor gap instead of computing a derivative across it.</li>
        <li><strong>Lid detection.</strong> A 30&deg;F drop inside 10 seconds latches "lid open", runs a small fixed feed, and freezes the PID, so opening the lid doesn't light the igniter. Recovery starts only after 45 seconds below the check temperature.</li>
        <li><strong>Fail-safe paths.</strong> An out-of-range probe reads as NaN, never a stale value. Five more seconds of NaN during a cook forces Error, which cuts fuel and igniter and runs the blower. A clean shutdown de-energizes the relays.</li>
        <li><strong>Testable time.</strong> Time-based rules use an injected <code>TimeProvider</code> on a monotonic clock, so a clock jump on the RTC-less Pi can't trip a timeout. Tests drive the fire minder with a fake clock, and CI runs them on every push.</li>
        <li><strong>Home Assistant without YAML.</strong> The MQTT bridge publishes discovery configs, so entities and controls appear on their own, and it publishes retained state only on change.</li>
        <li><strong>Deployed with Pulumi.</strong> A version tag triggers a Pulumi C# program that deploys to the Pi over SSH.</li>
      </ul>
    </section>

    <section>
      <h2>Code and talks</h2>
      <ul>
        <li><a href="https://github.com/CamSoper/Inferno">Inferno on GitHub</a></li>
        <li><a href="https://www.youtube.com/watch?v=4kJGRuXZ4kg">On .NET: "BBQ, Bots and .NET Core"</a></li>
        <li><a href="https://www.youtube.com/watch?v=Ps3bHwY8dSg">The .NET Docs Show: "Smoking ribs with .NET and Cam Soper"</a></li>
        <li><a href="https://github.com/CamSoper/smokin-dotnet">"Smokin' .NET to Perfection" talk materials (KCDC 2021)</a></li>
      </ul>
      <p class="back"><a href="{{ '/portfolio/' | relative_url }}">Back to the portfolio</a></p>
    </section>

  </article>

</div>
