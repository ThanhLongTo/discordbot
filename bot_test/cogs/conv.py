import discord
from discord.ext import commands
import datetime
import numpy as np
import sympy as sp
import math
from scipy.special import lambertw



list = ['acos(', 'acosh(', 'asin(', 'asinh(',
                'atan(', 'atan2(', 'atanh(', 'ceil(', 'comb(', 'copysign(', 'cos(', 'cosh(', 'degrees(', 'dist(',
                'erf(', 'erfc(',
                'exp(', 'expm1(', 'fabs(', 'factorial(', 'floor(', 'fmod(', 'frexp(', 'fsum(', 'gamma(',
                'gcd(', 'hypot(', 'inf', 'isclose(', 'isfinite(', 'isinf(', 'isnan(', 'isqrt(', 'ldexp(', 'lgamma(',
                'log(',
                'log10(', 'log1p(', 'log2(', 'modf(', 'nan', 'perm(',
                'pow(', 'prod(', 'radians(', 'remainder(', 'sin(', 'sinh(', 'sqrt(', 'tan(', 'tanh(', 'tau', 'trunc(',
                'pi', 'e'
                ]



class Converter(commands.Cog):
    def __init__(self, client):
        self.client = client

        # UNIT CONVERTER HERE

    @commands.command()
    async def le_conv(self, ctx, amount, unit1, unit2):


        converter_embed = discord.Embed(
            title='Converter',
            color=discord.Color.blurple(),

        )
        with open('length_conv.txt') as uc:
            lines = uc.readlines()

        currencyDict = {}
        for line in lines:
            line1 = line.replace(')\n', ' ]]')
            line2 = line1.replace('(', ' ')
            parsed = line2.split(' ')
            currencyDict[parsed[0]] = parsed[1]

        a = float(currencyDict[unit1])
        b = float(currencyDict[unit2])

        total = a / b
        result = float(amount) / total
        converter_embed.add_field(name='Input', value=f'```\n{amount} {unit1} to {unit2}\n```', inline=False)
        converter_embed.add_field(name='Output', value=f'```\n{result} {unit2}\n```', inline=False)
        await ctx.send(embed=converter_embed)

    @commands.command()
    async def we_conv(self, ctx, amount, unit1, unit2):

        converter_embed = discord.Embed(
            title='Converter',
            color=discord.Color.blurple(),

        )
        with open('weight_conv.txt') as uc:
            lines = uc.readlines()

        currencyDict = {}
        for line in lines:
            line1 = line.replace(')\n', ' ]]')
            line2 = line1.replace('(', ' ')
            parsed = line2.split(' ')
            currencyDict[parsed[0]] = parsed[1]

        a = float(currencyDict[unit1])
        b = float(currencyDict[unit2])

        total = a / b
        result = float(amount) / total
        converter_embed.add_field(name='Input', value=f'```\n{amount} {unit1} to {unit2}\n```', inline=False)
        converter_embed.add_field(name='Output', value=f'```\n{result} {unit2}\n```', inline=False)
        await ctx.send(embed=converter_embed)

    @commands.command()
    async def te_conv(self, ctx, amount, unit1, unit2):

        converter_embed = discord.Embed(
            title='Converter',
            color=discord.Color.blurple(),

        )
        with open('tem_conv.txt') as uc:
            lines = uc.readlines()

        currencyDict = {}

        temp_dict = {
            'kelvin': 'K',
            'celsius': '°C',
            'fahrenheit': '°F',
            'rankine': '°R',
            'reaumur': '°r'
        }

        for line in lines:
            line1 = line.replace(')\n', ' ]]')
            line2 = line1.replace('(', ' ')
            parsed = line2.split(' ')
            currencyDict[parsed[0]] = parsed[1]

        a = float(currencyDict[unit1])
        b = float(currencyDict[unit2])

        total = a / b
        result = float(amount) / total

        converter_embed.add_field(name='Input', value=f'```\n{amount} {unit1} to {unit2}\n```', inline=False)
        converter_embed.add_field(name='Output', value=f'```\n{result}{temp_dict[unit2]}\n```', inline=False)
        await ctx.send(embed=converter_embed)

    @commands.command()
    async def vo_conv(self, ctx, amount, unit1, unit2):

        converter_embed = discord.Embed(
            title='Converter',
            color=discord.Color.blurple(),

        )
        with open('volume_conv.txt') as uc:
            lines = uc.readlines()

        currencyDict = {}
        for line in lines:
            line1 = line.replace(')\n', ' ]]')
            line2 = line1.replace('(', ' ')
            parsed = line2.split(' ')
            currencyDict[parsed[0]] = parsed[1]

        a = float(currencyDict[unit1])
        b = float(currencyDict[unit2])

        total = a / b
        result = float(amount) / total
        converter_embed.add_field(name='Input', value=f'```\n{amount} {unit1} to {unit2}\n```', inline=False)
        converter_embed.add_field(name='Output', value=f'```\n{result} {unit2}\n```', inline=False)
        await ctx.send(embed=converter_embed)

    @commands.command()
    async def ar_conv(self, ctx, amount, unit1, unit2):

        converter_embed = discord.Embed(
            title='Converter',
            color=discord.Color.blurple(),

        )
        with open('area_conv.txt') as uc:
            lines = uc.readlines()

        currencyDict = {}
        for line in lines:
            line1 = line.replace(')\n', ' ]]')
            line2 = line1.replace('(', ' ')
            parsed = line2.split(' ')
            currencyDict[parsed[0]] = parsed[1]

        a = float(currencyDict[unit1])
        b = float(currencyDict[unit2])

        total = a / b
        print(total)
        result = float(amount) / total
        converter_embed.add_field(name='Input', value=f'```\n{amount} {unit1} to {unit2}\n```', inline=False)
        converter_embed.add_field(name='Output', value=f'```\n{result} {unit2}\n```', inline=False)
        await ctx.send(embed=converter_embed)

    @commands.command()
    async def sp_conv(self, ctx, amount, unit1, unit2):

        converter_embed = discord.Embed(
            title='Converter',
            color=discord.Color.blurple(),

        )
        with open('speed_conv.txt') as uc:
            lines = uc.readlines()


        currencyDict = {}
        for line in lines:
            line1 = line.replace(')\n', ' ]]')
            line2 = line1.replace('(', ' ')
            parsed = line2.split(' ')
            currencyDict[parsed[0]] = parsed[1]

        a = float(currencyDict[unit1])
        b = float(currencyDict[unit2])



        total = (a) / (b)
        result = float(amount) / (total)

        converter_embed.add_field(name='Input', value=f'```\n{amount} {unit1} to {unit2}\n```', inline=False)
        converter_embed.add_field(name='Output', value=f'```\n{result} {unit2}\n```', inline=False)
        await ctx.send(embed=converter_embed)

    @commands.command()
    async def cur_conv(self, ctx, amount, unit1, unit2):

        converter_embed = discord.Embed(
            title='Converter',
            color=discord.Color.blurple(),

        )
        with open('currency.txt') as uc:
            lines = uc.readlines()

        currencyDict = {}
        for line in lines:
            line1 = line.replace(')\n', ' ]]')
            line2 = line1.replace('(', ' ')
            parsed = line2.split(' ')
            currencyDict[parsed[0]] = parsed[1]

        a = float(currencyDict[unit1.upper()])
        b = float(currencyDict[unit2.upper()])

        total = a / b
        result = float(amount) / total
        converter_embed.add_field(name='Input', value=f'```\n{amount} {unit1.upper()} to {unit2.upper()}\n```',
                                  inline=False)
        converter_embed.add_field(name='Output', value=f'```\n{result} {unit2.upper()}\n```', inline=False)
        await ctx.send(embed=converter_embed)

    @commands.command()
    async def calc_per(self, ctx, shape, *, input):
        conv_list = ['square', 'circle', 'triangle', 'rectangle']
        convDict = {}

        if '^' in input:
            input = input.replace('^', '**')
        if '%' in input:
            input = input.replace('%', '/100')

        for i in list:
            if i in input:
                input = input.replace(i, f'math.{i}')


                if 'amath.' in input:
                    input = input.replace('amath.', 'math.a')
                if 'lambmath.' in input:
                    input = input.replace('lambmath.', 'lamb')
                if 'math.math.' in input:
                    input = input.replace('math.math.', 'math.')



        input = input.replace(' ', '')



        if shape not in conv_list:
            await ctx.send("```diff\n- ERROR: Invalid Shape. n!help for instruction\n```")
            return
        else:
            pass


        if shape == 'square':
            if 's=' in input:
                input = input.replace('s=', '')
                if eval(input) < 0:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'rectangle':
            if 'a=' and 'b=' in input:
                input = input.replace('a=', 'a=')
                input = input.replace('b=', ' b=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                re1 = convDict['a']
                re2 = convDict['b']
                if eval(re1) and eval(re2) > 0:
                    input = f'2*({re1}+{re2})'

                else:
                    await ctx.send("```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'triangle':
            if 'a=' and 'b=' and 'c=' in input:
                input = input.replace('a=', 'a=')
                input = input.replace('b=', ' b=')
                input = input.replace('c=', ' c=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]


                re1 = convDict['a']
                re2 = convDict['b']
                re3 = convDict['c']
                if eval(re1) and eval(re2) and eval(re3) > 0:

                    #check_list = input.split('+')

                    if eval(re1) + eval(re2) < eval(re3):
                        await ctx.send(
                            "```diff\n- ERROR: The sum of the lengths of 2 sides of a triangle must be greater than the third side. n!help for instruction\n```")
                        return
                    if eval(re2) + eval(re3) < eval(re1):
                        await ctx.send(
                            "```diff\n- ERROR: The sum of the lengths of 2 sides of a triangle must be greater than the third side. n!help for instruction\n```")
                        return
                    if eval(re3) + eval(re1) < eval(re2):
                        await ctx.send(
                            "```diff\n- ERROR: The sum of the lengths of 2 sides of a triangle must be greater than the third side. n!help for instruction\n```")
                        return
                    else:
                        input = f'{re1}+{re2}+{re3}'





                else:
                    await ctx.send("```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'circle':
            if 'r=' in input:
                input = input.replace('r=', '')
                if eval(input) < 0:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return


        # Calculation




        # check if the triangle is existed


        try:
            answer1 = eval(input)


            if float(answer1) < 0:
                await ctx.send(
                    "```diff\n- ERROR: Invalid result ( Perimeter/Area/Volume must be GREATER than 0 )\n- Try again.\n```")
            else:

                # Insert to formulas
                if shape == 'square':
                    square_per = eval(f'4*({answer1})')
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nSquare's perimeter: 4s = 4*({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nP = {square_per} (unit of length)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)

                if shape == 'rectangle':
                    rectangle_per = answer1

                    rectangle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    rectangle_per_embed.add_field(name='Input',
                                                  value=f"```\nRectangle's perimeter: 2(l + w) = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                                  inline=False)
                    rectangle_per_embed.add_field(name='Output',
                                                  value=f'```\nP = {rectangle_per} (unit of length)\n```', inline=False)
                    await ctx.send(embed=rectangle_per_embed)

                if shape == 'triangle':
                    triangle_per = answer1

                    triangle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    triangle_per_embed.add_field(name='Input',
                                                 value=f"```\nTriangle's perimeter: a+b+c = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                                 inline=False)
                    triangle_per_embed.add_field(name='Output', value=f'```\nP = {triangle_per} (unit of length)\n```',
                                                 inline=False)
                    await ctx.send(embed=triangle_per_embed)

                if shape == 'circle':
                    circle_per = eval(f'2*({answer1})*math.pi')

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nCircle's perimeter: 2πr = 2π*({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nP = {circle_per} (unit of length)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)

        except ValueError as VE:
            await ctx.send(f'```diff\n- ERROR : {VE}\n```')
            return
        except ZeroDivisionError as ZDE:
            await ctx.send(f'```diff\n- ERROR : {ZDE}\n```')
            return
        except NameError as NE:
            await ctx.send(f'```diff\n- ERROR : {NE}\n```')
        except SyntaxError as SE:
            await ctx.send(f'```diff\n- ERROR : {SE}\n```')
        except OverflowError as OE:
            await ctx.send(f'```diff\n- ERROR : {OE}\n```')
            return
    @commands.command()
    async def calc_ar(self, ctx, shape, *, input):
        conv_list = ['square', 'triangle', 'triangle(Heron)', 'circle', 'sector', 'circular_sector', 'rectangle', 'trapezoid', 'parallelogram', 'hexagon', 'pentagon', 'sphere', 'cone', 'kite','rhombus', 'ellipse', 'octagon', 'annulus', 'conical_frustum']
        convDict = {}

        if '^' in input:
            input = input.replace('^', '**')
        if '%' in input:
            input = input.replace('%', '/100')


        for i in list:
            if i in input:
                input = input.replace(i, f'math.{i}')

                if 'amath.' in input:
                    input = input.replace('amath.', 'math.a')
                if 'lambmath.' in input:
                    input = input.replace('lambmath.', 'lamb')
                if 'math.math.' in input:
                    input = input.replace('math.math.', 'math.')


        input = input.replace(' ', '')

        if shape not in conv_list:
            await ctx.send("```diff\n- ERROR: Invalid Shape. n!help for instruction\n```")
            return
        else:
            pass


        # Square
        if shape == 'square':
            if 's=' in input:
                input = input.replace('s=', '')
                if eval(input) < 0:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return


        if shape == 'hexagon':
            if 's=' in input:
                input = input.replace('s=', '')
                if eval(input) < 0:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'pentagon':
            if 's=' in input:
                input = input.replace('s=', '')
                if eval(input) < 0:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass


            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'octagon':
            if 's=' in input:
                input = input.replace('s=', '')
                if eval(input) < 0:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass


            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'rectangle':
            if 'a=' and 'b=' in input:
                input = input.replace('a=', 'a=')
                input = input.replace('b=', ' b=')
                a = input.replace(' ', '\n')
                b = a.split('\n')
                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                re1 = convDict['a']
                re2 = convDict['b']
                if eval(re1) and eval(re2) > 0:
                    input = f'({re1})*({re2})'
                else:
                    await ctx.send("```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'triangle':
            if 'b=' and 'h=' in input:
                input = input.replace('b=', 'b=')
                input = input.replace('h=', ' h=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]


                re1 = convDict['b']
                re2 = convDict['h']

                if eval(re1) and eval(re2) > 0:
                    input = f'1/2*({re1})*({re2})'
                else:
                    await ctx.send("```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return


        if shape == 'triangle(Heron)':
            if 'a=' and 'b=' and 'c=' in input:
                input = input.replace('a=', 'a=')
                input = input.replace('b=', ' b=')
                input = input.replace('c=', ' c=')
                print(input)
                a = input.replace(' ', '\n')
                b = a.split('\n')
                print(b)


                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                print(convDict)


                re1 = convDict['a']
                re2 = convDict['b']
                re3 = convDict['c']

                if eval(re1) and eval(re2) > 0:
                    input = f'math.sqrt((({re1})**2 + ({re2})**2 + ({re3})**2)**2-2*(({re1})**4 + ({re2})**4 + ({re3})**4))/4'
                    print(input)
                else:
                    await ctx.send("```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return


        if shape == 'parallelogram':
            if 'b=' and 'h=' in input:
                input = input.replace('b=', 'b=')
                input = input.replace('h=', ' h=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]


                re1 = convDict['b']
                re2 = convDict['h']

                if eval(re1) and eval(re2) > 0:
                    input = f'({re1})*({re2})'
                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'trapezoid':
            if 'b1=' and 'b2=' and 'h=' in input:
                input = input.replace('b1=', 'b1=')
                input = input.replace('b2=', ' b2=')
                input = input.replace('h=', ' h=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]


                re1 = convDict['b1']
                re2 = convDict['b2']
                re3 = convDict['h']

                if eval(re1) and eval(re2) and eval(re3)> 0:
                    input = f'1/2*({re1}+{re2})*({re3})'
                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'circle':
            if 'r=' in input:
                input = input.replace('r=', '')
                if eval(input) < 0:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'sphere':
            if 'r=' in input:
                input = input.replace('r=', '')
                if eval(input) < 0:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'cone':
            if 'r=' and 'l=' in input:
                input = input.replace('r=', 'r=')
                input = input.replace('l=', ' l=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                re1 = convDict['r']
                re2 = convDict['l']


                if eval(re1) and eval(re2) > 0:
                    input = f'math.pi*({re1})*({re2})'
                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'sector' or shape == 'circular_sector':
            if 'r=' and 'n=' in input:
                input = input.replace('r=', 'r=')
                input = input.replace('n=', ' n=')
                a = input.replace(' ', '\n')
                b = a.split('\n')


                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                re1 = convDict['r']
                re2 = convDict['n']

                if eval(re1) and eval(re2) > 0:
                    if eval(re2) <= 360:
                        input = f'math.pi*({re1})**2*(({re2})/360)'

                    else:
                        await ctx.send("```diff\n- ERROR: Angle must be GREATER than 0 and LESS or EQUAL to 360.\n```")
                        return

                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'annulus':
            if 'R=' and 'r=' in input:
                input = input.replace('R=', 'R=')
                input = input.replace('r=', ' r=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                re1 = convDict['R']
                re2 = convDict['r']

                if eval(re1) and eval(re2) > 0:
                    if eval(re1) < eval(re2):
                        await ctx.send(
                            "```diff\n- ERROR: Outer radius must be GREATER than inner radius. n!help for instruction\n```")
                    else:
                        input = f'math.pi*(({re1})**2-({re2})**2)'
                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return


        if shape == 'conical_frustum':
            if 'r1=' and 'r2=' and 'h=' in input:
                input = input.replace('r1=', 'r1=')
                input = input.replace('r2=', ' r2=')
                input = input.replace('h=', ' h=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                re1 = convDict['r1']
                re2 = convDict['r2']
                re3 = convDict['h']

                if eval(re1) and eval(re2) and eval(re3) > 0:
                    input = f'math.pi*(({re1}) + ({re2}))*math.sqrt(({re1} - {re2})**2 + ({re3})^2)'
                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return


        if shape == 'kite':
            if 'd1=' and 'd2=' in input:
                input = input.replace('d1=', 'd1=')
                input = input.replace('d2=', ' d2=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                re1 = convDict['d1']
                re2 = convDict['d2']

                if eval(re1) and eval(re2) > 0:
                    input = f'(({re1})*({re2}))/2'
                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'rhombus':
            if 'd1=' and 'd2=' in input:
                input = input.replace('d1=', 'd1=')
                input = input.replace('d2=', ' d2=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]

                re1 = convDict['d1']
                re2 = convDict['d2']

                if eval(re1) and eval(re2) > 0:
                    input = f'(({re1})*({re2}))/2'
                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'ellipse':
            if 'a=' and 'b=' in input:
                input = input.replace('a=', 'a=')
                input = input.replace('b=', ' b=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]



                re1 = convDict['a']
                re2 = convDict['b']

                if eval(re1) and eval(re2) > 0:
                    input = f'({re1})*({re2})*math.pi'
                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return





        try:
            answer1 = eval(input)



            if float(answer1) < 0:
                await ctx.send(
                    "```diff\n- ERROR: Invalid result ( Perimeter/Area/Volume must be GREATER than 0 )\n- Try again.\n```")
            else:

                if shape == 'square'.lower():
                    square_per = eval(f'({answer1})**2')
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nSquare's area: s^2 = ({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})^2\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nS = {square_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)


                if shape == 'hexagon'.lower():
                    square_per = eval(f'(3*math.sqrt(3)*({answer1})**2)/2')
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nHexagon's area: (3√3*s^2)/2 = (3√3*({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})^2)/2\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nS = {square_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)


                if shape == 'pentagon'.lower():
                    rectangle_per = eval(f'({answer1})**2*math.sqrt(25 + 10*math.sqrt(5))/4')

                    rectangle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    rectangle_per_embed.add_field(name='Input',
                                                  value=f"```\nPentagon's area: a^2 * √(25 + 10√5) / 4 = ({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})^2*√(25 + 10√5) / 4\n```",
                                                  inline=False)
                    rectangle_per_embed.add_field(name='Output', value=f'```\nS = {rectangle_per} (Unit of area)\n```',
                                                  inline=False)
                    await ctx.send(embed=rectangle_per_embed)


                if shape == 'octagon'.lower():
                    rectangle_per = eval(f'({answer1})**2 * 2 * (1 + math.sqrt(2))')

                    rectangle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    rectangle_per_embed.add_field(name='Input',
                                                  value=f"```\nPentagon's area: a^2 * 2 * (1 + sqrt(2)) = ({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})* 2 * (1 + sqrt(2))\n```",
                                                  inline=False)
                    rectangle_per_embed.add_field(name='Output', value=f'```\nS = {rectangle_per} (Unit of area)\n```',
                                                  inline=False)
                    await ctx.send(embed=rectangle_per_embed)

                if shape == 'rectangle'.lower():
                    rectangle_per = answer1

                    rectangle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    rectangle_per_embed.add_field(name='Input',
                                                  value=f"```\nRectangle's area: l*w = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                                  inline=False)
                    rectangle_per_embed.add_field(name='Output', value=f'```\nS = {rectangle_per} (Unit of area)\n```',
                                                  inline=False)
                    await ctx.send(embed=rectangle_per_embed)

                if shape == 'triangle':
                    triangle_per = answer1

                    triangle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    triangle_per_embed.add_field(name='Input',
                                                 value=f"```\nTriangle's area: 1/2*b*h = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                                 inline=False)
                    triangle_per_embed.add_field(name='Output', value=f'```\nS = {triangle_per} (Unit of area)\n```',
                                                 inline=False)
                    await ctx.send(embed=triangle_per_embed)


                if shape == 'triangle(Heron)':
                    triangle_per = answer1

                    triangle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    triangle_per_embed.add_field(name='Input',
                                                 value=f"```\nTriangle's area: √((a^2+b^2+c^2)^2 - 2(a^4+b^4+c^4)) / 4 = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                                 inline=False)
                    triangle_per_embed.add_field(name='Output', value=f'```\nS = {triangle_per} (Unit of area)\n```',
                                                 inline=False)
                    await ctx.send(embed=triangle_per_embed)

                if shape == 'parallelogram':
                    parallelogram_per = answer1

                    parallelogram_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    parallelogram_per_embed.add_field(name='Input',
                                                      value=f"```\nParallelogram's area: b*h = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                                      inline=False)
                    parallelogram_per_embed.add_field(name='Output',
                                                      value=f'```\nS = {parallelogram_per} (Unit of area)\n```',
                                                      inline=False)
                    await ctx.send(embed=parallelogram_per_embed)

                if shape == 'trapezoid':
                    trapezoid_per = answer1

                    trapezoid_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    trapezoid_per_embed.add_field(name='Input',
                                                  value=f"```\nTrapezoid's area: 1/2(b1 + b2)*h = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                                  inline=False)
                    trapezoid_per_embed.add_field(name='Output', value=f'```\nS = {trapezoid_per} (Unit of area)\n```',
                                                  inline=False)
                    await ctx.send(embed=trapezoid_per_embed)

                if shape == 'circle':
                    circle_per = eval(f'({answer1})**2*math.pi')

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nCircle's area: r^2*π = ({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})^2*π\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)

                if shape == 'sphere':
                    circle_per = eval(f'4*math.pi*({answer1})**2')

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nSurface area of sphere: 4π*r^2 = 4*π*({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})^2\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)

                if shape == 'cone':
                    circle_per = answer1

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nSurface area of cone: π*r*l = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)


                if shape == 'sector' or shape == 'circular_sector':
                    circle_per = answer1

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\n(Circular) Sector's area: π*r^2*(n/360) = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)


                if shape == 'annulus':
                    circle_per = answer1

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nAnnulus (Ring)'s area: π*(R^2-r^2) = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)


                if shape == 'conical_frustum':
                    circle_per = answer1

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nSurface area of Conical frustum: π*(r1+r2)*sqrt((r1-r2)^2+h) = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)


                if shape == 'kite':
                    circle_per = answer1

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nKite's area: (d1*d2)/2 = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)

                if shape == 'rhombus':
                    circle_per = answer1

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nRhombus's area: (d1*d2)/2 = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)

                if shape == 'ellipse':
                    circle_per = answer1

                    circle_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    circle_per_embed.add_field(name='Input',
                                               value=f"```\nEllipse's area: a*b*π = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    circle_per_embed.add_field(name='Output', value=f'```\nS = {circle_per} (Unit of area)\n```',
                                               inline=False)
                    await ctx.send(embed=circle_per_embed)

        except ValueError as VE:
            await ctx.send(f'```diff\n- ERROR : {VE}\n```')
            return
        except ZeroDivisionError as ZDE:
            await ctx.send(f'```diff\n- ERROR : {ZDE}\n```')
            return
        except NameError as NE:
            await ctx.send(f'```diff\n- ERROR : {NE}\n```')
            return
        except SyntaxError as SE:
            await ctx.send(f'```diff\n- ERROR : {SE}\n```')
            return
        except OverflowError as OE:
            await ctx.send(f'```diff\n- ERROR : {OE}\n```')
            return

    @commands.command()
    async def calc_vol(self, ctx, shape, *, input):

        convDict = {}
        conv_list = [ 'box', 'cube', 'cylinder', 'circular_prism', 'cone', 'sphere', 'conical_frustum']

        if '^' in input:
            input = input.replace('^', '**')
        if '%' in input:
            input = input.replace('%', '/100')

        for i in list:
            if i in input:
                input = input.replace(i, f'math.{i}')

                if 'amath.' in input:
                    input = input.replace('amath.', 'math.a')
                if 'lambmath.' in input:
                    input = input.replace('lambmath.', 'lamb')
                if 'math.math.' in input:
                    input = input.replace('math.math.', 'math.')


        input = input.replace(' ', '')


        if shape not in conv_list:
            await ctx.send("```diff\n- ERROR: Invalid Shape. n!help for instruction\n```")
            return
        else:
            pass



        if shape == 'box':
            if 'a=' and 'b=' and 'h=' in input:
                input = input.replace('a=', 'a=')
                input = input.replace('b=', ' b=')
                input = input.replace('h=', ' h=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]


                re1 = convDict['a']
                re2 = convDict['b']
                re3 = convDict['h']

                if eval(re1) and eval(re2)  and eval(re3)> 0:
                    input = f'({re1})*({re2})*({re3})'

                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return
        if shape == 'sphere':
            if 'r=' in input:
                input = input.replace('r=', '')
                if eval(input) < 0:
                    await ctx.send(
                            "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass
            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'cube':
            if 's=' in input:
                input = input.replace('s=', '')
                if eval(input) < 0:
                    await ctx.send(
                            "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return
                else:
                    pass

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return

        if shape == 'cylinder' or shape == 'circular_prism':
            if 'r=' and 'h=' in input:
                input = input.replace('r=', 'r=')
                input = input.replace('h=', ' h=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]


                re1 = convDict['r']
                re2 = convDict['h']
                if eval(re1) and eval(re2) > 0:
                    input = f'2*math.pi*({re1})**2*({re2})'

                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return


        if shape == 'cone' :
            if 'r=' and 'h=' in input:
                input = input.replace('r=', 'r=')
                input = input.replace('h=', ' h=')
                a = input.replace(' ', '\n')
                b = a.split('\n')

                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]


                re1 = convDict['r']
                re2 = convDict['h']
                if eval(re1) and eval(re2) > 0:
                    input = f'1/3*math.pi*({re1})**2*({re2})'

                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return


        if shape == 'conical_frustum' :
            if 'r1=' and 'r2=' and 'h=' in input:
                input = input.replace('r1=', 'r1=')
                input = input.replace('r2=', ' r2=')
                input = input.replace('h=', ' h=')
                a = input.replace(' ', '\n')
                b = a.split('\n')


                for c in b:
                    d = c.split('=')
                    convDict[d[0]] = d[1]


                re1 = convDict['r1']
                re2 = convDict['r2']
                re3 = convDict['h']
                if eval(re1) and eval(re2) and eval(re3) > 0:
                    input = f'1/3*math.pi*(({re1})**2 + ({re2})**2 + ({re1})*({re2}))*({re3})'


                else:
                    await ctx.send(
                        "```diff\n- ERROR: Invalid Argument ( Any side must be GREATER than 0 ). n!help for instruction\n```")
                    return

            else:
                await ctx.send("```diff\n- ERROR: Missing required argument. n!help for instruction\n```")
                return






        try:
            answer1 = eval(input)

            if float(answer1) < 0:
                await ctx.send(
                    "```diff\n- ERROR: Invalid result ( Perimeter/Area/Volume must be GREATER than 0 )\n- Try again.\n```")
            else:

                if shape == 'cylinder'.lower() or shape == 'circular_prism'.lower():
                    square_per = answer1
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nCylinder/Circular prism's volume: 2πr^2*h = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nV = {square_per} (Unit of volume)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)

                if shape == 'cone'.lower():
                    square_per = answer1
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nCone's volume: 1/3*πr^2*h = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nV = {square_per} (Unit of volume)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)


                if shape == 'sphere'.lower():
                    square_per = eval(f'4/3*math.pi*({answer1})**3')
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nSphere's volume: 4/3*πr^3 = 4/3*π*({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})^3\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nV = {square_per} (Unit of volume)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)

                if shape == 'cube'.lower():
                    square_per = eval(f'({answer1})**3')
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nSphere's volume: s^3 = ({((input.replace('**', '^')).replace(' ', '')).replace('math.', '')})^3\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nV = {square_per} (Unit of volume)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)

                if shape == 'box'.lower():
                    square_per = answer1
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nBox's volume: l*w*h = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nV = {square_per} (Unit of volume)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)


                if shape == 'conical_frustum'.lower():
                    square_per = answer1
                    square_per_embed = discord.Embed(
                        title='Calculator',
                        color=discord.Color.blurple()
                    )

                    square_per_embed.add_field(name='Input',
                                               value=f"```\nConical frustum's volume: 1/3π*(r1^2 + r2^2 + r1*r2)*h = {((input.replace('**', '^')).replace(' ', '')).replace('math.', '')}\n```",
                                               inline=False)
                    square_per_embed.add_field(name='Output', value=f'```\nV = {square_per} (Unit of volume)\n```',
                                               inline=False)
                    await ctx.send(embed=square_per_embed)



        except ValueError as VE:
            await ctx.send(f'```diff\n- ERROR : {VE}\n```')
            return
        except ZeroDivisionError as ZDE:
            await ctx.send(f'```diff\n- ERROR : {ZDE}\n```')
            return
        except NameError as NE:
            await ctx.send(f'```diff\n- ERROR : {NE}\n```')
            return
        except SyntaxError as SE:
            await ctx.send(f'```diff\n- ERROR : {SE}\n```')
            return
        except OverflowError as OE:
            await ctx.send(f'```diff\n- ERROR : {OE}\n```')
            return


def setup(client):
    client.add_cog(Converter(client))