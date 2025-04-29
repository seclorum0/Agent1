import subprocess

def ask_mistral(prompt, model="mistral:7b-instruct"):
    process = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return process.stdout.strip()

class Agent:
    def __init__(self, name, model="mistral:7b-instruct"):
        self.name = name
        self.model = model

    def respond(self, prompt):
        return ask_mistral(prompt, self.model)
