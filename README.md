# Aaditya Desai

I'm a Computer Engineering student at San José State University, graduating in May 2028. I build software that has to work within real constraints: limited compute, unreliable connectivity, tight latency budgets, or a bounded context window. I like working through the full system, from the model or protocol to the application around it.

**Seeking Summer 2027 software engineering internships.**

<p>
  <a href="https://aadityad.dev" title="Portfolio"><img src="https://api.iconify.design/mdi/web.svg?color=%23006CFF" width="28" height="28" alt="Portfolio"></a>&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/aaditya-desai-12d" title="LinkedIn"><img src="https://api.iconify.design/simple-icons/linkedin.svg?color=%230A66C2" width="28" height="28" alt="LinkedIn"></a>&nbsp;&nbsp;
  <a href="mailto:aaditya.d.desai@gmail.com" title="Email"><img src="https://api.iconify.design/simple-icons/gmail.svg?color=%23EA4335" width="28" height="28" alt="Email"></a>&nbsp;&nbsp;
  <a href="https://aadityad.dev/Aaditya_Desai_Portfolio_Resume.pdf" title="Résumé"><img src="https://api.iconify.design/mdi/file-pdf-box.svg?color=%23EC1C24" width="28" height="28" alt="Résumé"></a>
</p>

## Selected work

### [Accordion](https://github.com/a-Fig/accordion) · [Live site](https://get-accordion.dev)

Reversible context management for long-running coding agents. Instead of replacing an entire conversation with a lossy summary, Accordion can fold, unfold, and pin individual blocks as the context budget changes.

I worked on its three-stage relevance pipeline, which combines keyword scoring, bi-encoder retrieval, and cross-encoder reranking. We built it at the 2026 UC Berkeley AI Hackathon, where it won The Token Company sponsor track.

<sub>Python · TypeScript · Hugging Face Transformers · SvelteKit</sub>

---

### [GazeBoard](https://github.com/aadityad12/GazeBoard)

An Android prototype that lets people select and speak phrases using their eyes. Camera data stays on the phone, and the app declares no network permission.

I built the pipeline from CameraX capture through face detection, LiteRT inference, four-point calibration, dwell selection, and text-to-speech. The inference path targets the Qualcomm Hexagon NPU through LiteRT's `CompiledModel` API.

<sub>Kotlin · Jetpack Compose · CameraX · LiteRT · ML Kit</sub>

---

### [ApexTracker](https://github.com/aadityad12/Apex-Tracker)

An offline-first Android app I use for budgeting, study tracking, reminders, notes, screen time, and research papers. Room is the source of truth, while sign-in adds optional Firestore sync.

The codebase includes encrypted local storage, biometric access, reboot-safe alarms, home-screen widgets, schema migrations, and automated tests. It has grown from a habit-building project into software I use every day.

<sub>Kotlin · Jetpack Compose · Room · SQLite · Firebase · WorkManager</sub>

---

### [Temper](https://github.com/aadityad12/Temper)

A prototype for evaluating the environment around an AI agent, including its system prompt, tools, and skill files, against a bare-model baseline on the same tasks.

I built the local evaluation harness and FastAPI service, along with the patch and re-evaluation loop. The repository includes a deterministic integration path so the full workflow can be tested without model API keys.

<sub>Python · FastAPI · JSON Schema · Server-Sent Events · LLM evaluation</sub>

More projects and longer writeups are available on [aadityad.dev](https://aadityad.dev).
