import discord

from discord import Intents, Client, Message, app_commands
from responses import get_response

# A class that holds the actual discord client and all associated commands 
class Commands:

    def __init__(self, intents : Intents) -> None:
        self.intents = intents
        self.intents.message_content = True

        self.client : Client = Client(intents=self.intents)
        self.tree = app_commands.CommandTree(client=self.client)

        pass

    def run(self) -> None:
        self.client.run()