<p align="center">
  <img src="./assets/profile-header.svg" width="100%" alt="Aaditya Desai, Computer Engineering student at San José State University, seeking Summer 2027 software engineering internships">
</p>

<p align="center">
  <a href="https://aadityad.dev" title="Portfolio"><img src="https://api.iconify.design/mdi/web.svg?color=%23EF5B2A" width="30" height="30" alt="Portfolio"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/aaditya-desai-12d" title="LinkedIn"><img src="https://api.iconify.design/simple-icons/linkedin.svg?color=%230A66C2" width="30" height="30" alt="LinkedIn"></a>&nbsp;&nbsp;&nbsp;
  <a href="mailto:aaditya.d.desai@gmail.com" title="Email"><img src="https://api.iconify.design/simple-icons/gmail.svg?color=%23EA4335" width="30" height="30" alt="Email"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://aadityad.dev/Aaditya_Desai_Portfolio_Resume.pdf" title="Résumé"><img src="https://api.iconify.design/mdi/file-pdf-box.svg?color=%23EC1C24" width="30" height="30" alt="Résumé"></a>
</p>

I build software that has to work within real constraints: limited compute, unreliable connectivity, tight latency budgets, or a bounded context window. I like working through the full system, from the model or protocol to the application around it.

## Selected work

### 01 / [Accordion](https://github.com/a-Fig/accordion) · [Live site](https://get-accordion.dev)

**The Problem:** Long coding sessions eventually fill an agent's context window. The usual fix is to compress everything into one summary, which can remove details the agent needs later.

**The Solution:** Accordion treats the context window as reversible blocks that can be folded, unfolded, and pinned. I worked on the keyword, bi-encoder, and cross-encoder relevance pipeline. Our team built it at the 2026 UC Berkeley AI Hackathon and won The Token Company sponsor track.

<p>
  <strong>Tech Stack:</strong>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="28" alt="Python" title="Python">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" height="28" alt="TypeScript" title="TypeScript">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/svelte/svelte-original.svg" height="28" alt="Svelte" title="Svelte">&nbsp;
  <img src="https://api.iconify.design/simple-icons/huggingface.svg?color=%23FFD21E" height="28" alt="Hugging Face Transformers" title="Hugging Face Transformers">
</p>

---

### 02 / [GazeBoard](https://github.com/aadityad12/GazeBoard)

**The Problem:** A gaze-based communication aid should not require dedicated hardware or send continuous face video to a server.

**The Solution:** GazeBoard turns an Android phone into an offline gaze-to-speech device. I built the pipeline from CameraX capture through face detection, LiteRT inference, four-point calibration, dwell selection, and text-to-speech. The app declares no network permission and targets the Qualcomm Hexagon NPU.

<p>
  <strong>Tech Stack:</strong>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kotlin/kotlin-original.svg" height="28" alt="Kotlin" title="Kotlin">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/android/android-original.svg" height="28" alt="Android" title="Android">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jetpackcompose/jetpackcompose-original.svg" height="28" alt="Jetpack Compose" title="Jetpack Compose">&nbsp;
  <img src="https://api.iconify.design/mdi/memory.svg?color=%23EF5B2A" height="28" alt="LiteRT on Qualcomm NPU" title="LiteRT on Qualcomm NPU">
</p>

---

### 03 / [ApexTracker](https://github.com/aadityad12/Apex-Tracker)

**The Problem:** Budgets, study time, reminders, notes, screen time, and reading lists often end up in separate apps, each with its own account and cloud dependency.

**The Solution:** ApexTracker puts those workflows in one offline-first Android app that I use every day. Room remains the source of truth, while sign-in adds optional Firestore sync. The codebase includes encrypted storage, biometric access, reboot-safe alarms, widgets, schema migrations, and automated tests.

<p>
  <strong>Tech Stack:</strong>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kotlin/kotlin-original.svg" height="28" alt="Kotlin" title="Kotlin">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jetpackcompose/jetpackcompose-original.svg" height="28" alt="Jetpack Compose" title="Jetpack Compose">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg" height="28" alt="SQLite" title="Room and SQLite">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/firebase/firebase-original.svg" height="28" alt="Firebase" title="Firebase and Firestore">
</p>

---

### 04 / [Temper](https://github.com/aadityad12/Temper)

**The Problem:** When an AI agent performs poorly, it is hard to tell whether the model is the problem or whether its prompt, tools, or skill files are getting in the way.

**The Solution:** Temper compares an agent environment with a bare-model baseline on the same tasks. It finds regressions, generates targeted replacement files, and runs the affected checks again. I built the local evaluation harness, FastAPI service, patch loop, and deterministic integration path.

<p>
  <strong>Tech Stack:</strong>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="28" alt="Python" title="Python">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" height="28" alt="FastAPI" title="FastAPI">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" height="28" alt="React" title="React">&nbsp;
  <img src="https://api.iconify.design/vscode-icons/file-type-json.svg" height="28" alt="JSON Schema" title="JSON Schema">
</p>

---

### 05 / [Echo](https://github.com/aadityad12/Echo)

**The Problem:** Emergency alerts depend on the same internet and cellular infrastructure that may fail during a disaster.

**The Solution:** Echo is a prototype for receiving, storing, and relaying alerts between nearby phones over Bluetooth Low Energy. It uses a custom chunked-transfer protocol with native Android and iOS GATT servers, plus Raspberry Pi relay tools and offline translation for received alerts.

<p>
  <strong>Tech Stack:</strong>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flutter/flutter-original.svg" height="28" alt="Flutter" title="Flutter">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/dart/dart-original.svg" height="28" alt="Dart" title="Dart">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/kotlin/kotlin-original.svg" height="28" alt="Kotlin" title="Kotlin">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/swift/swift-original.svg" height="28" alt="Swift" title="Swift">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/raspberrypi/raspberrypi-original.svg" height="28" alt="Raspberry Pi" title="Raspberry Pi">
</p>

---

### 06 / [Clear Dispatch](https://github.com/aadityad12/Clear-Dispatch)

**The Problem:** During call surges, dispatchers have to triage incidents and assign resources quickly. In a high-stakes workflow, automation also needs clear human control.

**The Solution:** Clear Dispatch is a local emergency-dispatch simulation with intake, triage, routing, and briefing stages. Heavy resources remain blocked until a dispatcher approves them, while a WebSocket dashboard streams calls, assignments, holds, and audit events in real time.

<p>
  <strong>Tech Stack:</strong>&nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="28" alt="Python" title="Python">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg" height="28" alt="FastAPI" title="FastAPI">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" height="28" alt="React" title="React">&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" height="28" alt="TypeScript" title="TypeScript">&nbsp;
  <img src="https://api.iconify.design/mdi/lan-connect.svg?color=%2357637A" height="28" alt="WebSockets" title="WebSockets">
</p>
