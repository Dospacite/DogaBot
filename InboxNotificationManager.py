from abc import ABC, abstractmethod


class InboxNotificationManager(ABC):

    @abstractmethod
    def send_all_notifications(self, inbox) -> list:
        pass

    @abstractmethod
    def send_notification(self, message):
        pass

    @abstractmethod
    def prepare_notification(self, message):
        pass
