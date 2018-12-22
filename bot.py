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
    embed.add_field(name = "S!kick", value = "Vyhodí uživatele!",inline=False)
    embed.add_field(name = "S!ban", value = "Banuje Uživatele!",inline=False)
    embed.set_footer(text = "Pouze pro AdminTeam!")
    await client.say(embed=embed)

@client.command()
async def helpfun():
    await client.say("**__Připravujeme!__**")
    
@client.command()
@commands.has_permissions(administrator=True)
async def dev():
    embed = discord.Embed(title = "Developers Help!", color = 0x191970)
    embed.add_field(name = "S!restart", value = "Restartuje bota!", inline=False)
    await client.say(embed=embed)

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
    
@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        embed1 = discord.Embed(title = "Error", color = 0xFFFF00)
        embed1.add_field(name = "Denied!", value = "On/Ona je Mod/Admin a nemám pravomoc ho/ji kicknout!!",inline=False)
        await client.say(embed=embed1)
        return
    
    try:
        embed2 = discord.Embed(title = "Povedli se!", color = 0x2E8B57)
        embed2.add_field(name = "Povoleno!", value = user.name+" byl vyhozen!",inline=False)
        await client.kick(user)
        await client.say(embed=embed2)
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        embed3 = diwcird.Embed(title = "Permissions denied!", color = 0xA52A2A)
        embed3.add_field(name = "Pravomoce Odebrány!", value = "Nemáš dostatečné pravomoce na tento příkaz!",inline=False)
        await client.say(embed=embed3)
        return

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        embed3 = discord.Embed(title = "Denied!", color = 0xFFFF00)
        embed3.add_field(name = "Denied!", value = "On/Ona je mod/Admin a nemam odvahu ho/ji zabanovat",inline=False)
        await client.say(embed=embed3)
        return

    try:
        embed2 = discord.Embed(title = "Povedlo se!", color = 0x2E8B57)
        embed2.add_field(name = "Ban se povedl!", valie = user.name+" byl zabanován!",inline=False)
        await client.ban(user)
        await client.say(embed=embed2)

    except discord.Forbidden:
        embed1 = discord.Embed(title = "Permission denied!", color = 0xA52A2A)
        embed1.add_field(name = "Permissions Error", value = "Nejspíše nemám práva na ban!",inline=False)
        await client.say(embed=embed1)
        return
    except discord.HTTPException:
        embed = discord.Embed(title = "Error!", color = 0xFFFF00)
        embed.add_field(name = "Nezdařilo se!", value = "Ban se nepodařil!",inline=False)
        await client.say(embed=embed)
        return		 
@client.command()
async def JustNela():
    embed = discord.Embed(title = "Info o JustNela#6666", icon_url = "https://cdn.discordapp.com/attachments/468928524267290634/525662927529836574/f054ab37k2ny.gif", color = 0x663399)
    embed.add_field(name = "Info", value = "",inline = False)
    embed.add_field(name = "Jmeno:", value = "@JustNela#6666",inline = False)
    embed.add_field(name = "Status", value = "Nejčastěji Online!",inline = False)
    embed.add_field(name = "ID:", value = "342364288310312970",inline = False)
    embed.set_footer(text = "Tohoto bota udělala JustNela#6666 & JustVojta#6969!")
    await client.say(embed=embed)
    
client.run(os.getenv("BOT_TOKEN"))
