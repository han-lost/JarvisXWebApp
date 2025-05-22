from flask import Flask, request
import telebot
import os
import logging

TOKEN = "8051188881:AAHbGSaljlNC5YASV5Jj3BheqEi27PaL0EU"
WEBHOOK_URL = f"https://jarvisx-web.onrender.com/{TOKEN}"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    try:
        update = telebot.types.Update.de_json(request.data.decode("utf-8"))
        bot.process_new_updates([update])
    except Exception as e:
        logging.error(f"Ошибка в webhook: {e}")
    return "OK", 200

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Бот работает!")

# Установка webhook происходит при импорте
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

