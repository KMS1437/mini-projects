import telebot
from sympy import sympify
TOKEN = '#ваш токен'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот по алгебре. Чем могу помочь?")
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_input = message.text
    try:
        result = sympify(user_input)
        result_str = str(result).replace("**", "^")
        response = f"Результат: {result_str}"
    except Exception as e:
        response = f"Ошибка: {e}"
    bot.send_message(message.chat.id, response)
if __name__ == "__main__":
    bot.polling(none_stop=True)
