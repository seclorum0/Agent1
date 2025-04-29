# 🦰 Agent1 — Autonomous AI Debate System

Welcome to **Agent1**,  
an experimental AI debate simulator where two autonomous agents, **Alpha0** and **Beta1**, battle over scientific topics — logically, critically, and *sometimes savagely* 🍊.  
Powered by **local LLMs** via **Ollama** and lightweight Python code, Agent1 brings machine discourse to life — right on your CPU.

---

## ✨ What is Agent1?

Agent1 is a **self-contained debate engine** featuring:
- Two AI agents with **contrasting roles**:  
  - **Alpha0** → *the researcher*, logical and supportive.  
  - **Beta1** → *the skeptic*, critical and sharp.
- Turn-based discussion on any scientific or technological topic.
- **Fully local** execution with **Mistral 7B Instruct** model (via Ollama).
- **Automatic saving** of debate transcripts for review or study.
- **Simple**, **extensible**, and **no heavy dependencies**.

---

## 🚀 Quickstart Guide

### 📋 Requirements
- Python 3.8+ installed
- Ollama installed (https://ollama.com)
- Mistral model downloaded:
  ```bash
  ollama run mistral:7b-instruct
  ```

### 📦 Installation
Clone or download this repository to your machine:
```bash
git clone https://github.com/yourusername/Agent1.git
cd Agent1
```

(No external Python packages needed. Clean and simple.)

### ▶️ How to Run
Execute the debate engine:
```bash
python main.py
```
- You will be prompted to enter a debate topic.
- Watch Alpha0 and Beta1 exchange arguments.
- After the debate (default: 5 turns), a transcript will be saved under `/transcript/`.

---

## 🧹 Project Structure

```
Agent1/
├── agents.py      # Defines the AI agents and communication with Ollama
├── main.py        # Main debate loop and conversation management
├── prompt.py      # English prompts (Alpha0 and Beta1)
├── prompts.py     # Indonesian prompts (optional)
├── README.md      # This file!
├── LICENSE        # License file (MIT)
├── .gitignore     # Ignored files/folders (like __pycache__, transcript/)
└── transcript/    # Where saved debates will be stored
```

---

## 🦰 Agent Roles

| Agent    | Personality & Goal | Language | Model         |
|:---------|:-------------------|:---------|:--------------|
| **Alpha0** | Calm, logical, scientific | English (prompt.py) | mistral:7b-instruct |
| **Beta1**  | Critical, skeptical, analytical | English (prompt.py) | mistral:7b-instruct |

> 🔹 If you want Indonesian debates, switch to using `prompts.py` easily!

---

## 💡 Example Topics You Can Try
- "Artificial intelligence will outperform humans in creativity by 2035."
- "Colonizing Mars is a necessary step for human survival."
- "Quantum computing will disrupt cybersecurity within a decade."
- "The benefits of gene editing outweigh the ethical risks."

(Or input your own crazy debate topics — unleash your inner mad scientist.)

---

## 🛠️ Customization

Want longer debates?  
In `main.py`, you can adjust:
```python
max_turns = 5
```
to any number you like!

Want different models?  
Modify `model="mistral:7b-instruct"` when initializing the agents.

Want different styles of argumentation?  
Tweak the prompt templates in `prompt.py` or `prompts.py`.

Agent1 is designed to be **hackable and expandable** for your experiments.

---

## 📄 License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgements

Built with ❤️ and curiosity about how machines might argue when given a stage.

Special thanks to:
- **Ollama Team** for making local LLMs accessible.
- **Mistral AI** for the wonderful open model.

---

# 🚀 Let's see what happens when machines debate!
