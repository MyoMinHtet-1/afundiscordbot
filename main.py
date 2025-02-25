import discord 
import os
import random 
from discord.ext import commands
import json 
from webserver import keep_alive
from discord.utils import get
import asyncio
import platform
from discord.ext.commands import CommandNotFound
bot = commands.Bot(command_prefix="^",  case_insensitive=True, owner_id = 1234) 
def read_json(files):
    with open("quotes.json", "r") as file:
        data = json.load(file)
    return data


def write_json(data, filename): 
    with open(f"{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

point = 0 
index = 0 
highest = 0
kss = []
data = read_json("quotes")
kss = data["quotes"]
data = read_json('quotes')
thumbsup = "👍"

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    await bot.change_presence(activity=discord.Game(name=f"Hi, my names {bot.user.name}.\nUse '^' to interact with me!")) # This changes the bots 'activity'


@bot.command(name = "hi", aliases = ['hello'])
async def _greeting(ctx):
    """
    it will greet u back
    """ 
    await ctx.send("hi, user")

@bot.command(aliases=['disconnect', 'close', 'stopbot'])
@commands.is_owner()
async def logout(ctx):
    """
    If the user running the command owns the bot then this will disconnect the bot from discord.
    """
    await ctx.send(f"Hey {ctx.author.mention}, I am now logging out")
    await bot.logout()

@bot.command(name = 'addquote', aliases = ['addquotes'])
async def add_quote(ctx, *, message= None):
    '''
    ^addquote: add your own quote to the database
    '''
    message = message or "type the command again with the message"
    if ctx.author == bot.user:
        return
    kss.append(message)
    data = read_json("quotes")
    data["quotes"].append(message)
    write_json(data, "quotes")
    await ctx.send("it is added successfully to the data basse  ")

@bot.command(name = 'addjoke', aliases = ['joke'])
async def add_urmom(ctx, *, message = None):
    
    ^addurmom: add ur own ur mom jokes to the database

    message = message or "type the command again with the message"
    await ctx.send(indianman)
    if ctx.author == bot.user:
        return
    urmom.append(message  
    data = read_json("quotes")
    data["urom"].append(message)
    write_json(data, "quotes")


@bot.command(aliases= ["quotes", "quote"])
async def sendquote(ctx):
    '''
    randomizes all the quotes in the database
    '''
    with open(f"quotes.json", "r") as files:
        data = json.load(files)
        await ctx.send(random.choice(data.get("quotes")))

@bot.command(name = "urmom")
async def sendurmom(ctx):
    '''
    randomizes all the quotes in the database
    '''
    with open(f"quotes.json", "r") as files:
        data = json.load(files)
        await ctx.send(random.choice(data.get("")))

@bot.command(name = "memes") #send reddit memes
async def sendmemes(ctx):
    with open(f"memes.json", "r") as files:
        data = json.load(files) 
        data1 = data.get("url")
        data2 = data.get("memes")
        data3 = data.get("memesupvotes")
        rand = random.randint(1, 989)
        name = data2[rand]
        url = data1[rand]
        upvotes = data3[rand]
        em_new = discord.Embed(title=name)
        em_new.set_image(url=url)
        em_new.set_footer(text=f"⬆ {upvotes}")
        await ctx.send(embed=em_new)

@bot.command(name = "deepmemes")
async def senddeepmemes(ctx):
    with open(f"memes.json", "r") as files:
        data = json.load(files) 
        data1 = data.get("deepmemesurl")
        data2 = data.get("deepmemes")
        data3 = data.get("deepmemesupvotes")
        rand = random.randint(1, 967)
        name = data2[rand]
        url = data1[rand]
        upvotes = data3[rand]
        em_new = discord.Embed(title=name)
        em_new.set_image(url=url)
        em_new.set_footer(text=f"⬆ {upvotes}")
        await ctx.send(embed=em_new)
        
        
@bot.command(name = "ihadastroke")
async def sendstrokememes(ctx):
        with open(f"memes.json", "r") as files:
            data = json.load(files) 
            data1 = data.get("ihadastrokeurl")
            data2 = data.get("ihadastroke")
            data3 = data.get("strokeupvotes")
            rand = random.randint(1, 967)
            name = data2[rand]
            url = data1[rand]
            upvotes = data3[rand]
            em_new = discord.Embed(title=name)
            em_new.set_image(url=url)
            em_new.set_footer(text=f"⬆ {upvotes}")
            await ctx.send(embed=em_new)

@bot.command(name = "flips", aliases = ['flip'])
async def fliprandom(ctx, *, message = None):
  choices = ['head', 'tail']
  await ctx.send(f"{ctx.message.author.mention} {random.choice(choices)}")

@bot.command(name = 'retard', aliases = ['nigga', "n1gga", 'faggot', 'fagg0t'])
async def eggy(ctx):
  await ctx.reply('Do not write a message including slurs', mention_author=False)
  
@bot.command(name = "findquote")
async def find_quote(ctx, *, message = None):
  with open(f"quotes.json", "r") as files:
    data = json.load(files)
    data = data.get('quotes')
    num = len(data)
    message = message or 'add a quote'
    point = 0 
    index = 0 
    highest = 0
    highestchar = []
    message = message.split()
    previous = ''
    indexnum = len(data)
    while index != indexnum:  
        indexlist = data[index]
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        # Removing punctuations in string
        # Using loop + punctuation string
        for ele in indexlist: 
          if ele in punc: 
            indexlist = indexlist.replace(ele, " ") 
            indexlist = indexlist.lower()
        indexlist = indexlist.split()
        for e in indexlist:
            for a in message:
                if e == a: 
                    point += 1
                else: 
                    pass
        if point > 0: 
          if point == highest:
            highestchar.append(data[index]) 
        if point > highest: 
            highest = point
            highestchar.append(data[index])

        previous = indexlist
        point = 0
        index += 1
    num2 = 0
    if len(highestchar) != 0:
      if len(highestchar) > 1:
        num2 = 1
      highestchar_for_text = highestchar
      highestchar = ', '.join(map(str, highestchar))
      emb = discord.Embed(title = 'Extracted quotes', description = f"This is the closest we can find {highestchar}")
      if num2 == 1:
        emb.add_field(name = 'There are more than 1 quotes found from the keyword. To remove one of the quote, copy paste the quote with ^removequote command.', value=f"Example = ^removequote {random.choice(highestchar_for_text)}", inline=False)
      elif num2 == 0:
        emb.add_field(name= "to remove a quote You do ^removequote 'quote", value = f"^removequote example", inline=False)
      await ctx.send(embed = emb)
    if len(highestchar) == 0:
        emb = discord.Embed(title = 'Extracted quotes', description = f"Sorry, we can't find any quotes containting {message}")
        await ctx.send(embed = emb)

#removing jokes or funny quotes from the database using a voting system
@bot.command(name = "removequote")
async def remove_quote(ctx, *, message = None):
  with open(f"quotes.json", "r") as files:
    with open(f"quptes.json", "w") as writefiles:
      data = json.load(files)
      data = data.get('quotes')
      message = message
      if message == "":
        await ctx.send("Add a quote when you ^removequote")
      elif message in data:
        identity = discord.Embed(title = f"This is the quote that you are going to delete {message}")
        identity.add_field(name = "If this is an accident, you can just leave it as it is.", value = 'react with 👍 to vote.', inline=False)
        identity = await ctx.send(embed = identity)
        print(identity.id)
        msg_id = identity.id
        await asyncio.sleep(30)
        msg = await ctx.channel.fetch_message(msg_id)
        try:
          reaction = get(msg.reactions, emoji = '👍')
          print(reaction.count)
        except AttributeError:
          await ctx.send("There were no reaction or the reaction wasn't a thumbs up or down so the poll will be discarded")
        if reaction.count > 0:
          emb = discord.Embed(name = f'POLL')
          emb.add_field(name = f"Do you want {message} to be removed?", value = '👍 - remove ----   👎 - to not remove', inline=False)
          botpolls = bot.get_channel(846681703057588295)
          emb_id = await botpolls.send(embed = emb)
          msg_id = emb_id.id
          msg_id = botpolls.fetch_message(msg_id)
          await emb_id.add_reaction("👍")
          await emb_id.add_reaction("👎")
          msg_id = emb_id.id
          print(msg_id)
          await asyncio.sleep(30)
          msg = await botpolls.fetch_message(msg_id)
          bad_reaction = get(msg.reactions, emoji = "👎")
          num_bad_reaction = bad_reaction.count
          num_bad_reaction -= 1 
          reaction = get(msg.reactions, emoji = '👍')
          num_reaction = reaction.count
          num_reaction -=1
          print(bad_reaction,'this is thumbs down')
          print("this is thumbsup" , reaction)
          if reaction == 0 and bad_reaction == 0:
            await botpolls.send("There were no reaction or the reaction wasn't a thumbs up or down so the poll will be discarded")
          if num_bad_reaction > num_reaction:
            print("👎 is more than 👍 \n So the quote won't be deleted")
          elif num_reaction > num_bad_reaction:
            print("👍 is more than 👎 \n the quote will be deleted")
            kss.remove(message)
            data = read_json("quotes")
            data["quotes"].remove(message)
            write_json(data, "quotes")

      elif message not in data:
        await ctx.send("That quote doesn't exist on our database")

#discord leveling sysstem based on number of questions sent
@bot.command(name = 'level')
async def level_check(ctx, *, message = None):

  with open("users.json", 'r') as file:
    data = json.load(file)
    with open('levels.json', "r") as levelfile:
      hashtag = ("█")
      space = ('░')
      leveldata = json.load(levelfile)
      levellist = leveldata["level"]
      def get_key(val):
        for key, value in levellist.items():
         if val == value:
             return key
 
        return "key doesn't exist"
      message = message
      if message is None: 
        msg_id = ctx.message.author.id
        msg_id = str(msg_id)
        dictionary = data.get(msg_id)
        level = dictionary[1]
        currentlevel = level
        levelvar = level +1
        var = get_key(levelvar)
        var = int(var)
        currentvar = get_key(currentlevel)
        currentvar = int(currentvar)
        xpvar = dictionary[0]
        subtraction = xpvar - var
        subtraction = abs(subtraction)
        difference = var - currentvar
        difference2 = xpvar - currentvar
        percentage = ((difference2/ difference) * 30)
        percentage = int(percentage)
        percentage = round(percentage)

        hashtag = percentage*(hashtag)
        spacemultiple = 30- percentage
        space = spacemultiple*(space)
        progressbar = (f"{hashtag}{space}")

        embed = discord.Embed(title = f"Your level is {level}", description=f"{ctx.author.mention}, You need {subtraction}xp to level up")
        embed.add_field(name = f"{progressbar}", value = f'{xpvar}/{var}', inline = False)
        await ctx.send(embed = embed)
      if message is not None:
        if message[0] == "<":
            message = message.replace("<","")
            message = message.replace(">","")
            message = message.replace("@","")
            message = message.replace("&","")
            message = message.replace("!","")
            print(message)
            dictionary = data.get(message)
            level = dictionary[1]
            currentlevel = level
            levelvar = level +1
            var = get_key(levelvar)
            var = int(var)
            currentvar = get_key(currentlevel)
            currentvar = int(currentvar)
            xpvar = dictionary[0] 
            subtraction = xpvar - var
            subtraction = abs(subtraction)
            difference = var - currentvar
            difference2 = xpvar - currentvar
            percentage = ((difference2/ difference) * 30)
            percentage = int(percentage)
            percentage = round(percentage)

            hashtag = percentage*(hashtag)
            spacemultiple = 30- percentage
            space = spacemultiple*(space)
            progressbar = (f"{hashtag}{space}")
            print(progressbar)
            message = await bot.fetch_user(message)
            embed = discord.Embed(title = f"{message} level is {level}", description=f"{message}, You need {subtraction}xp to level up")
            embed.add_field(name = f"{progressbar}", value = f'{xpvar}/{var}', inline = False)
            await ctx.send(embed = embed)

#leader board system which lists out all the usesr and number of messages they sent. 
@bot.command(name = "leaderboard", aliases=["rank", 'ranks'])
async def rank(ctx):
  embedlist = []
  listt = []
  with open('users.json', 'r') as users:
    dictionary = json.load(users)
    for a in dictionary: 
      lisst = dictionary[a]
      listt.append(lisst)  
    sortedlist = sorted(listt)
    listt = sortedlist[::-1]
    def get_key(val):
      for key, value in dictionary.items():
          if val == value:
              return key
  
      return "key doesn't exist"
    index = 0
    for i in listt:
      key = get_key(i)
      key = int(key)
      key1 = await bot.fetch_user(key)      
      key1 = key1.name
      embedlist.append(key1)
      indexlist = embedlist[index]
      i = map(str, i) 
      i = " = xp, ".join(i)
      if index == 0: 
        indexlist = ("🥇 " + indexlist + ' - '+ i + ' = level')
      elif index == 1:
        indexlist = ("🥈 " + indexlist + ' - '+ i + ' = level')
      elif index == 2:
        indexlist = ("🥉 " + indexlist + ' - '+ i + ' = level')
      else:
        indexlist = (indexlist + ' - '+ i + ' - level')
      embedlist[index] = indexlist
      if len(embedlist) == 7:
        break
      index +=1
    joinedlist = '\n'.join(embedlist)
    embed = discord.Embed(title = f"leaderboard", description = f"{joinedlist}")
    embed.set_thumbnail(url = ctx.guild.icon_url)
    embed.set_footer(text = (f'Pong! {round (bot.latency * 1000)} ms'))
    await ctx.send(embed = embed)
  
@bot.event
async def on_message(message):
  await bot.process_commands(message)
  nono_words = ["^level", "^rank", "memes", 'deepmemes']
  badnonoword = ['uwu', 'owo', 'twt', 'u3u', 'qwq']
  for a in nono_words:
    if message.content.startswith(a):
      return
  msg = message.content

  if any(terriblewords in msg.lower() for terriblewords in badnonoword):
    await message.channel.send('NOOOOOOOO')
  with open("users.json", 'r') as file:
    with open('levels.json', "r") as levelfile:
      index = 0
      leveldata = json.load(levelfile)
      data = json.load(file)
      list1 = data
      levellist = leveldata["level"]
      keydata = list(levellist.keys())
      authorid = message.author.id
      authorid = str(authorid)
      if authorid in list1: 
        xpandlevel = list1.get(authorid)
        xp = xpandlevel[0]
        level = xpandlevel[1]
        xp += 20
        xpandlevel[0] = xp
        try: 
          while index != len(keydata): 
            numm = keydata[index]
            index += 1
            if xp >= int(numm) and xp < int(keydata[index]):
              delevel = levellist.get(str(numm))
              xpandlevel[1] = delevel
          """
          if level != xpandlevel[1]:
            await message.channel.send(f"{message.author.mention} you just level up lol. Ur now level {xpandlevel[1]}")
          """
        except IndexError:
          pass
        write_json(list1, 'users')

@bot.command(description="Mutes the specified user.")
@commands.has_role("Shogun Waiting Room")
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@bot.command(description="Unmutes a specified user.")
@commands.has_role("Shogun Waiting Room")
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


@bot.command(description="Mutes the specified user.")
@commands.has_role("Shogun Waiting Room")
async def tempmute(ctx, member: discord.Member, *, mutetime = None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    try:
      mutetime = mutetime
      await member.add_roles(mutedRole)
      await ctx.send(f"Muted {member.mention} for {mutetime} seconds")
      await member.send(f"You were muted in the server {guild.name} for {mutetime} seconds")
      mutetime = int(mutetime)
      await asyncio.sleep(mutetime)
      await member.remove_roles(mutedRole)
      await ctx.send(f"Unmuted {member.mention}")
    except ValueError:
      await ctx.send('You need to enter a integer for seconds')
      await member.remove_roles(mutedRole)

@bot.command(name = 'avatar')
async def sendavatar(ctx, *, message = None):
  message = message
  if message == None:  
    ids = ctx.message.author
    avatar = ids.avatar_url
    embed = discord.Embed(title = "Avatar")
    embed.set_image(url = "{}".format(avatar))
    await ctx.send(embed = embed)
  elif message is not None:
    message = message.replace("<","")
    message = message.replace(">","")
    message = message.replace("@","")
    message = message.replace("&","")
    message = message.replace("!","")
    profile = await bot.fetch_user(message)
    avatar = profile.avatar_url
    embed = discord.Embed(title = "Avatar")
    embed.set_image(url = "{}".format(avatar))
    await ctx.send(embed = embed)

@bot.command()
async def stats(ctx):
    """
    A usefull command that displays bot statistics.
    """
@bot.command()
async def serverstats(ctx):
    embed=discord.Embed(title=f"Server Stat of  {ctx.guild.name}")
    embed.add_field(name="Users:", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Channels:", value=len(ctx.guild.channels), inline=False)
    embed.add_field(name ="Version", value = f'This is running on {platform.python_version()} and discord.py version {discord.__version__}')
    await ctx.send(embed=embed)

@bot.command(name = "ping")
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Pong! {round (bot.latency * 1000)} ms')

#describe the user name and details about them
@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)
    channels = ctx.guild.channels
    print(channels.name)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("That command doesn't exist")
        return
    raise error

keep_alive()
my_secret = os.environ['token']
bot.run(my_secret)
