import os
import discord
from dotenv import load_dotenv
import random


load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('GUILD_NAME')


client=discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    #guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user.name} has connected to Discord!\n'
    f'{guild.name}(id: {guild.id})'
    )
    
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to ECE23!/n'
        f'Kindly Introduce Yourself!'
    )

@client.event
async def on_message(message):
    if message.author==client.user:
        return 
    
    known={"Hi":"Hey, how are you?","Favorite Character":"Yamori from TKG.","Whats your age?":"Does it matter.","Who are you?":"Your future master, but rn I'm just a little bot."}

    if message.content in known:
        await message.channel.send(
            f'{known[message.content]}'
        )
    

client.run(TOKEN)
