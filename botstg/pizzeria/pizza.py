from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

menu = {
    "Пепперони": 12.99,
    "Вегетарианская": 10.99,
    "Гавайская": 11.99,
    "Маргарита": 9.99,
    "Мексиканская": 13.99,
    "Карбонара": 14.99,
    "Болоньезе": 12.99,
    "Альфредо": 13.99,
    "Томатный суп": 7.99,
    "Гороховый суп": 6.99,
    "Цезарь": 8.99,
    "Греческий": 7.99,
    "Стейк": 16.99,
    "Курица табака": 15.99,
    "Лосось с овощами": 18.99,
    "Тунец стейк": 17.99,
    "Тирамису": 6.99,
    "Чизкейк": 7.99
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Добро пожаловать в пиццерию! Сделайте свой заказ")
    for item, price in menu.items():
        update.message.reply_text(f"{item} - ${price:.2f}")

def show_menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Меню:")
    for item, price in menu.items():
        update.message.reply_text(f"{item} - ${price:.2f}")

def help_command(update: Update, context: CallbackContext) -> None:
update.message.reply_text("Команды:\n/start - Включить бота\n/menu - Показать меню\n/help - Показать команды")

updater = Updater("я не пишу токены, я не максик", use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("menu", show_menu))
dispatcher.add_handler(CommandHandler("help", help_command))

updater.start_polling()
