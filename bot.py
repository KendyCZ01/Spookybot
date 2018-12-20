import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType







client = commands.Bot(command_prefix = '!', case_insensitive=False)

client.remove_command('help')

@client.event
async def on_ready():
    channel = discord.utils.get(client.get_all_channels(), name='🌎・hlavní-chat')
    await client.change_presence(game=discord.Game(name= "Prefix: !"))
    print("The bot is online and connected with Discord!") 
    await client.send_message(channel, "``Jsem tu a připraven!!``")
    
def owner(ctx):
    return ctx.message.author.id == "342364288310312970", "522048274689949712"

@client.command()
async def help():
    embed = discord.Embed(title = "Pomoc!", color = 0x00FF00)
    embed.add_field(name = "!ghelp", value = "Ukáže Pomoc pro všechny! (připravuje se)",inline = False)
    embed.add_field(name = "!modhelp", value = "Ukáže ti pomoc pro moderátory! (připravuje se)",inline = False)
    embed.add_field(name = "!helpfun", value = "Ukáže ti vtipné přikazy! (doděláváme)",inline = False)
    embed.set_footer(text = "Bot vytvořen JustNela#6666")
    embed.set_image(url = "https://image.shutterstock.com/image-vector/help-bulb-word-cloud-collage-450w-415140307.jpg")
    await client.say(embed=embed)
    
@client.command()
async def ghelp():
    await client.say("**__Připravuje Se!__**")
    
@client.command()
async def modhelp():
    await client.say("**__Připravujeme!__**")

@client.command()
async def helpfun()
    await client.say("**__Připravujeme!__**")



client.run(os.getenv("BOT_TOKEN"))
