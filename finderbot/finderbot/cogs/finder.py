import discord
from discord.ext import commands
import random
from discord.ext.commands import BucketType
import time

import traceback
import wikipediaapi
from googletrans import Translator
from googlesearch import search
from youtube_search import YoutubeSearch
from PyDictionary import PyDictionary
import requests
from bs4 import BeautifulSoup

random_time_sleep = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1]
random_delay = [18, 19, 20, 21, 22, 24, 25]
lang_list = {
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
    'zh-cn': 'Chinese (simplified)',
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

bad_word_list = ['ahole', 'anus', 'ash0le', 'ash0les', 'asholes', 'ass', 'Ass Monkey', 'Assface', 'assh0le', 'assh0lez', 'asshole', 'assholes', 'assholz', 'asswipe', 'azzhole', 'bassterds', 'bastard', 'bastards', 'bastardz', 'basterds', 'basterdz', 'Biatch', 'bitch', 'bitches', 'Blow Job', 'boffing', 'butthole', 'buttwipe', 'c0ck', 'c0cks', 'c0k', 'Carpet Muncher', 'cawk', 'cawks', 'Clit', 'cnts', 'cntz', 'cock', 'cockhead', 'cock-head', 'cocks', 'CockSucker', 'cock-sucker', 'crap', 'cum', 'cunt', 'cunts', 'cuntz', 'dick', 'dild0', 'dild0s', 'dildo', 'dildos', 'dilld0', 'dilld0s', 'dominatricks', 'dominatrics', 'dominatrix', 'dyke', 'enema', 'f u c k', 'f u c k e r', 'fag', 'fag1t', 'faget', 'fagg1t', 'faggit', 'faggot', 'fagit', 'fags', 'fagz', 'faig', 'faigs', 'fart', 'flipping the bird', 'fuck', 'fucker', 'fuckin', 'fucking', 'fucks', 'Fudge Packer', 'fuk', 'Fukah', 'Fuken', 'fuker', 'Fukin', 'Fukk', 'Fukkah', 'Fukken', 'Fukker', 'Fukkin', 'g00k', 'gay', 'gayboy', 'gaygirl', 'gays', 'gayz', 'God-damned', 'h00r', 'h0ar', 'h0re', 'hells', 'hoar', 'hoor', 'hoore', 'jackoff', 'jap', 'japs', 'jerk-off', 'jisim', 'jiss', 'jizm', 'jizz', 'knob', 'knobs', 'knobz', 'kunt', 'kunts', 'kuntz', 'Lesbian', 'Lezzian', 'Lipshits', 'Lipshitz', 'masochist', 'masokist', 'massterbait', 'masstrbait', 'masstrbate', 'masterbaiter', 'masterbate', 'masterbates', 'Motha Fucker', 'Motha Fuker', 'Motha Fukkah', 'Motha Fukker', 'Mother Fucker', 'Mother Fukah', 'Mother Fuker', 'Mother Fukkah', 'Mother Fukker', 'mother-fucker', 'Mutha Fucker', 'Mutha Fukah', 'Mutha Fuker', 'Mutha Fukkah', 'Mutha Fukker', 'n1gr', 'nastt', 'nigger;', 'nigur;', 'niiger;', 'niigr;', 'orafis', 'orgasim;', 'orgasm', 'orgasum', 'oriface', 'orifice', 'orifiss', 'packi', 'packie', 'packy', 'paki', 'pakie', 'paky', 'pecker', 'peeenus', 'peeenusss', 'peenus', 'peinus', 'pen1s', 'penas', 'penis', 'penis-breath', 'penus', 'penuus', 'Phuc', 'Phuck', 'Phuk', 'Phuker', 'Phukker', 'polac', 'polack', 'polak', 'Poonani', 'pr1c', 'pr1ck', 'pr1k', 'pusse', 'pussee', 'pussy', 'puuke', 'puuker', 'queer', 'queers', 'queerz', 'qweers', 'qweerz', 'qweir', 'recktum', 'rectum', 'retard', 'sadist', 'scank', 'schlong', 'screwing', 'semen', 'sex', 'sexy', 'Sh!t', 'sh1t', 'sh1ter', 'sh1ts', 'sh1tter', 'sh1tz', 'shit', 'shits', 'shitter', 'Shitty', 'Shity', 'shitz', 'Shyt', 'Shyte', 'Shytty', 'Shyty', 'skanck', 'skank', 'skankee', 'skankey', 'skanks', 'Skanky', 'slut', 'sluts', 'Slutty', 'slutz', 'son-of-a-bitch', 'tit', 'turd', 'va1jina', 'vag1na', 'vagiina', 'vagina', 'vaj1na', 'vajina', 'vullva', 'vulva', 'w0p', 'wh00r', 'wh0re', 'whore', 'xrated', 'xxx', 'b!+ch', 'bitch', 'blowjob', 'clit', 'arschloch', 'fuck', 'shit', 'ass', 'asshole', 'b!tch', 'b17ch', 'b1tch', 'bastard', 'bi+ch', 'boiolas', 'buceta', 'c0ck', 'cawk', 'chink', 'cipa', 'clits', 'cock', 'cum', 'cunt', 'dildo', 'dirsa', 'ejakulate', 'fatass', 'fcuk', 'fuk', 'fux0r', 'hoer', 'hore', 'jism', 'kawk', 'l3itch', 'l3i+ch', 'lesbian', 'masturbate', 'masterbat*', 'masterbat3', 'motherfucker', 's.o.b.', 'mofo', 'nazi', 'nigga', 'nigger', 'nutsack', 'phuck', 'pimpis', 'pusse', 'pussy', 'scrotum', 'sh!t', 'shemale', 'shi+', 'sh!+', 'slut', 'smut', 'teets', 'tits', 'boobs', 'b00bs', 'teez', 'testical', 'testicle', 'titt', 'w00se', 'jackoff', 'wank', 'whoar', 'whore', '*damn', '*dyke', '*fuck*', '*shit*', '@$$', 'amcik', 'andskota', 'arse*', 'assrammer', 'ayir', 'bi7ch', 'bitch*', 'bollock*', 'breasts', 'butt-pirate', 'cabron', 'cazzo', 'chraa', 'chuj', 'Cock*', 'cunt*', 'd4mn', 'daygo', 'dego', 'dick*', 'dike*', 'dupa', 'dziwka', 'ejackulate', 'Ekrem*', 'Ekto', 'enculer', 'faen', 'fag*', 'fanculo', 'fanny', 'feces', 'feg', 'Felcher', 'ficken', 'fitt*', 'Flikker', 'foreskin', 'Fotze', 'Fu(*', 'fuk*', 'futkretzn', 'gay', 'gook', 'guiena', 'h0r', 'hentai', 'h4x0r', 'hell', 'helvete', 'hoer*', 'honkey', 'Huevon', 'hui', 'injun', 'jizz', 'kanker*', 'kike', 'klootzak', 'kraut', 'knulle', 'kuk', 'kuksuger', 'Kurac', 'kurwa', 'kusi*', 'kyrpa*', 'lesbo', 'mamhoon', 'masturbat*', 'merd*', 'mibun', 'monkleigh', 'mouliewop', 'muie', 'mulkku', 'muschi', 'nazis', 'nepesaurio', 'nigger*', 'orospu', 'paska*', 'perse', 'picka', 'pierdol*', 'pillu*', 'pimmel', 'piss*', 'pizda', 'poontsee', 'poop', 'porn', 'p0rn', 'pr0n', 'preteen', 'pula', 'pule', 'puta', 'puto', 'qahbeh', 'queef*', 'rautenberg', 'schaffer', 'scheiss*', 'schlampe', 'schmuck', 'screw', 'sh!t*', 'sharmuta', 'sharmute', 'shipal', 'shiz', 'skribz', 'skurwysyn', 'sphencter', 'spic', 'spierdalaj', 'splooge', 'suka', 'b00b*', 'testicle*', 'titt*', 'twat', 'vittu', 'wank*', 'wetback*', 'wichser', 'wop*', 'yed', 'zabourah', 'nsfw']


random_status = ['https://i.pinimg.com/originals/df/f9/ab/dff9abe32915bc4f5a2c694cdffe20c1.png',
                 'https://i.pinimg.com/originals/c5/47/bc/c547bc5834d630be6f6e9f95a7c7dc31.png',
                 'https://i.pinimg.com/originals/70/b7/68/70b7687edf0dd4e3e2e957b633ed1065.png',
                 'https://cdn1.iconfinder.com/data/icons/flat-and-simple-part-1/128/location-512.png'
                 ]



class Finder(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user)
    async def tr(self, ctx, lang, *, input):
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
                trans = Translator()

                input_translated1 = trans.translate(input, dest=lang)
                input_translated = input_translated1.text

                src = input_translated1.src
                dest = input_translated1.dest

                src1 = lang_list[src.lower()]
                dest1 = lang_list[dest]

                if len(input) < 1040:
                    translate_embed = discord.Embed(
                        title=f'{src1} ({src}) ➟ {dest1} ({dest})\n‎‏‏‎ ‎',
                        color=discord.Color.blue(),

                    )

                    translate_embed.add_field(name='Source:', value=f'```\n{input}\n```', inline=False)
                    translate_embed.add_field(name='Translation:', value=f'```\n{input_translated}\n```')
                    translate_embed.set_footer(text='Translator | WebFinder v1.0')

                    await ctx.send(embed=translate_embed)

                elif 2000 > len(input) > 1040:
                    translate_embed = discord.Embed(
                        title=f'{src1} ({src}) ➟ {dest1} ({dest})\n‎‏‏‎ ‎',
                        description=f'**TRANSLATION** :\n```\n{input_translated}\n```',
                        color=discord.Color.blue(),

                    )
                    translate_embed.set_footer(text='Translator | WebFinder v1.0')

                    await ctx.send(embed=translate_embed)

                elif len(input) > 2000:
                    await ctx.send('```diff\n- Too long input\n```')



            except ValueError as VE:
                await ctx.send(f'```diff\n- ERROR: {VE}\n```')
                return

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 20, BucketType.user)
    async def wiki(self, ctx, *, input):
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
                loading = await ctx.send('`Finding on wikipedia...... Please wait!`')
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
                    summary_embed = discord.Embed(
                        description='**ERROR**: Information not found. Please check your input value and be sure that what you want to summary is existed in Wikipedia !',
                        color=discord.Color.red()

                    )
                    await ctx.send(embed=summary_embed)
                    await loading.delete()

                if 'may refer to:' in page_summary:
                    summary_embed = discord.Embed(
                        color=discord.Color.orange()
                    )

                    summary_embed.add_field(name='Hmmm.....I cannot find exactly what you want. Try to get some reference at: ', value=f'{input.title()} may refer to : [https://en.wikipedia.org/wiki/{input_low_url.lower()}](https://en.wikipedia.org/wiki/{input_low_url.lower()})')
                    summary_embed.set_footer(text='Wikipedia | WebFinder v1.0', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Wikipedia%27s_W.svg/1024px-Wikipedia%27s_W.svg.png')
                    await ctx.send(embed=summary_embed)
                    await loading.delete()

                if len(page_summary) > 30:
                    if len(page_summary) > 2000:
                        #await ctx.send('```css\nBecause the information is too long, I decide to shorten it!\n```')


                        if len(enter_find1) > 1000:
                            list_find = enter_find1.split('.')
                            list_find2 = list_find[:7]
                            list_find3 = '.'.join(list_find2)

                            summary_embed = discord.Embed(
                                color=discord.Color.lighter_grey(),
                                description=f'**{input_translated.upper()}  (shorten version)**\n\n{list_find3}'
                            )

                            summary_embed.add_field(
                                name='Find more at: ',
                                value=f'[https://en.wikipedia.org/wiki/{input_low_url.lower()}](https://en.wikipedia.org/wiki/{input_low_url.lower()})')
                            summary_embed.set_footer(text='Wikipedia | WebFinder v1.0', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Wikipedia%27s_W.svg/1024px-Wikipedia%27s_W.svg.png')
                            await ctx.send(embed=summary_embed)
                            await loading.delete()


                        else:

                            summary_embed = discord.Embed(
                                color=discord.Color.lighter_grey(),
                                description=f'**{input_translated.upper()}  (shorten version)**\n\n{enter_find1}'
                            )


                            summary_embed.add_field(
                                name='Find more at: ',
                                value=f'[https://en.wikipedia.org/wiki/{input_low_url.lower()}](https://en.wikipedia.org/wiki/{input_low_url.lower()})')
                            summary_embed.set_footer(text='Wikipedia | WebFinder v1.0', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Wikipedia%27s_W.svg/1024px-Wikipedia%27s_W.svg.png')
                            await ctx.send(embed=summary_embed)
                            await loading.delete()





                    else:
                        summary_embed = discord.Embed(
                            color=discord.Color.lighter_grey(),
                            description=f'**{input_translated.upper()}**\n\n{page_summary}'
                        )
                        summary_embed.add_field(
                            name='Find more at: ',
                            value=f'[https://en.wikipedia.org/wiki/{input_low_url.lower()}](https://en.wikipedia.org/wiki/{input_low_url.lower()})')

                        summary_embed.set_footer(text='Wikipedia | WebFinder v1.0',
                                                 icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Wikipedia%27s_W.svg/1024px-Wikipedia%27s_W.svg.png')

                        await ctx.send(embed=summary_embed)

                    wiki_embed2 = discord.Embed(
                        title="Didn't find your request ?",
                        description='Try `wiki_drt [search keyword]` or `gg [search keyword]` or `gg_drt [search keyword]` to get more information from Google',
                        color=discord.Color.gold()
                    )
                    message = await ctx.send(embed=wiki_embed2)
                    await message.add_reaction('❌')

                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) == '❌'

                    await self.client.wait_for('reaction_add', check=check)
                    await message.delete()

            except BaseException as e:
                await ctx.send(traceback.print_exc())


    async def wiki_drt(self, ctx, *, input):
        wiki_embed = discord.Embed(
            title=f'{self.client.user} has found results for "{input}" !',

            color=discord.Color.lighter_grey()
        )

        url = f'https://en.wikipedia.org/wiki/{input}'.replace(' ', '_')

        wiki_embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        wiki_embed.add_field(name=f'‎‏‏‎ ',
                               value=f'\nClick the link below to view the direct search from Wikipedia\n **[Wikipedia search: {input}]({url})**')
        wiki_embed.set_footer(text='Wikipedia | WebFinder v1.0', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Wikipedia%27s_W.svg/1024px-Wikipedia%27s_W.svg.png')

        await ctx.send(embed=wiki_embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def gg(self, ctx, *, input):
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
            for bad in input.lower().split(' '):
                if bad in bad_word_list:

                    bad = discord.Embed(
                        description='**Not sure I can continue searching with this word...!** Try to search on your own browser',
                        color=discord.Color.red()
                    )
                    await ctx.send(embed=bad)
                    break
                else:



                    query = input
                    query_list = []

                    loading = await ctx.send('`Googling.... Please wait!`')
                    i = 0
                    for j in search(query, tld="com", num=5, stop=5, pause=2):
                        i += 1
                        query_list.append(j)
                    a = query_list[0]


                    await ctx.send(a)

                    google_embed2 = discord.Embed(
                        title="Didn't find your request ?",
                        description='Try `gg_drt [search keyword]` to get the direct link to Google search',
                        color=discord.Color.gold()
                    )
                    await loading.delete()
                    message = await ctx.send(embed=google_embed2)
                    await message.add_reaction('❌')

                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) == '❌'

                    await self.client.wait_for('reaction_add', check=check)
                    await message.delete()
                    break






    @commands.command()
    @commands.guild_only()
    async def gg_drt(self, ctx, *, input):

        for bad in input.lower().split(' '):
            if bad in bad_word_list:

                bad = discord.Embed(
                    description='**Not sure I can continue searching with this word...!** Try to search on your own browser',
                    color=discord.Color.red()
                )
                await ctx.send(embed=bad)
                break
            else:
                url = f'https://www.google.com/search?safe=active&q={input}'.replace(' ', '+')
                google_embed = discord.Embed(
                    title=f'{self.client.user} has found results for "{input}" !',
                    description=f'**[Google search: {input}]({url})**',

                    color=discord.Color.green()
                )

                google_embed.set_author(name=f'{ctx.author.name}',icon_url=f'{ctx.author.avatar_url}')
                google_embed.add_field(name=f'‎-', value=f'\nClick the link above to view the direct search from Google')
                google_embed.set_footer(text='Google | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/732/732205.png')



                await ctx.send(embed=google_embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def yt(self, ctx, *, input):

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
            for bad in input.lower().split(' '):
                if bad in bad_word_list:

                    bad = discord.Embed(
                        description='**Not sure I can continue searching with this word...!** Try to search on your own browser',
                        color=discord.Color.red()
                    )
                    await ctx.send(embed=bad)
                    break
                else:

                    loading = await ctx.send('`Searching on Youtube..... PLease wait!`')
                    search_input = input.replace(' ', '+')
                    results = YoutubeSearch(f'{search_input}', max_results=1).to_dict()
                    for v in results:
                        await ctx.send('https://www.youtube.com' + v['url_suffix'])

                    youtube_embed2 = discord.Embed(
                        title="Didn't find your request ?",
                        description='Try `yt_drt [search keyword]` to get the direct link to Youtube search',
                        color=discord.Color.gold()
                    )

                    await loading.delete()
                    message = await ctx.send(embed=youtube_embed2)
                    await message.add_reaction('❌')

                    def check(reaction, user):
                        return user == ctx.author and str(reaction.emoji) == '❌'

                    await self.client.wait_for('reaction_add', check=check)
                    await message.delete()
                    break



    @commands.command()
    @commands.guild_only()
    async def yt_drt(self, ctx, *, input):

        for bad in input.lower().split(' '):
            if bad in bad_word_list:

                bad = discord.Embed(
                    description='**Not sure I can continue searching with this word...!** Try to search on your own browser',
                    color=discord.Color.red()
                )
                await ctx.send(embed=bad)
                break
            else:
                google_embed = discord.Embed(
                    title=f'{self.client.user} has found results for "{input}" !',

                    color=discord.Color.red()
                )

                url = f'https://www.youtube.com/results?safe=active&q={input}'.replace(' ', '+')

                google_embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
                google_embed.add_field(name=f'‎‏‏‎ ',
                                       value=f'\nClick the link below to view the direct search from Youtube\n **[Youtube search: {input}]({url})**')
                google_embed.set_footer(text='Youtube | WebFinder v1.0', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/1280px-YouTube_full-color_icon_%282017%29.svg.png')

                await ctx.send(embed=google_embed)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def weather(self,ctx, *, query):

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


            url = f'https://www.timeanddate.com/weather/?query={query.replace(" ", "+")}'
            loading = await ctx.send('`Getting weather information...... Please wait!`')

            random_ua = random.choice(ua_list)
            headers = {
                'authority': 'www.timeanddate.com',
                'upgrade-insecure-requests': '1',
                'user-agent': random_ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://www.timeanddate.com/weather/',
                'accept-language': 'en-US,en;q=0.9',
            }


            html = requests.get(url, headers=headers)
            print(html.status_code)
            if html.status_code == 200:
                print('Successfully access')
            if html.status_code == 404:
                print('Not found')


            soup = BeautifulSoup(html.content, 'html.parser')

            a = soup.find('td')

            try:
                b = a.find_all('a')
                if str(b) == '[]':
                    weather_error_embed = discord.Embed(
                        description="**Location not found!** Try again with only __city name__ or use `;weather_country [country name]` to get weather information of country capital",
                        color=discord.Color.red()
                    )

                    await ctx.send(embed=weather_error_embed)
                    await loading.delete()

            except AttributeError:
                weather_error_embed = discord.Embed(
                    description="**Location not found!** Try again with only __city name__ or use `;weather_country [country name]` to get weather information of country capital",
                    color=discord.Color.red()
                )

                await ctx.send(embed=weather_error_embed)
                await loading.delete()
            link_list = []
            for i in b:
                link = i.get('href')
                link_list.append('https://www.timeanddate.com' + link)


            url2 = link_list[0]

            time.sleep(random.choice(random_time_sleep))

            html2 = requests.get(url2, headers=headers)
            soup2 = BeautifulSoup(html2.content, 'html.parser')
            title = soup2.find('h1', class_='headline-banner__title')

            general = soup2.find('div', attrs={'id': 'qlook'})

            temperature = general.find('div', class_='h2')
            te2 = temperature.text
            te2 = te2.replace('.', '')

            status = general.find('p')


            more_detail = soup2.find_all('div', attrs={'id': 'qlook'})
            more_detail2 = (more_detail[0].find_all('p'))[1].text
            #more_detail2 = more_detail2.replace('°C', '°C\n')
            more_detail2 = more_detail2.replace('Feels Like:', '\n**Feels Like :**')
            more_detail2 = more_detail2.replace('Forecast:', '\n**Forecast :**')
            more_detail2 = more_detail2.replace('Wind:', '\n**Wind :**')
            more_detail2 = more_detail2.replace('↑', '')


            more = soup2.find('table', class_='table table--left table--inner-borders-rows')
            more2 = more.text
            # print(more2)
            more3 = more2.replace('Location:', '**Location :**')
            more3 = more3.replace('Current Time:', '\n**Current Time :**')
            more3 = more3.replace('Latest Report:', '\n**Latest Report :**')
            more3 = more3.replace('Visibility:', '\n**Visibility :**')
            more3 = more3.replace('Pressure', '\n**Pressure :** ')
            more3 = more3.replace('Humidity:', '\n**Humidity :**')
            more3 = more3.replace('Dew Point:', '\n**Dew Point :**')




            weather_embed = discord.Embed(
                title=title.text,
                color=discord.Color.teal()
            )
            #weather_embed.set_author(name=title.text, icon_url=f'{ctx.author.avatar_url}')

            weather_embed.add_field(name='-', value=f'**Temperature :** {te2}\n**Weather status :** {status.text}', inline=False)
            weather_embed.add_field(name='-----------------------', value=more_detail2,inline=False)
            weather_embed.add_field(name='-----------------------', value=more3,inline=False)
            weather_embed.set_thumbnail(url=random.choice(random_status))

            weather_embed.set_footer(text='Weather forecast | WebFinder v1.0', icon_url='https://icon-library.com/images/weather-icon-png/weather-icon-png-15.jpg')

            await ctx.send(embed=weather_embed)
            await loading.delete()

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def weather_country(self, ctx, *, query):

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

            url = f'https://www.timeanddate.com/weather/{query.replace(" ", "-")}'
            loading = await ctx.send('`Getting weather information...... Please wait!`')
            random_ua = random.choice(ua_list)
            headers = {
                'authority': 'www.timeanddate.com',
                'upgrade-insecure-requests': '1',
                'user-agent': random_ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://www.timeanddate.com/weather/',
                'accept-language': 'en-US,en;q=0.9',
            }

            html = requests.get(url, headers=headers)

            if html.status_code == 200:
                print('Successfully access')
                soup = BeautifulSoup(html.content, 'html.parser')
                capital_list = []
                for a in soup.find_all('a'):
                    b = str(a.get('href'))
                    if '/weather/' in b:
                        capital_list.append(b)

                capital_url = 'https://www.timeanddate.com' + capital_list[3]

                capital_name = (capital_list[4].replace(f'/weather/{query.lower().replace(" ", "-")}/', ''))
                capital_name = capital_name.replace('-', ' ')
                capital_name = capital_name.title()

                time.sleep(random.choice(random_time_sleep))

                html2 = requests.get(capital_url, headers=headers)

                soup = BeautifulSoup(html2.content, 'html.parser')
                general = soup.find('div', attrs={'id': 'qlook'})
                general2 = general.text

                # general2 = general2.replace('Country Capital{}'.format(query.title()), '**Temperature:**  ')
                if '°F' in general2:
                    general2_find = general2.find('°F')
                    general2 = general2[general2_find + 2:]
                elif '°C' in general2:
                    general2_find = general2.find('°C')
                    general2 = general2[general2_find + 2:]

                general2 = '**Weather status:**  ' + general2
                general2 = general2.replace('Feels Like:', '\n**Feels Like:**  ')
                general2 = general2.replace('Forecast:', '\n**Forecast:**  ')
                general2 = general2.replace('Wind:', '\n**Wind:**  ')
                general2 = general2.replace('↑', '')
                general2_list = general2.split('\n')

                general3 = '\n'.join(general2_list)

                more = soup.find('table', class_='table table--left table--inner-borders-rows')
                more2 = more.find('tbody')
                more2 = more2.text
                find_more2 = more2.find('Country High:')
                more3 = more2[find_more2:]
                more3 = more3.replace('°C', '°C -- ')
                more3 = more3.replace('°F', '°F -- ')
                more3 = more3.replace('km/h', 'km/h -- ')
                more3 = more3.replace('mph', 'mph -- ')
                more3 = more3.replace('Country High:', '**Country High:**  ')
                more3 = more3.replace('Country Low:', '\n**Country Low:**  ')
                more3 = more3.replace('Max Wind:', '\n**Max Wind:**  ')

                weather_embed = discord.Embed(
                    title=f'Weather in ' + capital_name.upper() + f' ( the capital city )',
                    color=discord.Color.teal()
                )

                weather_embed.add_field(name='-', value=general3, inline=False)
                weather_embed.add_field(name='------More detail------', value=more3)
                weather_embed.set_footer(text='Weather forecast | WebFinder v1.0', icon_url='https://icon-library.com/images/weather-icon-png/weather-icon-png-15.jpg')
                weather_embed.set_thumbnail(
                    url=random.choice(random_status))

                await ctx.send(embed=weather_embed)
                await loading.delete()
            if html.status_code == 404:
                print('Not found')
                weather_error_embed = discord.Embed(
                    description="**Country not found!** Make sure to find the correct country name",
                    color=discord.Color.red()
                )

                await ctx.send(embed=weather_error_embed)
                await loading.delete()






    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 20, BucketType.user)
    async def sc(self, ctx, *, query):

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
                random_ua = random.choice(ua_list)
                headers = {
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Cache-Control': 'max-age=0',
                    'User-Agent': random_ua,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Referer': 'https://www.google.com/',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Accept-Language': 'en-US,en;q=0.9'}

                #await ctx.send('```\nGetting soundtracks..... Please wait!\n```')
                url = 'https://soundcloud.com/search?q=' + query.replace(' ', '%20')

                html = requests.get(url, headers=headers)


                soup = BeautifulSoup(html.content, 'html.parser')

                a = soup.find_all('a')


                query1 = query.replace(' ', "' and '")
                query2 = "'" + query1 + "'"

                re_list = []

                for b in a:
                    c = b.get('href')


                    if eval(query2) in c:
                        re_list.append('https://soundcloud.com' + c)

                await ctx.send(re_list[0])
                sc_embed2 = discord.Embed(
                    title="Didn't find your request ?",
                    description='Try `sc_drt [search keyword]` to get the direct link to Soundcloud search',
                    color=discord.Color.gold()
                )
                message = await ctx.send(embed=sc_embed2)
                await message.add_reaction('❌')


                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) == '❌'

                await self.client.wait_for('reaction_add', check=check)
                await message.delete()

    @commands.command()
    @commands.guild_only()
    async def sc_drt(self, ctx, *, input):
                google_embed = discord.Embed(
                    title=f'{self.client.user} has found results for "{input}" !',

                    color=discord.Color.orange()
                )

                url = f'https://soundcloud.com/search?q={input}'.replace(' ', '%20')

                google_embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
                google_embed.add_field(name=f'‎‏‏‎ ',
                                       value=f'\nClick the link below to view the direct search from Soundcloud\n **[Sonudcloud search: {input}]({url})**')
                google_embed.set_footer(text='Soundcloud | WebFinder v1.0',
                                        icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')
                await ctx.send(embed=google_embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def sc_list(self, ctx, number: int, *, query):
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
                if int(number) > 10:
                    sc2_embed = discord.Embed(
                        title='Max search is 10! Please try again.',
                        color=discord.Color.orange()
                    )

                    await ctx.send(embed=sc2_embed)
                else:

                    random_ua = random.choice(ua_list)
                    headers = {
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': random_ua,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Accept-Language': 'en-US,en;q=0.9'}

                    loading = await ctx.send('`Getting soundtracks..... Please wait!`')
                    url = 'https://soundcloud.com/search?q=' + query.replace(' ', '%20')

                    html = requests.get(url, headers=headers)


                    soup = BeautifulSoup(html.content, 'html.parser')

                    a = soup.find_all('a')


                    query1 = query.replace(' ', "' and '")
                    query2 = "'" + query1 + "'"

                    re_list = []
                    name_list = []
                    username_list = []

                    for b in a:

                        c = b.get('href')
                        username_find = c[1:].find('/')
                        username = c[1:username_find+1]
                        username_list.append(username)

                        d = b.text

                        name_list.append(d)

                        if eval(query2) in c:
                            re_list.append('https://soundcloud.com' + c)

                    username_list = username_list[6:-7]

                    name_list2 = name_list[6:-7]


                    try:
                        if len(name_list2) == 10:

                            links_result_list = []
                            w = 0
                            while w < int(number):
                                w = w+1
                                links_result = f'**{w}. {name_list2[w - 1]} :**\n- Posted by: [{username_list[w - 1]}](https://soundcloud.com/{username_list[w - 1]})\n- Link: {re_list[w - 1]}'
                                links_result_list.append(links_result)

                            sc_final = '\n'.join(links_result_list)


                            if len(sc_final) > 2048:
                                length_embed = discord.Embed(
                                    description="**The amount of words in soundtracks is larger than 2048 so I can't print out the result**! Sorry for this inconvenience...",
                                    color=discord.Color.orange()
                                )

                                url = f'https://soundcloud.com/search?q={query}'.replace(' ', '%20')


                                length_embed.add_field(name=f'‎‏‏‎ ',
                                                       value=f'\nClick the link below to view the direct search from Soundcloud\n [Cloudcloud search: {query}]({url})')
                                length_embed.set_footer(text='Soundcloud | WebFinder v1.0',
                                                        icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')
                                await ctx.send(embed=length_embed)
                                await loading.delete()

                            else:
                                if int(number) < 11:
                                    soundcloud_embed = discord.Embed(
                                        title=f'‎‏‏‎{self.client.user} has found tracks for " {query} " : ‎',
                                        description=sc_final,
                                        color=discord.Color.orange()
                                    )

                                    soundcloud_embed.set_footer(text='Soundcloud | WebFinder v1.0', icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')
                                    await ctx.send(embed=soundcloud_embed)
                                    await loading.delete()


                        elif len(name_list2) < 10:


                            links_result_list = []
                            w = 0
                            while w < len(name_list2):
                                w = w + 1
                                links_result = f'**{w}. {name_list2[w - 1]} :**\n- Posted by: [{username_list[w - 1]}](https://soundcloud.com/{username_list[w - 1]})\n- Link: {re_list[w - 1]}'
                                links_result_list.append(links_result)

                            sc_final = '\n'.join(links_result_list)

                            soundcloud_embed = discord.Embed(
                                title="**The amount of soundtracks didn't satisfy your request**! Sorry for this inconvenience...",
                                description=sc_final,
                                color=discord.Color.orange()
                            )

                            soundcloud_embed.set_footer(text='Soundcloud | WebFinder v1.0',
                                                        icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')
                            await ctx.send(embed=soundcloud_embed)
                            await loading.delete()

                    except BaseException as e:
                        await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def sc_playlist(self, ctx, number: int, *, query):

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

                if int(number) > 10:
                    sc2_embed = discord.Embed(
                        title='Max search is 10! Please try again.',
                        color=discord.Color.orange()
                    )

                    await ctx.send(embed=sc2_embed)
                else:

                    random_ua = random.choice(ua_list)
                    headers = {
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': random_ua,
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-User': '?1',
                        'Sec-Fetch-Dest': 'document',
                        'Accept-Language': 'en-US,en;q=0.9'}

                    loading = await ctx.send('`Getting playlists..... Please wait!`')
                    url = 'https://soundcloud.com/search/sets?q=' + query.replace(' ', '%20')

                    html = requests.get(url, headers=headers)

                    soup = BeautifulSoup(html.content, 'html.parser')

                    a = soup.find_all('a')

                    query1 = query.replace(' ', "' and '")
                    query2 = "'" + query1 + "'"

                    re_list = []
                    name_list = []
                    username_list = []

                    for b in a:

                        c = b.get('href')
                        username_find = c.find('/sets/')
                        username = c[1:username_find]
                        username_list.append(username)

                        d = b.text

                        name_list.append(d)

                        if eval(query2) in c:
                            re_list.append('https://soundcloud.com' + c)

                    username_list = username_list[6:-7]

                    name_list2 = name_list[6:-7]


                    if len(name_list2) == 10:
                        links_result_list = []
                        w = 0
                        while w < int(number):
                            w = w + 1
                            links_result = f'**{w}. {name_list2[w - 1]} :**\n- Posted by: [{username_list[w-1]}](https://soundcloud.com/{username_list[w-1]})\n- Link: {re_list[w - 1]}'
                            links_result_list.append(links_result)

                        sc_final = '\n'.join(links_result_list)




                        if int(number) < 11:
                            soundcloud_embed = discord.Embed(
                                title=f'‎‏‏‎{self.client.user} has found playlist for " {query} " : ‎',
                                description=sc_final,
                                color=discord.Color.orange()
                            )

                            soundcloud_embed.set_footer(text='© Soundcloud | WebFinder v1.0', icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')
                            await ctx.send(embed=soundcloud_embed)
                            await loading.delete()

                    elif len(name_list2) < 10:


                        links_result_list = []
                        w = 0
                        while w < len(name_list2):
                            w = w + 1
                            links_result = f'**{w}. {name_list2[w - 1]} :**\n- Posted by: [{username_list[w - 1]}](https://soundcloud.com/{username_list[w - 1]})\n- Link: {re_list[w - 1]}'
                            links_result_list.append(links_result)

                        sc_final = '\n'.join(links_result_list)

                        soundcloud_embed = discord.Embed(
                            title="**The amount of playlist didn't satisfy your request**! Sorry for this inconvenience...",
                            description=sc_final,
                            color=discord.Color.orange()
                        )

                        soundcloud_embed.set_footer(text='Soundcloud | WebFinder v1.0',
                                                    icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')
                        await ctx.send(embed=soundcloud_embed)
                        await loading.delete()



    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def sc_top(self, ctx):

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
            url = 'https://soundcloud.com/charts/top'

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
                title='Soundcloud top 10 most played tracks',
                description=the_final,
                color=discord.Color.orange()
            )
            top_embed.set_footer(text='© Soundcloud | WebFinder v1.0',
                                        icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')

            await loading.delete()
            await ctx.send(embed=top_embed)


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, random.choice(random_delay), BucketType.user)
    async def sc_user(self, ctx, *, query):

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
                random_ua = random.choice(ua_list)
                headers = {
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': random_ua,
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-User': '?1',
                        'Sec-Fetch-Dest': 'document',
                        'Accept-Language': 'en-US,en;q=0.9'}

                loading = await ctx.send('`Getting user information..... Please wait!`')
                url = 'https://soundcloud.com/search/people?q=' + query.replace(' ', '%20')

                html = requests.get(url, headers=headers)

                soup = BeautifulSoup(html.content, 'html.parser')

                a = soup.find_all('a')

                #query1 = query.replace(' ', "' and '")
                #query2 = "'" + query1 + "'"

                re_list = []
                name_list = []


                for b in a[6:-7]:

                    c = b.get('href')

                    d = b.text

                    name_list.append(d)

                    re_list.append('https://soundcloud.com' + c)


                try:
                    if len(name_list) == 10:
                        links_result_list = []
                        w = 0
                        while w < 12:
                            try:
                                w = w + 1
                                links_result = f'**{w}. {name_list[w - 1]} :**\n- Link: {re_list[w - 1]}'

                                links_result_list.append(links_result)

                            except IndexError:
                                print('')

                        sc_final = '\n'.join(links_result_list)



                        soundcloud_embed = discord.Embed(
                                title=f'‎‏‏‎{self.client.user} has found playlist for " {query} " : ‎',
                                description=sc_final,
                                color=discord.Color.orange()
                            )

                        soundcloud_embed.set_footer(text='© Soundcloud | WebFinder v1.0',
                                                            icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')
                        await ctx.send(embed=soundcloud_embed)
                        await loading.delete()

                    elif len(name_list) < 10:


                        links_result_list = []
                        w = 0
                        while w < len(name_list):
                            w = w + 1
                            links_result = f'**{w}. {name_list[w - 1]} :**\n- Link: {re_list[w - 1]}'
                            links_result_list.append(links_result)

                        sc_final = '\n'.join(links_result_list)

                        soundcloud_embed = discord.Embed(
                            title="**The amount of users didn't satisfy your request**! Sorry for this inconvenience...",
                            description=sc_final,
                            color=discord.Color.orange()
                        )

                        soundcloud_embed.set_footer(text='Soundcloud | WebFinder v1.0',
                                                    icon_url='https://cdn2.iconfinder.com/data/icons/significon-social/512/Significon-SoundCloud-512.png')
                        await ctx.send(embed=soundcloud_embed)
                        await loading.delete()

                except BaseException as e:
                    await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user)
    async def dict(self, ctx, *, query):
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
            loading = await ctx.send('`Finding for definition..... Please wait!`')
            dictionary = PyDictionary()
            try:
                meaning = dictionary.meaning(query)

                meaning_list2 = []
                for a in meaning:
                    meaning_list = meaning[a]
                    meaning_list2.append(f'**---------- {a} ----------**')
                    for i in meaning_list[:5]:
                        if '(' in i:
                            i2 = i + ')'
                            meaning_list2.append('- '+  i2)
                        if '(' not in i:
                            meaning_list2.append('- ' + i)
                    #meaning_list2.append('.....')

                final_meaning = "\n".join(meaning_list2)

                dict_embed = discord.Embed(
                    title=f'Definition of " {query.upper()} "',
                    description=final_meaning,
                    color=discord.Color.purple()
                )

                dict_embed.set_footer(text='Dictionary | WebFinder v1.0',
                                            icon_url='https://icons.iconarchive.com/icons/dtafalonso/android-lollipop/512/Play-Books-icon.png')

                await ctx.send(embed=dict_embed)
                await loading.delete()
            except TypeError :
                error_embed = discord.Embed(
                    description="**Word not found!** Make sure that you typed the word correctly (*this mustn't be a string*)",
                    color=discord.Color.red()
                )
                await ctx.send(embed=error_embed)
                await loading.delete()



def setup(client):
    client.add_cog(Finder(client))
