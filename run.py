from app import create_app
from config import Config

app = create_app()

if __name__ == "__main__":
    port = Config.PORT
    print(f"Starting Database Extraction Server on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
