import re
import aiohttp

from Account import Account
import URLS


class EdogaAccount(Account):

    def __init__(self, username, password, cookies, account_type, name):
        super().__init__(username, password, cookies, account_type, name)
        self.login_params = {
            'l_op': 'tibeslogin',
            'l_un': self.username,
            'l_pw': self.password,
            'l_kmli': False,
            'l_ru': "undefined"
        }

    async def login(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=URLS.LOGIN_URL, params=self.login_params) as r:
                if r.status == 200:
                    sid = re.search(pattern=r"(?<=<sidValue>).*(?=<\/sidValue>)",
                                    string=str(await r.read())).group()
        return {'sid': sid}

    async def logout(self) -> dict:
        pass

    async def renew_cookies_if_invalid(self) -> dict:
        pass

    async def are_cookies_valid(self) -> bool:
        pass

    async def get_inbox(self) -> dict:
        pass


