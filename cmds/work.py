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

class Work(Cog_Extension):

    @commands.command()
    async def jobs(self, ctx):
        with open('jobs.json','r') as f:
            jobslist = json.load(f)

        embed= discord.Embed(title="JOBS")

        for job in jobslist:
            embed.add_field(name=f"{jobslist[job]['emoji']} {job.title()}", value=f"{jobslist[job]['description']}\n**Salary** - {jobslist[job]['salary']}\n**Work Required** - {jobslist[job]['work_required']}")
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Work(bot))