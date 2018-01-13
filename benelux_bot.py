# This Python file uses the following encoding: utf-8
import command_messages
import sys

from telegram.ext import Updater, CommandHandler

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# input bot token as first argument in command line
updater = Updater(sys.argv[1])

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
updater.dispatcher.add_handler(CommandHandler('bycicle', command_messages.bycicle))

updater.start_polling()
updater.idle()
