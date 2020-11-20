import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import datetime
import numpy as np
import sympy as sp
from sympy import simplify
import DecInt


import math
from sympy.abc import x
from scipy.special import lambertw

list1 = {'acos(': 'math.acos(',
         'acosh(': 'math.acosh(',
         'asin(': 'math.asin(',
         'asinh(': 'math.asinh(',
         'atan(': 'math.atan(',
         'atan2(': 'math.atan2(',
         'atanh(': 'math.atanh(',
         'ceil(': 'math.ceil(',
         'comb(': 'math.comb(',
         'copysign(': 'math.copysign(',
         'cos(': 'math.cos(',
         'cosh(': 'math.cosh(',
         'degrees(': 'math.degrees(',
         'dist(': 'math.dist(',
         'erf(': 'math.erf(',
         'erfc(': 'math.erfc(',
         'exp(': 'math.exp(',
         'expm1(': 'math.expm1(',
         'e': 'math.e',
         'fabs(': 'math.fabs(',
         'factorial(': 'math.factorial(',
         'floor(': 'math.floor(',
         'fmod(': 'math.fmod(',
         'frexp(': 'math.frexp(',
         'fsum(': 'math.fsum(',
         'gamma(': 'math.gamma(',
         'gcd(': 'math.gcd(',
         'hypot(': 'math.hypot(',
         'inf': 'math.inf',
         'isclose(': 'math.isclose(',
         'isfinite(': 'math.isfinite(',
         'isinf(': 'math.isinf(',
         'isnan(': 'math.isnan(',
         'isqrt(': 'math.isqrt(',
         'ldexp(': 'math.ldexp(',
         'lgamma(': 'math.lgamma(',
         'log(': 'math.log(',
         'log10(': 'math.log10(',
         'log1p(': 'math.log1p(',
         'log2(': 'math.log2(',
         'modf(': 'math.modf(',
         'nan(': 'math.nan(',
         'perm(': 'math.perm(',
         'pi': 'math.pi',
         'pow(': 'math.pow(',
         'prod(': 'math.prod(',
         'radians(': 'math.radians(',
         'remainder(': 'math.remainder(',
         'sin(': 'math.sin(',
         'sinh(': 'math.sinh(',
         'sqrt(': 'math.sqrt(',
         'tan(': 'math.tan(',
         'tanh(': 'math.tanh(',
         'tau': 'math.tau',
         'trunc(': 'math.trunc('
         }

list = ['ceil(', 'comb(', 'copysign(', 'cos(', 'cosh(', 'degrees(', 'dist(',
        'fabs(', 'factorial(', 'floor(', 'fmod(', 'frexp(', 'fsum(', 'gamma(',
        'gcd(', 'hypot(', 'inf', 'isclose(', 'isfinite(', 'isinf(', 'isnan(', 'isqrt(', 'ldexp(', 'lgamma(',
        'log(',
        'log10(', 'log1p(', 'log2(', 'modf(', 'nan', 'perm(',
        'pow(', 'prod(', 'radians(', 'remainder(', 'sin(', 'sinh(', 'sqrt(', 'tan(', 'tanh(', 'tau', 'trunc(',
        'pi', 'e'
        ]


class Calculation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # SIMPLE CALCULATION
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def calc(self, ctx, *, input):



        if len(str(input)) > 60:
            await ctx.send('```diff\n- Too long input. Please try again!\n```')
        else:

            if '^' in input:
                input = input.replace('^', '**')
            if '%' in input:
                input = input.replace('%', '/100')

            calculation_embed = discord.Embed(
                title='Calculator',
                color=discord.Color.blurple(),

            )

            for i in list:
                if i in input:
                    input = input.replace(i, f'math.{i}')

                    if 'amath.' in input:
                        input = input.replace('amath.', 'math.a')
                    if 'lambmath.' in input:
                        input = input.replace('lambmath.', 'lamb')
                    if 'math.math.' in input:
                        input = input.replace('math.math.', 'math.')



            try:

                answer1 = eval(input)
                if 30000 > len(str(answer1)) > 1024:
                    try:
                        num = str(answer1)
                        n = 1980
                        c = [num[i:i + n] for i in range(0, len(num), n)]
                        count = len(c)
                        i = 0
                        await ctx.send(f'__{input} = (large result)__')
                        while i < (count + 1):
                            i = i + 1

                            await ctx.send(f'```\n{c[i - 1]}\n```')
                    except IndexError:
                        print('')
                        return


                if len(str(answer1)) > 30000:
                    await ctx.send('```diff\n- Too large result!\n```')

                else:

                    final_input = input.replace(' ', '')
                    if '**' in final_input:
                        final_input = final_input.replace('**', '^')

                        calculation_embed.add_field(name='Input', value=f'```\n{final_input.replace("math.", "")}\n```',
                                                            inline=False)
                        calculation_embed.add_field(name='Output', value=f'```\n{answer1}\n```', inline=False)

                        await ctx.send(embed=calculation_embed)
                        return

                    else:
                        calculation_embed.add_field(name='Input', value=f'```\n{final_input.replace("math.", "")}\n```',
                                                            inline=False)
                        calculation_embed.add_field(name='Output', value=f'```\n{answer1}\n```', inline=False)

                        await ctx.send(embed=calculation_embed)
                        return

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
    @commands.is_owner()
    @commands.cooldown(1, 10, BucketType.user)
    async def calc_pow(self, ctx, *, input):


        if len(str(input)) > 60:
            await ctx.send('```diff\n- Too long input. Please try again!\n```')
        else:

            input = input.replace('DecInt(', 'DecInt.DecInt(')
            input = input.replace('decint(', 'DecInt.DecInt(')

            if '^' in input:
                input = input.replace('^', '**')
            if '%' in input:
                input = input.replace('%', '/100')

            input = input.replace('Dmath.', 'D')

            calculation_embed = discord.Embed(
                title='Calculator',
                color=discord.Color.blurple(),

            )

            for i in list:
                if i in input:
                    await ctx.send('```diff\n- Warning: This is just for power calculation. Please consider using n!calc for simple one\n```')






            try:

                answer1 = eval(input)

                if 40000 > len(str(answer1)) > 1024:
                    try:
                        num = str(answer1)
                        n = 1980
                        c = [num[i:i + n] for i in range(0, len(num), n)]
                        count = len(c)
                        i = 0
                        await ctx.send(f'__{input} = (large result)__')
                        while i < (count + 1):
                            i = i + 1
                            await ctx.send(f'```\n{c[i - 1]}\n```')


                    except IndexError:
                        print('')
                        return


                if len(str(answer1)) > 40000:
                    await ctx.send('```diff\n- Too large result!\n```')
                else:

                    final_input = input.replace(' ', '')
                    if '**' in final_input:
                        final_input = final_input.replace('**', '^')

                        calculation_embed.add_field(name='Input', value=f'```\n{final_input.replace("math.", "")}\n```',
                                                            inline=False)
                        calculation_embed.add_field(name='Output', value=f'```\n{answer1}\n```', inline=False)

                        await ctx.send(embed=calculation_embed)
                        return

                    else:
                        calculation_embed.add_field(name='Input', value=f'```\n{final_input.replace("math.", "")}\n```',
                                                            inline=False)
                        calculation_embed.add_field(name='Output', value=f'```\n{answer1}\n```', inline=False)

                        await ctx.send(embed=calculation_embed)
                        return

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





    # SOLVE EQUATIONS
    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def equ_1(self, ctx, *, a):
        equ_1_embed = discord.Embed(
            title='Equation with 1 variable',
            color=discord.Color.blue(),

        )
        if len(str(a)) > 60:
            await ctx.send('```diff\n- Too long input. Please try again!\n```')
        else:
            try:
                a1 = a
                begin = a1.replace('=', '-(') + ')'

                begin = begin.replace('0x', '0*x')
                begin = begin.replace('2x', '2*x')
                begin = begin.replace('3x', '3*x')
                begin = begin.replace('4x', '4*x')
                begin = begin.replace('5x', '5*x')
                begin = begin.replace('6x', '6*x')
                begin = begin.replace('7x', '7*x')
                begin = begin.replace('8x', '8*x')
                begin = begin.replace('9x', '9*x')
                begin = begin.replace('10x', '10*x')
                begin = begin.replace('x(', 'x*(')
                begin = begin.replace(')x', ')*x')
                begin = begin.replace('pix', 'pi*x')
                begin = begin.replace('xpi', 'x*pi')

                c = begin.replace('^', '**')
                d = sp.solve(c)
                d1 = f'{d}nnn'

                if '[]' in d1:

                    de = simplify(c, evaluate=False)
                    de1 = sp.nsolve(de, 5)
                    equ_1_embed.add_field(name='Input', value=f'```\n{a1.replace(" ", "")}\n```', inline=False)
                    equ_1_embed.add_field(name='Output', value=f'```\n{de1}\n```', inline=False)

                    await ctx.send(embed=equ_1_embed)
                else:

                    equ_1_embed.add_field(name='Input', value=f'```\n{a1.replace(" ", "")}\n```', inline=False)
                    equ_1_embed.add_field(name='Output', value=f'```\n{d}\n```', inline=False)

                    await ctx.send(embed=equ_1_embed)
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
            except TypeError as TE:
                await ctx.send(f'```diff\n- ERROR : {TE}\n```')
                return


    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def equ_2(self, ctx, a1, b1, c1, a2, b2, c2):
        try:
            a1 = float(eval(str(a1)))
            b1 = float(eval(str(b1)))
            c1 = float(eval(str(c1)))
            a2 = float(eval(str(a2)))
            b2 = float(eval(str(b2)))
            c2 = float(eval(str(c2)))

            first = np.array([[a1, b1], [a2, b2]])
            second = np.array([c1, c2])
            result = np.linalg.solve(first, second)

            equ_2_embed = discord.Embed(
                title='Equation with 2 variables',
                color=discord.Color.blue(),

            )

            equ_2_embed.add_field(name='Input',
                                  value=f'```html\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}```',
                                  inline=False)
            equ_2_embed.add_field(name='Output', value=f'```css\n{result}\n```', inline=False)

            await ctx.send(embed=equ_2_embed)
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
        except np.linalg.LinAlgError as NLLE:
            await ctx.send(f'```diff\n- ERROR : {NLLE}\n```')


    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def equ_3(self, ctx, a1, b1, c1, d1, a2, b2, c2, d2,
                    a3, b3, c3, d3):
        try:
            a1 = float(eval(str(a1)))
            b1 = float(eval(str(b1)))
            c1 = float(eval(str(c1)))
            d1 = float(eval(str(d1)))

            a2 = float(eval(str(a2)))
            b2 = float(eval(str(b2)))
            c2 = float(eval(str(c2)))
            d2 = float(eval(str(d2)))

            a3 = float(eval(str(a3)))
            b3 = float(eval(str(b3)))
            c3 = float(eval(str(c3)))
            d3 = float(eval(str(d3)))
            first = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
            second = np.array([d1, d2, d3])
            result = np.linalg.solve(first, second)

            equ_3_embed = discord.Embed(
                title='Equation with 3 variables',
                color=discord.Color.blue(),

            )

            equ_3_embed.add_field(name='Input',
                                  value=f'```html\n{a1}x + {b1}y + {c1}z = {d1}\n{a2}x + {b2}y + {c2}z = {d2}\n{a3}x + {b3}y + {c3}z = {d3}\n```',
                                  inline=False)
            equ_3_embed.add_field(name='Output', value=f'```css\n{result}\n```', inline=False)

            await ctx.send(embed=equ_3_embed)

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
        except np.linalg.LinAlgError as NLLE:
            await ctx.send(f'```diff\n- ERROR : {NLLE}\n```')

            return


def setup(client):
    client.add_cog(Calculation(client))



