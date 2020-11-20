import random
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import traceback
import asyncio
import time
import datetime


class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def memory_game(self, ctx, *, level):
        try:

                if level == 'level 1':
                    guess_matrix = ['-']
                    guess1 = guess_matrix[0] = random.choice(range(10, 10000))
                    final_grid = f'**`{guess1}`**'

                    game_embed_lvl1 = discord.Embed(
                        title='Memory game **level 1** (1x1)',
                        description='You have **3 seconds** to memorize this grid',
                        color=discord.Color.orange()
                    )

                    game_embed_lvl1.set_footer(text='Memory game | WebFinder v1.0',
                                      icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                    game_embed_lvl1.add_field(name=final_grid, value='-')
                    game_embed_lvl1.add_field(name='Press `quit` to quit the game !', value='*-*', inline=False)

                    begin = await ctx.send(embed=game_embed_lvl1)

                    def check_quit(user):
                        def inner_check(message):
                            return user.author == ctx.author and message.content == "quit"

                        return inner_check

                    try:
                        await self.client.wait_for('message', check=check_quit, timeout=3)
                        # if quited.content == 'quit' or quited.content == 'Quit':
                        quit_embed = discord.Embed(
                            title='QUITED THE GAME !',
                            color=discord.Color.gold(),
                            timestamp=datetime.datetime.utcnow()
                        )
                        quit_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        quit_embed.set_footer(text='Memory game | WebFinder v1.0',
                                              icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                        await ctx.send(embed=quit_embed)
                    except asyncio.exceptions.TimeoutError:

                        #await asyncio.sleep(1.5)


                        game_embed2_lvl1 = discord.Embed(
                            title='Memory game **level 1** (1x1)',
                            description='Now input the previous grid. You have **5 seconds**',
                            color=discord.Color.orange()
                        )

                        await begin.delete()
                        await ctx.send(embed=game_embed2_lvl1)
                        def check(user):
                            return user.author == ctx.author

                        try:
                            start_time = time.time()
                            print(start_time)
                            m = await self.client.wait_for('message', check=check, timeout=5)



                            input_result = m.content
                            correct_result = f'{guess1}'

                            if input_result == correct_result:
                                print(time.time())
                                time_count = round((time.time()-start_time)*1000, 3)
                                correct_embed = discord.Embed(
                                    title='CORRECT !',
                                    description=f'**Congratulation!** You has finished in **{time_count}**ms',
                                    color=discord.Color.green()
                                )
                                correct_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/3004/3004584.png')
                                correct_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                           icon_url='https://image.flaticon.com/icons/png/128/2907/2907004.png')
                                await ctx.send(embed=correct_embed)
                            else:
                                incorrect_embed = discord.Embed(
                                    title='INCORRECT !',
                                    description=f'The correct result is : `{correct_result}`\n*Try harder next time!*',
                                    color=discord.Color.red()
                                )
                                incorrect_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                           icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                incorrect_embed.add_field(name='Original grid :', value=final_grid)

                                incorrect_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2550/2550327.png')
                                await ctx.send(embed=incorrect_embed)

                        except asyncio.exceptions.TimeoutError:
                            time_out_embed = discord.Embed(
                                title='TIME OUT !',
                                description='Perhaps you are quite slow.... Try faster next time !',
                                color=discord.Color.red()
                            )
                            time_out_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                       icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                            time_out_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/850/850960.png')
                            await ctx.send(embed=time_out_embed)


                elif level == 'level 2':
                    guess_matrix = ['-', '-',
                                    '-', '-']

                    guess1 = guess_matrix[0] = random.choice(range(1, 100))
                    guess2 = guess_matrix[1] = random.choice(range(1, 100))
                    guess3 = guess_matrix[2] = random.choice(range(1, 100))
                    guess4 = guess_matrix[3] = random.choice(range(1, 100))

                    final_grid = f'''
    
```cs
#          a            b
- - - - - - - - - - - - -
[1] ‎‎||    {guess1}    ||    {guess2}    ||
- - ||- - - - - ||- - - - - ||
[2] ||    {guess3}    ||    {guess4}    ||
- - - - - - - - - - - - -
```
'''
                    final_grid = final_grid.replace(' 1 ', ' 01 ').replace(' 2 ', ' 02 ').replace(' 3 ', ' 03 ').replace(
                        ' 4 ', ' 04 ').replace(' 5 ', ' 05 ').replace(' 6 ', ' 06 ').replace(' 7 ', ' 07 ').replace(' 8 ',
                                                                                                                    ' 08 ').replace(
                        ' 9 ', ' 09 ')

                    game_embed_lvl2 = discord.Embed(
                        title='Memory game **level 2** (2x2)',
                        description='You have **5 seconds** to memorize this grid',
                        color=discord.Color.orange()
                    )

                    game_embed_lvl2.set_footer(text='Memory game | WebFinder v1.0',
                                               icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                    game_embed_lvl2.add_field(name='-', value=final_grid)
                    game_embed_lvl2.add_field(name='Press `quit` to quit the game !', value='*-*', inline=False)

                    await ctx.send(
                        f'{ctx.author.mention} ! It is **much better** if you rotate your screen (*on phone*) to view full grid in the memory game')
                    begin = await ctx.send(embed=game_embed_lvl2)

                    def check_quit(user):
                        def inner_check(message):
                            return user.author == ctx.author and message.content == "quit"

                        return inner_check


                    try:
                        await self.client.wait_for('message', check=check_quit, timeout=5)
                        #if quited.content == 'quit' or quited.content == 'Quit':
                        quit_embed = discord.Embed(
                                title='QUITED THE GAME !',
                                color=discord.Color.gold(),
                                timestamp=datetime.datetime.utcnow()
                        )
                        quit_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        quit_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                     icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                        await ctx.send(embed=quit_embed)


                    except asyncio.exceptions.TimeoutError:


                        #await asyncio.sleep(2.5)

                        game_embed2_lvl3 = discord.Embed(
                            title='Memory game **level 2** (2x2)',
                            description='Now input the previous grid. You have **10 seconds**',
                            color=discord.Color.orange()
                        )

                        game_embed2_lvl3.add_field(name='-', value=f'''
```cs
#     a   b
[1]  ⬜  ⬜
        
[2]  ⬜  ⬜
```
''')
                        await begin.delete()
                        await ctx.send(embed=game_embed2_lvl3)

                        def check(user):
                            return user.author == ctx.author

                        try:
                            start_time = time.time()
                            print(start_time)
                            m = await self.client.wait_for('message', check=check, timeout=10)


                            print(f'{guess1} {guess2} {guess3} {guess4}')
                            input_result = (m.content).replace('01 ', '1 ').replace('02 ', '2 ').replace('03 ', '3 ').replace('04 ', '4 ').replace('05 ', '5 ').replace('06 ', '6 ').replace('07 ', '7 ').replace('08 ', '8 ').replace('09 ', '9 ').replace(' 01', ' 1').replace(' 02', ' 2').replace(' 03', ' 3').replace(' 04', ' 4').replace(' 05', ' 5').replace(' 06', ' 6').replace(' 07', ' 7').replace(' 08', ' 8').replace(' 09', ' 9')
                            correct_result = f'{guess1} {guess2} {guess3} {guess4}'.replace('01 ', '1 ').replace('02 ', '2 ').replace('03 ', '3 ').replace('04 ', '4 ').replace('05 ', '5 ').replace('06 ', '6 ').replace('07 ', '7 ').replace('08 ', '8 ').replace('09 ', '9 ').replace(' 01', ' 1').replace(' 02', ' 2').replace(' 03', ' 3').replace(' 04', ' 4').replace(' 05', ' 5').replace(' 06', ' 6').replace(' 07', ' 7').replace(' 08', ' 8').replace(' 09', ' 9')

                            print(time.time())
                            time_count = round((time.time() - start_time) * 1000, 3)
                            if input_result == correct_result:

                                correct_embed = discord.Embed(
                                    title='CORRECT !',
                                    description=f'You has finished in **{time_count}**ms',
                                    color=discord.Color.green()
                                )
                                correct_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                           icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                correct_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/3004/3004584.png')

                                await ctx.send(embed=correct_embed)
                            else:
                                incorrect_embed = discord.Embed(
                                    title='INCORRECT !',
                                    description=f'The correct result is : `{correct_result}`\n*Try harder next time!*',
                                    color=discord.Color.red()
                                )
                                incorrect_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                           icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                incorrect_embed.add_field(name='Original grid :', value=final_grid)

                                incorrect_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2550/2550327.png')
                                await ctx.send(embed=incorrect_embed)

                        except asyncio.exceptions.TimeoutError:
                            time_out_embed = discord.Embed(
                                title='TIME OUT !',
                                description='Perhaps you are quite slow.... Try faster next time !',
                                color=discord.Color.red()
                            )
                            time_out_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                       icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                            time_out_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/850/850960.png')
                            await ctx.send(embed=time_out_embed)

                elif level == 'level 3':
                    guess_matrix = [['-', '-', '-'],
                                    ['-', '-', '-'],
                                    ['-', '-', '-']]

                    guess1 = guess_matrix[0][0] = random.choice(range(1, 100))
                    guess2 = guess_matrix[0][1] = random.choice(range(1, 100))
                    guess3 = guess_matrix[0][2] = random.choice(range(1, 100))
                    guess4 = guess_matrix[1][0] = random.choice(range(1, 100))
                    guess5 = guess_matrix[1][1] = random.choice(range(1, 100))
                    guess6 = guess_matrix[1][2] = random.choice(range(1, 100))
                    guess7 = guess_matrix[2][0] = random.choice(range(1, 100))
                    guess8 = guess_matrix[2][1] = random.choice(range(1, 100))
                    guess9 = guess_matrix[2][2] = random.choice(range(1, 100))


                    final_grid = f'''
```cs
#          a            b             c
- - - - - - - - - - - - - - - - - - - - - - - -
[1] ‎‎||    {guess1}    ||      {guess2}      ||    {guess3}     ||
- - ||- - - - - ||- - - - - - - ||- - - - - -||
[2] ||    {guess4}    ||      {guess5}      ||    {guess6}     ||
- - ||- - - - - ||- - - - - - - ||- - - - - -||
[3] ||    {guess7}    ||      {guess8}      ||    {guess9}     ||
- - - - - - - - - - - - - - - - - - - - - - - -
```
'''
                    final_grid = final_grid.replace(' 1 ', ' 01 ').replace(' 2 ', ' 02 ').replace(' 3 ', ' 03 ').replace(' 4 ', ' 04 ').replace(' 5 ', ' 05 ').replace(' 6 ', ' 06 ').replace(' 7 ', ' 07 ').replace(' 8 ', ' 08 ').replace(' 9 ', ' 09 ')

                    game_embed_lvl3 = discord.Embed(
                        title='Memory game **level 3** (3x3)',
                        description='You have **10 seconds** to memorize this grid',
                        color=discord.Color.orange()
                    )
                    game_embed_lvl3.set_footer(text='Memory game | WebFinder v1.0',
                                              icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                    game_embed_lvl3.add_field(name='-', value=final_grid)
                    game_embed_lvl3.add_field(name='Press `quit` to quit the game!', value='*-*', inline=False)

                    await ctx.send(
                        f'{ctx.author.mention} ! It is **much better** if you rotate your screen (*on phone*) to view full grid in the memory game')
                    begin = await ctx.send(embed=game_embed_lvl3)

                    def check_quit(user):
                        def inner_check(message):
                            return user.author == ctx.author and message.content == "quit"

                        return inner_check


                    try:
                        await self.client.wait_for('message', check=check_quit, timeout=10)
                        #if quited.content == 'quit' or quited.content == 'Quit':
                        quit_embed = discord.Embed(
                                title='QUITED THE GAME !',
                                color=discord.Color.gold(),
                                timestamp=datetime.datetime.utcnow()
                        )
                        quit_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        quit_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                     icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                        await ctx.send(embed=quit_embed)

                    except asyncio.exceptions.TimeoutError:
                        #await asyncio.sleep(5)


                        game_embed2_lvl3 = discord.Embed(
                            title='Memory game **level 3** (3x3)',
                            description='Now input the previous grid. You have 20 seconds',
                            color=discord.Color.orange()
                        )


                        game_embed2_lvl3.add_field(name='-',value=f'''
```cs
#     a   b    c
[1]  ⬜  ⬜  ⬜
            
[2]  ⬜  ⬜  ⬜
            
[3]  ⬜  ⬜  ⬜
```
            ''')
                        await begin.delete()
                        await ctx.send(embed=game_embed2_lvl3)


                        def check(user):
                            return user.author == ctx.author

                        try:
                            start_time = time.time()
                            print(start_time)
                            m = await self.client.wait_for('message', check=check, timeout=20)


                            print(f'{guess1} {guess2} {guess3} {guess4} {guess5} {guess6} {guess7} {guess8} {guess9}')
                            input_result = (m.content).replace('01 ', '1 ').replace('02 ', '2 ').replace('03 ', '3 ').replace('04 ', '4 ').replace('05 ', '5 ').replace('06 ', '6 ').replace('07 ', '7 ').replace('08 ', '8 ').replace('09 ', '9 ').replace(' 01', ' 1').replace(' 02', ' 2').replace(' 03', ' 3').replace(' 04', ' 4').replace(' 05', ' 5').replace(' 06', ' 6').replace(' 07', ' 7').replace(' 08', ' 8').replace(' 09', ' 9')
                            correct_result = f'{guess1} {guess2} {guess3} {guess4} {guess5} {guess6} {guess7} {guess8} {guess9}'.replace('01 ', '1 ').replace('02 ', '2 ').replace('03 ', '3 ').replace('04 ', '4 ').replace('05 ', '5 ').replace('06 ', '6 ').replace('07 ', '7 ').replace('08 ', '8 ').replace('09 ', '9 ').replace(' 01', ' 1').replace(' 02', ' 2').replace(' 03', ' 3').replace(' 04', ' 4').replace(' 05', ' 5').replace(' 06', ' 6').replace(' 07', ' 7').replace(' 08', ' 8').replace(' 09', ' 9')

                            print(time.time())
                            time_count = round((time.time() - start_time) * 1000, 3)
                            if input_result == correct_result:

                                correct_embed = discord.Embed(
                                    title='CORRECT !',
                                    description=f'You has finished in **{time_count}**ms',
                                    color=discord.Color.green()
                                )
                                correct_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                          icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                correct_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/3004/3004584.png')

                                await ctx.send(embed=correct_embed)
                            else:
                                incorrect_embed = discord.Embed(
                                    title='INCORRECT !',
                                    description=f'The correct result is : `{correct_result}`\n*Try harder next time!*',
                                    color=discord.Color.red()
                                )
                                incorrect_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                          icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                incorrect_embed.add_field(name='Original grid :', value=final_grid)

                                incorrect_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2550/2550327.png')
                                await ctx.send(embed=incorrect_embed)

                        except asyncio.exceptions.TimeoutError:
                            time_out_embed = discord.Embed(
                                title='TIME OUT !',
                                description='Perhaps you are quite slow.... Try faster next time !',
                                color=discord.Color.red()
                            )
                            time_out_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                      icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                            time_out_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/850/850960.png')
                            await ctx.send(embed=time_out_embed)

                elif level == 'level 4':

                    guess_matrix = [['-', '-', '-', '-'],
                                    ['-', '-', '-', '-'],
                                    ['-', '-', '-', '-'],
                                    ['-', '-', '-', '-']]

                    guess1 = guess_matrix[0][0] = random.choice(range(1, 100))
                    guess2 = guess_matrix[0][1] = random.choice(range(1, 100))
                    guess3 = guess_matrix[0][2] = random.choice(range(1, 100))
                    guess4 = guess_matrix[0][3] = random.choice(range(1, 100))
                    guess5 = guess_matrix[1][0] = random.choice(range(1, 100))
                    guess6 = guess_matrix[1][1] = random.choice(range(1, 100))
                    guess7 = guess_matrix[1][2] = random.choice(range(1, 100))
                    guess8 = guess_matrix[1][3] = random.choice(range(1, 100))
                    guess9 = guess_matrix[2][0] = random.choice(range(1, 100))
                    guess10 = guess_matrix[2][1] = random.choice(range(1, 100))
                    guess11 = guess_matrix[2][2] = random.choice(range(1, 100))
                    guess12 = guess_matrix[2][3] = random.choice(range(1, 100))
                    guess13 = guess_matrix[3][0] = random.choice(range(1, 100))
                    guess14 = guess_matrix[3][1] = random.choice(range(1, 100))
                    guess15 = guess_matrix[3][2] = random.choice(range(1, 100))
                    guess16 = guess_matrix[3][3] = random.choice(range(1, 100))


                    final_grid = f'''
```cs
#          a            b             c            d
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
[1] ‎‎||    {guess1}    ||      {guess2}      ||    {guess3}     ||    {guess4}     ||
- - ||- - - - - ||- - - - - - - ||- - - - - -||- - - - - -||
[2] ||    {guess5}    ||      {guess6}      ||    {guess7}     ||    {guess8}     ||
- - ||- - - - - ||- - - - - - - ||- - - - - -||- - - - - -||
[3] ||    {guess9}    ||      {guess10}      ||    {guess11}     ||    {guess12}     ||
- - ||- - - - - ||- - - - - - - ||- - - - - -||- - - - - -||
[4] ||    {guess13}    ||      {guess14}      ||    {guess15}     ||    {guess16}     ||
- - - - - - - - - - - - - - - - - - - - - - - -
```
'''
                    final_grid = final_grid.replace(' 1 ', ' 01 ').replace(' 2 ', ' 02 ').replace(' 3 ', ' 03 ').replace(
                        ' 4 ', ' 04 ').replace(' 5 ', ' 05 ').replace(' 6 ', ' 06 ').replace(' 7 ', ' 07 ').replace(' 8 ',
                                                                                                                    ' 08 ').replace(
                        ' 9 ', ' 09 ')

                    game_embed_lvl4 = discord.Embed(
                        title='Memory game **level 4** (4x4)',
                        description='You have **20 seconds** to memorize this grid',
                        color=discord.Color.orange()
                    )

                    game_embed_lvl4.set_footer(text='Memory game | WebFinder v1.0',
                                             icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')

                    game_embed_lvl4.add_field(name='-', value=final_grid)
                    game_embed_lvl4.add_field(name='Press `quit` to quit the game !', value='*-*', inline=False)

                    await ctx.send(
                        f'{ctx.author.mention} ! It is **much better** if you rotate your screen (*on phone*) to view full grid in the memory game')
                    begin = await ctx.send(embed=game_embed_lvl4)

                    def check_quit(user):
                        def inner_check(message):
                            return user.author == ctx.author and message.content == "quit"

                        return inner_check


                    try:
                        await self.client.wait_for('message', check=check_quit, timeout=20)
                        #if quited.content == 'quit' or quited.content == 'Quit':
                        quit_embed = discord.Embed(
                                title='QUITED THE GAME !',
                                color=discord.Color.gold(),
                                timestamp=datetime.datetime.utcnow()
                        )
                        quit_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        quit_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                     icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                        await ctx.send(embed=quit_embed)
                    except asyncio.exceptions.TimeoutError:


                        #await asyncio.sleep(10)

                        game_embed2_lvl3 = discord.Embed(
                            title='Memory game **level 4** (4x4)',
                            description='Now input the previous grid. You have **25 seconds**',
                            color=discord.Color.orange()
                        )

                        game_embed2_lvl3.add_field(name='-', value=f'''
```cs
#     a   b    c    d
[1]  ⬜  ⬜  ⬜  ⬜
        
[2]  ⬜  ⬜  ⬜  ⬜
        
[3]  ⬜  ⬜  ⬜  ⬜
        
[4]  ⬜  ⬜  ⬜  ⬜
```
                            ''')
                        await begin.delete()
                        await ctx.send(embed=game_embed2_lvl3)

                        def check(user):
                            return user.author == ctx.author

                        try:
                            start_time = time.time()
                            print(start_time)
                            m = await self.client.wait_for('message', check=check, timeout=25)

                            print(f'{guess1} {guess2} {guess3} {guess4} {guess5} {guess6} {guess7} {guess8} {guess9} {guess10} {guess11} {guess12} {guess13} {guess14} {guess15} {guess16}')
                            input_result = (m.content).replace('01 ', '1 ').replace('02 ', '2 ').replace('03 ', '3 ').replace(
                                '04 ', '4 ').replace('05 ', '5 ').replace('06 ', '6 ').replace('07 ', '7 ').replace('08 ',
                                                                                                                    '8 ').replace(
                                '09 ', '9 ').replace(' 01', ' 1').replace(' 02', ' 2').replace(' 03', ' 3').replace(' 04',
                                                                                                                    ' 4').replace(
                                ' 05', ' 5').replace(' 06', ' 6').replace(' 07', ' 7').replace(' 08', ' 8').replace(' 09', ' 9')

                            correct_result = f'{guess1} {guess2} {guess3} {guess4} {guess5} {guess6} {guess7} {guess8} {guess9} {guess10} {guess11} {guess12} {guess13} {guess14} {guess15} {guess16}'.replace(
                                '01 ', '1 ').replace('02 ', '2 ').replace('03 ', '3 ').replace('04 ', '4 ').replace('05 ',
                                                                                                                    '5 ').replace(
                                '06 ', '6 ').replace('07 ', '7 ').replace('08 ', '8 ').replace('09 ', '9 ').replace(' 01',
                                                                                                                    ' 1').replace(
                                ' 02', ' 2').replace(' 03', ' 3').replace(' 04', ' 4').replace(' 05', ' 5').replace(' 06',
                                                                                                                    ' 6').replace(
                                ' 07', ' 7').replace(' 08', ' 8').replace(' 09', ' 9')

                            print(time.time())
                            time_count = round((time.time() - start_time) * 1000, 3)
                            if input_result == correct_result:

                                correct_embed = discord.Embed(
                                    title='CORRECT !',
                                    description=f'You has finished in **{time_count}**ms',
                                    color=discord.Color.green()
                                )
                                correct_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                          icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                correct_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/3004/3004584.png')

                                await ctx.send(embed=correct_embed)
                            else:
                                incorrect_embed = discord.Embed(
                                    title='INCORRECT !',
                                    description=f'The correct result is : `{correct_result}`\n*Try harder next time!*',
                                    color=discord.Color.red()
                                )
                                incorrect_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                          icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                incorrect_embed.add_field(name='Original grid :', value=final_grid)

                                incorrect_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2550/2550327.png')
                                await ctx.send(embed=incorrect_embed)

                        except asyncio.exceptions.TimeoutError:
                            time_out_embed = discord.Embed(
                                title='TIME OUT !',
                                description='Perhaps you are quite slow.... Try faster next time !',
                                color=discord.Color.red()
                            )
                            time_out_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                      icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                            time_out_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/850/850960.png')
                            await ctx.send(embed=time_out_embed)


                elif level == 'level 5':

                            guess_matrix = [['-', '-', '-', '-', '-'],
                                            ['-', '-', '-', '-', '-'],
                                            ['-', '-', '-', '-', '-'],
                                            ['-', '-', '-', '-', '-'],
                                            ['-', '-', '-', '-', '-']]

                            guess1 = guess_matrix[0][0] = random.choice(range(1, 100))
                            guess2 = guess_matrix[0][1] = random.choice(range(1, 100))
                            guess3 = guess_matrix[0][2] = random.choice(range(1, 100))
                            guess4 = guess_matrix[0][3] = random.choice(range(1, 100))
                            guess5 = guess_matrix[0][4] = random.choice(range(1, 100))

                            guess6 = guess_matrix[1][0] = random.choice(range(1, 100))
                            guess7 = guess_matrix[1][1] = random.choice(range(1, 100))
                            guess8 = guess_matrix[1][2] = random.choice(range(1, 100))
                            guess9 = guess_matrix[1][3] = random.choice(range(1, 100))
                            guess10 = guess_matrix[1][4] = random.choice(range(1, 100))

                            guess11 = guess_matrix[2][0] = random.choice(range(1, 100))
                            guess12 = guess_matrix[2][1] = random.choice(range(1, 100))
                            guess13 = guess_matrix[2][2] = random.choice(range(1, 100))
                            guess14 = guess_matrix[2][3] = random.choice(range(1, 100))
                            guess15 = guess_matrix[2][4] = random.choice(range(1, 100))

                            guess16 = guess_matrix[3][0] = random.choice(range(1, 100))
                            guess17 = guess_matrix[3][1] = random.choice(range(1, 100))
                            guess18 = guess_matrix[3][2] = random.choice(range(1, 100))
                            guess19 = guess_matrix[3][3] = random.choice(range(1, 100))
                            guess20 = guess_matrix[3][4] = random.choice(range(1, 100))

                            guess21 = guess_matrix[4][0] = random.choice(range(1, 100))
                            guess22 = guess_matrix[4][1] = random.choice(range(1, 100))
                            guess23 = guess_matrix[4][2] = random.choice(range(1, 100))
                            guess24 = guess_matrix[4][3] = random.choice(range(1, 100))
                            guess25 = guess_matrix[4][4] = random.choice(range(1, 100))

                            final_grid = f'''
```cs
 #      a        b         c        d        e
- - - - - - - - - - - - - - - - - - - - - - - -
[1] ‎‎||  {guess1}  ||   {guess2}   ||   {guess3}  ||   {guess4}  ||   {guess5}  ||
- - ||- - - ||- - - - ||- - - -||- - - -||- - - -||
[2] ‎‎||  {guess6}  ||   {guess7}   ||   {guess8}  ||   {guess9}  ||   {guess10}  ||
- - ||- - - ||- - - - ||- - - -||- - - -||- - - -||
[3] ‎‎||  {guess11}  ||   {guess12}   ||   {guess13}  ||   {guess14}  ||   {guess15}  ||
- - ||- - - ||- - - - ||- - - -||- - - -||- - - -||
[4] ‎‎||  {guess16}  ||   {guess17}   ||   {guess18}  ||   {guess19}  ||   {guess20}  ||
- - ||- - - ||- - - - ||- - - -||- - - -||- - - -||
[5] ‎‎||  {guess21}  ||   {guess22}   ||   {guess23}  ||   {guess24}  ||   {guess25}  ||
- - - - - - - - - - - - - - - - - - - - - - - - -
```
'''
                            final_grid = final_grid.replace(' 1 ', ' 01 ').replace(' 2 ', ' 02 ').replace(' 3 ',
                                                                                                          ' 03 ').replace(
                                ' 4 ', ' 04 ').replace(' 5 ', ' 05 ').replace(' 6 ', ' 06 ').replace(' 7 ', ' 07 ').replace(
                                ' 8 ',
                                ' 08 ').replace(
                                ' 9 ', ' 09 ')

                            game_embed_lvl5 = discord.Embed(
                                title='Memory game **level 5** (5x5)',
                                description='You have **30 seconds** to memorize this grid',
                                color=discord.Color.orange()
                            )
                            game_embed_lvl5.set_footer(text='Memory game | WebFinder v1.0',
                                                     icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')

                            game_embed_lvl5.add_field(name='-', value=final_grid)
                            game_embed_lvl5.add_field(name='Press `quit` to quit the game !', value='*-*', inline=False)

                            await ctx.send(
                                f'{ctx.author.mention} ! It is **much better** if you rotate your screen (*on phone*) to view full grid in the memory game')
                            begin = await ctx.send(embed=game_embed_lvl5)

                            def check_quit(user):
                                def inner_check(message):
                                    return user.author == ctx.author and message.content == "quit"

                                return inner_check

                            try:
                                await self.client.wait_for('message', check=check_quit, timeout=30)
                                # if quited.content == 'quit' or quited.content == 'Quit':
                                quit_embed = discord.Embed(
                                    title='QUITED THE GAME !',
                                    color=discord.Color.gold(),
                                    timestamp=datetime.datetime.utcnow()
                                )
                                quit_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                quit_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                      icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                await ctx.send(embed=quit_embed)
                            except asyncio.exceptions.TimeoutError:

                                #await asyncio.sleep(15)

                                game_embed2_lvl5 = discord.Embed(
                                    title='Memory game **level 5** (5x5)',
                                    description='Now input the previous grid. You have **40 seconds**',
                                    color=discord.Color.orange()
                                )

                                game_embed2_lvl5.add_field(name='-', value=f'''
```cs
#     a   b    c   d   e
[1]  ⬜  ⬜  ⬜  ⬜  ⬜
        
[2]  ⬜  ⬜  ⬜  ⬜  ⬜
        
[3]  ⬜  ⬜  ⬜  ⬜  ⬜
        
[4]  ⬜  ⬜  ⬜  ⬜  ⬜
        
[5]  ⬜  ⬜  ⬜  ⬜  ⬜
```
''')
                                await begin.delete()
                                await ctx.send(embed=game_embed2_lvl5)

                                def check(user):
                                    return user.author == ctx.author

                                try:
                                    start_time = time.time()
                                    print(start_time)
                                    m = await self.client.wait_for('message', check=check, timeout=40)

                                    print(
                                        f'{guess1} {guess2} {guess3} {guess4} {guess5} {guess6} {guess7} {guess8} {guess9} {guess10} {guess11} {guess12} {guess13} {guess14} {guess15} {guess16} {guess17} {guess18} {guess19} {guess20} {guess21} {guess22} {guess23} {guess24} {guess25}')
                                    input_result = (m.content).replace('01 ', '1 ').replace('02 ', '2 ').replace('03 ',
                                                                                                                 '3 ').replace(
                                        '04 ', '4 ').replace('05 ', '5 ').replace('06 ', '6 ').replace('07 ', '7 ').replace(
                                        '08 ',
                                        '8 ').replace(
                                        '09 ', '9 ').replace(' 01', ' 1').replace(' 02', ' 2').replace(' 03', ' 3').replace(
                                        ' 04',
                                        ' 4').replace(
                                        ' 05', ' 5').replace(' 06', ' 6').replace(' 07', ' 7').replace(' 08', ' 8').replace(
                                        ' 09', ' 9')

                                    correct_result = f'{guess1} {guess2} {guess3} {guess4} {guess5} {guess6} {guess7} {guess8} {guess9} {guess10} {guess11} {guess12} {guess13} {guess14} {guess15} {guess16}  {guess17} {guess18} {guess19} {guess20} {guess21} {guess22} {guess23} {guess24} {guess25}'.replace(
                                        '01 ', '1 ').replace('02 ', '2 ').replace('03 ', '3 ').replace('04 ', '4 ').replace(
                                        '05 ',
                                        '5 ').replace(
                                        '06 ', '6 ').replace('07 ', '7 ').replace('08 ', '8 ').replace('09 ', '9 ').replace(
                                        ' 01',
                                        ' 1').replace(
                                        ' 02', ' 2').replace(' 03', ' 3').replace(' 04', ' 4').replace(' 05', ' 5').replace(
                                        ' 06',
                                        ' 6').replace(
                                        ' 07', ' 7').replace(' 08', ' 8').replace(' 09', ' 9')

                                    print(time.time())
                                    time_count = round((time.time() - start_time) * 1000, 3)
                                    if input_result == correct_result:

                                        correct_embed = discord.Embed(
                                            title='CORRECT !',
                                            description=f'You has finished in **{time_count}**ms',
                                            color=discord.Color.green()
                                        )
                                        correct_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                                 icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                        correct_embed.set_thumbnail(
                                            url='https://image.flaticon.com/icons/png/128/3004/3004584.png')

                                        await ctx.send(embed=correct_embed)
                                    else:
                                        incorrect_embed = discord.Embed(
                                            title='INCORRECT !',
                                            description=f'The correct result is : `{correct_result}`\n*Try harder next time!*',
                                            color=discord.Color.red()
                                        )
                                        incorrect_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                                   icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                        incorrect_embed.add_field(name='Original grid :', value=final_grid)

                                        incorrect_embed.set_thumbnail(
                                            url='https://image.flaticon.com/icons/png/128/2550/2550327.png')
                                        await ctx.send(embed=incorrect_embed)

                                except asyncio.exceptions.TimeoutError:
                                    time_out_embed = discord.Embed(
                                        title='TIME OUT !',
                                        description='Perhaps you are quite slow.... Try faster next time !',
                                        color=discord.Color.red()
                                    )
                                    time_out_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                              icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                                    time_out_embed.set_thumbnail(
                                        url='https://image.flaticon.com/icons/png/128/850/850960.png')
                                    await ctx.send(embed=time_out_embed)



                else:

                    else_embed = discord.Embed(
                        title='Level not found !',
                        description='''
**Please make sure that you follow the correct level :**
- Level 1 ( *__easy__* ) : `memory_game level 1`
- Level 2 ( *__medium__* ) : `memory_game level 2`
- Level 3 ( *__hard__* ) : `memory_game level 3`
- Level 4 ( *__harder__* ) : `memory_game level 4`
- Level 5 ( ***__insane__*** ) : `memory_game level 5`
- Level 6 ( *__Unknown__* ) : `Coming soon`
''',
                        color=discord.Color.dark_red()
                    )

                    else_embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar_url)
                    else_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2748/2748614.png')
                    else_embed.set_footer(text='Memory game | WebFinder v1.0',
                                                          icon_url='https://image.flaticon.com/icons/png/128/1993/1993328.png')
                    await ctx.send(embed=else_embed)



        except BaseException as e:
            await ctx.send(traceback.print_exc())



    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user)
    async def tictactoe(self, ctx, member: discord.Member):

        if member.id == ctx.author.id:
            duplicate_player = discord.Embed(
                description='**You cannot play against yourself! Try to find someone to play with**',
                color=discord.Color.red()
            )

            await ctx.send(embed=duplicate_player)
        elif member.id != ctx.author.id:
            try:
                confirm_list = ["✅", '❌']
                check = "✅"
                cancel = '❌'
                await ctx.send(member.mention)
                choose_embed = discord.Embed(
                    title=f'{member.display_name}, Would you like to play __tic tac toe__ with {ctx.author.name} ?',
                    description=f'*- You have 30 seconds to decide*',
                    color=discord.Color.teal()
                )
                choose_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2076/2076261.png')
                choose_embed.set_footer(text='Tic tac toe | Webfinder v1.0')
                choose = await ctx.send(embed=choose_embed)
                await choose.add_reaction(check)
                await choose.add_reaction(cancel)

                def check(reaction, user):
                    return user == member and str(reaction.emoji) in confirm_list
                try:

                    reaction = await self.client.wait_for('reaction_add', check=check, timeout=30)


                    if reaction[0].emoji == cancel:
                        cancel_embed = discord.Embed(
                            description=f'**{member} has declined your request.....What a pity !**',
                            color=discord.Color.red()
                        )
                        cancel_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2550/2550327.png')
                        cancel_embed.set_footer(text='Tic tac toe | Webfinder v1.0',
                                                icon_url='https://image.flaticon.com/icons/png/128/1021/1021264.png')

                        await ctx.send(embed=cancel_embed)
                    else:
                        grid = ['⬛', '⬛', '⬛',
                                '⬛', '⬛', '⬛',
                                '⬛', '⬛', '⬛']

                        start_embed_x = discord.Embed(
                            title=f'{ctx.author} vs {member}',
                            color=discord.Color.blurple(),

                        )

                        start_embed_x.set_author(name=f'TIC TAC TOE',
                                                  icon_url='https://image.flaticon.com/icons/png/128/2076/2076261.png')
                        start_embed_x.add_field(name=f'*-*',
                                                 value=f'{" ".join(grid[:3])}\n{" ".join(grid[3:6])}\n{" ".join(grid[6:9])}\n')

                        await ctx.send(embed=start_embed_x)


                        def check_player_x(user1):
                            return user1.author == ctx.author

                        def check_player_o(user2):
                            return user2.author == member




                        while '⬛' in grid:
                            print('in')


                            async def return_player_x():
                                await ctx.send(f'{ctx.author.mention} Now it is **your turn !**\n( *`a` `b` `c` for **row** and `1` `2` `3` for **column**. __Example :__ a1 , b2, c3,.....* )')

                                player_x_turn = await self.client.wait_for('message', check=check_player_x, timeout=20)

                                if player_x_turn.content == 'a1' or player_x_turn.content == 'A1':
                                    if grid[0] == '⬛':
                                        grid[0] = '❌'
                                    elif grid[0] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()
                                elif player_x_turn.content == 'a2' or player_x_turn.content == 'A2':
                                    if grid[3] == '⬛':
                                        grid[3] = '❌'
                                    elif grid[3] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()

                                elif player_x_turn.content == 'a3' or player_x_turn.content == 'A3':
                                    if grid[6] == '⬛':
                                        grid[6] = '❌'
                                    elif grid[6] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()
                                elif player_x_turn.content == 'b1' or player_x_turn.content == 'B1':
                                    if grid[1] == '⬛':
                                        grid[1] = '❌'
                                    elif grid[1] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()
                                elif player_x_turn.content == 'b2' or player_x_turn.content == 'B2':
                                    if grid[4] == '⬛':
                                        grid[4] = '❌'
                                    elif grid[4] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()
                                elif player_x_turn.content == 'b3' or player_x_turn.content == 'B3':
                                    if grid[7] == '⬛':
                                        grid[7] = '❌'
                                    elif grid[7] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()
                                elif player_x_turn.content == 'c1' or player_x_turn.content == 'C1':
                                    if grid[2] == '⬛':
                                        grid[2] = '❌'
                                    elif grid[2] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()
                                elif player_x_turn.content == 'c2' or player_x_turn.content == 'C2':
                                    if grid[5] == '⬛':
                                        grid[5] = '❌'
                                    elif grid[5] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()
                                elif player_x_turn.content == 'c3' or player_x_turn.content == 'C3':
                                    if grid[8] == '⬛':
                                        grid[8] = '❌'
                                    elif grid[8] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_x()



                                else:
                                    await ctx.send('**`This position is not available in tic tac toe 3x3 grid`**')
                                    await return_player_x()
                                battle_embed_x = discord.Embed(
                                        title=f'{ctx.author} vs {member}',
                                        color=discord.Color.blurple(),

                                )

                                battle_embed_x.set_author(name=f'TIC TAC TOE', icon_url='https://image.flaticon.com/icons/png/128/2076/2076261.png')
                                battle_embed_x.add_field(name=f'*-*', value=f'{" ".join(grid[:3])}\n{" ".join(grid[3:6])}\n{" ".join(grid[6:9])}\n')
                                #battle_embed_x.add_field(name=' ‍ ', value='**Press `quit` to quit the game**', inline=False)


                                await ctx.send(embed=battle_embed_x)





                            try:
                                await return_player_x()

                            except asyncio.exceptions.TimeoutError:
                                time_out_x = discord.Embed(
                                    title='TIME OUT !',
                                    description=f'**{ctx.author} did not response in time... *Loser !!!***',
                                    color=discord.Color.from_rgb(255, 70, 70)
                                )

                                await ctx.send(embed=time_out_x)
                                break


                            if grid[0] == grid[1] == grid[2] == '❌' or grid[3] == grid[4] == grid[5] == '❌' or grid[6] == grid[
                                    7] == grid[8] == '❌' or grid[0] == grid[3] == grid[6] == '❌' or grid[1] == grid[4] == grid[7] == '❌' or \
                                        grid[2] == grid[5] == grid[8] == '❌' or grid[0] == grid[4] == grid[8] == '❌' or grid[2] == \
                                        grid[4] == grid[6] == '❌':
                                winner_embed = discord.Embed(
                                    title=f'CONGRATULATIONS ! {ctx.author}',
                                    description=f'{ctx.author.mention} You beated **{member}** !!!! GG boy',
                                    color=discord.Color.from_rgb(128, 255, 230),
                                    timestamp=datetime.datetime.utcnow()
                                )

                                winner_embed.set_footer(text='Tic tac toe | WebFinder v1.0',
                                                            icon_url='https://image.flaticon.com/icons/png/128/2076/2076261.png')
                                winner_embed.set_thumbnail(
                                    url='https://image.flaticon.com/icons/png/128/2829/2829661.png')

                                await ctx.send(embed=winner_embed)
                                break




                            if '⬛' not in grid:
                                draw_embed = discord.Embed(
                                    title='D R A W !',
                                    description=f'The game between **{ctx.author}** and **{member}** has come to the end without winner.....',
                                    color=discord.Color.from_rgb(247, 255, 128)

                                )

                                draw_embed.set_footer(text='Tic tac toe | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/2076/2076261.png')

                                await ctx.send(embed=draw_embed)
                                break



                            async def return_player_o():

                                await ctx.send(f'{member.mention} Now it is **your turn !**\n( *`a` `b` `c` for **row** and `1` `2` `3` for **column**. __Example :__ a1 , b2, c3,.....* )')

                                player_o_turn = await self.client.wait_for('message', check=check_player_o, timeout=20)


                                if player_o_turn.content == 'a1' or player_o_turn.content == 'A1':
                                    if grid[0] == '⬛':
                                        grid[0] = '⭕'
                                    elif grid[0] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                elif player_o_turn.content == 'a2' or player_o_turn.content == 'A2':
                                    if grid[3] == '⬛':
                                        grid[3] = '⭕'
                                    elif grid[3] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                elif player_o_turn.content == 'a3' or player_o_turn.content == 'A3':
                                    if grid[6] == '⬛':
                                        grid[6] = '⭕'
                                    elif grid[6] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                elif player_o_turn.content == 'b1' or player_o_turn.content == 'B1':
                                    if grid[1] == '⬛':
                                        grid[1] = '⭕'
                                    elif grid[1] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                elif player_o_turn.content == 'b2' or player_o_turn.content == 'B2':
                                    if grid[4] == '⬛':
                                        grid[4] = '⭕'
                                    elif grid[4] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                elif player_o_turn.content == 'b3' or player_o_turn.content == 'B3':
                                    if grid[7] == '⬛':
                                        grid[7] = '⭕'
                                    elif grid[7] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                elif player_o_turn.content == 'c1' or player_o_turn.content == 'C1':
                                    if grid[2] == '⬛':
                                        grid[2] = '⭕'
                                    elif grid[2] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                elif player_o_turn.content == 'c2' or player_o_turn.content == 'C2':
                                    if grid[5] == '⬛':
                                        grid[5] = '⭕'
                                    elif grid[5] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                elif player_o_turn.content == 'c3' or player_o_turn.content == 'C3':
                                    if grid[8] == '⬛':
                                        grid[8] = '⭕'
                                    elif grid[8] != '⬛':
                                        await ctx.send(f'**`This position has already filled`**')
                                        await return_player_o()
                                else:
                                    await ctx.send('**`This position is not available in tic tac toe 3x3 grid`**')
                                    await return_player_o()
                                battle_embed_o = discord.Embed(
                                    title=f'{ctx.author} vs {member}',
                                    color=discord.Color.blurple(),

                                )

                                battle_embed_o.set_author(name=f'TIC TAC TOE',
                                                          icon_url='https://image.flaticon.com/icons/png/128/2076/2076261.png')
                                battle_embed_o.add_field(name=f'*-*',
                                                         value=f'{" ".join(grid[:3])}\n{" ".join(grid[3:6])}\n{" ".join(grid[6:9])}\n')


                                await ctx.send(embed=battle_embed_o)


                            try:
                                await return_player_o()
                            except asyncio.exceptions.TimeoutError:
                                time_out_o = discord.Embed(
                                    title='TIME OUT !',
                                    description=f'**{member} did not response in time... *Loser !!!***',
                                    color=discord.Color.from_rgb(255, 70, 70)
                                )

                                await ctx.send(embed=time_out_o)
                                break

                            if grid[0] == grid[1] == grid[2] == '⭕' or grid[3] == grid[4] == grid[5] == '⭕' or grid[6] == grid[
                                    7] == grid[8] == '⭕' or grid[0] == grid[3] == grid[6] == '⭕' or grid[1] == grid[4] == grid[7] == '⭕' or \
                                        grid[2] == grid[5] == grid[8] == '⭕' or grid[0] == grid[4] == grid[8] == '⭕' or grid[2] == \
                                        grid[4] == grid[6] == '⭕':
                                winner_embed = discord.Embed(
                                        title=f'CONGRATULATIONS !  {member}',
                                        description=f'{member.mention} You beated **{ctx.author}** !!!! GG boy*',
                                        color=discord.Color.from_rgb(128, 255, 230),
                                        timestamp=datetime.datetime.utcnow()
                                )

                                winner_embed.set_footer(text='Tic tac toe | WebFinder v1.0',
                                                            icon_url='https://image.flaticon.com/icons/png/128/2076/2076261.png')
                                winner_embed.set_thumbnail(
                                    url='https://image.flaticon.com/icons/png/128/2829/2829661.png')
                                winner_embed.set_footer(text='Tic tac toe | WebFinder v1.0')
                                await ctx.send(embed=winner_embed)
                                break


                            if '⬛' not in grid:

                                draw_embed = discord.Embed(
                                    title='D R A W !',
                                    description=f'The game between **{ctx.author}** and **{member}** has come to the end without winner.....',
                                    color=discord.Color.from_rgb(247, 255, 128)

                                )

                                draw_embed.set_footer(text='Tic tac toe | WebFinder v1.0', icon_url='https://image.flaticon.com/icons/png/128/2076/2076261.png')
                                await ctx.send(embed=draw_embed)
                                break

                except asyncio.exceptions.TimeoutError:
                    pass


            except BaseException as e:
                await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user)
    async def hangman(self, ctx, member: discord.Member):
        author = self.client.get_user(ctx.author.id)
        if member.id == ctx.author.id:
            duplicate_player = discord.Embed(
                description='**You cannot play against yourself! Try to find someone to play with**',
                color=discord.Color.red()
            )

            await ctx.send(embed=duplicate_player)
        elif member.id != ctx.author.id:
                try:
                    confirm_list = ["✅", '❌']
                    check = "✅"
                    cancel = '❌'
                    await ctx.send(member.mention)
                    choose_embed = discord.Embed(
                        title=f'{member.display_name}, Would you like to play __hangman__ with {ctx.author.name} ?',
                        description=f'*- You have 30 seconds to decide*',
                        color=discord.Color.teal()
                    )
                    choose_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2241/2241299.png')
                    choose_embed.set_footer(text='Hangman | Webfinder v1.0')
                    choose = await ctx.send(embed=choose_embed)
                    await choose.add_reaction(check)
                    await choose.add_reaction(cancel)

                    def check(reaction, user):
                        return user == member and str(reaction.emoji) in confirm_list

                    try:

                        reaction = await self.client.wait_for('reaction_add', check=check, timeout=30)

                        if reaction[0].emoji == cancel:
                            cancel_embed = discord.Embed(
                                description=f'**{member} has declined your request.....What a pity !**',
                                color=discord.Color.red()
                            )
                            cancel_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2550/2550327.png')
                            cancel_embed.set_footer(text='Hangman | Webfinder v1.0',
                                                    icon_url='https://image.flaticon.com/icons/png/128/2241/2241299.png')

                            await ctx.send(embed=cancel_embed)
                        else:
                            await ctx.send(f'`{ctx.author.name} is picking a secret word....`')
                            author_word = self.client.get_user(ctx.author.id)
                            author_word_chose = discord.Embed(
                                title='HANGMAN',
                                description=f'**{ctx.author.name}**, please pick a word to play __hangman__. ( *You have 30 seconds* )\n**- NOTE :** Make sure that the word has no more than **2 spaces**. Example: living room, the Earth,... are accepted',
                                color=discord.Color.from_rgb(247, 255, 128)
                            )

                            await author_word.send(embed=author_word_chose)

                            def check_dm(message):
                                return message.channel.type == discord.ChannelType.private

                            wait_for_word = await self.client.wait_for('message', check=check_dm, timeout=30)


                            secret_word = wait_for_word.content
                            word_chose = discord.Embed(
                                description=f'{member.mention} ! **Now you can start guessing the word which {ctx.author.name} picked**',
                                color=discord.Color.green()
                            )

                            await ctx.send(embed=word_chose)
                            await author.send('`The game has been started in the channel`')


                            word = secret_word.lower()
                            if word.count(' ') > 2:
                                denied = discord.Embed(
                                    title='DENIED !',
                                    description=f'**The game has been denied due to __unacceptable word__ from {ctx.author}**',
                                    color=discord.Color.red()
                                )

                                await ctx.send(embed=denied)
                                await author.send(embed=denied)


                            else:


                                guesses = ''
                                hidden_list = []

                                turns = 6
                                hangman = [
                                    '''
|- - - - - 
|       |
|       
|
|
|
|
^^^^^^^^^^^^
''',
'''
|- - - - - 
|       |
|       O
|
|
|
|
^^^^^^^^^^^^
''',
'''
|- - - - - 
|       |
|       O
|       |
|       |
|
|
^^^^^^^^^^^^
''',
'''
|- - - - - 
|       |
|       O
|      /|
|       |
|
|
^^^^^^^^^^^^
''',
'''
|- - - - - 
|       |
|       O
|    ---|---
|       |
|
|
^^^^^^^^^^^^
''',
'''
|- - - - - 
|       |
|       O
|    ---|---
|       |
|      /
|
^^^^^^^^^^^^
''',
'''
|- - - - - 
|       |
|       O
|    ---|---
|       |
|      / \\
|
^^^^^^^^^^^^
'''
                                ]

                                turns_left = 6
                                guess_words = []
                                hints = []




                                if ' ' not in word:
                                    hints.append(f'The hidden word has {len(word)} character(s)')
                                elif ' ' in word:
                                    hints.append(f'The hidden word has {len(word)} character(s) with {word.count(" ")} space(s)')

                                start = time.strftime('%S')
                                while turns > 0:
                                    hangman_stage = hangman[0]
                                    if turns_left == 6:
                                        hangman_stage = hangman[0]
                                    elif turns_left == 5:
                                        hangman_stage = hangman[1]
                                    elif turns_left == 4:
                                        hangman_stage = hangman[2]
                                    elif turns_left == 3:
                                        hangman_stage = hangman[3]
                                    elif turns_left == 2:
                                        hangman_stage = hangman[4]
                                    elif turns_left == 1:
                                        hangman_stage = hangman[5]
                                    elif turns_left == 0:
                                        hangman_stage = hangman[6]

                                    failed = 0
                                    for char in word:
                                        if char in guesses:

                                            hidden_list.append(char)
                                        elif char == ' ':

                                            hidden_list.append(' ')

                                        else:
                                            hidden_list.append('*')

                                            # for every failure 1 will be
                                            # incremented in failure
                                            failed += 1



                                    guess_embed = discord.Embed(
                                        title=f'{ctx.author} vs {member}',
                                        color=discord.Color.from_rgb(117, 255, 168)
                                    )

                                    guess_embed.set_author(name='Hangman', icon_url='https://image.flaticon.com/icons/png/128/3119/3119316.png')
                                    guess_embed.add_field(name='Hints :', value=f'`{"".join(hints)}`\n**- Turn left :** `{turns} turn(s)`\n**- Characters guessed :** `{len(guess_words)} character(s)`')

                                    guess_embed.add_field(name='-', value=f'''
```diff
{hangman_stage}
    
- Word to guess : {"".join(hidden_list)}
```
                                    ''', inline=False)

                                    guess_embed.set_footer(text='Hangman | WebFinder v1.0')

                                    await ctx.send(embed=guess_embed)


                                    hidden_list.clear()

                                    if failed == 0:
                                        end = time.strftime('%S')
                                        duration = int(end)-int(start)

                                        win_embed = discord.Embed(
                                            title=f'CONGRATULATION ! {member}',
                                            description=f'You won the game in `{duration} seconds` with `{len(guess_words)} guesses` and `{turns_left} turn(s) left`',
                                            color=discord.Color.from_rgb(128, 255, 230),
                                            timestamp=datetime.datetime.utcnow()
                                        )
                                        win_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2829/2829661.png')
                                        win_embed.add_field(name=f'The correct word is : " __{secret_word}__ "', value='‏‏‎ ‎')

                                        await ctx.send(embed=win_embed)

                                        break

                                    def check_guesser(user2):
                                        return user2.author == member
                                    try:
                                        guess0 = await self.client.wait_for('message', check=check_guesser, timeout=20)

                                        guess = guess0.content

                                        if len(guess) > 1 and guess != word:
                                            await ctx.send('**`Please guess only 1 character`**')

                                        elif len(guess) > 1 and guess == word:
                                            end = time.strftime('%S')
                                            duration = int(end) - int(start)
                                            win_embed = discord.Embed(
                                                title=f'CONGRATULATION ! {member}',
                                                description=f'You guessed the **whole word** and won the game in `{duration} seconds` with `{len(guess_words)} guesses` and `{turns_left} turn(s) left`',
                                                color=discord.Color.from_rgb(128, 255, 230),
                                                timestamp=datetime.datetime.utcnow()
                                            )
                                            win_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2829/2829661.png')

                                            win_embed.add_field(name=f'The correct word is : " __{secret_word}__ "', value='‏‏‎ ‎')

                                            await ctx.send(embed=win_embed)

                                            break

                                        if guess in guesses:
                                            await ctx.send('`Character has already been guessed`')
                                        elif guess not in guesses:


                                            guesses += guess
                                            guess_words.append(guess)


                                        if guess not in word:

                                            turns -= 1
                                            turns_left = turns
                                            wrong_embed = discord.Embed(
                                                description=f'**WRONG ! You have `{turns_left} turn(s)` left**',
                                                color=discord.Color.red()
                                            )
                                            await ctx.send(embed=wrong_embed)

                                            if turns == 0:
                                                end = time.strftime('%S')
                                                duration = int(end) - int(start)
                                                lose_embed = discord.Embed(
                                                    title=f'GAME OVER ! {member}',
                                                    description=f'You lost the game in `{duration} seconds` with `{len(guess_words)} guesses`',
                                                    color=discord.Color.from_rgb(255, 111, 111),
                                                    timestamp=datetime.datetime.utcnow()
                                                )
                                                lose_embed.set_thumbnail(url='https://image.flaticon.com/icons/png/128/2927/2927829.png')
                                                lose_embed.add_field(name=f'The correct word is : " __{secret_word}__ "', value='‏‏‎ ‎')

                                                await ctx.send(embed=lose_embed)

                                    except asyncio.exceptions.TimeoutError:
                                        time_out_o = discord.Embed(
                                            title='TIME OUT !',
                                            description=f'**{member} did not response in time... *Loser !!!***',
                                            color=discord.Color.from_rgb(255, 70, 70)
                                        )

                                        await ctx.send(embed=time_out_o)
                                        break


                    except asyncio.exceptions.TimeoutError:
                        pass

                except BaseException:
                    await ctx.send(traceback.print_exc())


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, BucketType.user)
    async def guess(self, ctx):
        random_number = random.choice(range(100))
        random_word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        try:
            random_choice = random.choice([random_number, random_word])
            if random_choice == random_number:
                random_plus = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                plus = f'larger than `{random_number - random.choice(random_plus)}`'
                random_minus = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
                minus = f'less than `{random_number - random.choice(random_minus)}`'
                random_plus_or_minus = [plus, minus, f'{plus} and {minus}', f'{minus} and {plus}']

                hint_embed = discord.Embed(
                    description=f'This number is {random.choice(random_plus_or_minus)}',
                    color=discord.Color.teal()
                )

                hint_embed.set_author(name='Guess number', icon_url='https://image.flaticon.com/icons/png/128/2357/2357423.png')
                hint_embed.set_footer(text='Number | webFinder v1.0')
                await ctx.send(embed=hint_embed)

                def check(user):
                    return user.author == ctx.author

                i = 0
                print(random_number)
                while i < 11:


                        response = await self.client.wait_for('message', check=check, timeout=10)


                        if response.content == str(random_number):
                            right_embed = discord.Embed(
                                color=discord.Color.from_rgb(119, 255, 197)
                            )

                            right_embed.set_author(name=f'" {response.content} " is the correct number !', icon_url='https://emoji.gg/assets/emoji/6943_Check_Mark.gif')
                            await ctx.send(embed=right_embed)
                            break

                        elif response.content != str(random_number):
                            wrong_embed = discord.Embed(
                                color=discord.Color.from_rgb(255, 142, 142)
                            )

                            wrong_embed.set_author(name=f'Not that number ! You have {11-i} attempt(s) left', icon_url='https://image.flaticon.com/icons/png/128/1828/1828665.png')
                            await ctx.send(embed=wrong_embed)

                        if (response.content).lower() == 'quit' or (response.content).lower() == 'exit' or (response.content).lower() == 'esc':
                            await ctx.send('```diff\n- Quited the game\n```')
                            break
                        i += 1



            if random_choice == random_word:
                hint_embed = discord.Embed(
                    description=f'Guess one letter in the alphabet',
                    color=discord.Color.teal()
                )

                hint_embed.set_author(name='Guess letter', icon_url='https://image.flaticon.com/icons/png/128/3094/3094209.png')
                hint_embed.set_footer(text='Letter | WebFinder v1.0')
                await ctx.send(embed=hint_embed)


                def check(user):
                    return user.author == ctx.author

                i = 0

                while i < 11:

                        response = await self.client.wait_for('message', check=check, timeout=10)


                        if (response.content).lower() == random.choice(random_word):
                            right_embed = discord.Embed(
                                color=discord.Color.from_rgb(119, 255, 197)
                            )

                            right_embed.set_author(name=f'" {(response.content).lower()} " is the correct letter !',
                                                   icon_url='https://emoji.gg/assets/emoji/6943_Check_Mark.gif')
                            await ctx.send(embed=right_embed)
                            break

                        elif (response.content).lower() != random.choice(random_word):
                            wrong_embed = discord.Embed(
                                color=discord.Color.from_rgb(255, 142, 142)
                            )

                            wrong_embed.set_author(name=f'Not that letter ! You have {11 - i} attempt(s) left', icon_url='https://image.flaticon.com/icons/png/128/1828/1828665.png')
                            await ctx.send(embed=wrong_embed)
                        if (response.content).lower() == 'quit' or (response.content).lower() == 'exit' or (response.content).lower() == 'esc':
                            await ctx.send('```diff\n- Quited the game\n```')
                            break

                        i += 1

        except asyncio.exceptions.TimeoutError:
            time_out = discord.Embed(
                description=f'**TIME OUT ! You are too slow**',
                color=discord.Color.red()
            )

            await ctx.send(embed=time_out)
        except BaseException:
            await ctx.send(traceback.print_exc())
def setup(client):
    client.add_cog(Games(client))
