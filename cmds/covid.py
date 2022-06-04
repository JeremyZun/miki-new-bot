import discord
import asyncio
import requests
from discord.ext import commands


class covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def covid(self, ctx, *, countryName = None):
        try:
            if countryName is None:
                embed=discord.Embed(title="該指令使用格式/方式: ```m/covid [country]```", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)


            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]

                embed2 = discord.Embed(title=f"**COVID-19 Status Of {country}**!", description="此信息並非始終存在，因此可能不准確!", colour=0x0000ff, timestamp=ctx.message.created_at)
                embed2.add_field(name="**確診案件總數**", value=totalCases, inline=True)
                embed2.add_field(name="**今日確診人數**", value=todayCases, inline=True)
                embed2.add_field(name="**累計死亡人數**", value=totalDeaths, inline=True)
                embed2.add_field(name="**今日死亡人數**", value=todayDeaths, inline=True)
                embed2.add_field(name="**康復人數**", value=recovered, inline=True)
                embed2.add_field(name="**活躍度**", value=active, inline=True)
                embed2.add_field(name="**病況危急[重症]**", value=critical, inline=True)
                embed2.add_field(name="**每百萬例**", value=casesPerOneMillion, inline=True)
                embed2.add_field(name="**每百萬人的死亡人數**", value=deathsPerOneMillion, inline=True)
                #embed2.add_field(name="**Total Tests**", value=totalTests, inline=True)
                #embed2.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=True)

                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
                embed2.set_footer(text=f"Commands sent by {ctx.author}", icon_url= ctx.author.avatar_url)
                await ctx.send(embed=embed2)

        except:
            embed3 = discord.Embed(title="輸入 國家 名稱錯誤 請再次輸入!", colour=0xFF0000, timestamp=ctx.message.created_at)
            embed3.set_author(name="錯誤! Error!")
            await ctx.send(embed=embed3)

def setup(bot):
    bot.add_cog(covid(bot))