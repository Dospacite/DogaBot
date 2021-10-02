from EdogaAccount import EdogaAccount
from DiscordInboxNotificationManager import DiscordInboxNotificationManager
from InboxChecker import InboxChecker
from discord.ext import tasks
from RegistryHandler import RegistryHandler
import URLS
import aiohttp


class EdogaInboxChecker(InboxChecker):

    check_interval_in_seconds = 600
    edoga_account: EdogaAccount

    def __init__(self, registry_handler: RegistryHandler):
        self.registry_handler = registry_handler
        self.discord_notification_manager = DiscordInboxNotificationManager(registry_handler=self.registry_handler)
        self.edoga_account = EdogaAccount()

    async def get_inbox(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(URLS.INBOX_URL) as r:
                if r.status == 200:
                    json = await r.json()
                    return json

    def get_message_by_id(self):
        pass

    @tasks.loop(seconds=check_interval_in_seconds)
    async def checker_loop(self):
        inbox = await self.get_inbox()
        last_message_id = inbox['entities'][0]['id']
        if last_message_id == self.registry_handler.get_key("last_message_id"):
            return
        self.registry_handler.set_key("last_message_id", last_message_id)
        self.discord_notification_manager.send_all_notifications(inbox)
