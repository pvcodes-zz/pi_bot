from random import random
import discord
from discord import client
from discord import guild
from discord.ext import commands, tasks
from datetime import timedelta, timezone
import datetime


import json
from dotenv.main import set_key
from six import with_metaclass
from src.helper import _textFormatting, _isValid, _userInfo, _getProblem, _getChannelId, _getRoleId, _sendEmbed


def _getContest():
    with open('src/contests.json', 'r') as f:
        returndata = json.load(f)
        print(returndata[0])
    return returndata


class Codeforces(commands.Cog):
    """Module for Codeforces Stuff"""

    def __init__(self, bot):
        self.bot = bot
        # task = self.test.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'----{self.__class__.__name__} Cog have been loaded----')

    @commands.command(
        name='rating', aliases=['r'], description='Get the rating of the user'
    )
    async def __rating(self, ctx, username: str):
        """For getting the rating of an user"""

        data = _isValid(username)
        if data:
            if 'rating' in data['result'][0]:
                rating = data["result"][0]["rating"]
                return_msg = f"``{username}``'s rating is: {rating}"
            else:
                return_msg = f"``{username}`` has not rating, yet!"
        else:
            return_msg = 'User not found'

        await ctx.send(return_msg)

    @commands.command(
        name='info', aliases=['i'], description='Get the full info of the user'
    )
    async def __user(self, ctx, username: str):
        """For getting the full info of an user"""
        data = _isValid(username)

        if data:
            # parsed data
            data = data["result"][0]
            data = _userInfo(data)
            name = f"{data['firstName']} {data['lastName']} @{username}"
            embed = discord.Embed(
                title=name, url=f"https://codeforces.com/profile/{username}", color=discord.Color.blue())

            # local variables
            img_url = data['titlePhoto']
            country = data['country']
            rank = f"{data['rank']} (**Max** : {data['maxRank']})"
            rating = f"{data['rating']} (**Max** : {data['maxRating']})"
            contri = data['contribution']
            frnd = data['friendOfCount']
            registered_on = data['registrationTimeSeconds']
            registered_on = datetime.datetime.fromtimestamp(registered_on)
            # embedding for return message
            embed.set_author(name=ctx.author.display_name,
                             icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=img_url)
            embed.add_field(name="Country", value=country, inline=False)
            embed.add_field(name="Rank", value=rank, inline=False)
            embed.add_field(name="Rating", value=rating, inline=False)
            embed.add_field(name="Contribution", value=contri, inline=False)
            embed.add_field(name="Total Friends", value=frnd, inline=False)
            embed.add_field(name="Registered On",
                            value=registered_on, inline=False)
            await _sendEmbed(ctx, embed)
        else:
            await ctx.send("User not found")

    @commands.command(
        name='gimme', aliases=['getproblem', 'getprob'], description='Gives the problem based on given tags'
    )
    async def __gimme(self, ctx, *args):
        """For getting a codeforces problem based on given tags"""
        if not args:
            await ctx.send('>>> No arguments passed')
            return
        rating = 0
        tags = []
        problems = []
        for arg in args:
            if arg.isdigit():
                rating = int(arg)
            else:
                tags.append(arg)

        # If the problem is solved by the curr user we have to skip, this will be done when database is managed :)

        problem = _getProblem(rating, tags)

        if type(problem) == str:
            await ctx.send(f">>> {problem}")
        else:
            prob_url = f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}"
            embed = discord.Embed()
            embed.description = f'>>> [{problem["index"]} {problem["name"]} ]({prob_url})'
            tags_str = '`'
            for tag in args:
                tags_str += tag+'` `'
            tags_str = tags_str[: -2]
            embed.add_field(name="Tags", value=tags_str, inline=False)
            embed.set_footer(text='HFGL')
            await _sendEmbed(ctx, embed)

    @commands.command(
        name='contestreminder', aliases=['ctr'],
        description='For Contest Times',

    )
    @commands.has_permissions(administrator=True)
    async def __contestreminder(self, ctx):
        """For enabling Contest Notifications **Administrator Permission Required**"""
        print('entered')
        role = int(_getRoleId(ctx))
        role = f'<@&{role}>'
        print(role)
        channel = int(_getChannelId(ctx))
        print(channel)
        channel = ctx.bot.get_channel(channel)
        print(channel)
        contests = _getContest()

        await ctx.send('>>> Contest Reminder Enabled..')
        for contest in contests:
            UTC = timezone.utc
            summary = _textFormatting(contest['summary'])
            url = contest['htmlLink']
            if 'location' in contest:
                url = contest['location']
            if 'dateTime' in contest['start']:

                conteststart = contest['start']['dateTime']
                conteststart = datetime.datetime.strptime(
                    conteststart, '%Y-%m-%dT%H:%M:%S%z')
                conteststart = conteststart.astimezone(UTC)

                contestend = contest['end']['dateTime']
                contestend = datetime.datetime.strptime(
                    contestend, '%Y-%m-%dT%H:%M:%S%z')
                contestend = contestend.astimezone(UTC)

                time_duration = contestend - conteststart
                time_duration = str(time_duration)
                time_duration = time_duration[: -3]
                time_duration += ' hr'
                print(time_duration)
            else:
                conteststart = contest['start']['date']
                conteststart = datetime.datetime.strptime(
                    conteststart, '%Y-%m-%d')
                conteststart = conteststart.astimezone(UTC)

                contestend = contest['end']['date']
                contestend = datetime.datetime.strptime(contestend, '%Y-%m-%d')
                contestend = contestend.astimezone(UTC)

                time_duration = 'All day'

            print(f'conteststart : {conteststart}')
            print(f'contestend : {contestend}')
            print(time_duration)

            remindertime = conteststart - \
                timedelta(minutes=30)  # 30 min before time

            print(f'remindertime : {remindertime}')

            prindate = conteststart.strftime("%d %b %Y, %H:%M %Z")
            message = f'`{prindate} | {time_duration}`'

            embed = discord.Embed(title='Contest Reminder')
            embed.add_field(name=summary, value=f'{message}', inline=False)
            embed.add_field(name='*Contest Link*', value=f'[Link]({url})')
            embed.set_footer(text='Provided to you by Pi bot')

            await discord.utils.sleep_until(remindertime)
            await channel.send(role, embed=embed)

        # @tasks.loop(seconds=1)
        # async def test(self):
        #     # print('Test')
        #     # channel = int(_getChannelId(ctx))
        #     # channel = client.get_channel(channel)
        #     print(bot.guild.id)
        #     # await channel.send('chot vol 1')


def setup(bot):
    bot.add_cog(Codeforces(bot))
