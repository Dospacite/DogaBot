from discord.ext import commands
import json
import pathlib

from cogs.EdogaInbox import EdogaInbox


class Bot(commands.Bot):

    config: dict

    def register_cogs(self):
        cogs_dir = pathlib.Path("cogs")
        for file in cogs_dir.iterdir():
            if file.name.endswith(".py"):
                self.load_extension("cogs." + file.stem)

    async def on_ready(self):
        ei = EdogaInbox(self)
        await ei.inbox_checker.checker_loop.start()
        print("DogaBot is ready on {} servers".format(len(self.guilds)))


with open("config.json", "r") as f:
    config = dict(json.load(f))

client = Bot(
    command_prefix="e!"
)
client.register_cogs()
client.run(config['bot']['token'])
client.config = config
