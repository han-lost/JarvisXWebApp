import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def register_handlers():
    from handlers import register_all_handlers
    register_all_handlers(bot)
