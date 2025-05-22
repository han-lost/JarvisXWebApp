from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

WEBHOOK_URL = f"https://jarvisx-web.onrender.com/{TOKEN}"

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)
print(f"Webhook установлен: {WEBHOOK_URL}")
