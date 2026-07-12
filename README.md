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

### 🪗 [Accordion](https://github.com/aadityad12/Accordion)

**Reversible context management for LLM coding agents** &nbsp;·&nbsp; 🏆 *Winner — The Token Company prize @ UC Berkeley AI Hackathon 2026*

Treats the entire context window as foldable blocks under a token budget — fold what's irrelevant now, unfold it when it matters again.

- Three-stage relevance pipeline (`the-conductor-v2`): keyword filter → bi-encoder cosine → cross-encoder rerank
- Self-calibrating fold targets that adapt compression to the live token budget
- Live dashboard for watching fold/unfold decisions in real time

<kbd>TypeScript</kbd> <kbd>Node.js</kbd> <kbd>SvelteKit</kbd> <kbd>bi- + cross-encoder retrieval</kbd>

---

### 🌡️ [Temper](https://github.com/aadityad12/Temper)

**Evaluate the environment around an LLM, not the model.**

Most eval tools score the model. Temper scores everything wrapped around it — system prompt, tools, skill files — because that's where most deployed quality is won or lost.

- Scores a harness against a bare-model baseline across six dimensions
- Generates targeted patches, then re-evaluates to confirm they actually worked
- Core eval engine built end-to-end: baseline → diagnosis → patch → re-eval loop

<kbd>Python</kbd> <kbd>FastAPI</kbd> <kbd>Gemini</kbd> <kbd>LLM evals</kbd>

---

### 🧿 [GazeBoard](https://github.com/aadityad12/GazeBoard)

**Speak with your eyes — on an off-the-shelf phone.**

Lets ALS patients type and speak using only their eyes. No dedicated hardware, no cloud, no connectivity required.

- MediaPipe FaceMesh (478 landmarks) compiled to the Qualcomm Hexagon NPU via the LiteRT `CompiledModel` API — **~8 ms inference, fully offline**
- Custom 4-point affine calibration engine mapping gaze vectors to screen coordinates
- End-to-end Android deployment: camera pipeline → NPU → UI at interactive framerates

<kbd>Kotlin</kbd> <kbd>Android</kbd> <kbd>LiteRT</kbd> <kbd>MediaPipe</kbd> <kbd>Hexagon NPU</kbd> <kbd>CameraX</kbd>

---

### 📡 [Echo](https://github.com/aadityad12/Echo)

**Emergency alerts that hop phone-to-phone with zero infrastructure.**

When the internet and cell towers go down in a disaster, alerts still need to move. Echo makes phones the network.

- Custom GATT chunked-transfer protocol with native Kotlin *and* Swift implementations
- Gossip mesh with SHA-1 deduplication; Raspberry Pi relay nodes extend range
- Offline translation into 23 languages — alerts arrive readable, not just received

<kbd>Flutter</kbd> <kbd>Kotlin</kbd> <kbd>Swift</kbd> <kbd>BLE / GATT</kbd> <kbd>gossip mesh</kbd> <kbd>Raspberry Pi</kbd>

---

### 📱 [ApexTracker](https://github.com/aadityad12/Trackers)

**Budget, study, screen time, reminders & notes — one native Android app.**

Consolidates the trackers you'd otherwise juggle across five different apps into six independent MVVM modules behind a single menu — fully offline-first.

- Room is the source of truth; Google Sign-In adds optional Firestore sync — never required
- Recurring reminders with exact `AlarmManager` scheduling that survives reboots, with graceful fallback when the exact-alarm permission is revoked
- Per-app screen time via `UsageStatsManager`; subscriptions auto-generate budget items, back-filling missed months

<kbd>Kotlin</kbd> <kbd>Jetpack Compose</kbd> <kbd>Material 3</kbd> <kbd>Room / SQLite</kbd> <kbd>Firebase</kbd>

---

### 🚒 [Clear Dispatch](https://github.com/aadityad12/Clear-Dispatch)

**Four LLM agents behind a 911 dispatcher during wildfire surges.**

During wildfire call surges, dispatchers drown in volume. Clear Dispatch puts four cooperating agents behind them — with the human always in control.

- Agents handle triage, unit routing, and voice briefings; the dispatcher keeps final authority on every action
- Real-time WebSocket pipeline with zero polling — updates push the instant state changes
- Human-in-the-loop by design, not as an afterthought

<kbd>Python</kbd> <kbd>FastAPI</kbd> <kbd>React</kbd> <kbd>Claude</kbd> <kbd>WebSockets</kbd>

<br/>

## 📊 Signal, Not Noise

<sub>Metrics that mean something — pulled live from the GitHub API and re-rendered on every visit, so they never go stale.</sub>

<div align="center">
  <img height="170" src="https://github-readme-stats-sigma-five.vercel.app/api?username=aadityad12&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github&include_all_commits=true" alt="GitHub stats"/>
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
