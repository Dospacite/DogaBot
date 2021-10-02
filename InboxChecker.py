from abc import ABC, abstractmethod

from RegistryHandler import RegistryHandler


class InboxChecker(ABC):

    check_interval_in_seconds: float
    registry_handler: RegistryHandler

    @abstractmethod
    def get_inbox(self):
        pass

    @abstractmethod
    def get_message_by_id(self):
        pass

    @abstractmethod
    def checker_loop(self):
        pass
