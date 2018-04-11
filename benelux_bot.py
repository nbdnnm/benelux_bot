# This Python file uses the following encoding: utf-8
import logging
import os

from telegram.ext import Updater, CommandHandler

import command_messages

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# bot token from environment variables
bot_key = os.environ['BENELUX_BOT_KEY']
updater = Updater(bot_key)
PORT = int(os.environ.get('PORT', '5000'))

# registration of bot commands
updater.dispatcher.add_handler(CommandHandler('ruling', command_messages.ruling))
updater.dispatcher.add_handler(CommandHandler('google_doc', command_messages.google_doc))
updater.dispatcher.add_handler(CommandHandler('rassvet', command_messages.rassvet))
updater.dispatcher.add_handler(CommandHandler('apostil', command_messages.apostil))
updater.dispatcher.add_handler(CommandHandler('driver_license', command_messages.driver_license))
updater.dispatcher.add_handler(CommandHandler('bank_cards', command_messages.bank_cards))
updater.dispatcher.add_handler(CommandHandler('bank_account', command_messages.bank_account))
updater.dispatcher.add_handler(CommandHandler('post_taxes', command_messages.post_taxes))
updater.dispatcher.add_handler(CommandHandler('shops', command_messages.shops))
updater.dispatcher.add_handler(CommandHandler('transport', command_messages.transport))
updater.dispatcher.add_handler(CommandHandler('bicycle', command_messages.bicycle))
updater.dispatcher.add_handler(CommandHandler('work', command_messages.work))
updater.dispatcher.add_handler(CommandHandler('pets', command_messages.pets))
updater.dispatcher.add_handler(CommandHandler('utilities', command_messages.utilities))
updater.dispatcher.add_handler(CommandHandler('devices', command_messages.devices))
updater.dispatcher.add_handler(CommandHandler('mobile', command_messages.mobile))
updater.dispatcher.add_handler(CommandHandler('buy_buckwheat', command_messages.buy_buckwheat))
updater.dispatcher.add_handler(CommandHandler('callsaul', command_messages.callsaul))

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=bot_key)
updater.bot.setWebhook("https://benelux-bot.herokuapp.com/" + bot_key)
updater.idle()
