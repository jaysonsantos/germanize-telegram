import telebot
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

import spell_it

help_message = """Hey, to use this bot just do this:
/spell any word to be spelled
"""

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, help_message)
  
@bot.message_handler()
def spell(message):
  text = message.text.replace('/spell', '').replace('/germanize', '').strip()
  bot.reply_to(message, 'Spelling of {}\n\n{}'.format(text, spell_it.spell(text.lower())))

webhook_url = "https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN'])
bot.set_webhook(webhook_url)
