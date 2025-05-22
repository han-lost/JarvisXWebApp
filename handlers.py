import telebot
from config import ADMIN_ID, START_MESSAGE, LINK

def register_all_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        print("✅ start_handler вызван")  # Проверка
        chat_id = message.chat.id
        try:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("Перейти на сайт", url=LINK))
            bot.send_message(chat_id, START_MESSAGE, reply_markup=markup)
            print("✅ Сообщение отправлено")
        except Exception as e:
            print(f"❌ Ошибка при отправке: {e}")

    @bot.message_handler(func=lambda msg: msg.chat.id == ADMIN_ID and msg.text.startswith("/signal"))
    def signal_handler(message):
        bot.send_message(message.chat.id, "Сигнал: X10 скоро!")
