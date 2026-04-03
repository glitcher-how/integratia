from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/")
def root():
    return jsonify({"status": "ok", "service": "fake-gcs"})

@app.route("/<path:path>", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def catch_all(path):
    data = request.get_json(silent=True)
    return jsonify({
        "ok": True,
        "path": path,
        "method": request.method,
        "data": data,
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8091)
