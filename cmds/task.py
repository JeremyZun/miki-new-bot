from typing_extensions import Self
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio , datetime, random

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.counter = 0

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(874954099647451169)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json','r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter == 0:
                    embed=discord.Embed(title="test!", description=f"@everyone ", color=discord.Color.random())
                    await self.channel.send(embed=embed)
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
                
        self.bg_task = self.bot.loop.create_task(time_task())
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.counter = 0

        async def time_task1():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(874954099647451169)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json','r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time1'] and self.counter == 0:
                    embed=discord.Embed(title="各位早八了!工作起來!", description=f"@everyone ", color=discord.Color.random())
                    await self.channel.send(embed=embed)
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
                
        self.bg_task = self.bot.loop.create_task(time_task1())

    @commands.command()
    async def set_channel(self, ctx , ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(F'Set Channel :{self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        with open('setting.json','r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json','w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.send('`設定成功!`')
    @commands.command()
    async def set_time1(self, ctx, time):
        self.counter = 0
        with open('setting.json','r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time1'] = time
        with open('setting.json','w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.send('`設定成功!`')



def setup(bot):
    bot.add_cog(Task(bot))