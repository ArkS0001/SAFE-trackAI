# import requests

# def query_ollama(prompt):
#     response = requests.post(
#         'http://localhost:11434/api/generate',
#         json={
#             'model': 'gemma3:1b',
#             'prompt': prompt,
#             'stream': False  # Set to True if you want streamed responses
#         }
#     )
#     result = response.json()
#     return result.get('response', '')

# if __name__ == "__main__":
#     prompt = "Explain quantum physics"
#     answer = query_ollama(prompt)
#     print("Gemma says:", answer)



import requests

def query_ollama(prompt):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'gemma3:1b',
            'prompt': prompt,
            'stream': False
        }
    )
    result = response.json()
    return result.get('response', '')

def save_to_markdown(prompt, response, filename="ollama_output.md"):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("## Prompt\n")
        f.write(f"{prompt}\n\n")
        f.write("## Response\n")
        f.write(f"{response}\n\n")
        f.write("---\n\n")

if __name__ == "__main__":
    prompt = "Explain quantum physics like I'm five."
    answer = query_ollama(prompt)
    print("Gemma says:", answer)
    save_to_markdown(prompt, answer)
