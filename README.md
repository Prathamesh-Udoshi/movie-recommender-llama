# 🎬 Local LLM-Based Movie Recommender (LLaMA 3 + Ollama)

This project is a simple Python-based movie recommender that uses a **local LLaMA 3.2 model via Ollama** to suggest **top-rated movies** based on your preferred **language** and **genre**. Instead of using any online API or cloud-based service, it prompts a locally running large language model (LLM) to generate a table of movie titles and short summaries.

💡 Example:  
You input `"Language: Hindi"` and `"Genre: Thriller"` — the model responds with a Markdown table listing relevant movie recommendations like *Cure*, *Audition*, etc., with short plot summaries.

---

## ✅ Advantages of Using a Local LLM

- **No API keys or tokens required** – completely self-contained
- **Data stays on your machine** – nothing is sent to the cloud
- **Offline capability** – works without internet access
- **Customizable prompts** – full control over interaction style
- **No rate limits or costs** – run it as much as you want

---

## ⚠️ Limitations

- 🐌 **Slower inference** compared to cloud models (especially on low-spec machines)
- 💻 **High RAM/CPU usage** – requires decent hardware to run smoothly
- 📦 **Large model size** – downloads of 3–8 GB are common
- 📅 **No real-time knowledge** – model is only trained on static data

---

## 🤯 Why It’s Cool

It’s amazing how a few gigabytes of model weights can generate intelligent and personalized recommendations — without any internet connection. Your laptop becomes the AI.

This project is a small example of how powerful and private local LLMs can be for building intelligent tools.
