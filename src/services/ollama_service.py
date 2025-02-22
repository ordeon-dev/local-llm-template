import httpx
import os

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

async def query_ollama(prompt: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{OLLAMA_HOST}/api/generate", json={"model": "llama3", "prompt": prompt})
        return response.json().get("response", "Erro ao obter resposta")