import telebot

TOKEN = "8051188881:AAHbGSaljlNC5YASV5Jj3BheqEi27PaL0EU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """
👋 Приветствуем тебя в JarvisXBot!

🎯 Здесь ты получаешь сигналы по **легендарным стратегиям Lucky Jet** — созданным на опыте, математике и анализе.

🎰 **Ссылка на 1win**: [НАЧАТЬ ИГРАТЬ](https://goo.su/qnkvtL)  
💰 **Промокод:** `FXX86` — получи бонус на депозит!

⚡️ Просто следуй сигналам, делай ставки — и зарабатывай.  
🧠 Наш бот обучается, анализирует и совершенствуется с каждой минутой.

Удачи, чемпион!  
— Твой Джарвис
"""
)

bot.polling()
