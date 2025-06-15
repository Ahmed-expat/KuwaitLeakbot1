import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to Kuwait Expat Insider Access (Leaked Edition)!\nPlease fill the form to begin: https://forms.gle/AzrCMBFpTEob31oq6")

@bot.message_handler(commands=['status'])
def check_status(message):
    bot.reply_to(message, "⏳ We're currently processing your request. Please wait up to 30 minutes after submitting the form and payment.")

bot.polling()
