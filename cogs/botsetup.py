from discord.ext import commands
import json

from src.helper import _isValidPrefix, _isValidChannel, _isValidRole


class BotSetup(commands.Cog):
    """Module for Administrator Stuff"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'----{self.__class__.__name__} Cog have been loaded----')

    @commands.command(
        name='setprefix', aliases=['setp'])
    @commands.has_permissions(administrator=True)
    async def __setprefix(self, ctx, prefix):
        """For setting the bot prefix"""
        if _isValidPrefix(prefix):
            with open('src/server_config.json', 'r') as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)]['prefix'] = prefix

            with open('src/server_config.json', 'w') as f:
                json.dump(prefixes, f, indent=4)
            await ctx.send(f'prefix changed to: {prefix}')
        else:
            await ctx.send('>>> Prefix can be only a symbol, Try again.')

    @commands.command(
        name='setchannelid', aliases=['setcnl'])
    @commands.has_permissions(administrator=True)
    async def __setchannelid(self, ctx, channel):
        """For setting the Contest Notification Channel"""
        channel = channel[2:-1]
        print(channel)
        if _isValidChannel(ctx, channel):
            with open('src/server_config.json', 'r') as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)]['channel_id'] = channel

            with open('src/server_config.json', 'w') as f:
                json.dump(prefixes, f, indent=4)

            await ctx.send(f'Default ping channel changed to: <#{channel}>')
        else:
            await ctx.send('>>> Not a valid channel, Try again.')

    @commands.command(name='setpingrole', aliases=['setrole'])
    @commands.has_permissions(administrator=True)
    async def __setpingrole(self, ctx, roleid):
        """For setting the Contest Notification pining Role"""
        roleid = roleid[3:-1]
        print(roleid)
        if _isValidRole(ctx, roleid):
            print(roleid)
            with open('src/server_config.json', 'r') as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)]['role_id'] = roleid

            with open('src/server_config.json', 'w') as f:
                json.dump(prefixes, f, indent=4)

            await ctx.send(f'Default ping role changed to: <@&{roleid}>')
        else:
            await ctx.send('>>> Not a valid Role, Try again.')


def setup(bot):
    bot.add_cog(BotSetup(bot))


# Auxillary/Helper Function
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
