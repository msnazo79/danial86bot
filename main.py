import telebot
import requests

TOKEN = "7923818163:AAESxfP1d-QUorPzWJuZExslSPZnxsSVJDM"

# تنظیم پراکسی برای کتابخانه requests
telebot.apihelper.proxy = {
    'http': 'http://127.0.0.1:53463',
    'https': 'http://127.0.0.1:53463'
}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من ربات پایتونی دانیال هستم 🤖")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"شما گفتید: {message.text}")

bot.polling(timeout=200)
