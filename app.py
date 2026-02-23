from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "ok", 200

@app.post("/irca")
def irca():
    data = request.json
    print(data)
    return jsonify({"ok": True})

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
