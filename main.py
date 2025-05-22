from flask import Flask, request, render_template
import telebot
import logging

# Логирование
logging.basicConfig(level=logging.INFO)

# Токен Telegram
TOKEN = "8051188881:AAHbGSaljlNC5YASV5Jj3BheqEi27PaL0EU"
bot = telebot.TeleBot(TOKEN)

# Flask
app = Flask(__name__)
admin_password = "jarvispass"
latest_signal = "Нажми кнопку, чтобы получить сигнал."

# Webhook URL
WEBHOOK_URL = f"https://jarvisx-web.onrender.com/{TOKEN}"

# Главная страница
@app.route("/", methods=["GET", "POST"])
def index():
    global latest_signal
    if request.method == "POST":
        return render_template("index.html", signal=latest_signal)
    return render_template("index.html", signal=None)

# Админ-панель
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

# Обработка обновлений Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    try:
        json_str = request.get_data().decode('UTF-8')
        logging.info(">> Получено обновление:")
        logging.info(json_str)

        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
    except Exception as e:
        logging.error(f">> Ошибка обработки обновления: {e}")
    return "OK", 200

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    logging.info(f">> Команда /start от {message.chat.id}")
    bot.send_message(message.chat.id, """
👋 Приветствуем тебя в JarvisXBot!

🎯 Здесь ты получаешь сигналы по **легендарным стратегиям Lucky Jet** — созданным на опыте, математике и анализе.

🎰 **Ссылка на 1win**: [НАЧАТЬ ИГРАТЬ](https://goo.su/qnkvtL)  
💰 **Промокод:** `FXX86` — получи бонус на депозит!

⚡️ Просто следуй сигналам, делай ставки — и зарабатывай.  
🧠 Наш бот обучается, анализирует и совершенствуется с каждой минутой.

Удачи, чемпион!  
— Твой Джарвис
""")

# Запуск
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host="0.0.0.0", port=10000)

