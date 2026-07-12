<!-- ============================================================ -->
<!--  HEADER · animated gradient wave (Tokyo Night palette)       -->
<!-- ============================================================ -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1b27,50:414868,100:7aa2f7&height=180&section=header&text=Aaditya%20Desai&fontSize=42&fontColor=c0caf5&animation=fadeIn&fontAlignY=32&desc=AI%20systems%2C%20down%20to%20the%20hardware&descSize=16&descAlignY=52" width="100%" alt="banner"/>
</div>

<!-- Auto-typing headline -->
<div align="center">
  <a href="https://github.com/aadityad12">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=500&size=20&duration=2800&pause=900&color=7AA2F7&center=true&vCenter=true&width=620&lines=On-device+NPU+inference+%C2%B7+8ms+on+a+phone;Custom+BLE+wire+protocols+%C2%B7+offline+mesh;LLM+agents%2C+evals+%26+context+engineering;End-to-end+deployments%2C+not+demo+notebooks" alt="typing intro"/>
  </a>
</div>

<p align="center">
  <a href="https://www.linkedin.com/in/aaditya-desai-12d"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:aaditya.d.desai@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <img src="https://img.shields.io/badge/SJSU-Computer%20Engineering%20'27-1a1b27?style=flat-square&labelColor=414868" alt="SJSU"/>
  <img src="https://img.shields.io/badge/Open%20to-AI%2FML%20%26%20Edge%20AI%20Internships-1a1b27?style=flat-square&labelColor=414868&color=9ece6a" alt="Open to internships"/>
</p>

Computer Engineering student at San Jose State University (Dec 2027) building AI systems down to the hardware: on-device NPU inference, custom BLE wire protocols, and LLM agents and evals. I ship end-to-end deployments, not demo notebooks.

<br/>

## ⚡ Featured Builds

> Each project lists the exact stack it was built with — no generic badge wall.

<!-- ──────────────────────────── Accordion ──────────────────────────── -->
<table width="100%">
  <tr>
    <td colspan="2">
      <h3>🪗 <a href="https://github.com/aadityad12/Accordion">Accordion</a> &nbsp;·&nbsp; <sub><i>Reversible context management for LLM coding agents</i></sub></h3>
      🏆 <i>Winner — The Token Company sponsor prize @ UC Berkeley AI Hackathon 2026</i>
    </td>
  </tr>
  <tr>
    <td width="62%" valign="top">
      Treats the entire LLM context window as foldable blocks under a token budget — fold what's irrelevant now, unfold it when it matters again.
      <ul>
        <li>Built <b><code>the-conductor-v2</code></b>: a three-stage relevance pipeline — keyword filter → bi-encoder cosine → cross-encoder rerank</li>
        <li><b>Self-calibrating fold targets</b> that adapt compression to the live token budget</li>
        <li>Live conductor activity dashboard for observing fold/unfold decisions in real time</li>
      </ul>
    </td>
    <td width="38%" valign="top">
      <sub><b>CORE</b></sub><br/>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
      <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js"/>
      <br/><br/>
      <sub><b>AI · RETRIEVAL</b></sub><br/>
      <img src="https://img.shields.io/badge/Bi--encoder%20%2B%20Cross--encoder-1a1b27?style=flat-square&labelColor=414868&color=bb9af7" alt="Encoders"/>
      <img src="https://img.shields.io/badge/Token%20Budgeting-1a1b27?style=flat-square&labelColor=414868&color=bb9af7" alt="Token budgeting"/>
      <br/><br/>
      <sub><b>FRONTEND</b></sub><br/>
      <img src="https://img.shields.io/badge/SvelteKit-FF3E00?style=flat-square&logo=svelte&logoColor=white" alt="SvelteKit"/>
    </td>
  </tr>
</table>

<!-- ──────────────────────────── Temper ──────────────────────────── -->
<table width="100%">
  <tr>
    <td colspan="2">
      <h3>🌡️ <a href="https://github.com/aadityad12/Temper">Temper</a> &nbsp;·&nbsp; <sub><i>Evaluate the environment around an LLM, not the model</i></sub></h3>
    </td>
  </tr>
  <tr>
    <td width="62%" valign="top">
      Most eval tools score the model. Temper scores everything wrapped around it — system prompt, tools, skill files — because that's where most deployed quality is won or lost.
      <ul>
        <li>Scores a harness against a <b>bare-model baseline across six dimensions</b></li>
        <li>Generates <b>targeted patches</b>, then re-evaluates to confirm they actually worked</li>
        <li>Built the <b>core eval engine end-to-end</b>: baseline → diagnosis → patch → re-eval loop</li>
      </ul>
    </td>
    <td width="38%" valign="top">
      <sub><b>CORE</b></sub><br/>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
      <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
      <br/><br/>
      <sub><b>AI · EVALS</b></sub><br/>
      <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini"/>
      <img src="https://img.shields.io/badge/LLM%20Evals-1a1b27?style=flat-square&labelColor=414868&color=bb9af7" alt="LLM Evals"/>
    </td>
  </tr>
</table>

<!-- ──────────────────────────── GazeBoard ──────────────────────────── -->
<table width="100%">
  <tr>
    <td colspan="2">
      <h3>🧿 <a href="https://github.com/aadityad12/GazeBoard">GazeBoard</a> &nbsp;·&nbsp; <sub><i>Speak with your eyes — on an off-the-shelf phone</i></sub></h3>
    </td>
  </tr>
  <tr>
    <td width="62%" valign="top">
      Lets ALS patients type and speak using only their eyes. No dedicated hardware, no cloud, no connectivity required.
      <ul>
        <li>MediaPipe FaceMesh (478 landmarks) compiled to the <b>Qualcomm Hexagon NPU</b> via the LiteRT <code>CompiledModel</code> API — <b>~8ms inference, fully offline</b></li>
        <li>Custom <b>4-point affine calibration engine</b> mapping gaze vectors to screen coordinates</li>
        <li>End-to-end Android deployment: camera pipeline → NPU → UI at interactive framerates</li>
      </ul>
    </td>
    <td width="38%" valign="top">
      <sub><b>CORE</b></sub><br/>
      <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin"/>
      <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=black" alt="Android"/>
      <br/><br/>
      <sub><b>AI · ON-DEVICE</b></sub><br/>
      <img src="https://img.shields.io/badge/LiteRT%20(TFLite)-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="LiteRT"/>
      <img src="https://img.shields.io/badge/MediaPipe-0097A7?style=flat-square&logo=google&logoColor=white" alt="MediaPipe"/>
      <img src="https://img.shields.io/badge/Hexagon%20NPU-3253DC?style=flat-square&logo=qualcomm&logoColor=white" alt="Hexagon NPU"/>
      <br/><br/>
      <sub><b>SYSTEMS</b></sub><br/>
      <img src="https://img.shields.io/badge/CameraX-4285F4?style=flat-square&logo=android&logoColor=white" alt="CameraX"/>
    </td>
  </tr>
</table>

<!-- ──────────────────────────── Echo ──────────────────────────── -->
<table width="100%">
  <tr>
    <td colspan="2">
      <h3>📡 <a href="https://github.com/aadityad12/Echo">Echo</a> &nbsp;·&nbsp; <sub><i>Emergency alerts that hop phone-to-phone with zero infrastructure</i></sub></h3>
    </td>
  </tr>
  <tr>
    <td width="62%" valign="top">
      When the internet and cell towers go down in a disaster, alerts still need to move. Echo makes phones the network.
      <ul>
        <li>Custom <b>GATT chunked-transfer protocol</b> with native Kotlin <i>and</i> Swift implementations</li>
        <li>Gossip mesh with <b>SHA-1 deduplication</b>; Raspberry Pi relay nodes extend range</li>
        <li>Offline translation into <b>23 languages</b> — alerts arrive readable, not just received</li>
      </ul>
    </td>
    <td width="38%" valign="top">
      <sub><b>CORE</b></sub><br/>
      <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter"/>
      <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin"/>
      <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white" alt="Swift"/>
      <br/><br/>
      <sub><b>SYSTEMS · PROTOCOL</b></sub><br/>
      <img src="https://img.shields.io/badge/BLE%20%2F%20GATT-0082FC?style=flat-square&logo=bluetooth&logoColor=white" alt="BLE/GATT"/>
      <img src="https://img.shields.io/badge/Gossip%20Mesh-1a1b27?style=flat-square&labelColor=414868&color=7dcfff" alt="Gossip mesh"/>
      <br/><br/>
      <sub><b>HARDWARE</b></sub><br/>
      <img src="https://img.shields.io/badge/Raspberry%20Pi-A22846?style=flat-square&logo=raspberrypi&logoColor=white" alt="Raspberry Pi"/>
    </td>
  </tr>
</table>

<!-- ──────────────────────── ApexTracker / Trackers ─────────────────── -->
<table width="100%">
  <tr>
    <td colspan="2">
      <h3>📱 <a href="https://github.com/aadityad12/Trackers">ApexTracker</a> &nbsp;·&nbsp; <sub><i>Budget, study, screen time, reminders &amp; notes — one native Android app</i></sub></h3>
    </td>
  </tr>
  <tr>
    <td width="62%" valign="top">
      Consolidates the trackers you'd otherwise juggle across five different apps into six independent MVVM modules behind a single menu — fully offline-first.
      <ul>
        <li><b>Offline-first by design</b>: Room is the source of truth; Google Sign-In adds optional Firestore sync across devices — never required</li>
        <li>Recurring reminders with <b>exact <code>AlarmManager</code> scheduling that survives reboots</b>, and graceful fallback when the exact-alarm permission is revoked</li>
        <li>Per-app screen time via <code>UsageStatsManager</code>; subscriptions auto-generate budget items, back-filling missed months</li>
      </ul>
    </td>
    <td width="38%" valign="top">
      <sub><b>CORE</b></sub><br/>
      <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin"/>
      <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=black" alt="Android"/>
      <br/><br/>
      <sub><b>UI</b></sub><br/>
      <img src="https://img.shields.io/badge/Jetpack%20Compose-4285F4?style=flat-square&logo=jetpackcompose&logoColor=white" alt="Jetpack Compose"/>
      <img src="https://img.shields.io/badge/Material%203-757575?style=flat-square&logo=materialdesign&logoColor=white" alt="Material 3"/>
      <br/><br/>
      <sub><b>DATA · SYNC</b></sub><br/>
      <img src="https://img.shields.io/badge/Room%20%2F%20SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="Room/SQLite"/>
      <img src="https://img.shields.io/badge/Firebase%20Auth%20%2B%20Firestore-DD2C00?style=flat-square&logo=firebase&logoColor=white" alt="Firebase"/>
    </td>
  </tr>
</table>

<!-- ──────────────────────── Clear Dispatch ─────────────────────── -->
<table width="100%">
  <tr>
    <td colspan="2">
      <h3>🚒 <a href="https://github.com/aadityad12/Clear-Dispatch">Clear Dispatch</a> &nbsp;·&nbsp; <sub><i>Four LLM agents behind a 911 dispatcher during wildfire surges</i></sub></h3>
    </td>
  </tr>
  <tr>
    <td width="62%" valign="top">
      During wildfire call surges, dispatchers drown in volume. Clear Dispatch puts four cooperating agents behind them — with the human always in control.
      <ul>
        <li>Agents handle <b>triage, unit routing, and voice briefings</b>; the dispatcher keeps final authority on every action</li>
        <li>Real-time <b>WebSocket pipeline with zero polling</b> — updates push the instant state changes</li>
        <li>Human-in-the-loop by design, not as an afterthought</li>
      </ul>
    </td>
    <td width="38%" valign="top">
      <sub><b>CORE</b></sub><br/>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
      <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
      <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React"/>
      <br/><br/>
      <sub><b>AI · REALTIME</b></sub><br/>
      <img src="https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=claude&logoColor=white" alt="Claude"/>
      <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socketdotio&logoColor=white" alt="WebSockets"/>
    </td>
  </tr>
</table>

<br/>

## 📊 Signal, Not Noise

<div align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=aadityad12&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github&include_all_commits=true" alt="GitHub stats"/>
  <img height="170" src="https://streak-stats.demolab.com/?user=aadityad12&theme=tokyonight&hide_border=true" alt="Streak"/>
</div>

<br/>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=aadityad12&theme=tokyo-night&hide_border=true&area=true&radius=8" width="96%" alt="Contribution graph"/>
</div>

<br/>

## 📫 Reach Me

<div align="center">
  <a href="mailto:aaditya.d.desai@gmail.com">
    <img src="https://img.shields.io/badge/aaditya.d.desai%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  &nbsp;
  <a href="https://www.linkedin.com/in/aaditya-desai-12d">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
</div>

<!-- FOOTER · mirrored wave to bookend the header -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,50:414868,100:1a1b27&height=120&section=footer" width="100%" alt="footer"/>
</div>
