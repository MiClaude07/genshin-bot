import discord
from dotenv import load_dotenv

import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv(".env")

@client.event
async def on_ready():
    print(f"We logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content
    if content.startswith('!genshin'):
        await message.channel.send()
    
    


client.run(os.getenv('DISCORD_TOKEN'))