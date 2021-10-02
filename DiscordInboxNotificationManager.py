from abc import ABC

from InboxNotificationManager import InboxNotificationManager
from RegistryHandler import RegistryHandler


class DiscordInboxNotificationManager(InboxNotificationManager):

    registry_handler: RegistryHandler

    def __init__(self, registry_handler: RegistryHandler):
        self.registry_handler = registry_handler

    def send_all_notifications(self, inbox) -> list:
        for message in inbox['entities']:
            for channel in self.registry_handler.get_key("channels"):
                print(channel)
        pass

    def send_notification(self, message):
        pass

    def prepare_notification(self, message):
        pass
