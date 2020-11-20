import discord
import os
import datetime
from discord.ext import commands


prefix = ['n!', 'N!']
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')





@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Discord.py | n!help'))
    print('BOT is online')



# L O A D
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
    await ctx.send('Reloaded successfully!')




@commands.has_permissions(manage_messages=True)
@commands.is_owner()
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):  # tìm những file có đuôi .py
        client.load_extension(f'cogs.{filename[:-3]}')   # "-3" bỏ đuôi .py khi try cập vào file






client.run('NzIzMzgyNzE2MzMwMDE2Nzc5.Xuw0sA.iVHWqs1RLFTBcYDBnPSJBgchlfQ')
