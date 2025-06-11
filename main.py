import telebot
import requests

TOKEN = "7117854493:AAFmkXbinHewDsas1j8ZOfQoMTW1dZL4aUA"

bot = telebot.TeleBot(TOKEN)
bot.set_webhook()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام جیگر طلا")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"نمره 20 منو بده")
bot.polling(timeout=200)
