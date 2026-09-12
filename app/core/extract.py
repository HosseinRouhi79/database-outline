import os
import outlines
from pydantic import ValidationError
from .schema import QueryIntent
from .prompt import build_prompt
from config import Config

_loaded_models = {}

def get_model(model_name: str = Config.MODEL_NAME):
    if model_name not in _loaded_models:
        print(f"Loading model '{model_name}'...")
        ollama_url = Config.OLLAMA_URL
        import ollama
        host_url = ollama_url.replace("/v1", "").replace("/v1/", "")
        client = ollama.Client(host=host_url)
        model = outlines.models.from_ollama(client, model_name)
        _loaded_models[model_name] = model
        print(f"Model '{model_name}' ready.")
    return _loaded_models[model_name]

def extract_intent_json(text: str, model_name: str = Config.MODEL_NAME) -> QueryIntent:
    model = get_model(model_name)
    prompt = build_prompt(text)
    
    # We use num_predict for ollama
    kwargs = {"options": {"num_predict": 1024}}
    
    result = model(prompt, QueryIntent, **kwargs)
    payload = QueryIntent.model_validate_json(result)
    return payload

