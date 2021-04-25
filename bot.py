import discord
import logging
import os

# from discord import embeds, client (not used in this file)
from discord.ext import commands, tasks
from discord.utils import to_json
from dotenv import load_dotenv
from itertools import cycle  # used at line 75 for background task

# Loading Discord Token
load_dotenv()
dc_token = os.getenv("DISCORD_TOKEN")
description = '> All in one bot, for now works with Codeforces API'

# Logging Stuff
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Intents Stuff
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-',help_command=None,description=description, intents=intents)


# -----------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    change_status.start() #Is changes the bot's status SEE LINE '71'
    print(f'We have logged in as {bot.user}')


# Commands

@bot.command()
async def ping(ctx):
    print("Called ping")
    await ctx.send(f"Ping is: {round(bot.latency*1000)}ms")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')


# Background Task
status = cycle(
    ['Currently solving problem at universe', 'OMG, It\'s important'])


@tasks.loop(minutes=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

# -------------------------------------------------------------------------------------------------------------------------------


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"> {error}, Have a look at ``!help``")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(dc_token)
