
from ollama import chat

reponse = chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "Bonjour, comment vas-tu ?"
        }
    ]
)

print(reponse["message"]["content"])
