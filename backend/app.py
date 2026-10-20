from flask import Flask, request, jsonify
from flask_cors import CORS
from models import (
    init_db,
    get_all_transactions,
    add_transaction,
    update_transaction,
    delete_transaction
)

app = Flask(__name__)
CORS(app)

# Initialize database when server starts
init_db()

@app.route("/transactions", methods=["GET"])
def get_transactions():
    return jsonify(get_all_transactions())

@app.route("/transactions", methods=["POST"])
def create_transaction():
    data = request.json
    add_transaction(data)
    return jsonify({"message": "Transaction added"}), 201

@app.route("/transactions/<int:id>", methods=["PUT"])
def edit_transaction(id):
    data = request.json
    update_transaction(id, data)
    return jsonify({"message": "Transaction updated"})

@app.route("/transactions/<int:id>", methods=["DELETE"])
def remove_transaction(id):
    delete_transaction(id)
    return jsonify({"message": "Transaction deleted"})

if __name__ == "__main__":
    app.run(debug=True)
