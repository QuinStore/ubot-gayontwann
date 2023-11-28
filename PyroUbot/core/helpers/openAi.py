import requests

from PyroUbot import OPENAI_KEY


class OpenAi:
    @staticmethod
    def ChatGPT(question):
        headers = {
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": question}],
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=data
        )
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"].strip()

    @staticmethod
    def ImageDalle(question):
        headers = {
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "prompt": question,
            "n": 1,
            "size": "1024x1024",
        }

        response = requests.post(
            "https://api.openai.com/v1/images/generations", headers=headers, json=data
        )
        response_data = response.json()
        return response_data["data"][0]["url"]

    @staticmethod
    def SpeechToText(file):
        headers = {
            "Authorization": f"Bearer {OPENAI_KEY}",
        }

        data = {
            "model": "whisper-1",
        }

        with open(file, "rb") as audio:
            files = {"file": audio}

            response = requests.post(
                "https://api.openai.com/v1/audio/transcriptions",
                headers=headers,
                data=data,
                files=files,
            )
            response_data = response.json()
            return response_data["text"]
