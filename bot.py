from discord import *
from discord.ext import *
import discord.ext.commands
from discord.ext.commands import *
from datetime import *
from re import *
from settings import *

client = discord.ext.commands.Bot(command_prefix=prefix,
                   description='Unique BOT for School\nDeveloped by: {developers}\nCurrent version: "{current_version}"\nCurrent prefix: "{prefix}"'.format(developers=", ".join(developers), current_version=current_version, prefix=prefix))

@client.event
async def on_ready():
    print(f'Successful start;\n\
Bot UserName: "{client.user.name}";')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=activity_name))

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