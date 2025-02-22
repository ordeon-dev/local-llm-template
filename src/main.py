from fastapi import FastAPI
from api.endpoints import router

app = FastAPI(title="Ollama API", description="API para interagir com o Ollama")

app.include_router(router)