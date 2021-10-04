from abc import ABC, abstractmethod
from enum import Enum


class AccountType(Enum):
    EDOGA: int = 1
    RAUNT: int = 2


class Account(ABC):

    username: str
    password: str
    cookies: dict
    account_type: AccountType
    name: str

    def __init__(self, username, password, cookies, account_type, name):
        self.username = username
        self.password = password
        self.cookies = cookies
        self.account_type = account_type
        self.name = name

    @abstractmethod
    async def login(self) -> dict:
        pass

    @abstractmethod
    async def logout(self) -> dict:
        pass

    @abstractmethod
    async def renew_cookies_if_invalid(self) -> dict:
        pass

    @abstractmethod
    async def are_cookies_valid(self) -> bool:
        pass

    @abstractmethod
    async def get_inbox(self) -> dict:
        pass
