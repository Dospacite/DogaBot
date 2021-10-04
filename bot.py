from discord.ext import commands
import json
import pathlib


class Bot(commands.Bot):

    def register_cogs(self):
        cogs_dir = pathlib.Path("cogs")
        for file in cogs_dir.iterdir():
            if file.name.endswith(".py"):
                self.load_extension("cogs." + file.stem)

    async def on_ready(self):
        print("DogaBot is ready on {} servers".format(len(self.guilds)))


with open("config.json", "r") as f:
    config = dict(json.load(f))

client = Bot(
    command_prefix=config['bot']['command_prefix']
)
client.register_cogs()
client.run(config['bot']['token'])