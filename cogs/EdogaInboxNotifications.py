from pathlib import Path

from discord.ext import commands

from Account import AccountType
from AccountRegistry import AccountRegistry


class EdogaInboxNotifications(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client
        self.account_registry = AccountRegistry(Path("accounts.json"))

    @commands.group(name="account")
    async def account(self, ctx: commands.Context):
        pass

    @account.command(name="add")
    async def add(self, ctx: commands.Context, account_type, username: str, password: str, name: str):
        if isinstance(account_type, int):
            account_type = AccountType(account_type)
        elif isinstance(account_type, str):
            account_type = AccountType[account_type]
        else:
            raise ValueError("{} is not a valid AccountType".format(account_type))
        self.account_registry.write_account(account_type=AccountType(account_type),
                                            username=username,
                                            password=password,
                                            account_name=name)
        await ctx.send(content="Account was successfully added.")

    @account.command(name="remove")
    async def remove(self, ctx: commands.Context, account_type, account_name: str):
        if isinstance(account_type, int):
            account_type = AccountType(account_type)
        elif isinstance(account_type, str):
            account_type = AccountType[account_type]
        else:
            raise ValueError("{} is not a valid AccountType".format(account_type))
        self.account_registry.remove_account(account_type=account_type, account_name=account_name)
        await ctx.send(content="Account was successfully removed.")

    @commands.command(name="start")
    async def start(self, ctx: commands.Context):
        pass


def setup(client: commands.Bot):
    client.add_cog(EdogaInboxNotifications(client))
