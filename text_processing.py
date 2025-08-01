# text_processing.py

import ollama
from platform_navigation import navigate_to_platform

def process_input(text):
    desired_model = 'llama3.2:3b'
    
    prompt = f"""
You are an AI that processes food ordering commands.
Extract and return the following two things from the user's command:
1. The name of the pizza
2. The platform (like Zomato, Swiggy, Domino's, Pizza Hut)

Return output in the exact format:
Pizza: <pizza name>
Platform: <platform name>

User said: "{text}"
"""

    response = ollama.chat(model=desired_model, messages=[{
        'role': 'user',
        'content': prompt.strip(),
    }])

    result = response['message']['content'].strip()
    print("\n[LLAMA Output]\n" + result)

    # Extract pizza and platform from response
    pizza = ""
    platform = ""
    for line in result.splitlines():
        if line.lower().startswith("pizza:"):
            pizza = line.split(":", 1)[1].strip()
        elif line.lower().startswith("platform:"):
            platform = line.split(":", 1)[1].strip()

    if pizza and platform:
        navigate_to_platform(pizza, platform)
    else:
        print("Could not extract pizza or platform from response.")
