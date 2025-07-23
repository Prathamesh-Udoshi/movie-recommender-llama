# 🎬 Local Movie Recommender using LLaMA 3.2 (via Ollama)

This is a minimal Python project that gives you **movie recommendations** based on your preferred **language** and **genre**, using a locally running **LLaMA 3.2 model via Ollama** — all on your own machine.  
No API keys. No cloud. Fully private.

---

## 🧠 What It Does

- Asks for your input (e.g., “Japanese Thriller”)
- Sends a custom prompt to the local LLaMA 3.2 model
- Receives a list of **10 movie suggestions** with short summaries
- Displays them as a clean **Markdown table** (best in Jupyter or terminal Markdown viewers)

---

## ✅ Why Local LLMs?

Running models **locally** has its perks:

- 🔐 **No API key needed** — fully self-contained
- 📴 **Works offline** — no internet = no problem
- 👁️ **Privacy-first** — your inputs stay on your machine
- 💸 **Free & Open** — no rate limits, no cost per request

This small project shows how powerful local models can be, even on limited hardware.

---

## ⚠️ Limitations of Local CPU-based LLMs

While it's cool to run LLMs locally, especially using Ollama + CPU:

- 🐢 Performance may be slow (especially first runs)
- 💾 8GB RAM machines can’t handle huge models like `llama3:70b`  
- 🧠 Generation size needs to be controlled (shorter prompts are better)

For lightweight, structured output like this movie recommendation — it's perfect! But don’t expect GPT-4-level reasoning on a CPU 😅

---

