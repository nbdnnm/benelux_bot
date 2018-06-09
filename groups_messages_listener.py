import datetime

from sqlalchemy import Column, String, JSON, DateTime, Integer

from base import Base


class GroupsMessagesListener(Base):
    __tablename__ = 'groups_messages_listeners'

    username = Column(String, primary_key=True)
    listeners = Column(JSON)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)
    update_nr = Column(Integer)

    def __init__(self, username, listeners, update_nr):
        self.username = username
        self.listeners = listeners
        self.update_nr = update_nr
