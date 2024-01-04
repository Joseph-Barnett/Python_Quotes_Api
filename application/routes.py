from application import app
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome to the best quoutes api ever made",
        "description": "Quotes API",
        "endpoints": [
            "GET /",
            "GET /quotes",
            "GET /quotes/<int:id>",
            "POST /quotes",
            "PATCH /quotes/<int:id>",
            "DELETE /quotes/<int:id>"
        ]
    }), 200
