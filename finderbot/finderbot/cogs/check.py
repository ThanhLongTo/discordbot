import discord
from discord.ext import commands
import datetime
import json





class Check(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        #await self.client.process_commands(message)
        #print(message.content)
        if message.content[:2] == 'w;' or message.content[:2] == 'W;':
            try:
                id = message.author.id
                server_id = message.guild.id
                server_name = message.guild
                #print(server_name)
                #print(server_id)
                #print(id)

                now = datetime.datetime.utcnow()
                date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
                channel = self.client.get_channel(747078451802144918)     #bot-logs   in   Nautilus's server
                logs = f'{message.author} ({id}) used command from {server_name} : {server_id}'
                await channel.send(f'```css\n.{message.author} <{id}>  from  :{server_name} <{server_id}>        {date_time}\n```')

                afile = open('users.json', 'r')
                load = json.load(afile)
                if str(id) in load:
                    load[str(id)] = int(load[str(id)])+1

                    afile = open('users.json', 'w')
                    json.dump(load, afile, indent=2)
                    afile.close()

                    final = open('users.json', 'r')
                    #print(json.load(final))

                if str(id) not in load:
                    load[str(id)] = 1

                    afile = open('users.json', 'w')
                    json.dump(load, afile, indent=2)
                    afile.close()

                    final = open('users.json', 'r')
                    #print(json.load(final))

            except AttributeError as AE:


                error = discord.Embed(
                    title='Are you using commands in DM ?',
                    description='As I told you before, WebFinder disabled you from using commands in DM (`except help commands`) to reduce errors caused by __bad users__.... So please use in the server!\n**Sorry for this inconvernience**',
                    color=discord.Color.gold()
                )

                user = self.client.get_user(message.author.id)
                message1 = await user.send(embed=error)

                await message1.add_reaction('❌')

                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) == '❌'

                await self.client.wait_for('reaction_add', check=check)
                await message1.delete()

def setup(client):
    client.add_cog(Check(client))