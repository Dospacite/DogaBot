from Registry import Registry
from Account import AccountType, Account


class AccountRegistry(Registry):

    cached_accounts: list[Account]

    def write_account(self, account_type: AccountType, account_name: str,
                      username: str = None, password: str = None, cookies: dict = None):
        reg = self.load()
        reg[account_type.name][account_name] = {
            'username': username,
            'password': password,
            'cookies': cookies
        }
        self.dump(reg)

    def write_account_from_obj(self, account: Account):
        self.write_account(account_type=account.account_type,
                           account_name=account.name,
                           username=account.username,
                           password=account.password,
                           cookies=account.cookies)

    def remove_account(self, account_type: AccountType, account_name: str):
        reg = self.load()
        del reg[account_type.name][account_name]
        self.dump(reg)
