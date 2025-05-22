import logging
import telebot  # <== Добавь этот импорт
from flask import Flask, request
from init_bot import bot, register_handlers
from config import TOKEN

# Настройка логирования
telebot.logger.setLevel(logging.DEBUG)

# Flask-приложение
app = Flask(__name__)

# Регистрируем все хэндлеры
register_handlers()

# Вебхук-роут
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    print(f"Raw update: {json_str}")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

# Страница-заглушка
@app.route('/')
def index():
    return "JarvisXBot работает."

# Устанавливаем Webhook (после всего остального)
bot.remove_webhook()
bot.set_webhook(url=f"https://jarvisx-web.onrender.com/{TOKEN}")
