#!/usr/bin/env python3
"""
Simple LLM inference server using Ollama
"""
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "model": "llama3.1-cpu"})

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt', 'Hello!')
    # Simulate inference for demo
    response = {
        "model": "llama3.1-cpu",
        "prompt": prompt,
        "response": f"Response to: {prompt}",
        "tokens": len(prompt.split()) * 5
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
