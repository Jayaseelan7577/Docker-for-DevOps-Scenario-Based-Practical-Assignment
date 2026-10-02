from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Legacy Python App - APP_ENV={os.getenv('APP_ENV', 'development')}"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
