import telebot
from telebot.types import Message

bot = telebot.TeleBot(token="6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10")


@bot.message_handler(commands=["start"])
def echo(message: Message):
    print("Мне написал пользователь с id: ", message.from_user.id, message.from_user.username)


bot.polling()
