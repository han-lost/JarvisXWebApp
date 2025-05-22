from flask import Flask, request, render_template
import telebot
import logging

# Логирование
logging.basicConfig(level=logging.INFO)

# Telegram токен
TOKEN = "8051188881:AAHbGSaljlNC5YASV5Jj3BheqEi27PaL0EU"
bot = telebot.TeleBot(TOKEN)

# Flask
app = Flask(__name__)
admin_password = "jarvispass"
latest_signal = "Нажми кнопку, чтобы получить сигнал."

# Webhook URL
WEBHOOK_URL = f"https://jarvisx-web.onrender.com/{TOKEN}"

@app.route("/", methods=["GET", "POST"])
def index():
    global latest_signal
    if request.method == "POST":
        return render_template("index.html", signal=latest_signal)
    return render_template("index.html", signal=None)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    global latest_signal
    if request.method == "POST":
        if request.form.get("password") == admin_password:
            signal = request.form.get("signal")
            if signal:
                latest_signal = signal
            return render_template("admin.html", success=True, signal=latest_signal)
        else:
            return render_template("admin.html", error="Неверный пароль")
    return render_template("admin.html")

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    try:
        json_str = request.get_data().decode('UTF-8')
        logging.info(">> [Telegram] Update received")
        logging.info(json_str)
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
    except Exception as e:
        logging.error(f">> Ошибка обработки обновления: {e}")
    return "OK", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    logging.info(f">> Команда /start от {message.chat.id}")
    bot.send_message(message.chat.id, """
Приветствуем в JarvisXBot!

Сигналы по стратегиям Lucky Jet
Ссылка: https://goo.su/qnkvtL
Промокод: FXX86
""")

if __name__ == "__main__":
    # Раскомментировать для polling:
    # bot.remove_webhook()
    # bot.polling(none_stop=True)

    # Для webhook:
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host="0.0.0.0", port=10000)
