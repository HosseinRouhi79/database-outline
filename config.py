import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_NAME = os.environ.get("MODEL_NAME", "qwen2.5:7b")
    OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://172.16.20.77:11434")
    GO_SERVICE_URL = os.environ.get("GO_SERVICE_URL", "http://localhost:8080/api/execute")
    PORT = int(os.environ.get("PORT", 5001))
