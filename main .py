import os
import telebot
from flask import Flask
from threading import Thread

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبا بيك في بوت Flexi ⚡\nاكتب /flexi باش تشوف العروض")

@bot.message_handler(commands=['flexi'])
def flexi(message):
    bot.reply_to(message, "عروض Flexi:\n- 100 DA = 100 Flexi\n- 200 DA = 220 Flexi\n- 500 DA = 550 Flexi")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "اكتب /start باش تبدا")

if __name__ == "__main__":
    Thread(target=run_flask, daemon=True).start()
    bot.infinity_polling()
