from msilib.schema import Component
from pydoc import describe
from sqlite3 import Timestamp
import discord,asyncio
from  itertools import cycle
from discord.ext import commands, tasks
from core.classes import Cog_Extension
import datetime, random ,json
from discord_components import Button, ButtonStyle, DiscordComponents 
    
with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='m/',help_command=None)

class Game(Cog_Extension):

    @commands.command()
    async def rd_num(self, ctx):
        random_num = random.choice(jdata['rd_num'])
        await ctx.send(f'{ctx.author.mention}')
        embed=discord.Embed(title=f"隨機數字抽獎機", description=f'0~20隨機抽出的數字是\n{random_num}', color= discord.Color.random())
        embed.set_footer(text=f"Commands sent by {ctx.author}", icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def luck(self, ctx):
        random_luck = random.choice(jdata['rd_luck'])
        random_number = random.choice(jdata['rd_number'])
        random_color = random.choice(jdata['rd_color'])
        random_clock = random.choice(jdata['rd_clock'])
        await ctx.send(f'{ctx.author.mention}')
        embed=discord.Embed(title=f'今日運勢: {random_luck}\n今日幸運數字: {random_number}\n今日幸運顏色: {random_color}\n今日良辰吉時: {random_clock}', description="", color= discord.Color.random())
        embed.set_footer(text=f"Commands sent by {ctx.author}", icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def rps(self ,ctx, message):
        answer = message.lower()
        choices = ["rock","paper","scissors"]
        computer_answer = random.choice(choices)
        if answer not in choices:
            await ctx.send(f"{ctx.author.mention}錯誤選項! 後面選項請填寫:rock, paper, scissors!")
            return
        else:
            if computer_answer == answer:
                await ctx.send(f"{ctx.author.mention}")
                embed=discord.Embed(title=f"平手! 我們都出了{answer}!", describe="", color=discord.Color.random())
                await ctx.send(embed=embed)
            #玩家win
            if computer_answer == "rock":
                if answer == "paper":
                    await ctx.send(f"{ctx.author.mention}")
                    embed=discord.Embed(title=f"你贏了! 我出了{computer_answer} 你則出了 {answer}", describe="", color=discord.Color.random())
                    await ctx.send(embed=embed)
            if computer_answer == "scissors":
                if answer == "rock":
                    await ctx.send(f"{ctx.author.mention}")
                    embed=discord.Embed(title=f"你贏了! 我出了{computer_answer} 你則出了 {answer}", describe="", color=discord.Color.random())
                    await ctx.send(embed=embed)
            if computer_answer == "paper":
                if answer == "scissors":
                    await ctx.send(f"{ctx.author.mention}")
                    embed=discord.Embed(title=f"你贏了! 我出了{computer_answer} 你則出了 {answer}", describe="", color=discord.Color.random())
                    await ctx.send(embed=embed)
            #機器人win
            if computer_answer == "rock":
                if answer == "scissors":
                    await ctx.send(f'{ctx.author.mention}')
                    embed=discord.Embed(title=f"我贏了! 我出了{computer_answer} 你則出了 {answer}所以輸了!", describe="", color=discord.Color.random())
                    await ctx.send(embed=embed)
            if computer_answer == "scissors":
                if answer == "paper":
                    await ctx.send(f'{ctx.author.mention}')
                    embed=discord.Embed(title=f"我贏了! 我出了{computer_answer} 你則出了 {answer}所以輸了!", describe="", color=discord.Color.random())
                    await ctx.send(embed=embed)
            if computer_answer == "paper":
                if answer == "rock":
                    await ctx.send(f'{ctx.author.mention}')
                    embed=discord.Embed(title=f"我贏了! 我出了{computer_answer} 你則出了 {answer}所以輸了!", describe="", color=discord.Color.random())
                    await ctx.send(embed=embed)

    @commands.command(aliases = ["8ball"])
    async def ball(self, ctx):
        possible_responses = (jdata['8ball'])

        embed=discord.Embed(title=random.choice(possible_responses) ,description=ctx.message.author.mention,color=discord.Color.random())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Game(bot))