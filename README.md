# Multi-LLM Evaluation Pipeline

This project shows how two Large Language Models (LLMs) can work together to answer and review questions.

One model generates an answer for a given prompt.  
A second model checks that answer, finds mistakes or missing details, and gives a better or corrected response.

The goal is to understand how LLMs can be used not only to generate text, but also to evaluate and improve each other’s output.

---

## How It Works

1. Prompts are read from a CSV file  
2. Llama 3 generates an initial answer  
3. Llama 3.1 reviews the answer and suggests improvements  
4. The results are saved to a new CSV file  

---

## Technologies Used

- Python  
- Ollama (for running LLMs locally)  
- Pandas (for handling CSV files)  

---

## Project Structure

```text
multi-llm-evaluation-pipeline/
│
├── run_pipeline.py
├── prompts.csv
├── results.csv
├── README.md
├── .gitignore
└── LICENSE
