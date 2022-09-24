import discord
from discord.ext import commands
b = open('channels.txt', 'w')
b.close()
k = open('roles.txt', 'w')
TOKEN = input("Enter your bot's token: ")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='null', intents=intents)
bot.event
async def on_ready():
    print(f'[SUCCESFUL]  - Logged in as {client.user}.')
    GUILD = int(input("\nGuild ID to scrape: "))
    id = client.get_guild(GUILD)
    y = open('members.txt', 'a')
    for member in id.members:
        y.write(f"{member.id}\n")
    i = open('channels.txt','a')
    for channel in id.channels:
        i.write(f"{channel.id}\n")
    y6 = open('roles.txt', 'a')
    for role in id.roles:
        y6.write(f"{role.id}\n")
    em = open ('emojis.txt', 'a')
    for emoji in id.emojis:
        em.write(f"{emoji.id}\n")
    print("Scraped Channels\nScraped Roles\n[SUCCESFUL] - Server has been scraped you may close this window now.")
bot.run(TOKEN)
