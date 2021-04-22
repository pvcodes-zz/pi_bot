from requests.sessions import dispatch_hook
import discord
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()


client = discord.Client()


dc_token = os.getenv("DISCORD_TOKEN")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as: {0.user}'
          .format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send("Hi, how's the day")

    quote = get_quote()
    if message.content.startswith('!motivate'):
        await message.channel.send(quote)


client.run(dc_token)
