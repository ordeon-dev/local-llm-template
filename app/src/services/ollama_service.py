import httpx
import os
import json
from typing import AsyncGenerator
from config import OLLAMA_HOST, OLLAMA_MODEL
from functools import lru_cache

@lru_cache(maxsize=128)
async def query_ollama(prompt: str) -> str:
    async with httpx.AsyncClient(timeout=300) as client:
        payload = {
            "model": OLLAMA_MODEL,
            "options": {
                "temperature": 0.1, 
                "num_ctx": 512 
            },
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
        response = await client.post(f"{OLLAMA_HOST}/api/generate", json=payload)
        print(response)
        response_data = response.json()
        return response_data.get("message", {}).get("content", "Erro ao obter resposta")