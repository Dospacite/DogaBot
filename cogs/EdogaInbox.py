from pathlib import Path

from discord.ext import commands
import discord

from EdogaInboxChecker import EdogaInboxChecker
from NotificationRegistryHandler import NotificationRegistryHandler


class EdogaInbox(commands.Cog,
                 name="Edoğa Inbox",
                 description="Edoğa mesajları ile ilgili komutlar."):

    client: commands.Bot
    registry_handler: NotificationRegistryHandler
    inbox_checker: EdogaInboxChecker

    def __init__(self, client: commands.Bot):
        self.client = client
        self.registry_handler = NotificationRegistryHandler(Path("registry.json"))
        self.inbox_checker = EdogaInboxChecker(registry_handler=self.registry_handler)

    @commands.command(name="register")
    async def register(self, ctx: commands.Context, channel: discord.TextChannel):
        self.registry_handler.write_channel_message_to_registry(channel_id=channel.id,
                                                                last_sent_message_id=0)

    @commands.command(name="refresh")
    async def refresh(self, ctx: commands.Context):
        self.inbox_checker.checker_loop.restart()

    @commands.command(name="start")
    async def start(self, ctx: commands.Context = None):
        self.inbox_checker.checker_loop.start()

    @commands.command(name="stop")
    async def stop(self, ctx: commands.Context):
        self.inbox_checker.checker_loop.stop()


def setup(client: commands.Bot):
    client.add_cog(EdogaInbox(client))
