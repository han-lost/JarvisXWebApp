import telebot
from config import TELEGRAM_API_KEY, PARTNER_LINK
from flask import Flask, request

bot = telebot.TeleBot(TELEGRAM_API_KEY)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "Добро пожаловать в LuckyJet сигнал бот!\n\n"
        f"Перейдите по ссылке: {PARTNER_LINK}\n"
        "Введите промокод при регистрации.\n"
        "Для доступа к сигналам посетите веб-приложение."
    )
    bot.send_message(message.chat.id, text)

@app.route(f"/{TELEGRAM_API_KEY}", methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

def start_bot():
    bot.remove_webhook()
    bot.set_webhook(url="https://your-render-url.com/" + TELEGRAM_API_KEY)
