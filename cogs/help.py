import discord
from discord.ext import commands
from src.helper import _getPrefix2, _sendEmbed


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='help', aliases=['h'], description='This is a bot command'
    )
    # @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def __help(self, ctx, *input):
        """Shows all modules of that bot"""

        prefix = _getPrefix2(ctx)
        version = 'π bot - (pre α)'

        owner = '<@441501033294987264>'
        owner_name = 'undefined#1977'

        # checks if cog parameter was given
        # if not: sending all modules and commands not associated with a cog
        if not input:
            # checks if owner is on this server - used to 'tag' owner
            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError as e:
                owner = owner

            # starting to build embed
            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description=f'Use `{prefix}help <module>` to gain more information about that module '
                                            f':smiley:\n')

            # iterating trough cogs, gathering descriptions
            cogs_desc = ''
            for cog in self.bot.cogs:
                if cog != 'Help':
                    cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

            # adding 'list' of cogs to embed
            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            # integrating trough uncategorized commands
            commands_desc = ''
            for command in self.bot.walk_commands():
                # if cog not in a cog
                # listing command if cog name is None and command isn't hidden
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            # adding those commands to embed
            if commands_desc:
                emb.add_field(name='Not belonging to a module',
                              value=commands_desc, inline=False)

            # setting information about author
            emb.add_field(
                name="About",
                value=f"The Bots is developed and currently maintained by [{owner_name}](https://pvcodes.netlify.app), based on discord.py.\
                        Please visit https://github.com/pvcodes/pi_bot to submit ideas or bugs.",
                inline=False

            )
            emb.add_field(
                name="To get more about commands",
                value=f"Visit [Commands Docs](https://pvcodes.github.io/pi_bot_commands) or join our [Support Server](https://discord.gg/uGWfQY4dj4)",
                inline=False
            )
            emb.set_footer(text=f"Bot is running {version}")

        # block called when one cog-name is given
        # trying to find matching cog and it's commands
        elif len(input) == 1:

            # iterating trough cogs
            for cog in self.bot.cogs:
                # check if cog is the matching one
                if cog.lower() == input[0].lower():

                    # making title - getting description from doc-string below class
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                        color=discord.Color.green())

                    # getting commands from cog
                    for command in self.bot.get_cog(cog).get_commands():
                        # if cog is not hidden
                        if not command.hidden:
                            emb.add_field(
                                name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    # found cog - breaking loop
                    break

            # if input not found
            # yes, for-loops have an else statement, it's called when no 'break' was issued
            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{input[0]}` before :scream:",
                                    color=discord.Color.orange())

        # too many cogs requested - only one at a time allowed
        elif len(input) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once :sweat_smile:",
                                color=discord.Color.orange())

        else:
            emb = discord.Embed(title="It's a magical place.",
                                description="I don't know how you got here. But I didn't see this coming at all.\n"
                                            "Would you please be so kind to report that issue to me on github?\n"
                                            "https://github.com/pvcodes/pi_bot/issues\n"
                                            "Thank you! ~Chris",
                                color=discord.Color.red())

        # sending reply embed using our own function defined above
        await _sendEmbed(ctx, emb)


def setup(bot):
    bot.add_cog(Help(bot))
