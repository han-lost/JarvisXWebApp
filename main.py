import logging
telebot.logger.setLevel(logging.DEBUG)
from flask import Flask, request
import telebot
from config import TOKEN, ADMIN_ID, START_MESSAGE, LINK, PROMO

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_handler(message):
    print(">>> ОБРАБОТЧИК /start СРАБОТАЛ <<<")
    chat_id = message.chat.id
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Перейти на сайт", url=LINK))
    bot.send_message(chat_id, START_MESSAGE, reply_markup=markup)

@bot.message_handler(func=lambda msg: str(msg.chat.id) == ADMIN_ID and msg.text.startswith("/signal"))
def signal_handler(message):
    bot.send_message(message.chat.id, "Сигнал: X10 скоро!")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    print(f"Raw update: {json_str}")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return "JarvisXBot работает."

# Устанавливаем webhook
bot.remove_webhook()
bot.set_webhook(url=f"https://jarvisx-web.onrender.com/{TOKEN}")
