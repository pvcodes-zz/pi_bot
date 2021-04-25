import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='helpcmd',aliases=['help','h'],invoke_without_command=True)
    async def help_cmd(self,ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed(title='π bot Help Center', description='All Category are listed below')
            em.add_field(name='for commands related to codeforces',value='> ``-help cf``')
            em.add_field(name='for commands related to maths',value='> ``-help maths`` ')
            await ctx.channel.send(embed=em)
            
    @help_cmd.command(name='cf')
    async def codeforces_help(self,ctx):
        em = discord.Embed(title='Codeforces Command Help', description='All Commands are listed below')
        em.add_field(name='To get user rating',value='> ``-rating cf_username``')
        em.add_field(name='To get user info',value='> ``!info cf_username`` ')
        await ctx.channel.send(embed=em)   

    @help_cmd.command(name='maths',aliases=['math'])
    async def maths_help(self,ctx):
        em = discord.Embed(title='Maths Command Help', description='All Commands are listed below')
        em.add_field(name='Addition (+)',value='> ``-maths add``   *n1*  *n2*  ...')
        em.add_field(name='Modulo (%)',value='> ``-maths mod``   *n1*  *n2* ')
        await ctx.channel.send(embed=em)   


def setup(bot):
    bot.add_cog(Help(bot))
