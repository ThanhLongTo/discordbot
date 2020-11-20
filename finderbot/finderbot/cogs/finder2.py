import discord
from discord.ext import commands
import traceback
from discord.ext.commands import BucketType
from imdb import IMDb
from imdb import IMDbError
import requests
import time
from disputils import BotEmbedPaginator
import json


from bs4 import BeautifulSoup
import random
random_delay = [19, 20, 21, 22, 23, 24, 25]
ua_list = [
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Mozilla/5.0 (X11; Datanyze; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.24 Safari/537.36'
   ]

random_ua = random.choice(ua_list)

tag_list = ['/music', '/looking-for-game', '/moderation', '/fun', '/economy', '/music', '/moderation', '/fun', '/economy', '/anime', '/game', '/meme', '/social', '/leveling', '/roleplay', '/role-management', '/logging', '/web-dashboard', '/stream', '/crypto', '/media', '/turkish', '/soundboard', '/utility', '/customizable-behavior', '/pubg', '/rocket-league', '/fortnite', '/overwatch', '/csgo', '/osu!', '/minecraft', '/league-of-legends', '/warframe', '/diablo-iii', '/rust', '/dota-2', '/starcraft-2', '/factorio', '/runescape', '/apex-legends', '/looking-for-game', '/sneaker', '/pokemon', '/reddit', '/twitch', '/animal-crossing', '/valorant']
server_tag_list = ['/anime', '/gaming', '/roblox', '/roleplay', '/economy', '/meme', '/stream', '/social', '/fun', '/music', '/crypto', '/developer', '/api', '/kpop', '/emotes', '/support-server', '/sneaker', '/giveaway', '/dnd', '/lfg', '/ring-of-elysium', '/overwatch', '/rocket-league', '/osu!', '/minecraft', '/league-of-legends', '/warframe', '/diablo-iii', '/csgo', '/fortnite', '/pubg', '/dota-2', '/starcraft-2', '/factorio', '/rust', '/apex-legends', '/valorant', '/animal-crossing', '/fall-guys', '']

class Finder2(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 20, BucketType.user)
    async def movie(self, ctx, id):

        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:

            # creating instance of IMDb
            ia = IMDb()
            loading = await ctx.send('`Getting movie info..... Please wait!`')
            try:
                # search = ia.search_movie(name)
                search = ia.get_movie(id)
                release_date = ia.get_movie_release_dates(id)
                rd1 = release_date['data']
                rd2 = rd1['raw release dates']
                rd_list = []
                for rd3 in rd2:
                    country = rd3['country']
                    date = rd3['date']
                    rd_list.append(country.replace('\n', ': ') + date)
                    break

                final_release_date = ''.join(rd_list)
                runtime = search.data['runtimes']


                thumbnail = search['cover url']


                rating = search.data['rating']


                country = search.data['countries']


                language = search.data['languages']


                year = search['year']



                plot = search['plot']
                plot_list = []
                story_list = []
                if len(plot) == 1:

                    plot_list.append(plot[0])
                    story_list.append('-')
                if len(plot) > 1:

                    plot_list.append(plot[0])

                    story_list.append(plot[1][:plot[1].find(".::")])
                storyline = ''.join(story_list)


                genres_list = []
                for genres in search['genres']:
                    genres_list.append(genres)

                final_genres = ', '.join(genres_list)


                cast = search['cast']

                cast_list = []
                for casts in cast[:5]:
                    cast_list.append('- ' + casts['name'])


                if len(cast_list) < 5:
                    final_cast = '\n'.join(cast_list)
                else:
                    final_cast = '\n'.join(cast_list) + '\n....*and more*....'


                drt_list = []
                try:
                    for directors in search['directors']:
                        drt_list.append(directors['name'])

                except KeyError:
                    drt_list.append('-')


                final_drt = ', '.join(drt_list)



                imdb_embed = discord.Embed(
                    title=f'{search} | ({year})',
                    description=f'*.... {plot_list[0][:plot_list[0].find(".::")]}.....*',
                    color=discord.Color.dark_gold()
                )

                imdb_embed.add_field(name='Rating :', value=str(rating) + ' /10')
                imdb_embed.add_field(name='Length :', value=str(''.join(runtime)) + ' mins')
                imdb_embed.add_field(name='Release date :', value=final_release_date)
                imdb_embed.add_field(name='Genres :', value=final_genres)
                imdb_embed.add_field(name='Country/Language :', value=f'{country[0]} / {language[0]}')
                imdb_embed.add_field(name='Director :', value=final_drt)
                imdb_embed.add_field(name='Cast :', value=final_cast, inline=False)
                imdb_embed.add_field(name='Story line :', value=storyline, inline=False)
                imdb_embed.add_field(name='Find more at', value=f'https://www.imdb.com/title/tt{id}/',inline=False)
                imdb_embed.set_thumbnail(url=thumbnail)
                imdb_embed.set_footer(text='Movies | WebFinder v1.0',
                                      icon_url='https://cdn4.iconfinder.com/data/icons/small-n-flat/24/movie-alt2-512.png')

                await ctx.send(embed=imdb_embed)
                await loading.delete()

            #except BaseException as e:
                #await ctx.send(traceback.print_exc())
            except IndexError:
                print('')
            except IMDbError as IE:
                error_embed = discord.Embed(
                    description="**Movie not found!** Make sure that you typed the **ID** correctly",
                    color=discord.Color.red()
                )
                await ctx.send(embed=error_embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, BucketType.user)
    async def movie_search(self, ctx, *, name):

        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:

            loading = await ctx.send('`Searching for movies...... Please wait!`')
            ia = IMDb()
            search = ia.search_movie(name)

            result_list = []

            for i in range(len(search)):
                id = search[i].movieID
                kind = search[i].data['kind']
                year = search[i].data['year']
                result_list.append(f"**{search[i]['title']}** | ({year}) | {kind}\n- ID: `{id}`")

            movie_embed = discord.Embed(
                title=f'Movie search for : {name}',
                description='\n'.join(result_list),

            )

            movie_embed.set_footer(text='Movies | WebFinder v1.0',
                                   icon_url='https://cdn4.iconfinder.com/data/icons/small-n-flat/24/movie-alt2-512.png')

            await ctx.send(embed=movie_embed)
            await loading.delete()

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 20, BucketType.user)
    async def movie_top(self, ctx):

        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:

            loading = await ctx.send('`Loading top 50 best movies..... Please wait!`')
            ia = IMDb()
            top250 = ia.get_top250_movies()
            top_list = []
            i = 0
            for item in range(50):
                i += 1
                top_list.append(
                    f"**{i}. {top250[item]['title']}** |   {str(top250[item]['year'])}\n> ID: `{top250[item].getID()}`\n> Rating: `{str(top250[item]['rating'])} / 10`")

            top = '\n'.join(top_list[:25])
            top2 = '\n'.join(top_list[25:])

            movie_embed = discord.Embed(
                title=f'⇨ Top 50 best rated movies ⇦',
                description=top,
                color=discord.Color.dark_gold()
            )


            await loading.delete()
            movie2_embed = discord.Embed(
                description=top2,
                color=discord.Color.dark_gold()
            )
            movie2_embed.add_field(name='Find top 250 best movies at:', value='[Top 250 best rated movies on IMDb](https://www.imdb.com/chart/top/?ref_=nv_mv_250)')
            movie2_embed.set_footer(text='Movies | WebFinder v1.0',
                                    icon_url='https://cdn4.iconfinder.com/data/icons/small-n-flat/24/movie-alt2-512.png')

            pages = [movie_embed, movie2_embed]
            paginator = BotEmbedPaginator(ctx, pages)
            await paginator.run()

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 15, BucketType.user)
    async def people_search(self, ctx, *, query):
        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:

            loading = await ctx.send('`Finding people..... Please wait!`')
            ia = IMDb()

            search = ia.search_person(query)

            cast_list = []
            for i in range(len(search)):
                name = search[i]['name']
                id = search[i].personID
                cast_list.append(f'- **{name}** | ID: `{id}`')

            final_cast = '\n'.join(cast_list)

            cast_embed = discord.Embed(
                title=f'People search for : {query}',
                description=final_cast
            )

            cast_embed.set_footer(text='People | WebFinder v1.0',
                                  icon_url='https://cdn4.iconfinder.com/data/icons/small-n-flat/24/movie-alt2-512.png')

            await ctx.send(embed=cast_embed)
            await loading.delete()

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 20, BucketType.user)
    async def people(self, ctx, id):

        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)
        else:
            ia = IMDb()
            try:
                loading = await ctx.send('`Getting person info..... Please wait!`')
                julia = ia.get_person(id)



                thumbnail = julia['headshot']

                general = ''.join(julia['biography'])[:''.join(julia['biography']).find('.::')]
                general_list = general.split('.')
                biography = '. '.join(general_list[:3])



                movies_list = []

                for job in julia['filmography']:
                    for role in job:


                        title_list = []
                        for movies in job[role][:3]:

                            title_list.append(movies['title'])
                        if len(job[role]) > 1:
                            movies_list.append(
                                f'**- {role.title()} ({len(job[role])} credits):** ' + ', '.join(title_list).replace('()',
                                                                                                                     '') + ',.....')
                        if len(job[role]) < 2:
                            movies_list.append(
                                f'**- {role.title()} ({len(job[role])} credit):** ' + ', '.join(title_list).replace('()', ''))

                description = '\n'.join(movies_list)


                info_embed = discord.Embed(
                    title=julia['name'],
                    description=f'**---------BIOGRAPHY---------**\n*{biography}*\n**---------FILMOGRAPHY---------**\n' + description,
                    color=discord.Color.dark_gold()
                )
                info_embed.add_field(name='Find more at:', value=f'https://www.imdb.com/name/nm{id}/',inline=False)

                info_embed.set_footer(text='People | WebFinder v1.0',
                                      icon_url='https://cdn4.iconfinder.com/data/icons/small-n-flat/24/movie-alt2-512.png')
                info_embed.set_thumbnail(url=thumbnail)
                await ctx.send(embed=info_embed)
                await loading.delete()


            except IMDbError as IE:

                error_embed = discord.Embed(

                    description="**Person not found!** Make sure that you typed the **ID** correctly",

                    color=discord.Color.red()

                )

                await ctx.send(embed=error_embed)

            except BaseException as e:
                await ctx.send(traceback.print_exc())



    @commands.command()
    @commands.guild_only()
    async def twitch(self, ctx, *, query):
        url = f'https://www.twitch.tv/{query}'
        await ctx.send(url)
        twtich_embed2 = discord.Embed(
            title="Didn't find your request ?",
            description='Try `twitch_drt [search keyword]` to get more results from Twitch',
            color=discord.Color.gold()
        )
        message = await ctx.send(embed=twtich_embed2)
        await message.add_reaction('❌')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '❌'

        await self.client.wait_for('reaction_add', check=check)
        await message.delete()

    @commands.command()
    @commands.guild_only()
    async def twitch_drt(self,ctx,*,query):
        url = f'https://www.twitch.tv/search?term={query.replace(" ", "%20")}'

        twitch_embed = discord.Embed(
            title=f'{self.client.user} has found results for "{query}" !',

            color=discord.Color.purple()
        )

        twitch_embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        twitch_embed.add_field(name=f'‎‏‏‎ ',
                             value=f'\nClick the link below to view the direct search from Twitch\n **[Twitch search: {query}]({url})**')
        twitch_embed.set_footer(text='Twitch | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/356/356001.png')

        await ctx.send(embed=twitch_embed)



    @commands.command()
    @commands.guild_only()
    async def twitter(self, ctx, *, query):
        url = f'https://twitter.com/{query}'
        await ctx.send(url)
        embed = discord.Embed(
            title="Didn't find your request ?",
            description='Try `twitter_drt [search keyword]` to get more results from Twitter',
            color=discord.Color.gold()
        )
        message = await ctx.send(embed=embed)
        await message.add_reaction('❌')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '❌'

        await self.client.wait_for('reaction_add', check=check)
        await message.delete()


    @commands.command()
    @commands.guild_only()
    async def twitter_drt(self, ctx, *, query):
        url = f'https://twitter.com/search?q={query.replace(" ", "%20")}&src=typed_query'
        url2 = f'https://twitter.com/search?q={query.replace(" ", "%20")}&src=typed_query&f=user'

        twitch_embed = discord.Embed(
            title=f'{self.client.user} has found results for "{query}" !',

            color=discord.Color.blue()
        )

        twitch_embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        twitch_embed.add_field(name=f'‎‏‏‎ ',
                               value=f'\nClick the link below to view the direct search from Twitter\n **[Twitter search: {query}]({url})** or **[Twitter user search: {query}]({url2})**')
        twitch_embed.set_footer(text='Twitter| WebFinder v1.0',
                                icon_url='https://image.flaticon.com/icons/png/128/1383/1383265.png')
        await ctx.send(embed=twitch_embed)


    @commands.command()
    @commands.guild_only()
    async def artsandculture(self, ctx):
        url = 'https://artsandculture.google.com'
        embed = discord.Embed(
            title='Bringing the world’s art and culture online for everyone',
            description=f'*[Google Arts & Culture]({url}) is a non-profit initiative. We work with cultural institutions and artists around the world. Together, our mission is to preserve and bring the world’s art and culture online so it’s accessible to anyone, anywhere....*',
            color=discord.Color.green()
        )
        embed.set_author(name='Google Arts & Culture', icon_url='https://img.icons8.com/bubbles/2x/google-logo.png')
        embed.add_field(name='[1] . Where will you start ?', value='- From the suffragettes who fought for women’s rights, to performing arts at the Paris Opera, to NASA’s archive of stunning images, discover stories about our cultural heritage.',inline=False)
        embed.add_field(name='[2] . Zoom into a masterpiece', value='- Discover hidden details in the world’s greatest treasures with ultra high-resolution images, and enjoy in-painting tours curated by experts.', inline=False)
        embed.add_field(name='[3] . As if you were there in person', value='''
- Travel to iconic landmarks, step inside museums from around the world and take virtual tours with Street View.
**- Art Projector :** See real-size artworks in augmented reality right in front of you, wherever you are.
**- Art Palette :** Take a photo to find its color match in art history.
**- In-painting-tours :** Let curators inspire you through guided tours of paintings. 
**- Art Selfie :** Discover portraits that look like you.
**- Culture in 360° :** See heritage come to life and step right into the action. 
**- Art Transfer :** Transform your photo in the style of an iconic artist.
**- Nearby :** Find museums and cultural events around you.''', inline=False)
        embed.add_field(name='[4] . Experiments', value='Explore the crossroads between culture and emerging tech. Try out experiments created at our Lab by engineers, artists, curators and creative coders.', inline=False)
        embed.add_field(name='-', value=f'[Explore the website !]({url})',inline=False)
        embed.set_image(url='https://lh3.googleusercontent.com/BieNVS75RLyfjvclNkui0r8E4nf8J_pxn2Es1dCcr_PSnYbOeN0-cIBuMNpz6WbVQzQw4LAhkyITUqXgo2FJqF-9m_fMEsK937um_f0=w1000-h800')
        embed.set_footer(text='Art & Culture | WebFinder v1.0')
        await ctx.send(embed=embed)



    @commands.command()
    @commands.guild_only()
    async def news(self, ctx):
        cnn = 'https://edition.cnn.com/world'
        fox = 'https://www.foxnews.com/world'
        nyt = 'https://www.nytimes.com/section/world'
        gg = 'https://news.google.com/'
        yahoo = 'https://news.yahoo.com/world/'
        try:
            embed = discord.Embed(
                title='Top 5 most popular website to get world news. Just for YOU !',
                color=discord.Color.from_rgb(158, 243, 206)
            )
            embed.add_field(name='1. Google News :', value='> Google News is a news aggregator service developed by Google. It presents a continuous flow of articles organized from thousands of publishers and magazines. Google News is available as an app on Android, iOS, and the Web.\n> Link: ' + gg,inline=False)
            embed.add_field(name='2. Yahoo! News :', value='> Yahoo! News is a news website that originated as an internet-based news aggregator by Yahoo!. The site was created by a Yahoo! software engineer named Brad Clawsie in August 1996.\n> Link: '+yahoo, inline=False)
            embed.add_field(name='3. CNN :', value="> CNN (Cable News Network) is an American news-based pay television channel owned by CNN Worldwide, a unit of the WarnerMedia News & Sports division of AT&T's WarnerMedia. CNN was founded in 1980 by American media proprietor Ted Turner and Reese Schonfeld as a 24-hour cable news channel.\n> Link: " + cnn, inline=False)
            embed.add_field(name='4. The New York Times :', value='> The New York Times is an American newspaper based in New York City with worldwide influence and readership. Nicknamed the Gray Lady, the Times has long been regarded within the industry as a national "newspaper of record".\n> Link: '+nyt, inline=False)
            embed.add_field(name='5. Fox News :', value="> Fox News is an American multinational conservative cable news television channel. It is owned by Fox News Media, which itself is owned by the Fox Corporation. The channel broadcasts primarily from studios at 1211 Avenue of the Americas in New York City.\n> Link: "+fox, inline=False)
            embed.set_footer(text='NEWS | WebFinder v1.0', icon_url='https://img.icons8.com/ios-glyphs/2x/google-news.png')
            embed.set_thumbnail(url='https://img.icons8.com/dusk/2x/news.png')

            await ctx.send(embed=embed)

        except BaseException as e:
            await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    async def news_search(self,ctx, *, query):
        gg = f'https://news.google.com/search?q={query.replace(" ", "%20")}'
        yahoo = f'https://news.search.yahoo.com/search?p={query.replace(" ", "+")}'
        cnn = f'https://edition.cnn.com/search?q={query.replace(" ", "+")}'
        nyt = f'https://www.nytimes.com/search?query={query.replace(" ", "+")}'
        fox = f'https://www.foxnews.com/search-results/search?q={query.replace(" ", "%20")}'
        try:
            embed = discord.Embed(
                title='News search for " {} "'.format(query),
                description=f'**1. Google News :** {gg}\n**2. Yahoo! News :** {yahoo}\n**3. CNN :** {cnn}\n**4. The New York Times :** {nyt}\n**5. Fox News :** {fox}',
                color=discord.Color.from_rgb(158, 243, 206)
            )

            embed.set_footer(text='NEWS | WebFinder v1.0', icon_url='https://img.icons8.com/ios-glyphs/2x/google-news.png')
            embed.set_thumbnail(url='https://img.icons8.com/dusk/2x/news.png')
            await ctx.send(embed=embed)
        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.command()
    @commands.guild_only()
    async def reddit(self, ctx, *, query):
        url = f'https://www.reddit.com/r/{query}/'
        await ctx.send(url)
        embed = discord.Embed(
            title="Didn't find your request ?",
            description='Try `reddit_drt [search keyword]` to get more results from Reddit',
            color=discord.Color.gold()
        )
        message = await ctx.send(embed=embed)
        await message.add_reaction('❌')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '❌'

        await self.client.wait_for('reaction_add', check=check)
        await message.delete()

    @commands.command()
    @commands.guild_only()
    async def reddit_drt(self, ctx, *, query):
        url = f'https://www.reddit.com/search/?q={query.replace(" ", "%20")}'
        url2 = f'https://www.reddit.com/search/?q={query.replace(" ", "%20")}&type=sr%2Cuser'

        twitch_embed = discord.Embed(
            title=f'{self.client.user} has found results for "{query}" !',

            color=discord.Color.from_rgb(255, 89, 38)
        )

        twitch_embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        twitch_embed.add_field(name=f'‎‏‏‎ ',
                               value=f'\nClick the link below to view the direct search from Reddit\n **[Reddit search: {query}]({url})** or **[Reddit user search: {query}]({url2})**')
        twitch_embed.set_footer(text='Reddit| WebFinder v1.0',
                                icon_url='https://image.flaticon.com/icons/png/128/1409/1409938.png')
        await ctx.send(embed=twitch_embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def sc_top_genre(self, ctx, genre):

        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:
            try:
                loading = await ctx.send('`Loading top 10 most played soundtracks..... Please wait`')
                random_ua = random.choice(ua_list)
                headers = {
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': random_ua,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Referer': 'https://www.google.com/',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Accept-Language': 'en-US,en;q=0.9'}
                # query = input('search: ')
                url = f'https://soundcloud.com/charts/top?genre={genre}&country=all-countries'

                html = requests.get(url, headers=headers)

                soup = BeautifulSoup(html.content, 'html.parser')

                a = soup.find_all('a')


                list = a[47:87]
                title = []
                link = []
                for i in list:
                    b = i.get('href')

                    title.append(i.text)
                    link.append(b)



                # Title
                count = 0
                title_list = []
                while count < 31:
                    title_list.append(title[count])
                    count += 2



                # Artist name
                count2 = 1
                artist_list = []
                while count2 < 32:
                    artist_list.append(title[count2])

                    count2 += 2



                # Link
                count3 = 0
                link_list = []
                while count3 < 31:
                    link_list.append(link[count3])
                    count3 += 2



                # Artist link
                count2 = 1
                artist_link = []
                while count2 < 32:
                    artist_link.append(link[count2])

                    count2 += 2



                count4 = 0
                final_link = []

                while count4 < 10:

                    title = title_list[:10][count4]
                    artist = artist_list[:10][count4]
                    link = link_list[:10][count4]
                    final = f'{count4 + 1}. **{title}** by **{artist}**\n> Artist link: https://soundcloud.com{artist_link[:10][count4]}\n> Link: https://soundcloud.com{link}'
                    final_link.append(final)

                    count4 += 1

                the_final = "\n".join(final_link)

                top_embed = discord.Embed(
                    title='Soundcloud top 10 most played tracks based on your genre',
                    description=the_final,
                    color=discord.Color.orange()
                )
                top_embed.set_footer(text='Soundcloud | WebFinder v1.0',
                                     icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')

                await loading.delete()
                await ctx.send(embed=top_embed)

            except BaseException as e:
                await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 20, BucketType.user)
    async def lyric(self, ctx, *, query):

        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:
            try:

                loading = await ctx.send('`Finding lyrics.... Please wait!`')
                channel = self.client.get_channel(747654328055103508)



                client_access_token = 'P38qSIpJ5gAWxvdS1o3cZ1b_KF2XYm1GJmw6GewjowVP1RFKBf5Uw_6_usz0DfQ6'
                base_url = 'https://api.genius.com'

                user_input = query.replace(" ", "-")

                path = 'search/'
                request_uri = '/'.join([base_url, path])


                params = {'q': user_input}

                token = 'Bearer {}'.format(client_access_token)
                headers = {'Authorization': token}

                r = requests.get(request_uri, params=params, headers=headers)

                loader = json.loads(r.content)

                await channel.send(loader['meta']['status'])

                if str(loader['response']['hits']) == '[]':
                    not_found = discord.Embed(
                        description='**Lyrics not found!** For an accurate result, please search with both **song name** and ** artist name**',
                        color=discord.Color.red()
                    )

                    message = await ctx.send(embed=not_found)
                    await message.add_reaction('❌')

                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) == '❌'

                    await self.client.wait_for('reaction_add', check=check)
                    await message.delete()




                else:
                    lyric_list = []
                    title0 = []
                    thumbnail0 = []
                    for i in loader['response']['hits']:
                        title = i['result']['full_title'].replace('\xa0', ' ')

                        title0.append(title)
                        api_lyric = 'https://genius.com' + i['result']['api_path']

                        thumbnail = i['result']['song_art_image_thumbnail_url']

                        thumbnail0.append(thumbnail)

                        lyric_list.append(api_lyric)
                        break

                    lyric_url = ''.join(lyric_list)


                    page = requests.get(lyric_url, headers=headers)
                    await channel.send(page.status_code)
                    html = BeautifulSoup(page.content, "html.parser")

                    lyrics2 = []

                    if 'None' in str(html.find('div', class_='lyrics')):

                        print(html.find_all('div',
                                            class_='SongPageGrid-sc-1vi6xda-0 DGVcp Lyrics__Root-sc-1ynbvzw-0 kkHBOZ'))

                        if '<a href' in str(html.find('div',
                                                   class_='SongPageGrid-sc-1vi6xda-0 DGVcp Lyrics__Root-sc-1ynbvzw-0 kkHBOZ')):
                            lyric_conv = html.find_all('div',
                                                       class_='SongPageGrid-sc-1vi6xda-0 DGVcp Lyrics__Root-sc-1ynbvzw-0 kkHBOZ')

                            for z in lyric_conv:
                                a = z.get('a').text

                                lyrics2.append(a)
                        elif '<a href' not in str(html.find('div',
                                                   class_='SongPageGrid-sc-1vi6xda-0 DGVcp Lyrics__Root-sc-1ynbvzw-0 kkHBOZ')):
                            a = html.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-2 jgQsqn')
                            for z in a:
                                print(z.text)
                                lyrics2.append(z.text)
                    elif 'None' not in str(html.find('div', class_='lyrics')):


                        lyric_conv = ((html.find('div',
                                                 class_='lyrics')).text).split('\n')
                        for z in lyric_conv:
                            lyrics2.append(z)


                    final_lyric = '\n'.join(lyrics2)

                    song_lyric = final_lyric.replace('[', '**[ ').replace(']', ' ]**')

                    lyric_list2 = song_lyric.split('\n')

                    if 4000 > len(song_lyric) > 2040:



                        lyric_part1 = '\n'.join(lyric_list2[:round(len(lyrics2)/2)])
                        lyric_part2 = '\n'.join(lyric_list2[round(len(lyrics2)/2):])

                        embed = discord.Embed(
                                title='' .join(title0),
                                description=lyric_part1,
                                color=discord.Color.from_rgb(118, 255, 178)
                            )

                        embed.set_thumbnail(url=''.join(thumbnail0))

                            #embed.set_footer(text='Lyrics | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/2907/2907004.png')


                        await loading.delete()

                        embed1 = discord.Embed(
                                description=lyric_part2,
                                color=discord.Color.from_rgb(118, 255, 178)
                        )

                        embed1.set_footer(text='Lyrics | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/2907/2907004.png')

                        embedpages = [embed, embed1]
                        paginator = BotEmbedPaginator(ctx, embedpages)
                        await paginator.run()


                    elif 6000 > len(song_lyric) > 4000:




                        lyric_part1 = '\n'.join(lyric_list2[:round(len(lyrics2)*(1/4))])


                        lyric_part2 = '\n'.join(lyric_list2[round(len(lyrics2)*(1/4)):round(len(lyrics2)*(2/4))])

                        lyric_part3 = '\n'.join(lyric_list2[round(len(lyrics2)*(2/4)):round(len(lyrics2)*(3/4))])

                        lyric_part4 = '\n'.join(lyric_list2[round(len(lyrics2)*(3/4)):round(len(lyrics2)*(4/4))])


                        embed = discord.Embed(
                                title='' .join(title0),
                                description=lyric_part1,
                                color=discord.Color.from_rgb(118, 255, 178)
                            )

                        embed.set_thumbnail(url=''.join(thumbnail0))

                            #embed.set_footer(text='Lyrics | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/2907/2907004.png')


                        await loading.delete()

                        embed1 = discord.Embed(
                                description=lyric_part2,
                                color=discord.Color.from_rgb(118, 255, 178)
                        )

                        embed2 = discord.Embed(
                            description=lyric_part3,
                            color=discord.Color.from_rgb(118, 255, 178)
                        )

                        embed3 = discord.Embed(
                            description=lyric_part4,
                            color=discord.Color.from_rgb(118, 255, 178)
                        )
                        embed3.set_footer(text='Lyrics | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/2907/2907004.png')



                        embedpages = [embed, embed1, embed2, embed3]
                        paginator = BotEmbedPaginator(ctx, embedpages)
                        await paginator.run()


                    elif len(song_lyric) > 6000:
                        large = discord.Embed(
                            description='**The lyric is too long to display**',
                            color=discord.Color.red()
                        )

                        await ctx.send(embed=large)
                    elif len(song_lyric) < 2040:

                        embed = discord.Embed(
                                title=''.join(title0),
                                description=song_lyric,
                                color=discord.Color.from_rgb(118, 255, 178)
                        )
                        embed.set_thumbnail(url=''.join(thumbnail0))
                        embed.set_footer(text='Lyrics | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/2907/2907004.png')

                        await loading.delete()
                        await ctx.send(embed=embed)





            except BaseException as e:
                await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 20, BucketType.user)
    async def dis_server(self, ctx, *, filter):

        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:
            try:
                user = self.client.get_user(ctx.author.id)
                query = filter.lower()
                loading = await ctx.send('`Finding for servers..... Please wait`')
                random_ua = random.choice(ua_list)
                headers = {
                    'authority': 'top.gg',
                    'upgrade-Insecure-Requests': '1',
                    'user-Agent': random_ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'accept-Language': 'en-US,en;q=0.9'}

                url_list = []

                if query == 'top':
                    url = 'https://top.gg/servers/list/top'
                    url_list.append(url)
                elif query == 'new' or query == 'new server' or query == 'new servers':
                    url = 'https://top.gg/servers/list/new'
                    url_list.append(url)
                elif 'tag=' in query or 'tag =' in query:

                    finder = filter.lower().replace('tag=', '').replace('tag =', '').replace(' ', '')


                    if f'/{finder}' in tag_list:
                        url = 'https://top.gg/servers/tag/' + finder

                        url_list.append(url)

                    if f'/{finder}' not in tag_list:
                        error_embed = discord.Embed(
                            description='**Tag not found!** Make sure to check your spelling then try again',
                            color=discord.Color.red()
                        )
                        await ctx.send(embed=error_embed)




                else:

                    url = 'https://top.gg/servers/search?q=' + filter.replace(' ', '%20')
                    url_list.append(url)

                real_url = ''.join(url_list)

                html = requests.get(str(real_url), headers=headers)
                if html.status_code == 200:
                    print('Access')
                if html.status_code == 404:
                    print('not found')

                soup = BeautifulSoup(html.content, 'html.parser')

                a = soup.find_all('a')
                # print(a)
                name = []
                link = []
                for i in a[15:-14]:
                    b = i.get('href')
                    name.append(i.text.replace('\n', ''))

                    if str(b) != 'None' and str(b) != '/servers/me':
                        link.append(b)

                name2 = []
                for i in name:
                    i = i.replace(' ', '')
                    name2.append(i)




                link_list = []
                i = 0
                for a in link:
                    i += 1
                    link_list.append(f'`[{i}].` https://top.gg/servers' + a)
                    time.sleep(0.3)

                # print(link_list[:-5])
                if str(link_list) == '[]':
                    error_embed = discord.Embed(
                        description='**Servers not found!** Make sure to check your spelling then try again',
                        color=discord.Color.red()
                    )
                    await ctx.send(embed=error_embed)
                else:

                    user_send = discord.Embed(
                        description='**This result is long and for not annoying the channels, please check you DM for the result**!',
                        color=discord.Color.gold()
                    )

                    await ctx.send(embed=user_send)
                    for links in link_list[:10]:
                        await user.send(links)
                    await loading.delete()

                    await user.send(f'**View more here :** {"".join(url_list)}')

            except BaseException as e:
                await ctx.send(traceback.print_exc())

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 20, BucketType.user)
    async def dis_bot(self, ctx, *, filter):
        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:
            try:
                user = self.client.get_user(ctx.author.id)
                query = filter.lower()
                loading = await ctx.send('`Finding for BOTs..... Please wait`')
                random_ua = random.choice(ua_list)
                headers = {
                    'authority': 'top.gg',
                    'upgrade-Insecure-Requests': '1',
                    'user-Agent': random_ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'accept-Language': 'en-US,en;q=0.9'}

                url_list = []

                if query == 'top':
                    url = 'https://top.gg/list/top'
                    url_list.append(url)
                elif query == 'music':
                    url = 'https://top.gg/tag/music'
                    url_list.append(url)
                elif query == 'certified':
                    url = 'https://top.gg/list/certified'
                    url_list.append(url)
                elif query == 'new' or query == 'new bots' or query == 'new bot':
                    url = 'https://top.gg/list/new'
                    url_list.append(url)
                elif 'tag=' in query or 'tag =' in query:

                    finder = filter.lower().replace('tag=', '').replace('tag =', '').replace(' ', '')


                    if f'/{finder}' in tag_list:
                        url = 'https://top.gg/tag/' + finder

                        url_list.append(url)

                    if f'/{finder}' not in tag_list:
                        error_embed = discord.Embed(
                            description='**Tag not found!** Make sure to follow the tag code here : `help_tag_code`',
                            color=discord.Color.red()
                        )
                        await ctx.send(embed=error_embed)




                else:

                    url = 'https://top.gg/search?q=' + filter.replace(' ', '%20')
                    url_list.append(url)

                real_url = ''.join(url_list)

                html = requests.get(str(real_url), headers=headers)
                if html.status_code == 200:
                    print('Access')
                if html.status_code == 404:
                    print('not found')

                soup = BeautifulSoup(html.content, 'html.parser')

                a = soup.find_all('a')
                # print(a)
                name = []
                link = []
                for i in a[15:-7]:
                    b = i.get('href')
                    # print(i.text.replace('\n', ''))
                    name.append(i.text.replace('\n', ''))
                    # print(b)
                    link.append(b)



                count = 0
                link_list = []
                i = 0
                for a in link[:-5]:
                    if '/vote' not in a and '/tag/' not in a:
                        i += 1
                        link_list.append(f'`[{i}].` https://top.gg' + a)

                # print(link_list[:-5])
                if str(link_list) == '[]':
                    error_embed = discord.Embed(
                        description='**BOTs not found!** Make sure to check your spelling then try again',
                        color=discord.Color.red()
                    )
                    await ctx.send(embed=error_embed)
                else:
                    user_send = discord.Embed(
                        description='**This result is long and for not annoying the channels, please check you DM for the result**!',
                        color=discord.Color.gold()
                    )

                    await ctx.send(embed=user_send)


                    for links in link_list[:10]:
                        await user.send(links)
                        time.sleep(0.4)
                    await loading.delete()

                    await user.send(f'**View more here :** {"".join(url_list)}')

            except BaseException as e:
                await ctx.send(traceback.print_exc())

    @commands.command()
    @commands.is_owner()
    async def lyric_for_owner(self, ctx, *, query):

        file = open("blacklist.txt", "r")
        read = str(file.read())

        black_list = read.split('\n')

        file.close()

        if str(ctx.author.id) in black_list:
            black_list_embed = discord.Embed(
                description='**You are not able to use this command!** Contact the owner (`Nautilus#3374`) to solve this problem',
                color=discord.Color.dark_red()
            )
            await ctx.send(embed=black_list_embed)

        else:


            loading = await ctx.send('`Finding for lyrics.... Please wait!`')
            url = f'https://search.azlyrics.com/search.php?q={query.lower().replace(" ", "+")}'

            random_ua = random.choice(ua_list)
            headers = {
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': random_ua,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Accept-Language': 'en-US,en;q=0.9',
            }
            channel = self.client.get_channel(747654328055103508)
            html = requests.get(url, headers=headers)
            await channel.send(html.status_code)
            await channel.send(html)
            if html.status_code == 200:
                print('Successfully access')
                await channel.send('Access')
            elif html.status_code == 404:
                print('Not found')
                await channel.send('not found')
            else:
                await channel.send('Unidentified error')


            soup = BeautifulSoup(html.content, 'html.parser')

            link = []
            title = []
            # artist_list = []
            for i in soup.find_all('a'):

                a = i.get('href')
                tt = i.text
                if 'https://www.azlyrics.com/lyrics/' in a and '.html' in a:
                    print(a)

                    link.append(a)
                    title.append(tt)


            await channel.send(link)
def setup(client):
    client.add_cog(Finder2(client))