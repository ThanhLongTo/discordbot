import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import datetime
import traceback

import wikipediaapi
from googletrans import Translator


lang_list ={
'ab': 'Abkhaz',
'aa': 'Afar',
'af': 'Afrikaans',
'ak': 'Akan',
'sq': 'Albanian',
'am': 'Amharic',
'ar': 'Arabic',
'an': 'Aragonese',
'hy': 'Armenian',
'as': 'Assamese',
'av': 'Avaric',
'ae': 'Avestan',
'ay': 'Aymara',
'az': 'Azerbaijani',
'bm': 'Bambara',
'ba': 'Bashkir',
'eu': 'Basque',
'be': 'Belarusian',
'bn': 'Bengali',
'bh': 'Bihari',
'bi': 'Bislama',
'bs': 'Bosnian',
'br': 'Breton',
'bg': 'Bulgarian',
'my': 'Burmese',
'ca': 'Catalan; Valencian',
'ch': 'Chamorro',
'ce': 'Chechen',
'ny': 'Chichewa; Chewa; Nyanja',
'zh-cn': 'Chinese',
'cv': 'Chuvash',
'kw': 'Cornish',
'co': 'Corsican',
'cr': 'Cree',
'hr': 'Croatian',
'cs': 'Czech',
'da': 'Danish',
'dv': 'Divehi; Maldivian;',
'nl': 'Dutch',
'dz': 'Dzongkha',
'en': 'English',
'eo': 'Esperanto',
'et': 'Estonian',
'ee': 'Ewe',
'fo': 'Faroese',
'fj': 'Fijian',
'fi': 'Finnish',
'fr': 'French',
'ff': 'Fula',
'gl': 'Galician',
'ka': 'Georgian',
'de': 'German',
'el': 'Greek, Modern',
'gn': 'Guaraní',
'gu': 'Gujarati',
'ht': 'Haitian',
'ha': 'Hausa',
'he': 'Hebrew modern',
'hz': 'Herero',
'hi': 'Hindi',
'ho': 'Hiri Motu',
'hu': 'Hungarian',
'ia': 'Interlingua',
'id': 'Indonesian',
'ie': 'Interlingue',
'ga': 'Irish',
'ig': 'Igbo',
'ik': 'Inupiaq',
'io': 'Ido',
'is': 'Icelandic',
'it': 'Italian',
'iu': 'Inuktitut',
'ja': 'Japanese',
'jv': 'Javanese',
'kl': 'Kalaallisut',
'kn': 'Kannada',
'kr': 'Kanuri',
'ks': 'Kashmiri',
'kk': 'Kazakh',
'km': 'Khmer',
'ki': 'Kikuyu, Gikuyu',
'rw': 'Kinyarwanda',
'ky': 'Kirghiz, Kyrgyz',
'kv': 'Komi',
'kg': 'Kongo',
'ko': 'Korean',
'ku': 'Kurdish',
'kj': 'Kwanyama, Kuanyama',
'la': 'Latin',
'lb': 'Luxembourgish',
'lg': 'Luganda',
'li': 'Limburgish',
'ln': 'Lingala',
'lo': 'Lao',
'lt': 'Lithuanian',
'lu': 'Luba-Katanga',
'lv': 'Latvian',
'gv': 'Manx',
'mk': 'Macedonian',
'mg': 'Malagasy',
'ms': 'Malay',
'ml': 'Malayalam',
'mt': 'Maltese',
'mi': 'Māori',
'mr': 'Marathi Marāṭhī',
'mh': 'Marshallese',
'mn': 'Mongolian',
'na': 'Nauru',
'nv': 'Navajo, Navaho',
'nb': 'Norwegian Bokmål',
'nd': 'North Ndebele',
'ne': 'Nepali',
'ng': 'Ndonga',
'nn': 'Norwegian Nynorsk',
'no': 'Norwegian',
'ii': 'Nuosu',
'nr': 'South Ndebele',
'oc': 'Occitan',
'oj': 'Ojibwe, Ojibwa',
'cu': 'Old Church Slavonic',
'om': 'Oromo',
'or': 'Oriya',
'os': 'Ossetian, Ossetic',
'pa': 'Panjabi, Punjabi',
'pi': 'Pāli',
'fa': 'Persian',
'pl': 'Polish',
'ps': 'Pashto, Pushto',
'pt': 'Portuguese',
'qu': 'Quechua',
'rm': 'Romansh',
'rn': 'Kirundi',
'ro': 'Romanian, Moldavan',
'ru': 'Russian',
'sa': 'Sanskrit Saṁskṛta',
'sc': 'Sardinian',
'sd': 'Sindhi',
'se': 'Northern Sami',
'sm': 'Samoan',
'sg': 'Sango',
'sr': 'Serbian',
'gd': 'Scottish Gaelic',
'sn': 'Shona',
'si': 'Sinhala, Sinhalese',
'sk': 'Slovak',
'sl': 'Slovene',
'so': 'Somali',
'st': 'Southern Sotho',
'es': 'Spanish; Castilian',
'su': 'Sundanese',
'sw': 'Swahili',
'ss': 'Swati',
'sv': 'Swedish',
'ta': 'Tamil',
'te': 'Telugu',
'tg': 'Tajik',
'th': 'Thai',
'ti': 'Tigrinya',
'bo': 'Tibetan',
'tk': 'Turkmen',
'tl': 'Tagalog',
'tn': 'Tswana',
'to': 'Tonga',
'tr': 'Turkish',
'ts': 'Tsonga',
'tt': 'Tatar',
'tw': 'Twi',
'ty': 'Tahitian',
'ug': 'Uighur, Uyghur',
'uk': 'Ukrainian',
'ur': 'Urdu',
'uz': 'Uzbek',
've': 'Venda',
'vi': 'Vietnamese',
'vo': 'Volapük',
'wa': 'Walloon',
'cy': 'Welsh',
'wo': 'Wolof',
'fy': 'Western Frisian',
'xh': 'Xhosa',
'yi': 'Yiddish',
'yo': 'Yoruba',
'za': 'Zhuang, Chuang',
'zu': 'Zulu'
}

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def ping(self, ctx):

        await ctx.send(f'Pong   :ping_pong: \nLatency: *{self.client.latency}s*')

    @commands.command()
    async def test(self, ctx):
        await ctx.send('Test')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)


    @commands.command()
    async def av(self, ctx, member: discord.Member):

        show_avatar = discord.Embed(
            color=discord.Color.blue()
        )
        show_avatar.set_author(name=f'{member.name}#{member.discriminator}')
        show_avatar.set_image(url="{}".format(member.avatar_url))
        show_avatar.set_footer(text='')
        await ctx.send(embed=show_avatar)


    # KICK
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *,
                   kick_reason):  # '*' allowed you to give reason with space between contents
        author = ctx.message.author

        await member.kick(reason=kick_reason)

        kick_embed = discord.Embed(
            title='***KICK***',
            color=discord.Color.red(),
            timestamp=datetime.datetime.utcnow()
        )

        kick_embed.add_field(name='**Member:** ', value=f'{member.mention}')
        kick_embed.add_field(name='**Action:** ', value='Kick', inline=False)
        kick_embed.add_field(name='**Actioned by:** ', value=f'{author.mention}', inline=False)
        kick_embed.add_field(name='**Reason:** ', value=f'{kick_reason}', inline=False)
        kick_embed.set_thumbnail(url='https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2009/4/29/1240996556472/exclamation-001.jpg?width=445&quality=85&auto=format&fit=max&s=5470a072aa054368dd115acd47e11e64')

        await ctx.send(f'{author.mention}', embed=kick_embed)



    # W A R N
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def warn(self, ctx, member: discord.Member, *,
                   warn_reason):
        author = ctx.message.author

        warn_embed = discord.Embed(
            title='***WARN***',
            color=discord.Color.gold(),
            timestamp = datetime.datetime.utcnow()
        )

        warn_embed.add_field(name='**Member:** ', value=f'{member.mention}')
        warn_embed.add_field(name='**Action:** ', value='Warn', inline=False)
        warn_embed.add_field(name='**Actioned by:** ', value=f'{author.mention}', inline=False)
        warn_embed.add_field(name='**Reason:** ', value=f'{warn_reason}', inline=False)
        warn_embed.set_thumbnail(
            url='https://www.doctorsataustraliafair.com.au/wp-content/uploads/2020/01/Exclamation-Mark-Transparent-Image.png')
        await ctx.send(f'{author.mention}', embed=warn_embed)




    # B A N   &   U N B A N
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, ban_reason):
        await member.ban(reason=ban_reason)

        author = ctx.message.author

        ban_embed = discord.Embed(
            title='***BAN***',
            color=discord.Color.red(),
            timestamp=datetime.datetime.utcnow()
        )

        ban_embed.add_field(name='**Member:** ', value=f'{member.mention}')
        ban_embed.add_field(name='**Action:** ', value='Ban', inline=False)
        ban_embed.add_field(name='**Actioned by:** ', value=f'{author.mention}', inline=False)
        ban_embed.add_field(name='**Reason:** ', value=f'{ban_reason}', inline=False)
        ban_embed.set_thumbnail(
            url='https://www.doctorsataustraliafair.com.au/wp-content/uploads/2020/01/Exclamation-Mark-Transparent-Image.png')
        await ctx.send(f'{author.mention}', embed=ban_embed)




    @commands.has_permissions(administrator=True)
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (member_name, member_discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                await ctx.send(f'```\nUnbanned {user.mention}\n```')

                return




    @commands.command()
    async def tr(self,ctx, lang, *, input):
        try:
            trans = Translator()
            if 'zh' in lang:
                lang = lang.replace('zh', 'zh-CN')

            input_translated1 = trans.translate(input, dest=lang)
            input_translated = input_translated1.text

            src = input_translated1.src

            dest = input_translated1.dest



            src1 = lang_list[src]
            dest1 = lang_list[dest]

            translate_embed = discord.Embed(
                title=f'{src1} ({src}) ➟ {dest1} ({dest})\n‎‏‏‎ ‎',
                color=discord.Color.blue(),

            )

            translate_embed.add_field(name='Source:',value=f'```\n{input}\n```', inline=False)
            translate_embed.add_field(name='Translation:', value=f'```\n{input_translated}\n```')
            await ctx.send(embed=translate_embed)

        except ValueError as VE:
            await ctx.send(f'```diff\n- ERROR: {VE}\n```')
            return
    # SUMMARY PAGE HERE
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def summary(self, ctx, *, input):
        try:
            '''Translate input to English'''
            input = input.replace('-', '_')
            trans = Translator()
            input_translated1 = trans.translate(input, dest='en')
            input_translated = input_translated1.text

            '''Find info'''
            wiki_wiki = wikipediaapi.Wikipedia('en')
            input_low = input_translated.lower()
            input_low_url = input_low.replace(' ', '_')

            page_py = wiki_wiki.page(input_low)
            page_summary = page_py.summary
            #page_url = page_py.fullurl

            enter_find = page_summary.find('\n')
            enter_find1 = page_summary[0:enter_find]


            if page_summary == '':
                await ctx.send('```diff\n- ERROR: Information not found. Please check your input value and be sure that what you want to summary is existed in Wikipedia.org !\n```')

            if 'may refer to:' in page_summary:
                await ctx.send('```bash\n"Hmmm.....I cannot find what you want =( . Try to get some references```')
                await ctx.send(f'Find more at: https://en.wikipedia.org/wiki/{input_low_url.lower()}')

            else:
                if len(page_summary) > 2000:
                    await ctx.send('```bash\nBecause the information is too long, I decide to shorten it!\n```')


                    if len(enter_find1) > 1000:
                        list_find = enter_find1.split('.')
                        list_find2 = list_find[:7]
                        list_find3 = '.'.join(list_find2)
                        await ctx.send(f'```bash\n"{input_translated.upper()}"\n\n"{list_find3}"```')
                        await ctx.send(f'Find more at: https://en.wikipedia.org/wiki/{input_low_url.lower()}')


                    else:
                        await ctx.send(f'```bash\n"{input_translated.upper()}"\n\n"{enter_find1}"```')
                        await ctx.send(f'Find more at: https://en.wikipedia.org/wiki/{input_low_url.lower()}')


                else:
                    await ctx.send(f'```bash\n"{input_translated.upper()}"\n\n"{page_summary}"```')
        except BaseException as e:
            await ctx.send(traceback.print_exc())




    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def lang_summary(self, ctx, lang, *, input):
        try:
            input = input.replace('-', '_')
            '''Translate input to English'''

            trans = Translator()
            input_translated1 = trans.translate(input, dest='en')
            input_translated = input_translated1.text

            '''Translate input to lang input again'''
            input_translated_again1 = trans.translate(input, dest=lang)
            input_translated_again = input_translated_again1.text
            input_translated_again_url = input_translated_again.replace(' ', '_')


            input_translated = input_translated.replace('-', '_')
            '''Find wiki in English'''
            wiki_wiki = wikipediaapi.Wikipedia('en')
            input_low = input_translated.lower()


            page_py = wiki_wiki.page(input_low)

            page_summary = page_py.summary
            '''Translate to lang input'''
            page_summary_translated1 = trans.translate(page_summary, dest=lang)
            page_summary_translated = page_summary_translated1.text
            #print(page_summary_translated)


            enter_find = page_summary_translated.find('\n')
            enter_find1 = page_summary_translated[0:enter_find]

            if page_summary == '':
                await ctx.send('```diff\n- ERROR: Information not found. Please check your input value and be sure that what you want to summary is existed in Wikipedia.org !\n```')


            if 'may refer to:' in page_summary:
                await ctx.send('```bash\n"Hmmm.....I cannot find what you want =( . Try to get some references```')
                await ctx.send(f'Find more at: https://{lang.lower()}.wikipedia.org/wiki/{input_translated_again_url.lower()}')

            else:
                if len(page_summary_translated) > 2000:
                    await ctx.send('```bash\nBecause the information is too long, I decide to shorten it!\n```')


                    if len(enter_find1) > 1000:
                        list_find = enter_find1.split('.')
                        list_find2 = list_find[:7]
                        list_find3 = '.'.join(list_find2)
                        await ctx.send(f'```bash\n"{input_translated_again.upper()}"\n\n"{list_find3}"```')
                        await ctx.send(f'Find more at: https://{lang.lower()}.wikipedia.org/wiki/{input_translated_again_url.lower()}')

                    else:
                        await ctx.send(f'```bash\n"{input_translated_again.upper()}"\n\n"{enter_find1}"```')
                        await ctx.send(f'Find more at: https://{lang.lower()}.wikipedia.org/wiki/{input_translated_again_url.lower()}')


                else:
                    await ctx.send(f'```bash\n"{input_translated_again.upper()}"\n\n"{page_summary_translated}"```')

        except BaseException as e:
            await ctx.send(traceback.print_exc())




def setup(client):
    client.remove_command('help')
    client.add_cog(Example(client))
