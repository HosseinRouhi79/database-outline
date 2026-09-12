from flask import current_app as app, jsonify, request, render_template
from .core.extract import extract_intent_json
import traceback
import requests
from config import Config

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/query", methods=["POST"])
def api_query():
    body = request.get_json(force=True)
    text = body.get("text", "").strip()
    
    if not text:
        return jsonify({"success": False, "error": "No text provided"}), 400

    try:
        payload = extract_intent_json(text, Config.MODEL_NAME)
        payload_dict = payload.model_dump()
        
        # Forward to Go service
        db_results = []
        try:
            go_resp = requests.post(Config.GO_SERVICE_URL, json=payload_dict)
            if go_resp.status_code == 200:
                resp_json = go_resp.json()
                if resp_json.get("success"):
                    db_results = resp_json.get("data", [])
        except Exception as go_err:
            print(f"Error calling Go service: {go_err}")

        return jsonify({
            "success": True,
            "payload": payload_dict,
            "db_results": db_results
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)}), 500
