import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import traceback
import datetime
import json
from operator import itemgetter
from disputils import BotEmbedPaginator
import random


#logo_url = 'https://i.pinimg.com/originals/b4/c8/21/b4c821f068f5b87a11b1b3923c26f364.png'
logo_url = 'https://i.pinimg.com/originals/3a/b0/b3/3ab0b35ae418a7eefe36aec352acd153.png'
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def av(self, ctx, member: discord.Member):

        show_avatar = discord.Embed(
            color=discord.Color.blue()
        )
        show_avatar.set_author(name=f'{member.name}#{member.discriminator}')
        show_avatar.set_image(url="{}".format(member.avatar_url))
        show_avatar.set_footer(text=f'Avatar of {member}')
        await ctx.send(embed=show_avatar)

    @commands.command()
    async def ping(self, ctx):
        ping = discord.Embed(
            color=discord.Color.teal()
        )
        ping.set_author(name=f'Wassup {ctx.message.author} !', icon_url='https://emoji.gg/assets/emoji/3983_My_best_verified.gif')

        await ctx.send(embed=ping)

    @commands.command()
    @commands.guild_only()
    async def wumpus(self, ctx):

        random_wumpus = ['https://emoji.gg/assets/emoji/7957_WumpusPizza.png',
                         'https://emoji.gg/assets/emoji/7912_WumpusPing.png',
                         'https://emoji.gg/assets/emoji/1147_WumpusHeart.png',
                         'https://emoji.gg/assets/emoji/5574_WumpusGamer.png',
                         'https://emoji.gg/assets/emoji/5864_WumpusCrown.png',
                         'https://emoji.gg/assets/emoji/8074_WumpusCozy.png',
                         'https://emoji.gg/assets/emoji/7232_WumpusCookie.png',
                         'https://emoji.gg/assets/emoji/9852_wumpus.png',
                         'https://emoji.gg/assets/emoji/8366_WumpusHype.gif',
                         'https://emoji.gg/assets/emoji/9950_WumpusKeyboardSlam.gif',
                         'https://emoji.gg/assets/emoji/1127_wumpushotdog.png',
                         'https://emoji.gg/assets/emoji/2861_wumpusshrimp.png',
                         'https://emoji.gg/assets/emoji/2184_wumpus_color_gif.gif',
                         'https://emoji.gg/assets/emoji/3519_MarioWumpus.png',
                         'https://emoji.gg/assets/emoji/WumpusNitro.png',
                         'https://emoji.gg/assets/emoji/WumpusPlus.png',
                         'https://emoji.gg/assets/emoji/7145_BasicWumpus.png']
        wumpus_name = ['Wumpus Pizza', 'Wumpus Ping', 'Wumpus Heart', 'Wumpus Gamer', 'Wumpus Crown', 'Wumpus Cozy', 'Wumpus Cookie', 'Wumpus Nitro', 'Wumpus Hype', 'Wumpus Keyboard Slam','Wumpus hot dog',
                       'Wumpus shrimp', 'Wumpus Hype', 'Wumpus Mario', 'Wumpus Nitro Booster', 'Wumpus Plus', 'Wumpus Basic']

        random_wumpus2 = random.choice(random_wumpus)


        wumpus = discord.Embed(
            color=discord.Color.blurple()
        )

        wumpus.set_author(name=f'{wumpus_name[random_wumpus.index(random_wumpus2)]}', icon_url='https://emoji.gg/assets/emoji/5564_Loading_Color.gif')
        wumpus.set_image(url=random_wumpus2)

        await ctx.send(embed=wumpus)

    @commands.command()
    async def help(self, ctx):
        try:
            embed = discord.Embed(
                title='HELP COMMAND',
                description='.....*Whenever you need help, I am here to listen*.....\n**Bot prefix :** `w;`',
                color=discord.Color.green()

            )
            embed.set_author(name='Here are available commands you can use', icon_url='https://emoji.gg/assets/emoji/4700_info.gif')
            embed.add_field(name='[1]. Main function : SEARCH', value='`help_search`', inline=False)
            embed.add_field(name='[2]. Info', value='`help_info`', inline=False)
            embed.add_field(name='[3]. Games', value='`help_games`', inline=False)
            embed.add_field(name='[4]. Support', value='`support [suggestions/complaints]` : Your suggestions/complaints will be directly send to the owner, so he can try hist best to improve the BOT.\n*NOTE : You must wait **1 hour** after you sent 2 supports*', inline=False)
            embed.add_field(name='[5]. Invite', value='`invite`', inline=False)
            embed.add_field(name='[6]. About', value='`about`', inline=False)
            embed.add_field(name='[7]. Fun', value='''
`av` , `wumpus` , `8ball` , `hacker`''')
            embed.add_field(name='NOTE: `WebFinder#9056` is slower than others Discord bot because it is a web search! Need more time to generate, parse links..... So please patient and sorry for this inconvenience!', value='....', inline=False)
            embed.set_thumbnail(url=logo_url)
            embed.set_footer(text='© WebFinder v1.0', icon_url=logo_url)

            await ctx.send(embed=embed)
        except BaseException as e:
            await ctx.send(traceback.print_exc())


    @commands.command()
    async def help_games(self, ctx):
        embed = discord.Embed(
            title='HELP GAMES',
            description='''
- `memory_game [level (1-5)]` : Play the memory game yourself
- `tictactoe [someone_to_play_with]` : Play tic tac toe against a user
- `hangman [someone_to_play_with]` : Play hangman with a user
- `guess` : Guess a random letter in alphabet or a number yourself
''',
            color=discord.Color.teal()
        )
        embed.set_footer(text='© WebFinder v1.0', icon_url=logo_url)
        embed.set_thumbnail(url=logo_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def help_info(self, ctx):
        embed= discord.Embed(
            title='HELP INFO',
            description='''
> `botinfo` : Get information of WebFinder
> `user_info [id/name]` : Get user information
> `server_info` : Get information of server that you are in
> `member_info [id/name]` : Get information of member in server
> `role_info [id/name]` : Get information of role in sevrer
> `channel_info [id/name]` : Get information of channel in server''',
            color=discord.Color.teal()
        )
        embed.set_footer(text='© WebFinder v1.0', icon_url=logo_url)
        embed.set_thumbnail(url=logo_url)
        await ctx.send(embed=embed)





    @commands.command()
    async def help_search(self, ctx):
        embed = discord.Embed(
            title='HELP SEARCH',
            description='Here are all search commands you can use!',
            color=discord.Color.orange()
        )

        embed.add_field(name='[1]. Google', value='''
> `gg [search]` : Get the link from Google search
> `gg_drt [search]` : Navigate directly to Google (*in case you want more results than only one*)''', inline=False)

        embed.add_field(name='[2]. Youtube', value='''
> `yt [search]` : Get the video link from Youtube 
> `yt_drt [search]` : Navigate directly to Youtube search (*in case you want more results than only one*)''', inline=False)


        embed.add_field(name='[3]. Wikipedia', value='''
> `wiki [search]` : Get the summary information from Wikipedia. NOT: Please sure your search information is existed in Wikipedia!
> `wiki_drt [search]` : Navigate directly to Wikipedia (*in case you did not find your exact result*)''', inline=False)


        embed.add_field(name='[4]. Soundcloud', value='''
> `sc [search]` : Get the link from Soundcloud search
> `sc_top` : Get the top 10 most played tracks
> `sc_top_genre [genre] [search]` : Get top 10 most played tracks based on genre. (*`help_genre` to get all genres can use to search*)
> `sc_user [username]` : Get the list of user with your input name
> `sc_list [number_of_list] [search]` : Get the list of links based on your keyword. NOTE: Limit number is **10**
> `sc_playlist [number_of_playlist] [search]]` : Get the list of playlists based on your keyword. NOTE: Limit number is **10**
> `sc_drt [search]` : Navigate directly to Soundcloud (*in case you did not find what you wanted*)''', inline=False)

        embed.add_field(name='[5]. Songs lyrics', value='''
> `lyric [song]` : Get the lyric of song
''')

        embed.add_field(name='[6]. Discord BOTs/ servers', value='''
> `dis_bot/dis_server [search]` : Search for Discord bots
> `dis_bot/dis_server [top/ music/ certified/ new]` : Get top most popular Discord bots based on the your selection
> `dis_bot/dis_server tag=[choose_your_tag]` : Search for bots based on your given tag. NOTE: `help_tag_code` to find available tags''',
                         inline=False)

        embed.add_field(name='[7]. Movie', value='''
> `movie_search [search]` : Get list of movie name and **ID**
> `movie [ID_of_movie]` : Get information of the movie based on the **ID**
> `movie_top` : Get top 50 best rated movies
> `people_search [search]` : Get list of people name and **ID**
> `people [ID_of_people]` : Get information of the person based on the **ID**
''', inline=False)






        embed2 = discord.Embed(

            color=discord.Color.orange()
        )

        embed2.add_field(name='[8]. Weather', value='''
> `weather [city]` : Get weather information of the city
> `weather_country [country_name]` : Get weather of the capital city of country (*in case the `weather` command did not work*)''',
                         inline=False)

        embed2.add_field(name='[9]. NEWS', value='''
> `news` : Show the top 5 most popular website to get news around the world
> `news_search` : Search for news on top 5 most popular website''', inline=False)

        embed2.add_field(name='[10]. Other website: Twitch/ Twitter/ Reddit', value='''
> `Other_website [username]` : Get profile based on username
> `Other_website_drt [username]` : Navigate directly to website (*in case you didn't find what you want*)
> `artsandculture` : Explore historic events and culture all over the world! *Anytime, anywhere*......''')

        embed2.add_field(name='[11]. Translator', value='''
> `tr [language_code] [text]` : Translate the text
>  NOTE: `help_lang_code` to see full language code you can use''', inline=False)

        embed2.add_field(name='[12]. Dictionary', value='''
> `dict [word]` : Get definition of word in English (*if you d not understand, use `translator` to translate the definition to your language*)''',
                         inline=False)

        embed2.add_field(name='PRO TIPS :',
                         value='**If you did not find your result in Twitch or Youtube,.......! Try `gg ` or `gg_drt ` and insert what website you want to find in (Youtube, Twitter,...)**\n- Example: gg Donald Trump twitter, gg_drt Davie504 Reddit, gg_drt weather in paris,....')
        embed2.set_footer(text='© WebFinder v1.0', icon_url=logo_url)



        pages = [embed, embed2]
        #await ctx.send(embed=response)
        paginator = BotEmbedPaginator(ctx, pages)
        await paginator.run()


    @commands.command()
    async def help_genre(self, ctx):
        embed = discord.Embed(
            title='Available genres code for top Soundcloud search',
            description='''
```css
#MUSIC_GENRES_CODE : all-music,  all-audio,  alternativerock,  ambient,  classical,  country,  danceedm,  dancehall,  deephouse,  disco,  drumbass,  dubstep,  electronic ,  folksingersongwriter ,  hiphoprap ,  house ,  indie ,  jazzblues ,  latin ,  metal ,  piano ,  pop ,  rbsoul ,  reggae ,  reggaeton ,  rock ,  soundtrack ,  techno ,  trance ,  trap ,  triphop,  world
```''',

        )
        embed.set_footer(text='© WebFinder v1.0', icon_url=logo_url)

        await ctx.send(embed=embed)


    @commands.command()
    async def help_tag_code(self, ctx):
        embed = discord.Embed(
            title='Available tags code for Discord bots/ servers search',
            description='''
```css
#BOTS_TAG_CODE : music, looking-for-game, moderation, fun, economy, music, moderation, fun, economy, anime, game, meme, social, leveling, roleplay, role-management, logging, web-dashboard, stream, crypto, media, turkish, soundboard, utility, customizable-behavior, pubg, rocket-league, fortnite, overwatch, csgo, osu!, minecraft, league-of-legends, warframe, diablo-iii, rust, dota-2, starcraft-2, factorio, runescape, apex-legends, looking-for-game, sneaker, pokemon, reddit, twitch, animal-crossing, valorant

#SERVERS_TAG_CODE : anime, gaming, roblox, roleplay, economy, meme, stream, social, fun, music, crypto, developer, api, kpop, emotes, support-server, sneaker, giveaway, dnd, lfg, ring-of-elysium, overwatch, rocket-league, osu!, minecraft, league-of-legends, warframe, diablo-iii, csgo, fortnite, pubg, dota-2, starcraft-2, factorio, rust, apex-legends, valorant, animal-crossing, fall-guys
```'''
        )



        await ctx.send(embed=embed)




    @commands.command()
    async def help_lang_code(self, ctx):
        lang_code_embed = discord.Embed(
            title='Available language code for translation ( ISO 639-1 CODES )',
            description='''
    ```css
    ab: Abkhaz
    aa: Afar
    af: Afrikaans
    ak: Akan
    sq: Albanian
    am: Amharic
    ar: Arabic
    an: Aragonese
    hy: Armenian
    as: Assamese
    av: Avaric
    ae: Avestan
    ay: Aymara
    az: Azerbaijani
    bm: Bambara
    ba: Bashkir
    eu: Basque
    be: Belarusian
    bn: Bengali
    bh: Bihari
    bi: Bislama
    bs: Bosnian
    br: Breton
    bg: Bulgarian
    my: Burmese
    ca: Catalan; Valencian
    ch: Chamorro
    ce: Chechen
    ny: Chichewa; Chewa; Nyanja
    zh-CN: Chinese (simplified)
    cv: Chuvash
    kw: Cornish
    co: Corsican
    cr: Cree
    hr: Croatian
    cs: Czech
    da: Danish
    dv: Divehi; Maldivian;
    nl: Dutch
    dz: Dzongkha
    en: English
    eo: Esperanto
    et: Estonian
    ee: Ewe
    fo: Faroese
    fj: Fijian
    fi: Finnish
    fr: French
    ff: Fula
    gl: Galician
    ka: Georgian
    de: German
    el: Greek Modern
    gn: Guaraní
    gu: Gujarati
    ht: Haitian
    ha: Hausa
    he: Hebrew modern
    hz: Herero
    hi: Hindi
    ho: Hiri Motu
    ```
    '''

        )
        lang_code_embed.set_footer(text='page 1')


        lang_code1_embed = discord.Embed(

            description='''   
    ```css
    hu: Hungarian
    ia: Interlingua
    id: Indonesian
    ie: Interlingue
    ga: Irish
    ig: Igbo
    ik: Inupiaq
    io: Ido
    is: Icelandic
    it: Italian
    iu: Inuktitut
    ja: Japanese
    jv: Javanese
    kl: Kalaallisut
    kn: Kannada
    kr: Kanuri
    ks: Kashmiri
    kk: Kazakh
    km: Khmer
    ki: Kikuyu Gikuyu
    rw: Kinyarwanda
    ky: Kirghiz Kyrgyz
    kv: Komi
    kg: Kongo
    ko: Korean
    ku: Kurdish
    kj: Kwanyama Kuanyama
    la: Latin
    lb: Luxembourgish
    lg: Luganda
    li: Limburgish
    ln: Lingala
    lo: Lao
    lt: Lithuanian
    lu: Luba-Katanga
    lv: Latvian
    gv: Manx
    mk: Macedonian
    mg: Malagasy
    ms: Malay
    ml: Malayalam
    mt: Maltese
    mi: Māori
    mr: Marathi Marāṭhī
    mh: Marshallese
    mn: Mongolian
    na: Nauru
    nv: Navajo Navaho
    nb: Norwegian Bokmål
    nd: North Ndebele
    ne: Nepali
    ng: Ndonga
    nn: Norwegian Nynorsk
    no: Norwegian
    ii: Nuosu
    nr: South Ndebele
    oc: Occitan
    oj: Ojibwe Ojibwa
    cu: Old Church Slavonic
    om: Oromo
    or: Oriya
    os: Ossetian Ossetic
    ```
    '''
        )
        lang_code1_embed.set_footer(text='page 2')


        lang_code2_embed = discord.Embed(
            description='''   
    ```css
    pa: Panjabi Punjabi
    pi: Pāli
    fa: Persian
    pl: Polish
    ps: Pashto Pushto
    pt: Portuguese
    qu: Quechua
    rm: Romansh
    rn: Kirundi
    ro: Romanian Moldavan
    ru: Russian
    sa: Sanskrit Saṁskṛta
    sc: Sardinian
    sd: Sindhi
    se: Northern Sami
    sm: Samoan
    sg: Sango
    sr: Serbian
    gd: Scottish Gaelic
    sn: Shona
    si: Sinhala Sinhalese
    sk: Slovak
    sl: Slovene
    so: Somali
    st: Southern Sotho
    es: Spanish; Castilian
    su: Sundanese
    sw: Swahili
    ss: Swati
    sv: Swedish
    ta: Tamil
    te: Telugu
    tg: Tajik
    th: Thai
    ti: Tigrinya
    bo: Tibetan
    tk: Turkmen
    tl: Tagalog
    tn: Tswana
    to: Tonga
    tr: Turkish
    ts: Tsonga
    tt: Tatar
    tw: Twi
    ty: Tahitian
    ug: Uighur Uyghur
    uk: Ukrainian
    ur: Urdu
    uz: Uzbek
    ve: Venda
    vi: Vietnamese
    vo: Volapük
    wa: Walloon
    cy: Welsh
    wo: Wolof
    fy: Western Frisian
    xh: Xhosa
    yi: Yiddish
    yo: Yoruba
    za: Zhuang Chuang
    zu: Zulu
    ```'''
        )
        lang_code2_embed.set_footer(text='page 3')


        user = self.client.get_user(ctx.author.id)

        await user.send(embed=lang_code_embed)
        await user.send(embed=lang_code1_embed)
        await user.send(embed=lang_code2_embed)

        response = discord.Embed(
            description='**This result is long and for not annoying the channels, please check you DM for the result**!  `Make sue your dm is opening`',
            color=discord.Color.gold(),
            timestamp=datetime.datetime.utcnow()

        )

        response.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
        #response.set_thumbnail(url='https://image.flaticon.com/icons/png/128/3062/3062634.png')
        response.set_footer(text='© WebFinder v1.0', icon_url=logo_url)

        await ctx.send(embed=response)



    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, text):
        advice_list = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
        random_advice = random.choice(advice_list)
        embed = discord.Embed(
            color=discord.Color.green()
        )
        embed.set_author(name=f'Hey! {ctx.author.name}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='You asked me :', value=f'```{text}```', inline=False)
        embed.add_field(name='I answered :', value=f'```{random_advice}```', inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def hacker(self, ctx):
        url = 'https://hackertyper.net/'
        embed = discord.Embed(
            title=f"Hey {ctx.author.name}! It's the time to become a hacker.....",
            description=f'[Hack it now!]({url})',
            color=discord.Color.dark_green()
        )
        embed.set_image(url='https://blackstormroofingmarketing.com/wp-content/uploads/2020/07/What-to-do-if-Your-Roofing-Website-is-hacked.gif')

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(2, 3600, BucketType.user)
    async def support(self, ctx, *, text):

        loading = await ctx.send('`Sending your suggestions/complaints..... Please wait!`')
        try:
            user = self.client.get_user(583586061838581760) # Owner ID
            support_embed = discord.Embed(
                title='Support from ' + str(ctx.author),
                description='**Dear Owner,**\n\n- ' + str(text)+ '\n\n**Best regard,\n' + str(ctx.author) + '**',
                color=discord.Color.orange(),
                timestamp=datetime.datetime.utcnow()
            )

            await user.send(embed=support_embed)
            embed = discord.Embed(
                title=f'{ctx.author}! Your support has just successfully sent to the owner!',
                description=f"- Thank you inviting `WebFinder` to your server as a web search assistant. If you like this bot, don't forget to advertise and vote for him!\n**- Special thanks, {ctx.author}**",
                color=discord.Color.green(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/3062/3062634.png')
            embed.set_footer(text='© WebFinder v1.0', icon_url=logo_url)
            await ctx.send(embed=embed)
            await loading.delete()

        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.command()
    async def invite(self,ctx):
        embed = discord.Embed(
            title='Invite WebFinder to your server now !',
            color=discord.Color.green(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='-',value='[Click here to invite WebFinder to your server](https://discord.com/api/oauth2/authorize?client_id=743031764301119528&permissions=97345&scope=bot)')
        embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2367/2367302.png')
        embed.set_footer(text='© WebFinder v1.0', icon_url=logo_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def leave_server(self, ctx, id: int):
        try:
            #guild = discord.utils.get(self.client.guilds, id=id)
            guild = self.client.get_guild(id)
            await ctx.send(f'`WebFinder` has left the server: `{str(guild)} <{id}>`')
            await guild.leave()

        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.command()
    @commands.is_owner()
    async def servers_in(self, ctx):

        servers = self.client.guilds
        i = 0
        severs_list = []
        severs_list.append('```md\nSEVERS ARE IN :\n')
        for guild in servers:
            i += 1
            name = guild.name
            id = guild.id
            members = guild.member_count
            channels = guild.channels
            severs_list.append(f'{i}. <' + str(id) + ' | ' + str(name) + ' | '+ str(members) + ' member(s)' + ' | '  + str(len(channels)) + ' channels + categories' + '>\n')


        severs_list.append('\n```')
        server1 = '\n'.join(severs_list)
        await ctx.send(server1)

            #print(guild.name)

    @commands.command()
    async def botinfo(self, ctx):
        try:
            servers = self.client.guilds
            server_list = []
            members_list = []
            channels_list = []
            for guilds in servers:

                members_list.append(int(guilds.member_count))
                channels_list.append(len(guilds.channels))
                server_list.append(guilds)

            servers_count = len(server_list)

            members_count = sum(members_list)
            channels_count = sum(channels_list)


            now = datetime.datetime.utcnow()
            d0 = datetime.datetime(2020, 8, 25, 9, 12, 17)

            d1 = datetime.datetime(int(now.strftime("%Y")), int(now.strftime("%m")), int(now.strftime("%d")),
                                   int(now.strftime("%H")), int(now.strftime("%M")), int(now.strftime("%S")))
            delta = d1 - d0



            embed = discord.Embed(
                title='Information of BOT: ' + str(self.client.user),
                color=discord.Color.from_rgb(208, 151, 151),
                timestamp=datetime.datetime.utcnow()
            )

            embed.add_field(name='GENERAL', value=f'''
```
- Name :  {self.client.user}
- ID :  {self.client.user.id}
- Published date :  2020-08-22 15:12:17
- Runtime :  {delta}
- Library :  discord.py
- Prefix :  w; 
- Counter :  {servers_count} servers | {members_count} members | {channels_count} channels
- Owner :  Nautilus#3374
```''')
            embed.add_field(name='SYSTEM INFO (bad)',value='''
```
- System :  Microsoft Windows 10 Pro
- System type :  x64-based PC
- Storage :  100 GB
- RAM :  4.00 GB
- Release :  10
- Version :  10.0.18362 Build 18362
- Machine :   AMD64
- Processor :  Intel(R) Pentium(R) CPU G4400 @ 3.30GHz, 3300 Mhz, 2 Core(s), 2 Logical Processor(s)
```''',inline=False)
            embed.add_field(name='Invite link', value='[Click here](https://discord.com/api/oauth2/authorize?client_id=743031764301119528&permissions=97345&scope=bot)', inline=False)
            embed.set_thumbnail(url='https://i.pinimg.com/originals/3a/b0/b3/3ab0b35ae418a7eefe36aec352acd153.png')
            embed.set_footer(text='WebFinder v1.0 | discord.py', icon_url=logo_url)

            await ctx.send(embed=embed)
        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.command()
    async def about(self, ctx):
        ads2_embed = discord.Embed(
            title='WebFinder, a useful tool for web search in Discord !\n',
            description='''
- `WebFinder` is a bot that is created for getting results from many website such as: Google, Youtube, Soundcloud,.....The bot is still primitive and cannot run so smoothly as others Discord bot.
- `WebFinder` is created by **LongTo** (*also known as `Nautilus#3374` on Discord*) as his first experiment in coding.''',
            color=discord.Color.green(),
            timestamp=datetime.datetime.utcnow()
        )

        ads2_embed.set_author(name=self.client.user,
                              icon_url='https://img.icons8.com/ultraviolet/2x/info.png')
        ads2_embed.add_field(name='▶ Twitter: ',
                             value='https://twitter.com/Thanhlongto', inline=False)
        ads2_embed.add_field(name='▶ Pinterest: ',
                             value='https://www.pinterest.com/thanhlongto132/boards/', inline=False)
        ads2_embed.add_field(name='▶ Soundcloud: ',
                             value='https://soundcloud.com/thanh-long-to-515173298', inline=False)
        ads2_embed.add_field(name='▶ Discord: ',
                             value='Nautilus#3374 and his team https://discord.gg/CpPpK48', inline=False)
        ads2_embed.add_field(
            name='▶ Youtube: ',
            value='https://www.youtube.com/channel/UCWJmQFOS5AgdaouBAQYd1Cw?view_as=subscriber (sorry for no video :P)',
            inline=False)
        ads2_embed.set_image(url='https://i.pinimg.com/originals/a7/f1/fe/a7f1feb29d89e49cbf9569e297e45ad9.jpg')
        ads2_embed.set_footer(text='WebFinder v1.0 | discord.py', icon_url=logo_url)
        await ctx.send(embed=ads2_embed)

    @commands.is_owner()
    @commands.command()
    async def blacklist(self, ctx, value):
        try:
            file1 = open("blacklist.txt", "r")
            lines = file1.read()
            lines_list = lines.split('\n')
            file1.close()

            file = open('blacklist.txt', "a")
            if value in lines_list:
                await ctx.send('`Already in Blacklist`')

            elif value not in lines_list:
                await ctx.send('`Successfully blacklisted`')
                file.write(value)
                file.write('\n')

        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.is_owner()
    @commands.command()
    async def read_blacklist(self, ctx):
        try:
            file = open("blacklist.txt", "r")
            await ctx.send(f'```\n{file.read()}\n```')
            print(file.read())
        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.is_owner()
    @commands.command()
    async def unblacklist(self, ctx, value):
        try:
            file = open('blacklist.txt', 'r+')
            reader = file.read()
            if value in str(reader):
                reader = reader.replace(value, "")
                lines = reader.split('\n')
                file.seek(0)
                file.truncate()
                file.close()



                file2 = open("blacklist.txt", "w")
                for id in lines:
                    if str(id) != '':
                        file2.write(id)
                        file2.write('\n')

                file2.close()
                await ctx.send('`Successfully unblacklisted`')
            else:
                await ctx.send('`Not in blacklist`')



        except BaseException as e:
            await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    async def user_info(self, ctx, member : discord.Member):
        try:

            #print(member.activity.name)
            color_conv = str(member.color).lstrip('#')
            color_rgb = tuple(int(color_conv[i:i + 2], 16) for i in (0, 2, 4))
            b = str(color_rgb).replace('(', '').replace(')', '').replace(' ', '')
            list = b.split(',')



            status = []
            emoji = []
            status2 = []
            activity = []


            if 'online' in str(member.status):
                status.append('Online')
                emoji.append('https://emoji.gg/assets/emoji/5886_online.gif')


                if 'online' in str(member.desktop_status):
                    status2.append(' | On desktop')
                if 'online' in str(member.mobile_status):
                    status2.append(' | On mobile')
                if 'online' in str(member.web_status):
                    status2.append(' | On website')
                else:
                    status2.append(' | ')



            if 'dnd' in str(member.status):
                status.append('Do Not Disturb')
                emoji.append('https://emoji.gg/assets/emoji/3359_dnd.gif')

                if 'dnd' in str(member.desktop_status):
                    status2.append(' | On desktop')
                if 'dnd' in str(member.mobile_status):
                    status2.append(' | On mobile')
                if 'dnd' in str(member.web_status):
                    status2.append(' | On website')
                else:
                    status2.append(' | ')

            if 'idle' in str(member.status):
                status.append('Idle')
                emoji.append('https://emoji.gg/assets/emoji/1656_idle.gif')

                if 'idle' in str(member.desktop_status):
                    status2.append(' | On desktop')
                if 'idle' in str(member.mobile_status):
                    status2.append(' | On mobile')
                if 'idle' in str(member.web_status):
                    status2.append(' | On website')
                else:
                    status2.append(' | ')

            if 'offline' in str(member.status):
                status.append('Offline')
                emoji.append('https://emoji.gg/assets/emoji/8500_offline.gif')

            if str(member.activity) != 'None':


                if str(member.activity.type) == 'ActivityType.custom':
                    activity.append(str(member.activity))
                else:
                    activity.append(
                        f'**{str(member.activity.type).replace("ActivityType.", "")}** {member.activity.name}')
            if str(member.activity) == 'None':
                activity.append('None')


            info_embed = discord.Embed(
                title=f'Information of user : __{member}__',
                color=discord.Color.from_rgb(int(list[0]), int(list[1]), int(list[2])),
                timestamp=datetime.datetime.utcnow()
            )


            info_embed.set_author(name=''.join(status) + ''.join(status2), icon_url=''.join(emoji))
            info_embed.add_field(name='Name :', value=f'{member.name}')
            info_embed.add_field(name='Discriminator :', value=member.discriminator)
            info_embed.add_field(name='ID :', value=member.id)
            info_embed.add_field(name='Color :', value=member.color, inline=False)
            info_embed.add_field(name='Activity :', value=''.join(activity), inline=False)
            info_embed.add_field(name='Account created date :', value=f'`{str(member.created_at)[:19]}`',inline=False)
            info_embed.add_field(name=f'Server joined date ({member.guild}) :', value=f'`{str(member.joined_at)[:19]}`',inline=False)

            info_embed.set_thumbnail(url=f'{member.avatar_url}')
            info_embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

            await ctx.send(embed=info_embed)
        except BaseException as e:
            await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    async def server_info(self, ctx):
        try:
            sever_id = ctx.guild.id
            server = self.client.get_guild(sever_id)
            print(server.verification_level)
            print(server.channels)
            print(server.members)
            print(server.roles)

            afk = []
            if 'None' in str(server.afk_channel):
                afk.append('None')
            else:
                afk.append(len(server.afk_channel))


            e_list = []
            count = 0
            for emojis in server.emojis:
                if server.emojis[count].animated == False:
                    e_list.append(f'<:{server.emojis[count].name}:{server.emojis[count].id}>')

                count += 1


            server_embed = discord.Embed(
                description=f'- Description: *{server.description}*',
                color=discord.Color.teal(),
                timestamp=datetime.datetime.utcnow()
            )
            server_embed.set_author(name=f'Information of server : {server.name}', icon_url='https://emoji.gg/assets/emoji/8840_wumpus.gif')
            server_embed.set_thumbnail(url=server.icon_url)
            server_embed.add_field(name='ID :', value=f'{server.id}')
            server_embed.add_field(name='Owner :', value=f'{server.owner}')
            server_embed.add_field(name='Region :', value=f'{server.region}')
            server_embed.add_field(name='Created date :', value=f'`{str(server.created_at)[:19]}`')
            server_embed.add_field(name='Members :', value=f'{str(server.member_count)} member(s)')
            server_embed.add_field(name='Channels :', value=f'{len(server.text_channels+server.voice_channels)} channels :\n- *{len(server.text_channels)} text channels\n- {len(server.voice_channels)} voice channels*')
            server_embed.add_field(name='AFK channels :', value=''.join(afk),inline=False)
            server_embed.add_field(name='Roles :', value=f'{len(server.roles)} role(s)')
            server_embed.add_field(name=f'Emoji : {len(server.emojis)}', value=' '.join(e_list[:30])+' .......')
            server_embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

            await ctx.send(embed=server_embed)

        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.command()
    @commands.guild_only()
    async def member_info(self, ctx, member: discord.Member):
        permission_list = ['create_instant_invite', 'kick_members', 'ban_members', 'administrator', 'manage_channels', 'manage_guild', 'add_reactions', 'view_audit_log', 'priority_speaker', 'stream', 'view_channel', 'send_messages', 'send_tts_messages', 'manage_messages ', 'embed_links', 'attach_files', 'read_message_history', 'mention_everyone', 'use_external_emojis', 'view_guild_insights', 'connect', 'speak', 'mute_members', 'deafen_members', 'move_members', 'use_vad', 'change_nickname', 'manage_nicknames', 'manage_roles ', 'manage_webhooks ', 'manage_emojis ']



        color_conv = str(member.color).lstrip('#')
        color_rgb = tuple(int(color_conv[i:i + 2], 16) for i in (0, 2, 4))
        b = str(color_rgb).replace('(', '').replace(')', '').replace(' ', '')
        list = b.split(',')

        status = []
        emoji = []
        status2 = []


        if 'online' in str(member.status):
            status.append('Online')
            emoji.append('https://emoji.gg/assets/emoji/5886_online.gif')

            if 'online' in str(member.desktop_status):
                status2.append(' | On desktop')
            if 'online' in str(member.mobile_status):
                status2.append(' | On mobile')
            if 'online' in str(member.web_status):
                status2.append(' | On website')
            else:
                status2.append(' | ')

        if 'dnd' in str(member.status):
            status.append('Do Not Disturb')
            emoji.append('https://emoji.gg/assets/emoji/3359_dnd.gif')

            if 'dnd' in str(member.desktop_status):
                status2.append(' | On desktop')
            if 'dnd' in str(member.mobile_status):
                status2.append(' | On mobile')
            if 'dnd' in str(member.web_status):
                status2.append(' | On website')
            else:
                status2.append(' | ')

        if 'idle' in str(member.status):
            status.append('Idle')
            emoji.append('https://emoji.gg/assets/emoji/1656_idle.gif')

            if 'idle' in str(member.desktop_status):
                status2.append(' | On desktop')
            if 'idle' in str(member.mobile_status):
                status2.append(' | On mobile')
            if 'idle' in str(member.web_status):
                status2.append(' | On website')
            else:
                status2.append(' | ')

        if 'offline' in str(member.status):
            status.append('Offline')
            emoji.append('https://emoji.gg/assets/emoji/8500_offline.gif')

        try:



            sever_id = ctx.guild.id
            server = self.client.get_guild(sever_id)
            top_role = server.get_role(member.top_role.id)
            permissions = top_role.permissions

            print(top_role.created_at)
            permission_verified = []

            if permissions.create_instant_invite == True:
                permission_verified.append("- create_instant_invite")

            if permissions.kick_members == True:
                permission_verified.append("- kick_members")

            if permissions.ban_members == True:
                permission_verified.append("- ban_members")

            if permissions.administrator == True:
                permission_verified.append("- administrator")

            if permissions.manage_channels == True:
                permission_verified.append("- manage_channels")

            if permissions.manage_guild == True:
                permission_verified.append("- manage_guild")

            if permissions.add_reactions == True:
                permission_verified.append("- add_reactions")

            if permissions.view_audit_log == True:
                permission_verified.append("- view_audit_log")

            if permissions.priority_speaker == True:
                permission_verified.append("- priority_speaker")

            if permissions.stream == True:
                permission_verified.append("- stream")

            if permissions.view_channel == True:
                permission_verified.append("- view_channel")

            if permissions.send_messages == True:
                permission_verified.append("- send_messages")

            if permissions.send_tts_messages == True:
                permission_verified.append("- send_tts_messages")

            if permissions.manage_messages == True:
                permission_verified.append("- manage_messages ")

            if permissions.embed_links == True:
                permission_verified.append("- embed_links")

            if permissions.attach_files == True:
                permission_verified.append("- attach_files")

            if permissions.read_message_history == True:
                permission_verified.append("- read_message_history")

            if permissions.mention_everyone == True:
                permission_verified.append("- mention_everyone")

            if permissions.use_external_emojis == True:
                permission_verified.append("- use_external_emojis")

            if permissions.view_guild_insights == True:
                permission_verified.append("- view_guild_insights")

            if permissions.connect == True:
                permission_verified.append("- connect")

            if permissions.speak == True:
                permission_verified.append("- speak")

            if permissions.mute_members == True:
                permission_verified.append("- mute_members")

            if permissions.deafen_members == True:
                permission_verified.append("- deafen_members")

            if permissions.move_members == True:
                permission_verified.append("- move_members")

            if permissions.use_voice_activation == True:
                permission_verified.append("- use_voice_activation")

            if permissions.change_nickname == True:
                permission_verified.append("- change_nickname")

            if permissions.manage_nicknames == True:
                permission_verified.append("- manage_nicknames")

            if permissions.manage_roles == True:
                permission_verified.append("- manage_roles ")

            if permissions.manage_webhooks == True:
                permission_verified.append("- manage_webhooks ")

            if permissions.manage_emojis == True:
                permission_verified.append("- manage_emojis ")

            if len(permission_verified) > 10:
                final = '◦ '+'\n'.join(permission_verified[:10]).replace("_", " ").title() + f'\n+{len(permission_verified)-10} more permissions'
            elif len(permission_verified) < 10:
                final = '◦ '+ '\n'.join(permission_verified[:10]).replace("_", " ").title()



            member_embed = discord.Embed(
                        title=f'Information of member : __{member}__',
                        color=discord.Color.from_rgb(int(list[0]), int(list[1]), int(list[2])),
                        timestamp=datetime.datetime.utcnow()
            )

            member_embed.set_author(name=''.join(status) + ''.join(status2), icon_url=''.join(emoji))
            member_embed.add_field(name='-', value=f'''
**◦ Name :** {member.display_name}
**◦ Discriminator :** {member.discriminator}
**◦ Nickname :** {member.nick}
**◦ ID :** {member.id}
**◦ Joined date :** `{str(member.joined_at)[:19]}`''')
            member_embed.add_field(name='-',value=f'''
**◦ Roles :** {len(member.roles)}
**◦ Top role :** __{member.top_role}__ (*created at `{str(top_role.created_at)[:10]}`*)
**◦ Permission :**
*{final}*
''')
            member_embed.set_thumbnail(url=member.avatar_url)

            member_embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=member_embed)

        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.command()
    @commands.guild_only()
    async def role_info(self, ctx, role: discord.Role):
        try:
            print(role.id)
            sever_id = ctx.guild.id
            server = self.client.get_guild(sever_id)
            top_role = server.get_role(role.id)
            permissions = top_role.permissions

            print(top_role.created_at)
            permission_verified = []

            if permissions.create_instant_invite == True:
                permission_verified.append("- create_instant_invite")

            if permissions.kick_members == True:
                permission_verified.append("- kick_members")

            if permissions.ban_members == True:
                permission_verified.append("- ban_members")

            if permissions.administrator == True:
                permission_verified.append("- administrator")

            if permissions.manage_channels == True:
                permission_verified.append("- manage_channels")

            if permissions.manage_guild == True:
                permission_verified.append("- manage_guild")

            if permissions.add_reactions == True:
                permission_verified.append("- add_reactions")

            if permissions.view_audit_log == True:
                permission_verified.append("- view_audit_log")

            if permissions.priority_speaker == True:
                permission_verified.append("- priority_speaker")

            if permissions.stream == True:
                permission_verified.append("- stream")

            if permissions.view_channel == True:
                permission_verified.append("- view_channel")

            if permissions.send_messages == True:
                permission_verified.append("- send_messages")

            if permissions.send_tts_messages == True:
                permission_verified.append("- send_tts_messages")

            if permissions.manage_messages == True:
                permission_verified.append("- manage_messages ")

            if permissions.embed_links == True:
                permission_verified.append("- embed_links")

            if permissions.attach_files == True:
                permission_verified.append("- attach_files")

            if permissions.read_message_history == True:
                permission_verified.append("- read_message_history")

            if permissions.mention_everyone == True:
                permission_verified.append("- mention_everyone")

            if permissions.use_external_emojis == True:
                permission_verified.append("- use_external_emojis")

            if permissions.view_guild_insights == True:
                permission_verified.append("- view_guild_insights")

            if permissions.connect == True:
                permission_verified.append("- connect")

            if permissions.speak == True:
                permission_verified.append("- speak")

            if permissions.mute_members == True:
                permission_verified.append("- mute_members")

            if permissions.deafen_members == True:
                permission_verified.append("- deafen_members")

            if permissions.move_members == True:
                permission_verified.append("- move_members")

            if permissions.use_voice_activation == True:
                permission_verified.append("- use_voice_activation")

            if permissions.change_nickname == True:
                permission_verified.append("- change_nickname")

            if permissions.manage_nicknames == True:
                permission_verified.append("- manage_nicknames")

            if permissions.manage_roles == True:
                permission_verified.append("- manage_roles ")

            if permissions.manage_webhooks == True:
                permission_verified.append("- manage_webhooks ")

            if permissions.manage_emojis == True:
                permission_verified.append("- manage_emojis ")

            if len(permission_verified) > 10:
                final = '⚬ ' + '\n'.join(permission_verified[:10]).replace("_",
                                                                           " ").title() + f'\n+{len(permission_verified) - 10} more permissions'
            elif len(permission_verified) < 10:
                final = '⚬ ' + '\n'.join(permission_verified[:10]).replace("_", " ").title()

            color_conv = str(role.color).lstrip('#')
            color_rgb = tuple(int(color_conv[i:i + 2], 16) for i in (0, 2, 4))
            b = str(color_rgb).replace('(', '').replace(')', '').replace(' ', '')
            list = b.split(',')

            print(role.members)
            holder = []
            for i in role.members:
                holder.append(f'- {i}')

            print(role.color)
            print(role.position)
            print(role.managed)

            if len(holder) > 10:
                final_holder = '\n'.join(holder[:10]) + f'\n**+{len(holder) - 10} more members**'
            elif len(holder) < 10:
                final_holder = '\n'.join(holder[:10])
            role_embed = discord.Embed(
                title='Information of role : {}'.format(role),
                color=discord.Color.from_rgb(int(list[0]), int(list[1]), int(list[2])),
                timestamp=datetime.datetime.utcnow()

            )

            role_embed.add_field(name='-', value=f'''
**◦ Role name :** __{role.name}__
**◦ Position :** {role.position}
**◦ Created date :** `{str(role.created_at)[:19]}`
**◦ Role holder(s) :**
*{final_holder}*
''')
            role_embed.set_thumbnail(url=server.icon_url)
            role_embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=role_embed)

        except BaseException as e:
            await ctx.send(traceback.print_exc())

    @commands.command()
    @commands.guild_only()
    async def channel_info(self, ctx, channel: discord.TextChannel):

        print(channel.name)
        print(channel.topic)
        if str(channel.topic) == '':
            channel.topic = 'None'

        print(channel.members)
        print(channel.created_at)
        print(channel.type)
        print(channel.category)
        print(channel.id)
        print(channel.last_message_id)

        msg = await channel.fetch_message(channel.last_message_id)

        print(msg.author)
        print(msg.created_at)
        if str(msg.content) == '':
            msg.content = '_'

        try:
            print(channel.guild)
            print(channel.slowmode_delay)
            print(channel.mention)
            print(channel.is_nsfw())


            server = self.client.get_guild(channel.guild.id)
            print(server.member_count)

            channel_embed = discord.Embed(
                title=f'Information of channel : __{channel.name}__ | {str(channel.type).title()}',
                description=f'*Topic : {channel.topic}*',
                color=discord.Color.blurple(),
                timestamp=datetime.datetime.utcnow()
            )
            channel_embed.set_author(name=f'{channel.guild} | {server.member_count} member(s)', icon_url='https://emoji.gg/assets/emoji/8840_wumpus.gif')
            channel_embed.add_field(name='-',value=f'''
**◦ ID :** {channel.id}
**◦ Category :** {channel.category}
**◦ Channel's member(s) :** {len(channel.members)} member(s)
**◦ Created date :** `{str(channel.created_at)[:19]}`
**◦ Slow_mode delay :** `{channel.slowmode_delay}s`
**◦ Mention :** {channel.mention}
**◦ NSFW :** {channel.is_nsfw()}
**◦ Last message :** ```{msg.content}```
*- Sent by **{msg.author}** at `{str(msg.created_at)[:19]}`*
*- Edited : {str(msg.edited_at)[:19]}*''')
            channel_embed.set_thumbnail(url=server.icon_url)
            channel_embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=channel_embed)

        except BaseException as e:
            await ctx.send(traceback.print_exc())



    @commands.command()
    @commands.is_owner()
    async def get_info(self, ctx, value):
        try:
            if 'server=' in value:
                server = self.client.get_guild(int(value.replace('server=', '')))
                await ctx.send(f'`{server}  :  {value.replace("server=", "")}`')

            elif 'user=' in value:
                user = self.client.get_user(int(value.replace('user=', '')))

                await ctx.send(f'`{user}  :  {value.replace("user=", "")}`')
            else:
                await ctx.send('```diff\n- Must contain "server=" or "user="\n```')

        except BaseException as e:
            await ctx.send(traceback.print_exc())



    @commands.command()
    @commands.is_owner()
    async def top_calls(self, ctx, value):
        afile = open('users.json', 'r')
        load = json.load(afile)
        N = 20
        res = dict(sorted(load.items(), key=itemgetter(1), reverse=True)[:N])
        top_list = []
        if 'user' in value:
            for i in res:
                top_list.append(f'**{self.client.get_user(int(i))}** : `{res[i]} calls`')

            top_embed = discord.Embed(
                title=f'Top most bot calls from users',
                description='\n'.join(top_list)+'\n*.....*',
                color=discord.Color.orange(),
                timestamp=datetime.datetime.utcnow()
            )

            top_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2282/2282580.png')
            top_embed.set_footer(text='© WebFinder v1.0', icon_url=logo_url)
            await ctx.send(embed=top_embed)

        elif 'id' in value:
            for i in res:
                top_list.append(f'**{i}** : `{res[i]} calls`')

            top_embed = discord.Embed(
                title=f'Top most bot calls from users (id)',
                description='\n'.join(top_list)+'\n*.....*',
                color=discord.Color.orange(),
                timestamp=datetime.datetime.utcnow()
            )

            top_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2282/2282580.png')
            top_embed.set_footer(text='© WebFinder v1.0', icon_url=logo_url)
            await ctx.send(embed=top_embed)
        else:
            await ctx.send('```diff\n- Must contain "id=" or "user="\n```')


    @commands.command()
    @commands.is_owner()
    async def owner_command(self, ctx):
        owner_embed = discord.Embed(
            title='Commands for owner',
            description='`blacklist` , `unblacklist` , `read_blacklist` , `get_info [user=id]/[server=id]` , `top_calls user=/id=` , `servers_in` , `leave_server [id]`',
            color=discord.Color.orange()
        )
        owner_embed.set_footer(text='Just for my owner ! Love')
        await ctx.send(embed=owner_embed)



def setup(client):
    client.add_cog(Help(client))