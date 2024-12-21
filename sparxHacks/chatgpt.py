import requests
from tkinter import messagebox

api_key = ""
url = "https://api.openai.com/v1/chat/completions"

def detectKey():
    global api_key

    try:
        api_key = open("api_key.txt", "r").read().strip()
    except FileNotFoundError:
        api_key = "no_key"
        print("no api key file")

    if api_key == "no_key":
        messagebox.showerror("Error", "Please enter your OpenAI API key in the terminal.")
        api_key = input("Please enter your OpenAI API key: ")
        with open("api_key.txt", "w") as f:
            f.write(api_key)

def getAnswer(string):
    global api_key
    

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": r"Please extract the answer, and only the answer. No full stops at the end of the string either.There may be functions such as \frac{}{} or \sqrt{} or \pm, just make it readable without them."},
            {"role": "user", "content": string}
        ],
        "temperature": 0.7,
        "max_tokens": 256
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"].strip()