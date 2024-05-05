from typing import Final
import requests
import json
from app.config import OPEN_AI_KEY
from telegram import Update
from telegram.ext import ContextTypes


def translate_message(text: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_KEY}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful translator assistant who translate english crypto information to chinese version."
            },
            {
                "role": "user",
                "content": f"{text}"
            }
        ]
    }
    print("Starting to translate it....")
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Response from OpenAI:", response.json())
        print('\n')
        return response.json()['choices'][0]['message']['content']
    else:
        print("Error:", response.status_code, response.text)
        return "Error getting response from OPENAI"

