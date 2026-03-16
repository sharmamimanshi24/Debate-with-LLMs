# 🔁 Multi-LLM Evaluation Pipeline

> Two LLMs collaborate — one generates, one critiques — to produce better, self-reviewed AI responses.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLMs-black?style=flat)
![Llama](https://img.shields.io/badge/Llama-3%20%7C%203.1-purple?style=flat)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat)

---

## 📋 Table of Contents
- [About](#about)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 About

This project explores how two Large Language Models can work together in a **generate-then-review** pipeline.

Most AI systems use a single model to generate a response and call it done. This project takes a different approach — one model generates an answer, and a second model acts as a critic, finding mistakes, filling gaps, and producing an improved response.

The result is a lightweight, locally-run peer review system for LLM outputs — no API keys, no cloud costs, just two models keeping each other honest.

---

## ⚙️ How It Works

```
prompts.csv
    ↓
Llama 3 generates an initial answer
    ↓
Llama 3.1 reviews the answer
— finds mistakes
— identifies missing details
— suggests improvements
    ↓
results.csv (original prompt + answer + review + improved response)
```

![Pipeline Demo](https://github.com/user-attachments/assets/3e488d48-7b08-4f39-8aa6-3db34ca1a434)

---

## 🛠️ Installation

### Prerequisites
- Python 3.11+
- [Ollama](https://ollama.ai) installed locally
- Llama 3 and Llama 3.1 models pulled

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/sharmamimanshi24/LLM-Peer-Review-System.git
cd LLM-Peer-Review-System
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Pull the models via Ollama**
```bash
ollama pull llama3
ollama pull llama3.1
```

**4. Make sure Ollama is running**
```bash
ollama serve
```

---

## 🚀 Usage

**1. Add your prompts to `prompts.csv`:**
```csv
prompt
"What is machine learning?"
"Explain the difference between RAM and ROM."
"How does a neural network learn?"
```

**2. Run the pipeline:**
```bash
python run_pipeline.py
```

**3. Check `results.csv` for outputs:**
```csv
prompt, initial_answer, review, improved_answer
"What is machine learning?", "...", "...", "..."
```

---

## 📁 Project Structure

```
multi_llm/
│
├── run_pipeline.py     # Main pipeline — runs both models
├── prompts.csv         # Input prompts
├── results.csv         # Output with answers + reviews
├── requirements.txt    # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

---

## 📄 License

This project is licensed under the Apache 2.0 License. See [LICENSE](LICENSE) for details.

---

## 🆘 Support

- **Issues:** [GitHub Issues](https://github.com/sharmamimanshi24/LLM-Peer-Review-System/issues)
- **Email:** sharma.mimanshi24@gmail.com

---

## 👩‍💻 Authors & Acknowledgments

**Mimanshi Sharma**

[![GitHub](https://img.shields.io/badge/GitHub-sharmamimanshi24-181717?style=flat&logo=github)](https://github.com/sharmamimanshi24)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-mimanshi--sharma-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/mimanshi-sharma/)

**Acknowledgments:**
- [Ollama](https://ollama.ai) — for making local LLM inference simple
- [Meta Llama](https://llama.meta.com) — for the open source models

---

*Built with Ollama · Llama 3 & 3.1 · 2025*
