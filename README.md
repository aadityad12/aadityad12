# Hi, I'm Aaditya 👋

Computer Engineering student at San Jose State University (Dec 2027) building AI systems down to the hardware: on-device NPU inference, custom BLE wire protocols, and LLM agents and evals. I ship end-to-end deployments, not demo notebooks.

**Currently:** seeking internships in AI/ML engineering and edge AI / embedded systems.

## What I build

🧿 **[GazeBoard](https://github.com/aadityad12/GazeBoard)** · Lets ALS patients speak using only their eyes, on an off-the-shelf phone. Runs MediaPipe FaceMesh (478 landmarks) on the Qualcomm Hexagon NPU via the LiteRT CompiledModel API at ~8ms inference, fully offline, with a custom 4-point affine calibration engine. *Kotlin · LiteRT · CameraX*

🪗 **[Accordion](https://github.com/aadityad12/Accordion)** · Reversible context management for LLM coding agents: the whole context window as foldable blocks under a token budget. I built `the-conductor-v2`, a three-stage relevance pipeline (keyword → bi-encoder cosine → cross-encoder rerank) with self-calibrating fold targets, plus the live conductor activity dashboard. Won The Token Company's sponsor prize at the UC Berkeley AI Hackathon 2026. *TypeScript · Node.js · SvelteKit*

🌡️ **[Temper](https://github.com/aadityad12/Temper)** · Evaluates the environment around an LLM (system prompt, tools, skill files) instead of the model itself: scores a harness against a bare-model baseline across six dimensions, generates targeted patches, and re-evaluates to confirm they worked. I built the core eval engine end to end. *Python · FastAPI · Gemini*

🚒 **[Clear Dispatch](https://github.com/aadityad12/Clear-Dispatch)** · Four LLM agents behind a 911 dispatcher during wildfire call surges: triage, unit routing, and voice briefings, with the human always in control. Real-time WebSocket pipeline, zero polling. *Python · FastAPI · React · Claude*

📡 **[Echo](https://github.com/aadityad12/Echo)** · Emergency alerts that hop phone to phone with no internet or cell service. Custom GATT chunked-transfer protocol with native Kotlin and Swift implementations, gossip mesh with SHA-1 deduplication, Raspberry Pi relay nodes, and offline translation into 23 languages. *Flutter · Kotlin · Swift · BLE*

## Stack

**Core:** Python · C++ · Kotlin · TypeScript · x86 Assembly
**AI/ML:** LiteRT/TFLite · MediaPipe · scikit-learn · LLM agents & evals
**Systems:** BLE/GATT protocol design · on-device inference · FastAPI · WebSockets

## Reach me

📧 aaditya.d.desai@gmail.com · 💼 [LinkedIn](https://www.linkedin.com/in/aaditya-desai-12d)