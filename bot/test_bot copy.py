from discord.ext import commands, tasks
from discord.utils import get
import discord
import re
import json 
import time 
import random
import asyncio
import os
import datetime


from live_ticker_scrape import wrangle_data 
from tokens import dev, dev1

client = commands.Bot('!')

#target_channel_id = 492405515931090964 
target_channel_id = 644682833511579668
'''
@tasks.loop() can be changed to seconds, minutes, hours
https://discordpy.readthedocs.io/en/latest/ext/tasks/
'''
@tasks.loop(seconds=1)
async def called_second():
    # guild_channel = client.get_guild(target_channel_id)
    guild_ids = [guild.id for guild in client.guilds]
    guild_channels = [client.get_guild(guild_id) for guild_id in guild_ids ]

    testing = wrangle_data()['dow']
    ticker = '{:20,.2f}'.format(testing['last'])
    watching = testing['change%']
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{watching}"))
    for guild_channel in guild_channels:
        red = get(guild_channel.roles, name='RED') 
        green = get(guild_channel.roles, name='GREEN')
        if "-" in watching:
            await guild_channel.me.remove_roles(green)
            await guild_channel.me.add_roles(red)
        else:
            await guild_channel.me.remove_roles(red)
            await guild_channel.me.add_roles(green)
        await guild_channel.me.edit(nick=f"example) {ticker}")
    print(f'updated ')

    # #await client.user.edit(nick='hello')

    # guild_channel = client.get_guild(target_channel_id)
    # discord_bot = guild_channel.me
    # red = get(guild_channel.roles, name='red')
    # green= get(guild_channel.roles, name='green')

    # for item in guild_channel.roles:
    #     if str(item).lower() == "red":
    #         await discord_bot.add_roles(red)
    #         await discord_bot.remove_roles(red)
    #         print('added red')
    #     if str(item).lower() =="green":
    #         await discord_bot.add_roles(green)
    #         await discord_bot.remove_roles(green)
    #         print('added green')

    # print(guild_channel.me)
    
    # something = await guild_channel.me.edit(nick=f"1) {ticker}",  colour=discord.Colour(colours[2]))

@called_second.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")
called_second.start()
client.run(dev1)