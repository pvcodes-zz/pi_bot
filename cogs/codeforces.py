# from os import sendfile
import discord
from discord.ext import commands
from datetime import datetime

import requests
import json


class Codeforces(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def ez(self, ctx):
        print("EZ BOLTE")
        await ctx.send("EZ BOLTE")


    # Commands
    @commands.command(name='rating')
    async def rating(self,ctx, username: str):
        
        data = is_valid(username)
        if data:
            if 'rating' in data['result'][0]:
                rating = data["result"][0]["rating"]
                return_msg = f"``{username}``'s rating is: {rating}"
            else:
                return_msg = f"``{username}`` has not rating, yet!"
        else:
            return_msg = 'User not found'

        await ctx.send(return_msg)


    @commands.command(name='info',aliases=['i'])
    async def user(self,ctx, username: str):
        data = is_valid(username)

        if data:
            # parsed data
            data = data["result"][0]
            data = user_info(data)

            # local variables
            name = f"{data['firstName']} {data['lastName']} @{username}"
            img_url = data['titlePhoto']
            country = data['country']
            rank = f"{data['rank']} (**Max** : {data['maxRank']})"
            rating = f"{data['rating']} (**Max** : {data['maxRating']})"
            contri = data['contribution']
            frnd = data['friendOfCount']
            registered_on = data['registrationTimeSeconds']
            registered_on = datetime.fromtimestamp(registered_on)

            # embedding for return message
            embed = discord.Embed(title=name, url=f"https://codeforces.com/profile/{username}", color=discord.Color.blue())
            embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=img_url)
            embed.add_field(name="Country", value=country, inline=False)
            embed.add_field(name="Rank", value=rank, inline=False)
            embed.add_field(name="Rating", value=rating, inline=False)
            embed.add_field(name="Contribution", value=contri, inline=False)
            embed.add_field(name="Total Friends", value=frnd, inline=False)
            embed.add_field(name="Registered On",value=registered_on, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("User not found")


def setup(bot):
    bot.add_cog(Codeforces(bot))


# Auxilarry Function
def is_valid(username: str):
    user_object = requests.get(f"https://codeforces.com/api/user.info?handles={username}")
    data = json.loads(user_object.text)
    status = data["status"]

    if status == 'OK':
        return data
    else:
        return False


def user_info(obj: dict):
    default_obj = {
        "lastName": "-",
        "country": "-",
        "lastOnlineTimeSeconds": 0,
        "city": "-",
        "rating": 0,
        "friendOfCount": 0,
        "titlePhoto": "-",
        "handle": "-",
        "avatar": "-",
        "firstName": "-",
        "contribution": 0,
        "organization": "-",
        "rank": "-",
        "maxRating": 0,
        "registrationTimeSeconds": 0,
        "maxRank": "-"
    }
    if len(default_obj) == len(obj):
        return obj
    else:
        key_obj = list(obj)
        for i in key_obj:
            default_obj[i] = obj[i]
    return default_obj

