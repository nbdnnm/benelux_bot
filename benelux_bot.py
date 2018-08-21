# This Python file uses the following encoding: utf-8
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import command_messages
import reactions

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

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
updater.dispatcher.add_handler(CommandHandler('parents_invitation', command_messages.parents_invitation))
updater.dispatcher.add_handler(CommandHandler('list_my_listeners', command_messages.list_my_listeners))
updater.dispatcher.add_handler(CommandHandler('start', command_messages.start))
updater.dispatcher.add_handler(CommandHandler('chats', command_messages.chats))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, reactions.new_member_greeting))
# updater.dispatcher.add_handler(MessageHandler(Filters.private, private_messages.private_messages))
# updater.dispatcher.add_handler(MessageHandler(Filters.group, messages_handlers.all_messages))

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=bot_key)
updater.bot.setWebhook("https://benelux-bot.herokuapp.com/" + bot_key)
updater.idle()
