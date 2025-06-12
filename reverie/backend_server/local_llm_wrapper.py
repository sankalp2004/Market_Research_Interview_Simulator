import requests
import json
import time
import re

class LocalLLMWrapper:
    def __init__(self, model_name="phi3.5", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"
        
    def generate_response(self, prompt, max_tokens=512, temperature=0.7):
        """Generate response using local Ollama model"""
        data = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
                "top_p": 0.9,
                "stop": ["\n\n", "Human:", "Assistant:"]
            }
        }
        
        try:
            response = requests.post(self.api_url, json=data, timeout=60)
            if response.status_code == 200:
                return response.json()["response"].strip()
            else:
                raise Exception(f"Ollama API error: {response.status_code}")
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Error: Unable to generate response"
    
    def extract_rating(self, response_text):
        """Extract numerical rating from response"""
        numbers = re.findall(r'\b([1-9]|10)\b', response_text)
        if numbers:
            return int(numbers[0])
        return 5  # Default rating
