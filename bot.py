import discord
import os
import requests
import json

from requests.sessions import dispatch_hook

client = discord.Client()

with open('.gitignore/config.json', 'r') as f:
    token_data = json.load(f)

dc_token = token_data["token"]


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
