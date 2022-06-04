from cProfile import label
from email.mime import application
from lib2to3.pgen2.token import TILDE
from multiprocessing import managers
from pydoc import describe
from sqlite3 import Timestamp
from tkinter import Button
from tkinter.ttk import Style
from turtle import color, tilt, title, update
from unicodedata import name
from unittest import async_case
from urllib.parse import urlencode
from certifi import contents
from time import sleep
import discord, random , os, json , nextcord, datetime, asyncio ,aiosqlite
from discord.ext.commands import has_permissions, MissingPermissions
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import discord.ext.commands as commands
from discord import Permissions, Role, RoleTags, member
from discord.ext import commands, tasks
from discord import Client, Emoji, Intents, Embed
from discord import VoiceChannel
from discord_components import Button, ComponentsBot, SelectOption, Select

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='m/',help_command=None)


mainshop = (jdata['mainshop'])
@bot.event
async def on_ready():
    

    print(">> Bot Is Online! <<") 
    
    await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)} servers"))

async def ch_pr():
    await bot.wait_until_ready()

    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    statuese = [f" {len(bot.guilds)} servers 🥰", f" {members} members ❤️", "m/help 👋", f"This Is miki BOT"]

    while not bot.is_closed():

        status = random.choice(statuese)

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching ,name=status))

        await asyncio.sleep(3)

bot.loop.create_task(ch_pr())

#streaming Activity.
#discord.Streaming(name="stream name", url="stream url")
# Gaming Activity.
#discord.Game("Name of the Game")
#listening Activity
#discord.Activity(type=discord.ActivityType.listening, name="name of the music")
#watching Activity
#discord.Activity(type=discord.ActivityType.watching, name="name of the movie")

#level system
with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json','r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
      f.write("{}")
      f.close()
    else:
      pass
 
with open('users.json', 'r') as f:
  users = json.load(f)
 
@bot.event    
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_experience(users, message.author)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f)
            await bot.process_commands(message)

 
async def add_experience(users, user):
  if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0
  users[f'{user.id}']['experience'] += 5
  print(f"{users[f'{user.id}']['level']}")
 
async def level_up(users, user, message):
  experience = users[f'{user.id}']["experience"]
  lvl_start = users[f'{user.id}']["level"]
  lvl_end = int(experience ** (1 / 4))
  if lvl_start < lvl_end:
    await message.author.send(f':tada: 恭喜你! 升級到了{lvl_end}等! :tada:')
    users[f'{user.id}']["level"] = lvl_end
 
@bot.command(pass_context=True)
async def rank(ctx, member: discord.Member = None):
  if member == None:
    userlvl = users[f'{ctx.author.id}']['level']
    embed=discord.Embed(title=f"你現在等級是 {userlvl} 等! ", description=ctx.message.author.mention, color= discord.Color.random(), timestamp=ctx.message.created_at)
    await ctx.send(embed=embed)
  else:
    userlvl2 = users[f'{member.id}']['level']
    await ctx.send(f'{member.mention} 現在等級在 {userlvl2}!')

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="機器人指令/BOT COMMANDS", description="以下指令皆m/開頭\n作者OM資訊 OMID:miki_come_back", color= discord.Color.random(), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/853089010511904798/970261648088653864/1_20220501175121.png")
    embed.add_field(name="🎁member", value="\n[`ping`, `now`, `say`, `omlets`, `search`]", inline=True)
    embed.add_field(name="🎁owner", value="\n[`clean`]", inline=True)
    embed.add_field(name="🎁Level", value="\n[`rank`]", inline=True)
    embed.add_field(name="🎁game", value="\n[`rd_num`, `luck`, `rps`, `ooxx`]", inline=True)
    embed.add_field(name="🎁放鬆/趣味", value="\n[`meme`,`punch`,`kic`,`bang`]", inline=True)
    embed.add_field(name="🎁互動", value="\n[`hug`,`kiss`,`kic`,`punch`,`bang`,`confession`]")
    embed.add_field(name="🦠COVID資訊", value="\n`covid [城市/國家]`", inline=True)
    embed.add_field(name="🎁查看伺服器資訊", value="\n`server`", inline=True)
    embed.add_field(name="🪙金錢系統", value="\n[`**daily**`,`money`,`shop`,`putbank`,`draw`,`slots`,`buy`,`bag`]", inline=True)
    embed.set_footer(text=f"Commands sent by {ctx.author}", icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


    @bot.command(name='8ball',
            description="Answers a yes/no question.",
            brief="Answers from the beyond.",
            aliases=['eight_ball', 'eightball', '8-ball'],
            pass_context=True)

    async def eight_ball(context):
        possible_responses = [

            'That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
            'Maybe so.'

    ]
        await context.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'`Loaded {extension} done.`')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'`Un - Loaded {extension} done.`')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'`RE - Loaded {extension} done.`')

#現在時刻
def gettime():
    x = datetime.datetime.now()
    err = datetime.timedelta(hours=0)
    x += err
    y = x.year
    m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
         'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][x.month - 1]
    d = x.day
    h = x.hour
    mi = x.minute
    s = x.second
    w = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][(x.weekday() + 1) % 7]
    res = '{} {} {:02d} {:02d}:{:02d}:{:02d} {}'.format(w, m, d, h, mi, s, y)
    return res

@bot.command()
async def now(ctx):
    await ctx.send(gettime())

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title=f"錯誤指令! 請輸入m/help取得更多資訊\nError Commands! Please type m/help get more Information!", color=discord.Color.random())
        await ctx.send(embed=embed)

#@bot.command()
#@commands.has_permissions(kick_members=True)
#async def kick(ctx, member:discord.Member , *, reason=None):
#    guild = ctx.guild
#    await member.kick(reason=reason)
#    embed = discord.Embed(title=f"{member} was kicked!\n Reason: {reason}", color=discord.Color.random())
#    await ctx.send(embed=embed)
#    await member.send(f" you have been kicked from: {ctx.guild.name} reason: {reason}")


@bot.command() #kick
@commands.has_permissions(manage_messages=True)
async def kick (ctx, member:discord.User=None, reason =None):
 try:
    if (reason == None):
        await ctx.channel.send("You  have to specify a reason!")
        return
    if (member == ctx.message.author or member == None):
        await ctx.send("""You cannot kick yourself!""") 

    message = f"You have been kicked from `{ctx.guild.name}` Reason: `{reason}`"
    await member.send(message)
    await ctx.guild.kick(member, reason=reason)
    print(member)
    print(reason)
    embed = discord.Embed(title="Kick Information", description=f"Kicked Member: {member}\n Reason: {reason}", color=discord.colour.red(), timestamp=ctx.message.created_at)
    await ctx.channel.send(embed=embed)
 except:
    await ctx.send(f"Error kicking user {member} (cannot kick owner or bot)")

@bot.command()
@commands.has_permissions(ban_members=True)
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    embed = discord.Embed(title=f"{member} was banned!\n Reason: {reason}", color=discord.Color.random())
    await ctx.send(embed=embed)
    user = ctx.message.author
    await user.send(f'Reason: {reason}')
    await user.send(reason=reason)

@bot.command()
@commands.has_permissions(ban_members=True)
@commands.has_permissions(manage_messages=True)
async def unban(ctx,* ,member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split('#')

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title=f"{member} was unbanned!", color=discord.Color.random())
            await ctx.send(embed=embed)
            return

@bot.command(description="Gets info about the user")
async def userinfo(ctx):
    user = ctx.author

    embed=discord.Embed(title="USER INFO", description=f"Here is the info we retrieved about {user}", colour=user.colour)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="NAME", value=user.name, inline=True)
    embed.add_field(name="NICKNAME", value=user.nick, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="STATUS", value=user.status, inline=True)
    embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx,*, num :int):
    if has_permissions(manage_messages=True):
        await ctx.channel.purge(limit=num+1)
        print(F'`Already Delete {num} Message!`') 
    else:
        await ctx.send(f'{ctx.author.mention} ❌ | 你未擁有此權限使用')

@bot.command(pass_context=True)
async def server(ctx, guild:discord.guild = None):
    guild = ctx.guild if not guild else guild
    embed = discord.Embed(title=f"Server Info {guild}", color=discord.Color.random(), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=guild.icon_url)    
    embed.add_field(name="`**Description:**`", value=guild.description ,inline=False)
    embed.add_field(name="`**Channel Count:**`", value=len(guild.channels) ,inline=False)
    embed.add_field(name="`**Roles Count:**`", value=len(guild.roles) ,inline=False)
    embed.add_field(name="`**Members Count:**`", value=guild.member_count ,inline=False)
    embed.add_field(name="`**Server Created At:**`", value=guild.created_at ,inline=False)
    embed.add_field(name="`**Max Emoji**`", value=guild.emoji_limit ,inline=False)
    embed.set_footer(text=f"Commands sent by {ctx.author}", icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def ooxx(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver
    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            myEmbed = discord.Embed(title= "遊戲進行中",description="現在是 <@" + str(player1.id) + "> 的回合.",color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        elif num == 2:
            turn = player2
            myEmbed = discord.Embed(title= "遊戲進行中",description="現在是 <@" + str(player2.id) + "> 的回合.",color=0xe74c3c)
            await ctx.send(embed=myEmbed)
    else:
        myEmbed = discord.Embed(title= "遊戲進行中",description="遊戲仍在進行中! 在開始一個新的之前完成它",color=0xe74c3c)
        await ctx.send(embed=myEmbed)

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    myEmbed = discord.Embed(title= "WINNER!",description=mark + " :crown: ",color=0xf1c40f)
                    await ctx.send(embed=myEmbed)
                elif count >= 9:
                    gameOver = True
                    myEmbed = discord.Embed(title= "平手",description="這是局平局! :handshake:",color=0xf1c40f)
                    await ctx.send(embed=myEmbed)

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                myEmbed = discord.Embed(title= "放置錯誤!",description="請務必選擇 1 到 9 之間的整數和未選取的白磚。 ",color=0xe74c3c)
                await ctx.send(embed=myEmbed)
        else:
            myEmbed = discord.Embed(title= "回合錯誤!",description=" 現在不是你的回合!",color=0xe74c3c)
            await ctx.send(embed=myEmbed)
    else:
        myEmbed = discord.Embed(title= "開始遊戲",description="開始新的一局, 使用 -tictactoe 指令",color=0x2ecc71)
        await ctx.send(embed=myEmbed)


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@ooxx.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = discord.Embed(title= "tag錯誤!",description="請tag兩個玩家",color=0xe74c3c)
        await ctx.send(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = discord.Embed(title= "錯誤!",description="請一定要tag玩家!",color=0xe74c3c)
        await ctx.send(embed=myEmbed)

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = discord.Embed(title= "沒有位置",description="請輸入要標記的位置",color=0xe74c3c)
        await ctx.send(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = discord.Embed(title= "錯誤整數!",description="請確認它是一個整數",color=0xe74c3c)
        await ctx.send(embed=myEmbed)

#coins
@bot.command()
async def money(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f"{ctx.author.name}'s blance", color=discord.Color.random())
    em.add_field(name="Wallet 🪙", value=wallet_amt)
    em.add_field(name="Bank 🏦", value=bank_amt)
    await ctx.send(embed= em)

#beg
@bot.command()
@commands.has_permissions(manage_messages=True)
async def givecoins(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(10001)

    if has_permissions(manage_messages=True):
        em = discord.Embed(description=f"{ctx.author.mention} Someone Gave you {earnings} Coins!",color=discord.Color.random())
        await ctx.send(embed=em)

        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump(users,f)
    else:
        await ctx.send(f"{ctx.author.mention} 你沒有權限")

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(11,151)

    has_permissions(manage_messages=True)
    em = discord.Embed(description=f"{ctx.author.mention} Someone Gave you {earnings} Coins!",color=discord.Color.random())
    await ctx.send(embed=em)

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)


#draw
@bot.command()
async def draw(ctx,amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("請輸入金額")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("你沒有那麼多錢!")
        return
    if amount<0:
        await ctx.send("數量必須是正數!")
        return    

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1*amount, "bank")

    await ctx.send(f"You withdrew {amount} coins!")

#shop
@bot.command()
async def shop(ctx):
    em = discord.Embed(title="Shop",color=discord.Color.random())

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name= name, value = f"${price} | {desc}")

    await ctx.send(embed=em)

#buy
@bot.command()
async def buy(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("The Object ins't here")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount}")
            return

    await ctx.send(f"You just bought {amount} {item}")

#buy_this
async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            obj = {"item":item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name, "amount":amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1, "wallet")

    return [True,"Worked"]

#sell
@bot.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount,0)

    if not res[0]:
        if res[1]==1:
            em=discord.Embed(description=f"That Obhect isn't there!", color=discord.Color.random())
            await ctx.send(embed=em)
            return
        if res[1]==2:
            em=discord.Embed(description=f"You don't have {amount} {item} in your bag!", color=discord.Color.random())
            await ctx.send(embed=em)
            return
        if res[1]==3:
            em=discord.Embed(description=f"You don't have {item} in your bag!", color=discord.Color.random())
            await ctx.send(embed=em)
            return

    em=discord.Embed(title=f"You just sold {amount} {item}.", color=discord.Color.random())
    await ctx.send(embed=em)

#sell_this
async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 1*item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            return [False,3]
    except:
        return [False,3]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost, "wallet")

    return [True,"Worked"]

#leadboard
@bot.command(aliases = ["lb"])
async def leaderboard(ctx, x=10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)
      
    total = sorted(total, reverse=True)    

    em = discord.Embed(title = f"🪙 Top {x} Richest People 🪙", description = "This is decided on the basis of raw money in the bank and wallet", color = discord.Color(0xfa43ee))
    
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = await bot.fetch_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}", value = f"{amt} 🪙", inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

#bag
@bot.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title="inventory", color=discord.Color.random())
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)

#open_account
async def open_account(user):
    with open("mainbank.json","r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False

    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"]=0
        users[str(user.id)]["bank"]=0

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)

    return users

#putbank
@bot.command()
async def putbank(ctx,amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("請輸入數量")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("你沒有那麼多錢!")
        return
    if amount<0:
        await ctx.send("數量必須是正數!")
        return    

    await update_bank(ctx.author, -1*amount)
    await update_bank(ctx.author, amount, "bank")

    await ctx.send(f"You deposited {amount} coins!")

#send
@bot.command()
async def send(ctx, member:discord.Member,amount=None):
    await open_account(ctx.author)
    await open_account(member)


    if amount == None:
        await ctx.send("請輸入數量")
        return

    bal = await update_bank(ctx.author)
    if amount == "all":
        amount = bal[0]

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("你沒有那麼多錢!")
        return
    if amount<0:
        await ctx.send("數量必須是正數!")
        return    

    await update_bank(ctx.author, -1*amount, "bank")
    await update_bank(member, amount, "bank")

    em=discord.Embed(description=f"You give {member} {amount} coins!", color=discord.Color.random())
    await ctx.send(embed=em)

#rob
@bot.command()
async def rob(ctx, member:discord.Member):
    await open_account(ctx.author)
    await open_account(member)

    bal = await update_bank(member)

    if bal[0]<1000:
        await ctx.send("It's not worth it!")
        return

    earnings = random.randrange(0, bal[0])

    await update_bank(ctx.author, earnings)
    await update_bank(member, -1*earnings)

    embed=discord.Embed(title=f"You robbed and got {earnings} coins!",color=discord.colour.red())
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.reply(f"Please wait {round(error.retry_after, 2)} seconds than use Command!")

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def test(ctx):
	await ctx.send("test work")

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def work(ctx):
    random_num = random.choice(jdata['rd_num'])
    await ctx.send(f'{ctx.author.mention}')
    embed=discord.Embed(title=f"隨機數字抽獎機", description=f'0~20隨機抽出的數字是\n{random_num}', color= discord.Color.random())
    embed.set_footer(text=f"Commands sent by {ctx.author}", icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)

#slots
@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def slots(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("請輸入數量")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        embed=discord.Embed(description=f"{ctx.author.mention} 你沒有那麼多錢!",color=discord.Color.random())
        await ctx.send(embed=embed)
        return
    if amount<0:
        embed=discord.Embed(description=f"{ctx.author.mention} 數量必須是正數!!!",color=discord.Color.random())
        await ctx.send(embed=embed)
        return    

    final = []
    for i in range(3):
        a = random.choice(["X","O","Q"])

        final.append(a)
    
    await ctx.send(str(final))

    if amount<=69:
        if final[0] == final[1] or final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await update_bank(ctx.author, 2*amount)
            embed=discord.Embed(title="You Won!!!",description=f"{ctx.author.mention}",color=discord.Color.random())
            await ctx.send(embed=embed)
        else:
            await update_bank(ctx.author, -3*amount)
            embed=discord.Embed(title=f"You Lost!!!",description=f"{ctx.author.mention}",color=discord.Color.random())
            await ctx.send(embed=embed)
    else:
        em = discord.Embed(description=f"{ctx.author.mention} 你超過固定金額 上限69 coins!", color=discord.Color.random())
        await ctx.send(embed=em)

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
@commands.has_any_role('owner')
async def rdplayer(ctx, number):
    try:
        arg = random.randint(1, int(number))
    except ValueError:
        await ctx.send("Invalid number")
    else:
        await ctx.send(f"@everyone")
        embed=discord.Embed(title=f"🎁本次抽獎抽出的數字是🎁",description=str(arg),color=discord.Color.random())
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.has_any_role('owner')
async def giveway(ctx, mins:int , *, prize:str):
    embed = discord.Embed(title="Giveway!", description= f"{prize}", color=ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=mins*60)

    embed.add_field(name="Ends At:", value=f"{end} UTC")
    embed.set_footer(text=f"Ends {mins} mintues from now! (UTC+10hr)")

    my_msg = await ctx.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def dm(ctx, user: discord.User,*, message=None):
    if message == None:
      message = "Hi!"
    embed = discord.Embed(title=f"Sent to {user}", description=message, color=discord.Color.random(), timestamp=ctx.message.created_at)
    await user.send(embed=embed)
    await ctx.channel.purge(limit=1)
    await ctx.send("Message sent!")
    print (f"{user} send {message}")

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def start(ctx):
    with open("work.json","r") as f:
        data = json.load(f)

    data[str(ctx.author.id)] = {}
    data[str(ctx.author.id)]["bank"] = 1000
    data[str(ctx.author.id)]["job"] = "none"
    data[str(ctx.author.id)]["experience"] = 1000
    data[str(ctx.author.id)]["incentory"] = []

    with open("work.json","w") as f:
        json.dump(data, f, indent=4)

    await ctx.reply(f"")


if __name__ == "__main__":
    bot.run(os.environ["OTcwMjEyMDI0MDk5NDI2MzQ2.Gdv5-Q.KoJhd-ZaLIfVFUznTUBHvddXkqFoz3Xb5chptg"])

