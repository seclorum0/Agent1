from agents import Agent
from prompts import get_alpha0_prompt, get_beta1_prompt
from datetime import datetime
import os

def save_transcript(topic, conversation):
    os.makedirs("transcript", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcript/debate_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"TOPIK: {topic}\n\n")
        for line in conversation:
            file.write(line + "\n")
    print(f"\n📄 Transkrip disimpan ke: {filename}")

def main():
    topic = input("Masukkan topik debat: ")

    alpha0 = Agent("Alpha0")
    beta1 = Agent("Beta1")

    conversation = []

    # Alpha0 memulai percakapan
    prompt_alpha = get_alpha0_prompt(topic)
    response_alpha = alpha0.respond(prompt_alpha)
    conversation.append(f"Alpha0:\n{response_alpha}\n")
    print(f"\nAlpha0:\n{response_alpha}\n")

    max_turns = 5  
    current_turn = 1
    last_response = response_alpha

    while current_turn < max_turns:
        if current_turn % 2 == 1:
            # Giliran Beta1
            prompt_beta = get_beta1_prompt(last_response)
            response_beta = beta1.respond(prompt_beta)
            conversation.append(f"Beta1:\n{response_beta}\n")
            print(f"Beta1:\n{response_beta}\n")
            last_response = response_beta
        else:
            # Giliran Alpha0
            prompt_alpha = get_alpha0_prompt(last_response)
            response_alpha = alpha0.respond(prompt_alpha)
            conversation.append(f"Alpha0:\n{response_alpha}\n")
            print(f"Alpha0:\n{response_alpha}\n")
            last_response = response_alpha

        current_turn += 1

    save_transcript(topic, conversation)

if __name__ == "__main__":
    main()
