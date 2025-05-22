import os
import telebot
from flask import Flask, request
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Конфигурация
TOKEN = "8051188881:AAHbGSaljlNC5YASV5Jj3BheqEi27PaL0EU"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Обработка webhook от Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    try:
        json_str = request.get_data().decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
    except Exception as e:
        logging.exception("Ошибка в webhook:")
    return "OK", 200

# Обработка команды /start
@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Бот работает.")

# Установка webhook при запуске
@app.before_first_request
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://jarvisx-web.onrender.com/{TOKEN}")
    logging.info("Webhook установлен.")

# Запуск Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
