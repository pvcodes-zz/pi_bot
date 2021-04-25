from typing import AnyStr
import discord
from discord.ext import commands


class Maths(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.group(name='maths', aliases=['m', 'math'])
    async def maths(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('> Invalid command, Look ``-help maths``')

    @maths.command(name='a')
    async def add(self, ctx, n1: int, n2: int, *numbers: int):
        sum = n1+n2
        for i in numbers:
            sum += i
        await ctx.send(f'> Sum is: {sum}')

    @maths.command(name='mod', aliases=['%'])
    async def modulos(self, ctx, n1: int, n2: int):
        await ctx.send(f'> {n1} % {n2} = {n1%n2}')


def setup(bot):
    bot.add_cog(Maths(bot))
