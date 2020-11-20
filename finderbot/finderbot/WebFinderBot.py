import discord
import os
import datetime
from discord.ext import commands


prefix = ['w;', 'W;', 'webfinder ', 'Webfinder ']
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='your requests | w;help'))
    print(f'{client.user} has connected')


@commands.has_permissions(manage_messages=True)
@commands.is_owner()
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@commands.has_permissions(manage_messages=True)
@commands.is_owner()
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('```bash\nReloaded successfully!\n```')


@commands.has_permissions(manage_messages=True)
@commands.is_owner()
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'): 
        client.load_extension(f'cogs.{filename[:-3]}')





client.run('NzQzMDMxNzY0MzAxMTE5NTI4.XzOwQQ.Hj81hbn9vhoVNHSXfNcSyS3vswQ')
