from typing import *
import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
image_path = "./test.jpg"
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "you are a proffesional discrete math teacher and you are given a question to solve break it down into smaller problems and solve them one by one and explain the logic behind each step and give the final answer"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 4096
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())