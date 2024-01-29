import telebot
import random

def read_quotes_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        quotes = [line.strip() for line in file.readlines()]
    return quotes

bot = telebot.TeleBot("Я не вставляю токен, я не Максик")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ежедневный цитатный бот. Я буду присылать тебе мотивационную цитату. Просто напиши /quote")

@bot.message_handler(commands=['quote'])
def send_quote(message):
    quotes = read_quotes_from_file("C:\\Users\\RussianEmpire\\OneDrive\\Рабочий стол\\telegrambot\\base.txt")
    quote = random.choice(quotes)
    bot.reply_to(message, quote)

bot.polling()
