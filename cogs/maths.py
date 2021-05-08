import math
from discord.ext import commands


class Maths(commands.Cog):
    """Module for Maths Stuff"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'----{self.__class__.__name__} Cog have been loaded----')

    @commands.command(
        name='add', aliases=['sum', 'a'], description='To get sum'
    )
    async def __add(self, ctx, n1: int, n2: int, *numbers: int):
        """To get sum"""
        sum = n1+n2
        for i in numbers:
            sum += i
        await ctx.send(f'> Sum is: `{sum}`')

    @commands.command(
        name='mod', aliases=[], description='To get modulus'
    )
    async def __modulos(self, ctx, n1: int, n2: int):
        """To get modulus"""
        await ctx.send(f'> {n1} % {n2} = `{n1%n2}`')

    @commands.command(
        name='multiply', aliases=['into', 'product'], description='To get multiplication'
    )
    async def __multiply(self, ctx, n1: int, n2: int, *numbers: int):
        """To get product of two nums"""
        product = n1*n2
        for i in numbers:
            product *= i
        await ctx.send(f'> Product is `{product}`')

    @commands.command(
        name='divide', aliases=['div'], description='To get division'
    )
    async def __divide(self, ctx, n1: int, n2: int):
        """To get division of two nums"""
        await ctx.send(f'> {n1} / {n2} = `{n1/n2}`')

    @commands.command(
        name='gcd', aliases=[], description='To get gcd'
    )
    async def __gcd(self, ctx, n1: int, n2: int):
        """To get GCD/HCF of two nums"""
        await ctx.send(f'> **GCD**({n1}, {n2}) = `{math.gcd(n1,n2)}`')

    @commands.command(
        name='floor', aliases=[], description='To get floor val'
    )
    async def floor(self, ctx, n):
        """To get floor val of a num"""
        await ctx.send(f'> **Floor**({n}) = `{math.floor(n)}`')

    @commands.command(
        name='ceil', aliases=[], description='To get ceil'
    )
    async def __ceil(self, ctx, n):
        """To get ceil val of a num"""
        await ctx.send(f'> **Ceil**({n}) = `{math.ceil(n)}`')

    @commands.command(
        name='factorial', aliases=['fact'], description='To get factorial'
    )
    async def __factorial(self, ctx, n: int):
        """To get floor factorial(!) of a num"""
        if n < 0:
            await ctx.send('>>> Negative number have no factorial')

        await ctx.send(f'> **Factorial**({n}) = `{math.factorial(n)}`')

    @commands.command(
        name='log', aliases=[], description='To get log'
    )
    async def __log(self, ctx, n: int, base: int):
        """To get LOG X base Y"""
        await ctx.send(f'> **Log**({n}, {base}) = `{math.log(n,base)}`')

    @commands.command(
        name='pow', aliases=[], description='To get (x\'s power y)'
    )
    async def __pow(self, ctx, n: int, power: int):
        """To get X's power Y"""
        await ctx.send(f'> **Pow**({n}, {power}) = `{math.pow(n,power)}`')


def setup(bot):
    bot.add_cog(Maths(bot))
