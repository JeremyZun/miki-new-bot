from ast import keyword
from http.client import OK
from pydoc import describe
from turtle import color, title
from typing import Counter
from unittest import async_case
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, random

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['安安','嗨嗨','安','嗨','Hi','hi',]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send(f'{msg.author.mention}hello阿')
        keyword = ['xd','XD','Xd','xD']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('https://pic.pimg.tw/kiafming8/1410003355-2714536248.png')
        keyword = ['<@970212024099426346>']
        if msg.content in keyword and msg.author != self.bot.user:
            random_tag = random.choice(jdata['rd_tag'])
            embed=discord.Embed(title=f"{random_tag}", describe='', color=discord.Color.random())
            await msg.channel.send(embed=embed)
        keyword = ["lol","LOL",'Lol','loL','lOL','Lol']
        if msg.content in keyword and msg.author != self.bot.user:
            random_lol = random.choice(jdata['rd_lol'])
            await msg.channel.send(random_lol)
        keyword = ['fkq','FKQ','fuckyou','Fuckyou','Fk','Fkq','fk']
        if msg.content in keyword and msg.author != self.bot.user:
            random_fk = random.choice(jdata['rd_fk'])
            await msg.channel.send(f"{msg.author.mention}")
            await msg.channel.send(random_fk)
        keyword = ['miki大ㄐㄐ的按 ✅  miki沒ㄐㄐ的按 ❎']    
        if msg.content in keyword and msg.author:
            await msg.add_reaction('☑️')
            await msg.add_reaction('✅')


    @commands.group()
    async def game(self,ctx):
        pass

    @game.command()
    async def rd_num(self,ctx):
        embed=discord.Embed(title=f"小遊戲🎲", description=f"rd_num", color=discord.Color.random())
        await ctx.send(embed=embed)

    @game.command()
    async def luck(self,ctx):
        embed=discord.Embed(title=f"小遊戲🎰", description=f"luck", color=discord.Color.random())
        await ctx.send(embed=embed)

    @game.command()
    async def rps(self,ctx):
        embed=discord.Embed(title=f"小遊戲✌️✊🤚", description=f"rps [rock,paper,scissors]", color=discord.Color.random())
        await ctx.send(embed=embed)

    @game.command()
    async def ooxx(self, ctx):
        embed=discord.Embed(title=f"小遊戲⭕⭕❌❌",
        description=f"ooxx [@player1, @player2]\n⚠️注意事項⚠️\n遊戲若未結束則無法下局!", color=discord.Color.random())
        await ctx.send(embed=embed)

    @commands.group()
    async def member(self,ctx):
        pass

    @member.command()
    async def ping(self,ctx):
        embed=discord.Embed(title=f"ping📶 [查看BOT延遲]", description=f"ping", color=discord.Color.random())
        await ctx.send(embed=embed)

    @member.command()
    async def omlets(self,ctx):
        embed=discord.Embed(title=f"omlets🔍 [搜尋OM玩家ID]", description=f"omlets", color=discord.Color.random())
        await ctx.send(embed=embed)

    @member.command()
    async def now(self,ctx):
        embed=discord.Embed(title=f"now🕰️ [現在時間]", description=f"now", color=discord.Color.random())
        await ctx.send(embed=embed)

    @member.command()
    async def search(self,ctx):
        embed=discord.Embed(title=f"search🔍 [在google上搜尋]", description=f"search", color=discord.Color.random())
        await ctx.send(embed=embed)

    @member.command()
    async def say(self,ctx):
        embed=discord.Embed(title=f"say🗣️ [需權限]", description=f"say", color=discord.Color.random())
        await ctx.send(embed=embed)

    @commands.group()
    async def owner(self, ctx):
        pass

    @owner.command()
    async def clean(self, ctx):
        embed=discord.Embed(title=f"clean🧹 [需高權限]", description=f"clean", color=discord.Color.random())
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Event(bot))