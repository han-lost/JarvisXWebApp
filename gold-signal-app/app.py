from flask import Flask, request, jsonify, abort
from config import ADMIN_TOKEN
from logic import strategy_gold
from logic.strategy_legendary import legendary_strategy  # Добавляем здесь

app = Flask(__name__)

@app.route('/')
def index():
    return "Gold Signal App работает."

@app.route('/admin-signal')
def admin_signal():
    token = request.args.get("token")
    if token != ADMIN_TOKEN:
        abort(403)
    signal = strategy_gold.generate_signal()
    return jsonify({"signal": signal})

# Новый маршрут для Легендарной стратегии
@app.route('/legendary')
def legendary():
    token = request.args.get("token")
    if token != ADMIN_TOKEN:
        abort(403)

    # Заглушка: пример истории коэффициентов
    history = [1.01, 1.25, 2.0, 6.5, 1.4, 1.35]
    result = legendary_strategy(history)
    return jsonify(result)
