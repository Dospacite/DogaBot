from abc import ABC, abstractmethod
from dataclasses import dataclass

import Group
from User import User


@dataclass()
class Message(ABC):

    id: str
    title: str
    body: str
    sender: User
    createDate: int
    receiverGroup: list[Group]

    @abstractmethod
    def serialize_body(self) -> str:
        pass

