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

from tokens import optional_ticker_1, optional_ticker_2, optional_ticker_3
from stocktwits import make_req

option_1 = commands.Bot('.')
option_2 = discord.Client() 
option_3 = discord.Client() 

loop = asyncio.get_event_loop()

'''
@tasks.loop() can be changed to seconds, minutes, hours
https://discordpy.readthedocs.io/en/latest/ext/tasks/
'''

try:
    with open('/tmp/json/ticker_choice', 'r') as f:
        ticker_choice = json.load(f)
    print('successfully loaded from json')
except:
    print('cant open json starting default var')
    ticker_choice = [
        'gme',
        'aapl',
        'googl'
    ]

def save(ticker_choice):
    with open('/tmp/json/ticker_choice', 'w') as f:
        json.dump(ticker_choice, f)
    print('saved') 
@option_1.command()
async def change1(ctx, *arg): 
    print('in change1 for option_1')
    print(arg)
    if arg and len(arg) == 1:
        ticker_choice[0] = arg[0]
        print(ticker_choice)
        save(ticker_choice)

@option_1.command()
async def change2(ctx, *arg): 
    print('in change2 for option_1')
    print(arg)
    if arg and len(arg) == 1:
        ticker_choice[1] = arg[0]
        print(ticker_choice)
        save(ticker_choice)

@option_1.command()
async def change3(ctx, *arg): 
    print('in change3 for option_1')
    print(arg)
    if arg and len(arg) == 1:
        ticker_choice[2] = arg[0]
        print(ticker_choice)
        save(ticker_choice)

@tasks.loop(seconds=5)
async def called_second():
    stocktwits_data = make_req(f"{ticker_choice[0]},{ticker_choice[1]},{ticker_choice[2]}")  

    # option 1
    guild_ids = [guild.id for guild in option_1.guilds]
    guild_channels = [option_1.get_guild(guild_id) for guild_id in guild_ids]
    try:
        ticker = stocktwits_data[ticker_choice[0]]
    except:
        print('key error in ticker')
    try:
        ext_hours_price= ticker['ExtendedHoursPrice']
        if ext_hours_price != 0.0 :
            ext_percent_change = ticker['ExtendedHoursPercentChange'] 
            ext_price_change =  ticker['ExtendedHoursChange']
            ext_price = '{:20,.2f}'.format(ext_hours_price)
            symbol = ticker['Symbol']
            for guild_channel in guild_channels:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if '-' in str(ext_percent_change):
                    await guild_channel.me.remove_roles(green)
                    await guild_channel.me.add_roles(red)
                    await option_1.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} {ext_percent_change}% {ext_price_change}"))
                else:
                    await guild_channel.me.remove_roles(red)
                    await guild_channel.me.add_roles(green)
                    await option_1.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} +{ext_percent_change}% +{ext_price_change}"))
                await guild_channel.me.edit(nick=f"{symbol} {ext_price}")
        else:
            print('market is live! Using live data')
            price = ticker['Last'] 
            symbol = ticker['Symbol']
            percent_change = '{:20,.2f}'.format(ticker['PercentChange'])
            price_change = '{:20,.2f}'.format(ticker['Change'])
            option_1_name = '{:20,.2f}' .format(price)
            for guild_channel in guild_channels:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if '-' in str(percent_change):
                    await guild_channel.me.remove_roles(green)
                    await guild_channel.me.add_roles(red)
                    await option_1.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} {percent_change}% {price_change}"))
                else:
                    await guild_channel.me.remove_roles(red)
                    await guild_channel.me.add_roles(green)
                    await option_1.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} +{percent_change}% +{price_change}"))
                await guild_channel.me.edit(nick=f"{symbol} {price}")
    except:
        print('error getting data')
        await option_1.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"BROKEN PROBABLY BAD TICKER / SYMBOL"))
    #option 2
   
    guild_ids = [guild.id for guild in option_2.guilds]
    guild_channels = [option_2.get_guild(guild_id) for guild_id in guild_ids]
    try:
        ticker = stocktwits_data[ticker_choice[1]]
    except:
        print('key error in ticker')
    try:
        ext_hours_price= ticker['ExtendedHoursPrice']
        if ext_hours_price != 0.0 :
            ext_percent_change = ticker['ExtendedHoursPercentChange'] 
            ext_price_change =  ticker['ExtendedHoursChange']
            ext_price = '{:20,.2f}'.format(ext_hours_price)
            symbol = ticker['Symbol']
            for guild_channel in guild_channels:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if '-' in str(ext_percent_change):
                    await guild_channel.me.remove_roles(green)
                    await guild_channel.me.add_roles(red)
                    await option_2.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} {ext_percent_change}% {ext_price_change}"))
                else:
                    await guild_channel.me.remove_roles(red)
                    await guild_channel.me.add_roles(green)
                    await option_2.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} +{ext_percent_change}% +{ext_price_change}"))
                await guild_channel.me.edit(nick=f"{symbol}  {ext_price}")
        else:
            print('market is live! Using live data')
            price = ticker['Last'] 
            symbol = ticker['Symbol']
            percent_change = '{:20,.2f}'.format(ticker['PercentChange'])
            price_change = '{:20,.2f}'.format(ticker['Change'])
            price = '{:20,.2f}' .format(price)
            for guild_channel in guild_channels:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if '-' in str(percent_change):
                    await guild_channel.me.remove_roles(green)
                    await guild_channel.me.add_roles(red)
                    await option_2.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} {percent_change}% {price_change}"))
                else:
                    await guild_channel.me.remove_roles(red)
                    await guild_channel.me.add_roles(green)
                    await option_2.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} +{percent_change}% +{price_change}"))
                await guild_channel.me.edit(nick=f"{symbol} {price}")
    except:
        print('error getting data')
        await option_2.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"BROKEN PROBABLY BAD TICKER / SYMBOL"))

    # option 3
   
    guild_ids = [guild.id for guild in option_3.guilds]
    guild_channels = [option_3.get_guild(guild_id) for guild_id in guild_ids]
    try:
        ticker = stocktwits_data[ticker_choice[2]]
    except:
        print('key error in ticker')
    try:
        ext_hours_price= ticker['ExtendedHoursPrice']
        if ext_hours_price != 0.0 :
            ext_percent_change = ticker['ExtendedHoursPercentChange'] 
            ext_price_change =  ticker['ExtendedHoursChange']
            ext_price = '{:20,.2f}'.format(ext_hours_price)
            symbol = ticker['Symbol']
            for guild_channel in guild_channels:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if '-' in str(ext_percent_change):
                    await guild_channel.me.remove_roles(green)
                    await guild_channel.me.add_roles(red)
                    await option_3.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} {ext_percent_change}% {ext_price_change}"))
                else:
                    await guild_channel.me.remove_roles(red)
                    await guild_channel.me.add_roles(green)
                    await option_3.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} +{ext_percent_change}% +{ext_price_change}"))
                await guild_channel.me.edit(nick=f"{symbol}  {ext_price}")
        else:
            print('market is live! Using live data')
            price = ticker['Last'] 
            symbol = ticker['Symbol']
            percent_change = '{:20,.2f}'.format(ticker['PercentChange'])
            price_change = '{:20,.2f}'.format(ticker['Change'])
            price = '{:20,.2f}' .format(price)
            for guild_channel in guild_channels:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if '-' in str(percent_change):
                    await guild_channel.me.remove_roles(green)
                    await guild_channel.me.add_roles(red)
                    await option_3.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} {percent_change}% {price_change}"))
                else:
                    await guild_channel.me.remove_roles(red)
                    await guild_channel.me.add_roles(green)
                    await option_3.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{symbol} +{percent_change}% +{price_change}"))
                await guild_channel.me.edit(nick=f"{symbol} {price}")
    except:
        print('error getting data')
        await option_3.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"BROKEN PROBABLY BAD TICKER / SYMBOL"))
@called_second.before_loop
async def before():
    await option_1.wait_until_ready()
    await option_2.wait_until_ready()
    await option_3.wait_until_ready()
    print("Finished waiting")

called_second.start()

async def create_bots():
    option1_task = loop.create_task(option_1.start(optional_ticker_1))
    option2_task = loop.create_task(option_2.start(optional_ticker_2))
    option3_task = loop.create_task(option_3.start(optional_ticker_3))

    await option1_task
    await option2_task
    await option3_task

loop.run_until_complete(create_bots())