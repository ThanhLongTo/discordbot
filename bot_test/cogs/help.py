import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import datetime


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # BASIC HELP
    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        embed1 = discord.Embed(
            title='Instruction',
            description='These are all available commands you can use\n**BOT prefix:**   `n!`',
            color=discord.Color.green()
        )

        embed1.set_author(name='Help',
                          icon_url='https://www.whywrong.com/wp-content/uploads/2018/05/question-mark_318-52837-600x600.jpg')
        embed1.add_field(name='Basic:',
                         value='ping\n'
                               'av\n',
                         inline=False)
        embed1.add_field(name='Management:',
                         value='clear [number]\n'
                               'kick [mention]\n'
                               'ban [mention]\n'
                               'unban [member name]\n',
                         inline=False)
        embed1.add_field(name='Solve equation:', value='help_equ')
        embed1.add_field(name='Calculation:', value='help_calc\nhelp_calc_pow\nhelp_calc_shape', inline=False)
        embed1.add_field(name='Summary:', value='help_summary\nhelp_lang_code', inline=False)
        embed1.add_field(name='Converter:', value='help_conv\nhelp_cur_conv', inline=False)
        embed1.add_field(name='Translate:', value='help_translate\nhelp_lang_code')
        embed1.add_field(name='Advertisement:', value='about', inline=False)

        await ctx.send(f'{author.mention}', embed=embed1)

        embed2 = discord.Embed(
            title='WARNING',
            description='**`TechNo#9240` is in beta version with variety of errors ( and __never be done__ because this is my first experiment), so please do not try to crash it.**',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed2)


    @commands.command()
    async def help_translate(self, ctx):
        translate_embed = discord.Embed(
            title='Instruction',
            description='These are all available commands you can use',
            color=discord.Color.orange()
        )

        translate_embed.add_field(name='Use: `n!tr [language to translate to] [messages]`', value='''Example: `n!tr vi Good morning` : Translate " Good morning " from English to Vietnamese\n `n!help_lang_code` for detailed codes you can use ''')
        await ctx.send(embed=translate_embed)
    # EQUATIONS HELP
    @commands.command()
    async def help_equ(self, ctx):
        author = ctx.message.author

        embed2 = discord.Embed(
            title='Instruction',
            description='These are all available commands you can use',
            color=discord.Color.orange()
        )

        embed2.set_author(name='Equation help',
                          icon_url='https://i.pinimg.com/564x/dd/81/1b/dd811bb6fc0cc852f351be0ab34b21ee.jpg')
        embed2.add_field(name='Solve equation:',
                         value='''```bash
  "EQUATION (WITH 1 VARIABLE): equ_1"
ax + b = c

ex:
2x -10 = 16
x + y = 2
Answer: [x]

 ex:
x^2 -7x + 12 = 0
 input:
 n!equ_1 x^2-7*x+12=0 
 Answer: [x1 , x2]


  "EQUATION (WITH 2 VARIABLES): equ_2"
(a1)x + (b1)y = (c1)
(a2)x + (b2)y = (c2)
    
 ex:
1x + 1y = 20     
250x + 350y = 5600
 input: n!equ_2 1 1 20 250 350 5600
 Answer: [x y]


  "EQUATION (WITH 3 VARIABLES): equ_3"
(a1)x + (b1)y + (c1)z = (d1)
(a2)x + (b2)y + (c2)z = (d2)
                           
 ex:
x + y + z = 2
6x -4y + 5z = 31
5x + 2y + 2z = 13
    
 input: n!equ_3 1 1 1 2 6 -4 5 31 5 2 2 13
 Answer: [x y z]

NOTE : Sometimes equation solver will cause a few problems. Sorry for this inconvenience 
     ```'''
                         )

        await ctx.send(f'{author.mention}', embed=embed2)

    # CALCULATION
    @commands.command()
    async def help_calc(self, ctx):
        calc_embed = discord.Embed(
            title='Instruction',
            description='These are all available commands you can use',
            color=discord.Color.orange()
        )

        calc_embed.add_field(name='Arithmetic operations:', value=''' 
`+` : addition
`-` : subtraction
`*` : multiplication
`/` : division
`^` : exponentiation
`!` : factorial''')
        calc_embed.add_field(name='Comparison:', value='''

`>`  : Greater than.
`<`  : Less than.
`==` : Equal to (**two = signs for comparison**)
`>=` : Greater or equal.
`<=` : Less than or equal.
`!=` : Not equal
                ''')

        await ctx.send(embed=calc_embed)

        # MATH FUNCTION HELP
        calc1_embed = discord.Embed(
            title='Function',
            description='''
    ```
    - ceil(x)        :  Returns the smallest integer greater than or equal to x.
    - copysign(x, y) :  Returns x with the sign of y
    - fabs(x)        :  Returns the absolute value of x
    - factorial(x)   :   Returns the factorial of x
    - floor(x)       :   Returns the largest integer less than or equal to x
    - fmod(x, y)     :   Returns the remainder when x is divided by y
    - frexp(x)       :   Returns the mantissa and exponent of x as the pair (m,e)
    - fsum(iterable) :   Returns an accurate floating point sum of values in the iterable
    - isfinite(x)    :   Returns True if x is neither an infinity nor a NaN (Not a Number)
    - isinf(x)       :   Returns True if x is a positive or negative infinity
    - isnan(x)       :   Returns True if x is a NaN
    - ldexp(x, i)    :   Returns x * (2**i)
    - modf(x)        :   Returns the fractional and integer parts of x
    - trunc(x)       :   Returns the truncated integer value of x
    - exp(x)         :   Returns e**x
    - expm1(x)       :   Returns e**x - 1
    ```
            ''',
            color=discord.Color.orange()
        )
        calc1_embed.set_footer(text='page 1')
        await ctx.send(embed=calc1_embed)

        calc2_embed = discord.Embed(
            title='',
            description='''
    ```
    - log(x[, base]):  Returns the logarithm of x to the base (defaults to e)
    - log1p(x)      :  Returns the natural logarithm of 1+x
    - log2(x)       :  Returns the base-2 logarithm of x
    - log10(x)      :  Returns the base-10 logarithm of x
    - pow(x, y)     :  Returns x raised to the power y
    - sqrt(x)       :  Returns the square root of x
    - acos(x)       :  Returns the arc cosine of x
    - asin(x)       :  Returns the arc sine of x
    - atan(x)       :  Returns the arc tangent of x
    - atan2(y, x)   :  Returns atan(y / x)
    - cos(x)        :  Returns the cosine of x
    - hypot(x, y)   :  Returns the Euclidean norm, sqrt(x*x + y*y)
    - sin(x)        :  Returns the sine of x
    - tan(x)        :  Returns the tangent of x
    - degrees(x)    :  Converts angle x from radians to degrees
    - radians(x)    :  Converts angle x from degrees to radians
            ```''',
            color=discord.Color.orange()
        )
        calc2_embed.set_footer(text='page 2')
        await ctx.send(embed=calc2_embed)

        calc3_embed = discord.Embed(
            title='',
            description='''
    ```
    - acosh(x)       :  Returns the inverse hyperbolic cosine of x
    - asinh(x)       :  Returns the inverse hyperbolic sine of x
    - atanh(x)       :  Returns the inverse hyperbolic tangent of x
    - cosh(x)        :  Returns the hyperbolic cosine of x
    - sinh(x)        :  Returns the hyperbolic cosine of x
    - tanh(x)        :  Returns the hyperbolic tangent of x
    - erf(x)         :  Returns the error function at x
    - erfc(x)        :  Returns the complementary error function at x
    - gamma(x)       :  Returns the Gamma function at x
    - lgamma(x)      :  Returns the natural logarithm of the absolute value of                       the Gamma function at x
    - pi             :  Mathematical constant, the ratio of circumference of a     circle to its diameter (3.14159...)
    - e              :  Mathematical constant e (2.71828...)
    - abs(x)         :  for absolute value
    - round(x)       :  to round a number to a certain decimal point
    - lambertw(x)    :
    ```''',
            color=discord.Color.orange()
        )
        calc3_embed.set_footer(text='page 3')
        await ctx.send(embed=calc3_embed)

        calc5_embed = discord.Embed(
            title='',
            description='''
ex:
n!calc 1+1
n!calc cos(60)
n!calc 2>1>-9
    ...
''',
            color=discord.Color.light_grey()

        )
        await ctx.send(embed=calc5_embed)


    @commands.command()

    async def help_calc_pow(self, ctx):
        pow_embed = discord.Embed(
            title='Instruction',
            description='Only `Nautilus#3374` can use this!',
            color=discord.Color.orange()
        )

        pow_embed.add_field(name='This is powerful module to calculate very large numbers and just in beta version so just for only me!',
                            value='Example: n!calc_pow 9999^9999')
        await ctx.send(embed=pow_embed)


    @commands.command()
    async def help_conv(self, ctx):
        conv_embed = discord.Embed(
            title='Instruction',
            description='These are all available commands you can use\n**__Note__: Remember to capitalize correct word or it will cause error!( n!help for instruction )**',
            color=discord.Color.orange()
            )

        conv_embed.set_author(name='Unit Converter')
        conv_embed.add_field(name='Length : `n!le_conv`', value='''
meter [m]
kilometer [km]
decimeter [dm]
centimeter [cm]
millimeter [mm]
micrometer [µm]
nanometer [nm]
mile [mi]
yard [yd]
foot [ft]
inch [in]
light year [ly]
exameter [Em]
petameter [Pm]
terameter [Tm]
gigameter [Gm]
megameter [Mm]
hectometer [hm]
dekameter [dam]
micron [µ]
picometer [pm]
femtometer [fm]
attometer [am]
megaparsec [Mpc]
kiloparsec [kpc]
parsec [pc]
astronomical-unit [AU]
league [lea]
chain [ch]
rod [rd]
angstrom [A]
handbreadth
fingerbreadth(
Planck length
Electron radius
Bohr radius
Sun radius
.......\n
''')
        conv_embed.add_field(name='Weight & Mass : `n!we_conv`', value='''
kilogram [kg]
gram [g]
milligram [mg]
ton (metric) [t]
pound [lbs]
ounce [oz]
carat [car]
ton [ton] 
Atomic-mass-unit [u]
exagram [Eg]
petagram [Pg]
teragram [Tg]
gigagram [Gg]
megagram [Mg]
hectogram [hg]
dekagram [dag]
decigram [dg]
centigram [cg]
microgram [µg]
nanogram [ng]
picogram [pg]
femtogram [fg]
attogram [ag]
Planck mass
Electron mass
Muon mass
Proton mass
Neutron mass
Deuteron mass
Earth mass
Sun mass
.........
''')

        conv_embed.add_field(name='Area : `n!ar_conv`', value='''
square meter [m^2]
square kilometer [km^2]
square centimeter [cm^2]
square millimeter [mm^2]
square micrometer [µm^2]
hectare [ha]
acre [ac]
square mile [mi^2]
square yard [yd^2]
square foot [ft^2]
square inch [in^2]
square hectometer [hm^2]
square dekameter [dam^2]
square decimeter [dm^2]
square nanometer [nm^2]
are [a]
barn [b]
square chain [ch^2]
square mil [mil^2]''')

        conv_embed.add_field(name='Volume : `n!vo_conv`', value='''
cubic meter [m^3] 
cubic kilometer [km^3] 
cubic centimeter [cm^3] 
cubic millimeter [mm^3] 
liter [l] 
milliliter [mL] 
gallon [gal] 
quart [qt] 
pint [pt] 
cup 
tablespoon 
teaspoon 
cubic mile [mi^3] 
cubic yard [yd^3] 
cubic foot [ft^3] 
cubic inch [in^3] 
cubic decimeter [dm^3] 
exaliter [EL] 
petaliter [PL] 
teraliter [TL] 
gigaliter [GL] 
megaliter [ML] 
kiloliter [kL] 
hectoliter [hL] 
dekaliter [daL] 
deciliter [dL] 
centiliter [cL] 
microliter [µL] 
nanoliter [nL] 
picoliter [pL] 
femtoliter [fL] 
attoliter [aL] 
drop 
barrel [bbl] 
fluid ounce [fl-oz] 
gill  [gi] 
minim 
acre foot [ac-ft] 
acre inch [ac-in] 
dekastere 
stere [st] 
Earth volume ''')

        conv_embed.add_field(name='Temperature : `n!te_conv`',value='''
Kelvin [K]
Celsius [°C]
Fahrenheit [°F]
Rankine [°R]
Reaumur [°r]
''')
        conv_embed.add_field(name='Speed : `n!sp_conv`', value='''
meter/second [m/s]
kilometer/hour [km/h]
mile/hour [mi/h]
meter/hour [m/h]
meter/minute [m/min]
kilometer/minute [km/min]
kilometer/second [km/s]
centimeter/hour [cm/h]
centimeter/minute [cm/min]
centimeter/second [cm/s]
millimeter/hour [mm/h]
millimeter/minute [mm/min]
millimeter/second [mm/s]
foot/hour [ft/h]
foot/minute [ft/min]
foot/second [ft/s]
yard/hour [yd/h]
yard/minute [yd/min]
yard/second [yd/s]
mile/minute [mi/min]
mile/second [mi/s]
knot [kt, kn]''')

        conv_embed.add_field(name='Example: ', value='''
__NOTE__ : use n!calc round(...) to round a number to a certain decimal point if the result wasn't as you want
           Put " - " instead of "space" ( ex: neutron-mass; cubic-meter;...)
           
n!le_conv 1 meter kilometer : Convert 1 meter to kilometer
n!we_conv 7 ton neutron-mass : Convert 7 ton to neutron-mass
....''')


        await ctx.send(embed=conv_embed)



    @commands.command()
    async def help_cur_conv(self, ctx):
        conv1_embed = discord.Embed(
            title='Instruction',
            description='These are all available commands you can use',
            color=discord.Color.blurple()
        )

        conv1_embed.set_author(name='Unit Converter')
        conv1_embed.set_footer(text='Page 1')
        conv1_embed.add_field(name='Currency Converter ', value='''
```ini
USD [United States Dollar] 
EUR [Euro] 
AUD [Australian Dollar] 
CAD [Canadian Dollar] 
CHF [Swiss Franc] 
CNY [Chinese Yuan] 
EUR [Euro] 
GBP [British Pound Sterling] 
INR [Indian Rupee] 
JPY [Japanese Yen] 
MXN [Mexican Peso] 
AED [United Arab Emirates Dirham] 
AFN [Afghan Afghani] 
ALL [Albanian Lek] 
AMD [Armenian Dram] 
ANG [Netherlands Antillean Guilder] 
AOA [Angolan Kwanza] 
ARS [Argentine Peso] 
AWG [Aruban Florin] 
AZN [Azerbaijani Manat] 
BAM [Bosnia-Herzegovina Convertible Mark] 
BBD [Barbadian Dollar] 
BDT [Bangladeshi Taka] 
BGN [Bulgarian Lev] 
BHD [Bahraini Dinar] 
BIF [Burundian Franc] 
BMD [Bermudan Dollar] 
BND [Brunei Dollar] 
BOB [Bolivian Boliviano] 
BRL [Brazilian Real] 
BSD [Bahamian Dollar] 
BTC [Bitcoin] 
BTN [Bhutanese Ngultrum] 
BWP [Botswanan Pula] 
BYN [Belarusian Ruble] 
```
''')
        await ctx.send(embed=conv1_embed)


        conv2_embed = discord.Embed(
            title='',
            description='''
```ini
BZD [Belize Dollar]
CDF [Congolese Franc]
CLF [Chilean Unit of Account]
CLP [Chilean Peso]
CNH [Chinese Yuan]
CNY [Chinese Yuan]
COP [Colombian Peso]
CRC [Costa Rican Colón]
CUC [Cuban Convertible Peso]
CUP [Cuban Peso]
CVE [Cape Verdean Escudo]
CZK [Czech Republic Koruna]
DJF [Djiboutian Franc]
DKK [Danish Krone]
DOP [Dominican Peso]
DZD [Algerian Dinar]
EGP [Egyptian Pound]
ERN [Eritrean Nakfa]
ETB [Ethiopian Birr]
FJD [Fijian Dollar]
FKP [Falkland Islands Pound]
GEL [Georgian Lari]
GGP [Guernsey Pound]
GHS [Ghanaian Cedi]
GIP [Gibraltar Pound]
GMD [Gambian Dalasi]
GNF [Guinean Franc]
GTQ [Guatemalan Quetzal]
GYD [Guyanaese Dollar]
HKD [Hong Kong Dollar]
HNL [Honduran Lempira]
HRK [Croatian Kuna]
HTG [Haitian Gourde]
HUF [Hungarian Forint]
IDR [Indonesian Rupiah]
```''',
        color=discord.Color.blurple()
        )
        conv2_embed.set_footer(text='Page 2')
        await ctx.send(embed=conv2_embed)


        conv3_embed = discord.Embed(
            title='',
            description='''
```ini
ILS [Israeli New Sheqel]
IMP [Manx pound]
IQD [Iraqi Dinar]
IRR [Iranian Rial]
ISK [Icelandic Króna]
JEP [Jersey Pound]
JMD [Jamaican Dollar]
JOD [Jordanian Dinar]
KES [Kenyan Shilling]
KGS [Kyrgystani Som]
KHR [Cambodian Riel]
KMF [Comorian Franc]
KPW [North Korean Won]
KRW [South Korean Won]
KWD [Kuwaiti Dinar]
KYD [Cayman Islands Dollar]
KZT [Kazakhstani Tenge]
LAK [Laotian Kip]
LBP [Lebanese Pound]
LKR [Sri Lankan Rupee]
LRD [Liberian Dollar]
LSL [Lesotho Loti]
LYD [Libyan Dinar]
MAD [Moroccan Dirham]
MDL [Moldovan Leu]
MGA [Malagasy Ariary]
MKD [Macedonian Denar]
MMK [Myanma Kyat]
MNT [Mongolian Tugrik]
MOP [Macanese Pataca]
MRO [Mauritanian Ouguiya]
MRU [Mauritanian Ouguiya]
MUR [Mauritian Rupee]
MVR [Maldivian Rufiyaa]
MWK [Malawian Kwacha]
```''',
            color=discord.Color.blurple()
        )
        conv3_embed.set_footer(text='Page 3')
        await ctx.send(embed=conv3_embed)

        conv4_embed = discord.Embed(
            title='',
            description='''
```ini
MYR [Malaysian Ringgit]
MZN [Mozambican Metical]
NAD [Namibian Dollar]
NGN [Nigerian Naira]
NIO [Nicaraguan Córdoba]
NOK [Norwegian Krone]
NPR [Nepalese Rupee]
NZD [New Zealand Dollar]
OMR [Omani Rial]
PAB [Panamanian Balboa]
PEN [Peruvian Nuevo Sol]
PGK [Papua New Guinean Kina]
PHP [Philippine Peso]
PKR [Pakistani Rupee]
PLN [Polish Zloty]
PYG [Paraguayan Guarani]
QAR [Qatari Rial]
RON [Romanian Leu]
RSD [Serbian Dinar]
RUB [Russian Ruble]
RWF [Rwandan Franc]
SAR [Saudi Riyal]
SBD [Solomon Islands Dollar]
SCR [Seychellois Rupee]
SDG [Sudanese Pound]
SEK [Swedish Krona]
SGD [Singapore Dollar]
SHP [Saint Helena Pound]
SLL [Sierra Leonean Leone]
SOS [Somali Shilling]
SRD [Surinamese Dollar]
SSP [South Sudanese Pound]
STD [São Tomé and Príncipe Dobra]
STN [São Tomé and Príncipe Dobra]
SVC [Salvadoran Colón]
```''',
        color=discord.Color.blurple())
        conv4_embed.set_footer(text='Page 4')
        await ctx.send(embed=conv4_embed)

        conv5_embed = discord.Embed(
            title='',
            description='''
```ini
SYP [Syrian Pound]
SZL [Swazi Lilangeni]
THB [Thai Baht]
TJS [Tajikistani Somoni]
TMT [Turkmenistani Manat]
TND [Tunisian Dinar]
TOP [Tongan Pa anga]
TRY [Turkish Lira]
TTD [Trinidad and Tobago Dollar]
TWD [New Taiwan Dollar]
TZS [Tanzanian Shilling]
UAH [Ukrainian Hryvnia]
UGX [Ugandan Shilling]
UYU [Uruguayan Peso]
UZS [Uzbekistan Som]
VEF [Venezuelan Bolívar Fuerte]
VES [Venezuelan Bolívar Soberano]
VND [Vietnamese Dong]
VUV [Vanuatu Vatu]
WST [Samoan Tala]
XAF [CFA Franc BEAC]
XAG [Silver Ounce]
XAU [Gold Ounce]
XCD [East Caribbean Dollar]
XDR [Special Drawing Rights]
XOF [CFA Franc BCEAO]
XPD [Palladium Ounce]
XPF [CFP Franc]
XPT [Platinum Ounce]
YER [Yemeni Rial]
ZAR [South African Rand]
ZMW [Zambian Kwacha]
ZWL [Zimbabwean Dollar]
```''',
        color=discord.Color.blurple())
        conv5_embed.set_footer(text='Page 5')
        conv5_embed.add_field(name='Example: ',value='''
n!cur_conv 1 usd vnd
n!cur_conv 7 cny eur''')
        await ctx.send(embed=conv5_embed)


    @commands.command()
    async def help_summary(self, ctx):
        summary_embed = discord.Embed(
            title='Instruction',
            description='These are all available commands you can use',
            color=discord.Color.orange()
        )
        summary_embed.set_author(name='This is where you can get the summary information of many things (based on Wikipedia.org) !')
        summary_embed.add_field(name='To get summary information: `n!summary [information_to_search]`', value='Example: n!summary Earth', inline=False)
        summary_embed.add_field(name='To get summary information in your language: `n!lang_summary [language] [information_to_search]`', value='Example: n!lang_summary vi Việt Nam', inline=False)
        summary_embed.add_field(name='Language code:',value='n!help_lang_code to get list of available codes you can use for each language ')
        #summary_embed.add_field(name='NOTE : ', value='**Rememmber to put " - " instead of "space" between words which you want to search**\nExample: n!summary Donald-Trump\n***I HIGHLY RECOMMEND TO USE `n!summary` TO MINIMIZE TH ERRORS. Sorry for this inconvenience....***', inline=False)

        await ctx.send(embed=summary_embed)

    @commands.command()
    async def help_lang_code(self,ctx):
        lang_code_embed=discord.Embed(
            tiitle='Instruction',
            description='''
```css
HERE ARE CODES OF EACH LANGUAGE YOU CAN USE 
( ISO 639-1 CODES )
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
zh: Chinese
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
        await ctx.send(embed=lang_code_embed)

        lang_code1_embed = discord.Embed(
            tiitle='Instruction',
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
        await ctx.send(embed=lang_code1_embed)


        lang_code2_embed = discord.Embed(
            tiitle='Instruction',
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
        await ctx.send(embed=lang_code2_embed)



    @commands.command()
    async def help_calc_shape(self,ctx):
        calc_per_embed = discord.Embed(
            title='Instruction',
            description='These are all available commands you can use',
            color=discord.Color.green()
        )
        calc_per_embed.set_author(name='''
    List of shapes you can use to calculate :''')
        calc_per_embed.add_field(name='  P E R I M E T E R  ', value='''
+ __Perimeter__: (basic shapes): square, circle, triangle, rectangle,..........\n Other shapes's perimeter are basically the length of a line surrounding a two-dimensional shape. So for others, you can calculate yourself without help of BOT ;)
 
 - Square: `n!calc_per square s=[...]` : `s` is a side of square
 - Circle: `n!calc_per circle r=[...]` : `r` is radius of circle ( = 1/2 diameter)
 - Triangle: `n!calc_per triangle a=[...] b=[...] c=[...]` : `a, b, c` are 3 sides of triangle
 - Rectangle: `n!calc_per rectangle a=[...] b=[...]` : `a` is a side, `b` is other side
 ''', inline=False)
        calc_per_embed.add_field(name='  A R E A  ', value='''
 + __Area__: (basic shapes): square, triangle, circle, sector, circular sector, rectangle, trapezoid, parallelogram, hexagon, pentagon, sphere, cone, kite, ellipse, octagon, annulus, conical_frustum..........\n You can still area of other irregular shapes by dividing them into basic shapes and calculate normally ;)
 
 - Square: `n!calc_ar square s=[...]` : `s` is a side of square
 - Circle: `n!calc_ar circle r=[...]` : `r` is radius of circle
 - (Circular) Sector: `n!calc_ar sector r=[...] n=[...]` : `r` is radius, `n` is in degrees
 - Triangle: `n!calc_ar triangle b=[...] h=[...]` : `b` is base, `h` is height
 - Triangle(Heron): `n!calc_ar triangle(Heron) a=[...] b=[...] c=[...]` : `a, b, c` is 3 sides of triangles
 - Rectangle: `n!calc_ar rectangle a=[...] b=[...]` : `a` is a side, `b` is another side
 - Trapezoid: `n!calc_ar trapezoid b1=[...] b2=[...] h=[...]` : `b1` is base, `b2` is another base, `h` is height
 - Parallelogram: `n!calc_ar parallelogram b=[...] h=[...]` : `b` is base, `h` is height
 ''')
        await ctx.send(embed=calc_per_embed)

        calc2_per_embed = discord.Embed(
            description='''
 - Hexagon: `n!calc_ar hexagon s=[...]` : `s` is a side of hexagon
 - Pentagon: `n!calc_ar pentagon s=[...]` : `s` is a side of pentagon
 - Octagon: `n!calc_ar octagon s=[...]` : `s` is a side of octagon
 - Sphere (Surface area): `n!calc_ar sphere r=[...]` : `r` is radius of sphere
 - Ellipse: `n!calc_ar ellipse a=[...] b=[...]` : `a` is half of the major axis, `b` is half of another major axis 
 - Kite/Rhombus: `n!calc_ar kite/rhombus d1=[...] d2=[...]` : `d1` is diagonal of kite/rhombus, `d2` is another diagonal
 - Cone (Surface area): `n!calc_ar cone r=[...] l=[...]` : `r` is radius of circular base, `l` is slant height
 - Annulus: `n!calc_ar annulus R=[...] r=[...]` : `R` is outer radius, `r` s inner radius
 - Conical frustum: `n!calc_ar conical_frustum r1=[...] r2=[...] h=[...]` : `r1, r2` are radius of 2 bases, `h` is height''',
            color=discord.Color.green()
        )

        await ctx.send(embed=calc2_per_embed)

        calc3_per_embed = discord.Embed(
            color=discord.Color.green()
        )
        calc3_per_embed.add_field(name='  V O L U M E  ', value='''
 + __Volume__: (basic shape): box, cube, cylinder, circular prism, cone, sphere, conical frsutum,.........
 
 - Box: `n!calc_vol box a=[...] b=[...] h=[...]` : `a` is a side, `b` another width, `h` is height
 - Cube: `n!calc_vol cube s=[...]` : `s` is a side
 - Cylinder: `n!calc_vol cylinder r=[...] h=[...]` : `r` is radius of circular base, `h` is height
 - Cone: `n!calc_vol cone r=[...] h=[...]` : `r` is radius of circular base, `h` is height
 - Sphere: `n!calc_vol sphere r=[...]` : `r` is radius of sphere
 - Conical frustum: `n!calc_vol conical_frustum r1=[...] r2=[...] h=[...]` : `r1, r2` are radius of 2 bases, `h` is height
 .......
 ..etc...
 **In order to calculate the volume of every 3D shapes, use : `V = A.h` : `A` is the area of base, `h` is the height. GOOD LUCK**''')
        await ctx.send(embed=calc3_per_embed)



        


def setup(client):
    client.remove_command('help')
    client.add_cog(Help(client))
