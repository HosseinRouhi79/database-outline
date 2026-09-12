# Database Extraction Service

A Flask-based web service for natural language database querying and intent extraction. This tool interprets user text in Persian (Farsi) and maps it to a structured JSON intent for database execution against an antivirus management platform.

## Features
- **Natural Language Intent Extraction:** Uses LLMs via Ollama (`qwen2.5:7b` by default).
- **Structured JSON Output:** Extracts target tables, fields, and logical operators for use by downstream services.
- **Go Service Integration:** Forwards validated queries to a backend Go execution service.
- **Web UI:** Provides an interactive frontend for querying.

## Project Structure
- `app/` - Core application logic including prompts, schema definitions, and LLM integrations.
- `app/static/` - Frontend Javascript and CSS.
- `app/templates/` - HTML templates.
- `config.py` - Application configurations (Model name, Ollama URL, Go Service URL).
- `run.py` - Entry point to start the Flask server.

## Setup

1. Make sure Python is installed and requirements are satisfied (Flask, pydantic, outlines, ollama, requests, python-dotenv).
2. Create a `.env` file if you want to override default configurations.
3. Start the application:
   ```bash
   python run.py
   ```

## Environment Variables
- `MODEL_NAME`: The Ollama model to use. (Default: `qwen2.5:7b`)
- `OLLAMA_URL`: URL to the Ollama server. (Default: `http://172.16.20.77:11434`)
- `GO_SERVICE_URL`: Downstream API endpoint. (Default: `http://localhost:8080/api/execute`)
- `PORT`: Port the Flask server will listen on. (Default: `5001`)
