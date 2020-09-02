import discord
from discord.ext import commands
import datetime
import re

############################### VARIABLES ################################

current_version = 0.1
prefix = "/"
activity_type = discord.ActivityType.playing
activity_name = f"{prefix}help".format(prefix=prefix)
activity_emoji = None
TOKEN = 'NzUwMjkyODU3MzM1NTc4NjI0.X04arA.y1_MTosO6vHvH5E7zgoGgs6JYkM'

############################### VARIABLES ################################

client = commands.Bot(command_prefix=prefix,
                   description='Unique BOT for School\nDeveloped by: Egor Blyablin\nCurrent version: "{current_version}"\nCurrent prefix: "{prefix}"'.format(current_version=current_version, prefix=prefix))

@client.event
async def on_ready():
    print(f'Successful start;\n\
Bot UserName: "{client.user.name}";')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=activity_type, name=activity_name))

@client.event
async def on_message(message):
    msg = message.content.lower()

############################### COMMANDS ##################################

@client.command()
async def echo(context, *arg):
    print(context.author,", ", "Echo",":", *arg)
    await context.send(embed=discord.Embed(color=0x7C85D8, title="Echo", description=" ".join(arg)))


@client.command()
async def school_pass(context, till):
    try:
        name, surname = context.author.split(" ")[0], context.author.split(" ")[1]
        print(name, surname)
        day = int(till[:1])
        month = int(till[3:4])
        year = int(till[6:])
        print(day, month, year)
        await context.send(embed=discord.Embed(color=0x00FF48, title="Success", description=f"Name = {name}, Surname = {surname}, You won't be at school till {till}".format(name=name, surname=surname, till=till)))
    except:
        await context.send(embed=discord.Embed(color=0xFF0000, title="Error", description="/school_pass [Буду отсутствовать до (включительно)]\nДату писать в формате ДД.MM.ГГ\nПример: /school_pass 31.12.99"))

############################### COMMANDS ##################################

client.run(TOKEN)