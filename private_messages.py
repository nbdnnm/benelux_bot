import re

from base import Session
from groups_messages_listener import GroupsMessagesListener


def private_messages(bot, update):
    session = Session()
    listener = re.search("chat\s(\w+)\skeyword\s(.*?)$", update.message.text)
    if listener:
        user = update.message.from_user.username
        userdata = session.query(GroupsMessagesListener).filter_by(username=user).first()
        array_of_listeners = list(userdata.listeners[listener.group(1)])
        array_of_listeners.append(listener.group(2))
        userdata.listeners[listener.group(1)] = array_of_listeners
        print("updated listener " + str(userdata.listeners[listener.group(1)]))
        session.commit()
        print("updated listener " + str(userdata.listeners[listener.group(1)]))
