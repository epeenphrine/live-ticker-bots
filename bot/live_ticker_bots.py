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
from tokens import dev, dev1, es, nas, dow, us10y, dollar, vix, btc, eth, silver , link

es_bot = discord.Client()
nas_bot = discord.Client()
dow_bot = discord.Client()


us10y_bot = discord.Client()
vix_bot = discord.Client()
ticker_vix = discord.Client()


dollar_bot = discord.Client()
silver_bot = discord.Client()

btc_bot = discord.Client()
eth_bot=  discord.Client()
link_bot = discord.Client()

loop = asyncio.get_event_loop()

@es_bot.event
async def on_ready():
    print('es started') 

@nas_bot.event
async def on_ready():
    print('nas started')

@dow_bot.event
async def on_ready():
    print('dow started')

@silver_bot.event
async def on_ready():
    print('silver started')

@us10y_bot.event
async def on_ready():
    print('us10y started')

@dollar_bot.event
async def on_Ready():
    print('dollar started')

@vix_bot.event
async def on_ready():
    print('vix started')

@btc_bot.event
async def on_ready():
    print('btc started')

@eth_bot.event
async def on_ready():
    print('eth started')
@link_bot.event
async def on_ready():
    print('link started')
    
'''
@tasks.loop() can be changed to seconds, minutes, hours
https://discordpy.readthedocs.io/en/latest/ext/tasks/
'''

@tasks.loop(seconds=5)
async def called_second():
    ## get all guild ids that the bot is joined in 


    data = wrangle_data()
    print(data)

    ticker_es       = data['es']
    ticker_nas      = data['nas'] 
    ticker_dow      = data['dow'] 
    ticker_vix      = data['vix']
    ticker_us10y    = data['us10y']
    ticker_dollar   = data['dxy']
    ticker_silver   = data['silver']
    ticker_btc      = data['btc']
    ticker_eth      = data['eth']
    ticker_link     = data['link']
    ## es
    if ticker_es:
        guild_ids = [guild.id for guild in es_bot.guilds] 
        name_es = '{:20,.2f}'.format(ticker_es['last'])
        watching_es = ticker_es['change%']
        guild_channels = [es_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in watching_es:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)
                await guild_channel.me.edit(nick=f"1) {name_es}") 
                await es_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"ES {watching_es}"))
            except:
                print(f'broke in {guild_channel}')
    else:
        print('no es data')
    ##nas
    if ticker_nas:
        guild_ids = [guild.id for guild in nas_bot.guilds] 
        name_nas = '{:20,.2f}'.format(ticker_nas['last'])
        watching_nas= ticker_nas['change%']
        guild_channels = [nas_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in watching_nas:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)
                await guild_channel.me.edit(nick=f"2) {name_nas}")
                await nas_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"NQ {watching_nas}"))
            except:
                print(f'broke in {guild_channel}')
    else: 
        print('no nas data')
    ## dow
    if ticker_dow: 
        guild_ids = [guild.id for guild in dow_bot.guilds] 
        name_dow = '{:20,.2f}'.format(ticker_dow['last'])
        watching_dow = ticker_dow['change%']

        guild_channels = [dow_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in watching_dow:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)
                await guild_channel.me.edit(nick=f"3) {name_dow}")
                await dow_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"DJI {watching_dow}"))

            except:
                print(f'broke in {guild_channel}')
    else:
        print('no dow data')

    ## vix 
    if vix:
        guild_ids = [guild.id for guild in vix_bot.guilds] 
        name_vix = '{:20,.2f}'.format(ticker_vix['last'])
        watching_vix = ticker_vix['change%']

        guild_channels = [vix_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in  watching_vix:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)

                await guild_channel.me.edit(nick=f"4) {name_vix}")
                await vix_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"VIX {watching_vix}"))
            except:
                print(f'broke in {guild_channel}')
    else:
        print('no vix data ')

    # dollar  
    if ticker_dollar:
        guild_ids = [guild.id for guild in dollar_bot.guilds] 
        name_dollar = '{:20,.2f}'.format(ticker_dollar['last'])
        watching_dollar = ticker_dollar['change%']
        guild_channels = [dollar_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in  watching_dollar:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)

                await guild_channel.me.edit(nick=f"5) {name_dollar}")
                await dollar_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"DXY {watching_dollar}"))
            except:
                print(f'broke in {guild_channel}')
    else:
        print('no dollar data')
    # us10y 
    if ticker_us10y:
        guild_ids = [guild.id for guild in us10y_bot.guilds] 
        name_us10y = '{:20,.2f}'.format(ticker_us10y['last'])
        watching_us10y = ticker_us10y['change%']
        guild_channels = [us10y_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in  watching_us10y:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)

                await guild_channel.me.edit(nick=f"4) {name_us10y}")
                await us10y_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"US10Y {watching_us10y}"))
            except:
                print(f'broke in {guild_channel}')
    else:
        print('no us10y data')

    # silver  
    if ticker_silver:
        guild_ids = [guild.id for guild in silver_bot.guilds] 
        name_silver = '{:20,.2f}'.format(ticker_silver['last'])
        watching_silver = ticker_silver['change%']
        
        guild_channels = [silver_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in  watching_silver:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)
                await guild_channel.me.edit(nick=f"6) {name_silver}")
                await silver_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{ticker_silver['name'].upper()} {watching_silver}"))
            except:
                print(f'broke in {guild_channel}')
    else:
        print('no silver data')
    #shit coin stuff
    # btc
    if ticker_btc:
        guild_ids = [guild.id for guild in btc_bot.guilds] 
        name_btc = '{:20,.2f}'.format(ticker_btc['last'])
        watching_btc = ticker_btc['change%']
        guild_channels = [btc_bot.get_guild(guild_id) for guild_id in guild_ids]

        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in watching_btc:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)
                await guild_channel.me.edit(nick=f"7) {name_btc}")
                await btc_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"BTC {watching_btc}"))
            except:
                print(f'broke in {guild_channel}')
    else:
        print('no data for btc')
    # eth 
    if ticker_eth:
        guild_ids = [guild.id for guild in eth_bot.guilds] 
        name_eth= '{:20,.2f}'.format(ticker_eth['last'])
        watching_eth = ticker_eth['change%']
        guild_channels = [eth_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in  watching_eth:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)
                await guild_channel.me.edit(nick=f"8) {name_eth}")
                await eth_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"ETH {watching_eth}"))
            except:
                print(f'broke in {guild_channel}')
    else:
        print('nodata for eth')
    # link
    if ticker_link:
        guild_ids = [guild.id for guild in link_bot.guilds] 
        name_link = '{:20,.2f}'.format(ticker_link['last'])
        watching_link = ticker_link['change%']
        guild_channels = [link_bot.get_guild(guild_id) for guild_id in guild_ids]
        for guild_channel in guild_channels:
            try:
                red = get(guild_channel.roles, name='RED')
                green = get(guild_channel.roles, name='GREEN')
                if "-" in  watching_link:
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(green)
                    await discord_bot.add_roles(red)
                else: 
                    discord_bot = guild_channel.me
                    await discord_bot.remove_roles(red)
                    await discord_bot.add_roles(green)
                await guild_channel.me.edit(nick=f"9) {name_link}")
                await link_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"LINK {watching_link}"))
            except:
                print(f'broke in {guild_channel}')
    else:
        print('nodata for eth')
    print(f'updated ')

@called_second.before_loop
async def before():
    await es_bot.wait_until_ready()
    await nas_bot.wait_until_ready()
    await dow_bot.wait_until_ready()
    await vix_bot.wait_until_ready()

    await us10y_bot.wait_until_ready()
    await dollar_bot.wait_until_ready()
    await silver_bot.wait_until_ready()    

    await btc_bot.wait_until_ready()
    await eth_bot.wait_until_ready()
    await link_bot.wait_until_ready()

    print("Finished waiting")

called_second.start()

async def create_bots():
    es_task= loop.create_task(es_bot.start(es))
    nas_task = loop.create_task(nas_bot.start(nas))
    dow_task = loop.create_task(dow_bot.start(dow))
    vix_task = loop.create_task(vix_bot.start(vix))

    us10y_task = loop.create_task(us10y_bot.start(us10y)) 
    dollar_task = loop.create_task(dollar_bot.start(dollar))
    silver_task = loop.create_task(silver_bot.start(silver))

    btc_task = loop.create_task(btc_bot.start(btc))
    eth_task = loop.create_task(eth_bot.start(eth))
    link_task = loop.create_task(link_bot.start(link))
    
    await es_task 
    await nas_task
    await dow_task
    await vix_task

    await us10y_task
    await dollar_task 
    await silver_task

    await btc_task 
    await eth_task
    await link_task 

loop.run_until_complete(create_bots())