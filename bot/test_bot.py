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
from tokens import optional_ticker_1, optional_ticker_2 
from stocktwits import make_req

option_1 = commands.Bot('.')
option_2 = commands.Bot('..')

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

    stocktwits_data = make_req()  
    guild_ids = [guild.id for guild in client.guilds]
    guild_channels = [client.get_guild(guild_id) for guild_id in guild_ids]
    for ticker in stocktwits_data:
        check_extended = stocktwits_data[ticker]['ExtendedHoursPrice']
        if check_extended:

        
    print(f'updated ')

@called_second.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")
called_second.start()
client.run(dev1)