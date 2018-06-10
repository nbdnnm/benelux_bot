from base import Session
from groups_messages_listener import GroupsMessagesListener


def all_messages(bot, update):
    print("all messages")
    chat_name = update.message.chat.username
    session = Session()
    userdata = session.query(GroupsMessagesListener).all()
    for user in userdata:
        if chat_name in user.listeners.keys():
            for listener in user.listeners[chat_name]:
                if listener in update.message.text:
                    bot.send_message(chat_id=user.chat_id,
                                     text="Listener " + listener + " for chat " + update.message.chat.username
                                          + " was triggered for next message")
                    bot.forward_message(chat_id=user.chat_id, from_chat_id=update.message.chat.id,
                                        message_id=update.message.message_id)
