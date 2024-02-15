from typing import Dict
import base64
import requests
import streamlit as st
import os
import json
from dotenv import load_dotenv
# Function to encode the image
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to process the image
def process_image(image_path: str) -> Dict:
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
                "text": "you are a professional discrete math teacher and you are given a question to solve break it down into smaller problems and solve them one by one and explain the logic behind each step and give the final answer in markdown format for tables and titles and math sympols use latex"
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
    text_response = response.json()["choices"][0]["message"]["content"]
    return text_response

# Function to save the uploaded file
def save_uploadedfile(uploadedfile):
    temp_dir = "tempDir"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    file_path = os.path.join(temp_dir, uploadedfile.name)
    with open(file_path, "wb") as f:
        f.write(uploadedfile.getbuffer())
    return file_path

# API Key (should be kept secure)

# Streamlit UI
st.title("Drop here your discrete math problem and get the answer")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])
if uploaded_file is not None:
    st.success("File Uploaded Successfully")
    image_path = save_uploadedfile(uploaded_file)
    st.write("Saved file path:", image_path)  # Debugging statement
    if st.button('Process'):
        result = process_image(image_path)
        st.markdown(result)
