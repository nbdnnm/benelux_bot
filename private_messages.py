import re

from base import Session
from groups_messages_listener import GroupsMessagesListener


def private_messages(bot, update):
    session = Session()
    listener = re.search("chat\s(\w+)\skeyword\s(.*?)$", update.message.text)
    if listener:
        user = update.message.from_user.username
        user_data = session.query(GroupsMessagesListener).filter_by(username=user).first()
        if user_data:
            dict_of_listeners = dict(user_data.listeners)

            if listener.group(1) in dict_of_listeners.keys():
                dict_of_listeners[listener.group(1)].append(listener.group(2))
                dict_of_listeners[listener.group(1)] = list(set(dict_of_listeners[listener.group(1)]))
            else:
                create_new_chat_listener(dict_of_listeners, listener)

            new_user_data = GroupsMessagesListener(username=user, chat_id=update.message.chat.id,
                                                   listeners=dict_of_listeners,
                                                   update_nr=user_data.update_nr + 1)
            session.delete(user_data)
        else:
            dict_of_listeners = dict()
            create_new_chat_listener(dict_of_listeners, listener)
            new_user_data = GroupsMessagesListener(username=user, chat_id=update.message.chat.id,
                                                   listeners=dict_of_listeners, update_nr=1)

        session.add(new_user_data)
        session.commit()


def create_new_chat_listener(dict_of_listeners, listener):
    dict_of_listeners.update({listener.group(1): list("")})
    dict_of_listeners[listener.group(1)].append(listener.group(2))
