from abc import ABC, abstractmethod


class Account(ABC):
    username: str
    password: str
    cookies: dict

    @abstractmethod
    def login(self) -> dict:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

