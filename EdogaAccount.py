from pathlib import Path

import aiohttp

from Account import Account
import URLS
from AccountsRegistryHandler import AccountsRegistryHandler


class EdogaAccount(Account):

    def __init__(self, username: str, password: str):
        self.account_registry_handler = AccountsRegistryHandler(Path("accounts.json"))
        self.username = username
        self.password = password
        self.login_params = {
            'l_op': 'tibeslogin',
            'l_un': self.username,
            'l_pw': self.password,
            'l_kmli': False,
            'l_ru': "undefined"
        }

    def get_cookies(self):
        if self.cookies:
            return self.cookies
        return self.account_registry_handler.get_key("edoga")[0]['cookies']

    def login(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=URLS.LOGIN_URL,
                                    data=self.login_params) as r:
                if r.status == 200:
                    print(r.cookies)
                    return r.cookies
        pass

    def logout(self) -> None:
        pass


    def are_cookies_valid(self):
        pass

