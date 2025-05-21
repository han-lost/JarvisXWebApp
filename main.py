from flask import Flask, render_template, request
import telebot
import os

TOKEN = "7605281790:AAHhl2iUFuv0vtO4GvCsU3JQ5gQ5ED8wyx4"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

admin_password = "jarvispass"
latest_signal = "Нажми кнопку, чтобы получить сигнал."

# Веб-интерфейс пользователя
@app.route("/", methods=["GET", "POST"])
def index():
    global latest_signal
    if request.method == "POST":
        return render_template("index.html", signal=latest_signal)
    return render_template("index.html", signal=None)

# Панель администратора
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

# Приветствие
@bot.message_handler(commands=['start'])
def send_welcome(message):
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

# Webhook для Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# Установка webhook при старте
@app.before_first_request
def setup_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://jarvisx-web.onrender.com/{TOKEN}")

# Запуск Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

