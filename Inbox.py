from abc import ABC, abstractmethod


class Inbox(ABC):

    messages: list

    def __init__(self, messages):
        self.messages = messages

    @staticmethod
    @abstractmethod
    def from_dict(self, dictionary: dict):
        return Inbox(messages=dictionary['entities'])
