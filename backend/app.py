from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask backend is running "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
)

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/messages")
def messages():
    data = Message.query.all()
    return jsonify([{"id": m.id, "text": m.text} for m in data])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
