import discord
import random
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
class React(Cog_Extension):

    @commands.command()
    async def meme(slef, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))