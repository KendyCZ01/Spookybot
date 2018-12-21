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



@client.event
async def on_ready():
    channel = discord.utils.get(client.get_all_channels(), name='🌎・hlavní-chat')
    await client.change_presence(game=discord.Game(name= "Prefix: S!"))
    print("The bot is online and connected with Discord!") 
    await client.send_message(channel, "``Jsem tu a připraven!!``")
    


@client.command()
async def help():
    embed = discord.Embed(title = "Pomoc!", color = 0x00FF00)
    embed.add_field(name = "S!ghelp", value = "Ukáže Pomoc pro všechny! (připravuje se)",inline = False)
    embed.add_field(name = "S!modhelp", value = "Ukáže ti pomoc pro moderátory! (připravuje se)",inline = False)
    embed.add_field(name = "S!helpfun", value = "Ukáže ti vtipné přikazy! (doděláváme)",inline = False)
    embed.add_field(name = "S!dev", value = "Ukáže pomoc pro developery! (jen pro developery!)",inline = False)
    embed.set_footer(text = "Bota vytvářejí JustVojta#6969 & JustNela#6666")
    embed.set_image(url = "http://www.pfpenergy.co.uk/media/1184/help-and-support.png")
    await client.say(embed=embed)
    
@client.command()
async def modhelp():
    embed = discord.Embed(title = "Pomoc Pro Moderátory!", color = 0x006400)
    embed.add_field(name = "S!clear", value = "Smaže daný počet zpráv!",inline=False)
    embed.add_field(name = "S!warn", value = "Varuje uživatele! Použití: S!warn @user Důvod",inline=False)
    embed.set_footer(text = "Pouze pro AdminTeam!")
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
        await client.say(str(number)+' zpráv vymazáno')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('Něco se pokazilo')
        return         
   
 
    await client.delete_messages(mgs)      

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)

async def warn(ctx, userName: discord.User, *, message:str):
    
    embed = discord.Embed(color = 0xB22222, title = "Varování")
    embed.add_field(name = "Hráč", value = "{0}".format(userName), inline=False)
    embed.add_field(name = "Moderátor", value = "{0}".format(ctx.message.author), inline=False)
    embed.add_field(name = "Důvod", value = "{0}".format(message), inline=False)
 
    await client.say(embed=embed)
   
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def restart():
    await client.logout()
    
    async def info(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);
    
client.run(os.getenv("BOT_TOKEN"))
