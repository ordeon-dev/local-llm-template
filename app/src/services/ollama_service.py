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
            "model": "phi4",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
        print(payload)
        response = await client.post(f"{OLLAMA_HOST}/api/chat", json=payload)
        print(response)
        response_data = response.json()
        return response_data.get("message", {}).get("content", "Erro ao obter resposta")