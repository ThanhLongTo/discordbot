import discord
from discord.ext import commands
from discord.ext.commands import CheckFailure


class Example2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            author = ctx.message.author

            MissingRequiredArgument_embed = discord.Embed(
                color=discord.Color.red(),
                description='**Missing Required Argument**'
            )

            MissingRequiredArgument_embed.set_author(name=f'{author.name}#{author.discriminator}', icon_url=f'{author.avatar_url}')
            MissingRequiredArgument_embed.add_field(name='Instruction:', value='n!help')

            await ctx.send(embed=MissingRequiredArgument_embed)




        elif isinstance(error, commands.CommandNotFound):
            author = ctx.message.author

            CommandNotFound_embed = discord.Embed(
                color=discord.Color.red(),
                description='**Command Not Found**'
            )

            CommandNotFound_embed.set_author(name=f'{author.name}#{author.discriminator}', icon_url=f'{author.avatar_url}')
            CommandNotFound_embed.add_field(name='Instruction:', value='n!help')
            await ctx.send(embed=CommandNotFound_embed)

        elif isinstance(error, commands.ArgumentParsingError):
            author = ctx.message.author

            ArgumentParsingError_embed = discord.Embed(
                color=discord.Color.red(),
                description='**Argument Parsing Error*'
            )

            ArgumentParsingError_embed.set_author(name=f'{author.name}#{author.discriminator}',
                                             icon_url=f'{author.avatar_url}')
            ArgumentParsingError_embed.add_field(name='Instruction:', value='n!help')
            await ctx.send(embed=ArgumentParsingError_embed)





        elif isinstance(error, commands.MissingPermissions):
            author = ctx.message.author

            MissingPermissions_embed = discord.Embed(
                color=discord.Color.red(),
                description='**Missing Permissions**'
            )

            MissingPermissions_embed.set_author(name=f'{author.name}#{author.discriminator}',
                                             icon_url=f'{author.avatar_url}')
            MissingPermissions_embed.add_field(name='Instruction:', value='n!help')

            await ctx.send(embed=MissingPermissions_embed)


        
        elif isinstance(error, commands.ExtensionNotFound):
            author = ctx.message.author

            ExtensionNotFound_embed = discord.Embed(
                color=discord.Color.red(),
                description='**Extension Not Found**'
            )

            ExtensionNotFound_embed.set_author(name=f'{author.name}#{author.discriminator}',
                                                icon_url=f'{author.avatar_url}')


            await ctx.send(embed=ExtensionNotFound_embed)

        elif isinstance(error, commands.CommandOnCooldown):
            author = ctx.message.author

            CommandOnCoolDown_embed = discord.Embed(
                color=discord.Color.red(),
                description=f'**Command On Cooldown**'
            )

            CommandOnCoolDown_embed.set_author(name=f'{author.name}#{author.discriminator}',
                                               icon_url=f'{author.avatar_url}')
            CommandOnCoolDown_embed.add_field(name='Instruction:', value=f'*Try again after {error.retry_after}s*\n\n`n!help`')

            await ctx.send(embed=CommandOnCoolDown_embed)

        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send('Agurment Parsing error')
        elif isinstance(error, commands.NoEntryPointError):
            await ctx.send('No entry point error')
        elif isinstance(error, commands.UnexpectedQuoteError):
            await ctx.send('Unexpected quote error')





        else:
            author = ctx.message.author

            Unknown_embed = discord.Embed(
                color=discord.Color.red(),
                description='**UNIDENTIFIED ERROR**',

            )

            Unknown_embed.set_author(name=f'{author.name}#{author.discriminator}',
                                               icon_url=f'{author.avatar_url}')
            Unknown_embed.add_field(name='Explanation:', value=' + This error occurs when some elements crashed while running the bot ( with variety of unknown error) or maybe this is the problem of creator while building the bot. SORRY!\n + However,  you should check your input value following the instruction and be sure that you typed correctly!', inline=False)
            Unknown_embed.add_field(name='Instruction:', value='n!help')

            await ctx.send(embed=Unknown_embed)







def setup(client):
    client.add_cog(Example2(client))