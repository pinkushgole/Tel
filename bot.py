#   bot name  : Gole Code
# username : GoleCode_Bot

import telebot
from googletrans import Translator
from deep_translator import GoogleTranslator
translater=Translator()



Token=""

bot=telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome")

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,""" /start -> Greeting
/help -> will give you all commands list 
This Bot use to Hindi to English Tranlation 
                 """)


@bot.message_handler()
def custom(message):
    try:
        translator = GoogleTranslator(source='auto', target='en')
        response_text = translator.translate(message.text)
    except Exception as e:
        print(f"Error during translation: {e}")
        response_text = "Translation failed. Please try again later."
    

    bot.reply_to(message, response_text)


# bot.polling()
import time
import telebot

def safe_polling(bot):
    while True:
        try:
            bot.polling(timeout=30, interval=0)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(10)  

bot = telebot.TeleBot('YOUR_BOT_TOKEN')
safe_polling(bot)

