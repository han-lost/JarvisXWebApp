from flask import Flask, request, jsonify, abort
from config import ADMIN_TOKEN  # Токен авторизации
from logic import strategy_gold  # Подключаем файл с логикой стратегии

app = Flask(__name__)  # Создаём веб-приложение

@app.route('/')
def index():
    return "Gold Signal App работает."

# Приватный маршрут — доступен только с правильным token
@app.route('/admin-signal')
def admin_signal():
    # Получаем параметр token из строки запроса (?token=...)
    token = request.args.get("token")

    # Если токен неверный — блокируем доступ
    if token != ADMIN_TOKEN:
        abort(403)  # HTTP 403 Forbidden — Доступ запрещён

    # Генерация сигнала через стратегию (заглушка пока)
    signal = strategy_gold.generate_signal()
    return jsonify({"signal": signal})  # Возвращаем в формате JSON

