from flask import Flask, request, render_template
import telebot
import logging
import os

# === Настройка логов ===
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/jarvis.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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
        logging.info(">> [WEB] Пользователь нажал кнопку на главной")
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
                logging.info(f">> [ADMIN] Обновлён сигнал: {signal}")
            return render_template("admin.html", success=True, signal=latest_signal)
        else:
            logging.warning(">> [ADMIN] Неверный пароль")
            return render_template("admin.html", error="Неверный пароль")
    return render_template("admin.html")

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    try:
        json_str = request.get_data().decode('UTF-8')
        logging.info(">> [Telegram] Обновление получено")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
    except Exception as e:
        logging.error(f">> Ошибка обработки обновления: {e}")
    return "OK", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    logging.info(f">> [Telegram] Команда /start от {message.chat.id}")
    bot.send_message(message.chat.id, """
Приветствуем в JarvisXBot!

Сигналы по стратегиям Lucky Jet
Ссылка: https://goo.su/qnkvtL
Промокод: FXX86
""")

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host="0.0.0.0", port=10000)
