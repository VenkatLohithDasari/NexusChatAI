import os
import requests


class TogetherAI:
    def __init__(self, api_key):
        # Ensure this matches your .env file
        self.api_key = api_key
        self.endpoint = "https://api.together.xyz/v1/completions"

    def generate_response(self, prompt, config):
        headers = {"accept": "application/json",
                   "content-type": "application/json",
                   "authorization": f"Bearer {self.api_key}"}
        data = {
            "prompt": prompt,
            "model": config["model"],
            "max_tokens": config["max_tokens"],
            "temperature": config["temperature"],
            "top_p": config["top_p"],
            "top_k": config["top_k"],
            "repetition_penalty": config["repetition_penalty"],
            # Default stop token if not in config
            "stop": config.get("stop", "<|eot_id|>")
        }
        response = requests.post(self.endpoint, headers=headers, json=data)
        response.raise_for_status()
        print(response.text)
        return response.json()["choices"][0]["text"]
