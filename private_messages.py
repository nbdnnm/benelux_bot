import re

from base import Session
from groups_messages_listener import GroupsMessagesListener


def private_messages(bot, update):
    session = Session()
    listener = re.search("chat\s(\w+)\skeyword\s(.*?)$", update.message.text)
    if listener:
        user = update.message.from_user.username
        userdata = session.query(GroupsMessagesListener).filter_by(username=user).first()
        if userdata:
            array_of_listeners = list(userdata.listeners[listener.group(1)])
            session.delete(userdata)
        else:
            array_of_listeners = list()
        array_of_listeners.append(listener.group(2))

        chat_dictionary = {listener.group(1): array_of_listeners}
        newuserdata = GroupsMessagesListener(username=user, listeners=chat_dictionary, update_nr=1)

        session.add(newuserdata)
        session.commit()
