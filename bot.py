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







client = commands.Bot(command_prefix = 'S!', case_insensitive=False)

client.remove_command('help')

async def status_task();
    while True:
        await client.change_presence(game=discord.Game(name='Devs: JustNela & Vojta'))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name='S mýma developerama!))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name='s!help pro pomoc!'))
        await asyncio.sleep(3)

@client.event
async def on_ready():
    channel = discord.utils.get(client.get_all_channels(), name='🌎・hlavní-chat')
    await client.change_presence(game=discord.Game(name= "Prefix: !"))
    print("The bot is online and connected with Discord!") 
    await client.send_message(channel, "``Jsem tu a připraven!!``")
    
def owner(ctx):
    return ctx.message.author.id == "342364288310312970, 522048274689949712"

@client.command()
async def help():
    embed = discord.Embed(title = "Pomoc!", color = 0x00FF00)
    embed.add_field(name = "S!ghelp", value = "Ukáže Pomoc pro všechny! (připravuje se)",inline = False)
    embed.add_field(name = "S!modhelp", value = "Ukáže ti pomoc pro moderátory! (připravuje se)",inline = False)
    embed.add_field(name = "S!helpfun", value = "Ukáže ti vtipné přikazy! (doděláváme)",inline = False)
    embed.add_field(name = "S!dev", value = "Ukáže pomoc pro developery! (jen pro developery!)",inline = False)
    embed.set_footer(text = "Bot vytvořen JustNela#6666")
    embed.set_image(url = "https://image.shutterstock.com/image-vector/help-bulb-word-cloud-collage-450w-415140307.jpg")
    await client.say(embed=embed)
    
@client.command()
async def ghelp():
    await client.say("**__Připravuje Se!__**")
    
@client.command()
async def modhelp():
    embed = discord.Embed(url = "https://cdn.discordapp.com/attachments/468928524267290634/525662927529836574/f054ab37k2ny.gif", title = "Pomoc Pro Moderátory!", 0x006400)
    embed.add_field(name = "S!clear", value = "Smaže daný počet zpráv!",inline=False)
    embed.set_footer(text = "Pomoc přivolána {0}!".format(message.author.name))
    await client.say(embed=embed)

@client.command()
async def helpfun():
    await client.say("**__Připravujeme!__**")

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)      

@client.command(pass_context = True)
@commands.check(is_owner)
async def restart():
    await client.logout()

client.run(os.getenv("BOT_TOKEN"))
