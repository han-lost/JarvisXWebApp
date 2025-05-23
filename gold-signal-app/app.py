# app.py

from flask import Flask, request, jsonify, abort
from config import ADMIN_TOKEN
from logic.strategy_gold import generate_signal
from logic.strategy_legendary import legendary_strategy
from logic.data_provider import get_latest_history

app = Flask(__name__)

@app.route('/')
def index():
    return "Gold Signal App работает."

@app.route('/admin-signal')
def admin_signal():
    token = request.args.get("token")
    if token != ADMIN_TOKEN:
        abort(403)

    history = get_latest_history()
    signal = generate_signal(history)
    return jsonify({"signal": signal})

@app.route('/legendary')
def legendary():
    token = request.args.get("token")
    if token != ADMIN_TOKEN:
        abort(403)

    history = get_latest_history()
    result = legendary_strategy(history)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
