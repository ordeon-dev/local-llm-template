#!/bin/bash

./bin/ollama serve &

pid=$!

sleep 5

MODEL=${OLLAMA_MODEL:-phi4}
echo "Pulling model: $MODEL"
ollama pull $MODEL

wait $pid