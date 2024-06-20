import requests
from app.config.config import OPEN_AI_KEY
from app.config.config import channels


def translate_message(text: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_KEY}"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": f"You are a helpful translator assistant who translate english crypto information to "
                           f"nicely formatted chinese post. Please "
                           f"rephrase the sentences to make them exciting and fun. Please do not add any additional phrases "
                           f"around the link on the last part. Please exclude sentences which "
                           f"contains words similar to any of the words in this list {channels} "
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
        return ""
