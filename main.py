from typing import Final
import os

import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message, app_commands
from responses import get_response

import art

# Load token
load_dotenv()
TOKEN : Final[str] = os.getenv('DISCORD_TOKEN')
SERVER_ID : Final[str] = os.getenv('SERVER_ID')

# Setup
intents : Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
tree = app_commands.CommandTree(client=client)

# Actual message functionality
async def send_message(message : Message, user_message : str) -> None:
    if not user_message:
        print('(Message empty, likely that intents were not enabled properly)')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Startup of bot 
@client.event
async def on_ready() -> None:
    await tree.sync(guild=discord.Object(id=SERVER_ID))
    print(f"{client.user} is now running!")

# Read incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    #TODO logic goes here

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = message.channel

    print(f"[{channel}] {username} : {user_message}")
    await send_message(message, user_message)

# Slash commands
@tree.command(
        name="robiflyart",
        description="Grabs a random piece of robifly art from pixiv, reddit, or twitter and posts it along with a source",
        guild=discord.Object(id=SERVER_ID)
)
async def robi_fly_art(interaction):
    link = art.get_random_tag_image('RobiFly Honkai Star Rail')
    await interaction.response.send_message(link)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()