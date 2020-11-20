import discord
from discord.ext import commands
import datetime


class Ads(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def about(self, ctx):
        author = ctx.message.author

        ads_embed = discord.Embed(
            title='Advertisement',
            description='''
`TechNo#9240` is a bot of `Nautilus#3374`. 
    It is mostly used for Math calculations and equations solver, with the support of :

 ▶ **HeroKu (*heroku.com*)**: a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

 ▶ **Git (*git-scm.com*)**: a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

 ▶ **Python (*python.org*)**: an interpreted, object-oriented, high-level programming language with dynamic semantics.

 ▶ **Github (*github.com*)**: the world's largest community of developers to discover, share, and build better software.
 ''',
            color=discord.Color.green(),
            timestamp=datetime.datetime.utcnow()
        )


        await ctx.send(embed=ads_embed)


        ads2_embed = discord.Embed(
            title='',
            description='',
            color=discord.Color.green(),
            timestamp=datetime.datetime.utcnow()
        )

        ads2_embed.set_author(name='If you like TechNo please find him on:', icon_url='https://img.icons8.com/ultraviolet/2x/info.png')
        ads2_embed.add_field(name='▶ Twitter: ',
                             value='https://twitter.com/Thanhlongto', inline=False)
        ads2_embed.add_field(name='▶ Pinterest: ',
                             value='https://www.pinterest.com/thanhlongto132/boards/', inline=False)
        ads2_embed.add_field(name='▶ Soundcloud: ',
                             value='https://soundcloud.com/thanh-long-to-515173298',inline=False)
        ads2_embed.add_field(name='▶ Discord: ',
                             value='Nautilus#3374 and his team https://discord.gg/CpPpK48',inline=False)
        ads2_embed.add_field(
            name='▶ Youtube: ',
            value='https://www.youtube.com/channel/UCWJmQFOS5AgdaouBAQYd1Cw?view_as=subscriber (sorry for no video :P)',inline=False)
        ads2_embed.set_image(url='https://i.pinimg.com/originals/a7/f1/fe/a7f1feb29d89e49cbf9569e297e45ad9.jpg')
        ads2_embed.set_footer(text='hello')



        await ctx.send(embed=ads2_embed)





def setup(client):
    client.add_cog(Ads(client))