from cProfile import label
from pydoc import describe
from sqlite3 import Timestamp
from tkinter import Button
from urllib import response
import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord.ui import Button, View
import datetime, random ,asyncio,json

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

kic_name= ['Kick You!']
punch_name=['Punch You!']
hug_name=['Hug You!']
kiss_name=['Kiss You!','Kiss You❤️','Kiss You🥰']
bang_name=['Bang You!','Bang You! than You die...']

class Main(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg,):
        keyword=['🏚️ 地震報告','⚠️ 偵測到地震　@近即時震度 / P-Alert']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('\n切記 [趴下,掩護,穩住] 並且不要驚慌\n點擊這裡查案地震報告https://www.cwb.gov.tw/V8/C/E/index.html')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{ctx.author.mention}')
        await ctx.reply(f'{round(self.bot.latency*1000)} 毫秒(ms)')

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        embed=discord.Embed(title=f"{msg}", color=discord.Color.random())
        embed.set_footer(text=f"Commands sent by {ctx.author}", icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #@commands.Cog.listener()
    #async def on_message_delete(self, msg):
    #    embed=discord.Embed(title="`刪除訊息` "+str(msg.content), color=discord.Color.random())
    #    msg = await msg.author.send(embed=embed)

    @commands.command()
    async def search(self ,ctx, *,msg):
        await ctx.message.delete()
        embed=discord.Embed(
        title=f'`搜尋到的資料:`https://google.com/search?q={msg}', color=discord.Color.random()
        )   
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🔍')

    @commands.command()
    async def yt(self,ctx,*,msg):
        await ctx.message.delete()
        embed=discord.Embed(
            title=f"`搜尋到的youtube影片:`", description=f"https://www.youtube.com/results?search_query={msg}", color=discord.Color.random()
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('▶️')

    @commands.command(pass_context=True)
    async def omlets(self,ctx,*,msg):
        await ctx.message.delete()
        embed=discord.Embed(
        title=f'`搜尋到的玩家資料:\n`https://omlet.gg/profile/{msg}', color=discord.Color.random()
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🔍')

    @commands.command()
    async def gg(self, ctx):
        random_gg = random.choice(jdata['rd_gg'])
        embed=discord.Embed(title=f'你的GG: {random_gg}', color= discord.Color.random())
        await ctx.send(embed=embed)

    @commands.command()
    async def kic(self, ctx):
        kick = (jdata['kick_gif'])
        embed = discord.Embed(
            color=discord.Color.random(),
            description= f"{ctx.author.mention} {(random.choice(kic_name))}"
        )
        embed.set_image(url=(random.choice(kick)))
        await ctx.send(embed=embed)

    @commands.command()
    async def punch(self, ctx):
        kick = (jdata['punch_gif'])
        embed = discord.Embed(
            color=discord.Color.random(),
            description= f"{ctx.author.mention} {(random.choice(punch_name))}"
        )
        embed.set_image(url=(random.choice(kick)))
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx):
        kick = (jdata['hug_gif'])
        embed = discord.Embed(
            color=discord.Color.random(),
            description= f"{ctx.author.mention} {(random.choice(hug_name))}"
        )
        embed.set_image(url=(random.choice(kick)))
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx,member:discord.Member):
        kick = (jdata['kiss_gif'])
        
        embed = discord.Embed(
            color=discord.Color.random(),
            description= f"{ctx.author.mention} {(random.choice(kiss_name))}"
        )
        if member.bot:
            await ctx.send(f"{ctx.author.mention} 好可憐阿 你怎麼會想親機器人呢")
        else:
            embed.set_image(url=(random.choice(kick)))
            await ctx.send(embed=embed)

    @commands.command()
    async def bang(self, ctx):
        kick = (jdata['bang_gif'])
        embed = discord.Embed(
            color=discord.Color.random(),
            description= f"{ctx.author.mention} {(random.choice(bang_name))}"
        )
        embed.set_image(url=(random.choice(kick)))
        await ctx.send(embed=embed)

    @commands.command()
    async def confession(sefl, ctx, *, member:discord.Member):
        love=(jdata['love_gif'])
        author_name = ctx.message.author.name
        if member.bot:
            embed = discord.Embed(
            color=discord.Color.random(),
            description= f"{ctx.author.mention} 好可憐阿 你怎麼會機跟器人告白呢"
        )
            embed.set_image(url="https://memeprod.ap-south-1.linodeobjects.com/user-template-thumbnail/a4557da978e0b044ff8b52e3ba13505b.jpg")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"告白信💌")
            embed=discord.Embed(description=f"{author_name} 向你發起了告白! {member} \n\n {member}你的選擇是? ", color=discord.Color.random())
            embed.set_image(url=(random.choice(love)))
            await ctx.send(embed=embed)

    @commands.command()
    async def report(self, ctx, user : discord.Member, *reason):
        channel = self.bot.get_channel(956038030332952586) #since it's a cog u need self.bot
        author = ctx.message.author
        rearray = ' '.join(reason[:]) #converts reason argument array to string
        if not rearray: #what to do if there is no reason specified
            embed=discord.Embed(description=f"Report Player: {author}\nReported Member: {user}\nReason: Not provided", color=discord.Color.random())
            await ctx.send(embed=embed)
            await ctx.author.send(f"{author}\n{user}\n{rearray}")
            await ctx.message.delete() #I would get rid of the command input
        else:
            embed=discord.Embed(description=f"Report Player: {author}\nReported Member: {user}\nReason: {rearray}", color=discord.Color.random())
            await ctx.send(embed=embed)
            await ctx.author.send(f"{author}\n{user}\n{rearray}")
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(Main(bot))