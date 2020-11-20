import discord
from discord.ext import commands



class Example2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            author = ctx.message.author

            MissingRequiredArgument_embed = discord.Embed(
                color=discord.Color.red(),

            )
            MissingRequiredArgument_embed.set_author(name='Missing Required Argument', icon_url='https://emoji.gg/assets/emoji/6982_NotixDeny.png')

            #MissingRequiredArgument_embed.set_author(name=f'{author.name}#{author.discriminator}', icon_url=f'{author.avatar_url}')
            MissingRequiredArgument_embed.add_field(name='Instruction:', value='`help`')

            message = await ctx.send(embed=MissingRequiredArgument_embed)

            await message.add_reaction('❌')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '❌'

            await self.client.wait_for('reaction_add', check=check)
            await message.delete()

        elif isinstance(error, commands.CommandNotFound):
            author = ctx.message.author

            CommandNotFound_embed = discord.Embed(
                color=discord.Color.red(),

            )
            CommandNotFound_embed.set_author(name='Command Not Found',
                                                     icon_url='https://emoji.gg/assets/emoji/6982_NotixDeny.png')

            #CommandNotFound_embed.set_author(name=f'{author.name}#{author.discriminator}', icon_url=f'{author.avatar_url}')
            CommandNotFound_embed.add_field(name='Instruction:', value='`help`')
            message = await ctx.send(embed=CommandNotFound_embed)

            await message.add_reaction('❌')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '❌'

            await self.client.wait_for('reaction_add', check=check)
            await message.delete()

        elif isinstance(error, commands.ArgumentParsingError):
            author = ctx.message.author

            ArgumentParsingError_embed = discord.Embed(
                color=discord.Color.red(),
                description='**Argument Parsing Error*'
            )

            #ArgumentParsingError_embed.set_author(name=f'{author.name}#{author.discriminator}',
                                             #icon_url=f'{author.avatar_url}')
            ArgumentParsingError_embed.add_field(name='Instruction:', value='`help`')
            message = await ctx.send(embed=ArgumentParsingError_embed)

            await message.add_reaction('❌')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '❌'

            await self.client.wait_for('reaction_add', check=check)
            await message.delete()





        elif isinstance(error, commands.MissingPermissions):
            author = ctx.message.author

            MissingPermissions_embed = discord.Embed(
                color=discord.Color.red(),

            )

            MissingPermissions_embed.set_author(name=f'Missing Permission',
                                             icon_url=f'https://emoji.gg/assets/emoji/6982_NotixDeny.png')
            MissingPermissions_embed.add_field(name='Instruction:', value='`help`')

            message = await ctx.send(embed=MissingPermissions_embed)

            await message.add_reaction('❌')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '❌'

            await self.client.wait_for('reaction_add', check=check)
            await message.delete()


        
        elif isinstance(error, commands.ExtensionNotFound):
            author = ctx.message.author

            ExtensionNotFound_embed = discord.Embed(
                color=discord.Color.red(),
                description='**Extension Not Found**'
            )

            #ExtensionNotFound_embed.set_author(name=f'{author.name}#{author.discriminator}',
                                                #icon_url=f'{author.avatar_url}')


            message = await ctx.send(embed=ExtensionNotFound_embed)

            await message.add_reaction('❌')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '❌'

            await self.client.wait_for('reaction_add', check=check)
            await message.delete()

        elif isinstance(error, commands.CommandOnCooldown):
            author = ctx.message.author

            CommandOnCoolDown_embed = discord.Embed(
                color=discord.Color.red(),

            )

            CommandOnCoolDown_embed.set_author(name=f'Command on Cooldown',
                                               icon_url=f'https://emoji.gg/assets/emoji/6982_NotixDeny.png')
            CommandOnCoolDown_embed.add_field(name='-', value=f'***WebFinder need to rest !...** Try again after __{round(error.retry_after, 2)}__ second(s)*')

            message = await ctx.send(embed=CommandOnCoolDown_embed)

            await message.add_reaction('❌')

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '❌'

            await self.client.wait_for('reaction_add', check=check)
            await message.delete()

        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send('Agurment Parsing error')
        elif isinstance(error, commands.NoEntryPointError):
            await ctx.send('No entry point error')
        elif isinstance(error, commands.UnexpectedQuoteError):
            await ctx.send('Unexpected quote error')
        else:
            other_embed = discord.Embed(
                color=discord.Color.red(),

            )

            other_embed.set_author(name='Something went wrong, an error occurred',
                                                     icon_url='https://emoji.gg/assets/emoji/6982_NotixDeny.png')

            await ctx.send(embed=other_embed)


















def setup(client):
    client.add_cog(Example2(client))