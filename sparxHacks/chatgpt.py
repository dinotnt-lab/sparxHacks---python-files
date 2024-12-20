import requests

api_key = "api-key"
url = "https://api.openai.com/v1/chat/completions"

def getAnswer(string):
    if api_key == "api-key":
        api_key = input("Please enter your OpenAI API key: ")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": r"Please extract the answer, and only the answer. There may be functions such as \frac{}{} or \sqrt{} or \pm, just make it readable without them."},
            {"role": "user", "content": string}
        ],
        "temperature": 0.7,
        "max_tokens": 256
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"].strip()