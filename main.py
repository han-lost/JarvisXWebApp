from flask import Flask, request
import telebot
import logging
import os

TOKEN = "8051188881:AAHbGSaljlNC5YASV5Jj3BheqEi27PaL0EU"
WEBHOOK_URL = f"https://jarvisx-web.onrender.com/{TOKEN}"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Логирование
logging.basicConfig(level=logging.INFO)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    try:
        json_str = request.get_data().decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
    except Exception as e:
        logging.error(f"Ошибка в webhook: {e}")
    return "OK", 200

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Бот работает! Вы нажали /start.")

# Установка webhook при старте
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
