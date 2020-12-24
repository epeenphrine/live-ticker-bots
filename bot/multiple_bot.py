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


from live_ticker_scrape import scrape_live_ticker
from tokens import dev, dev1, es, nas, dow, dollar, vix, btc, eth, gold 

es_bot = discord.Client()
nas_bot = discord.Client()
dow_bot = discord.Client()
dollar_bot = discord.Client()
vix_bot = discord.Client()
ticker_vix = discord.Client()

btc_bot = discord.Client()
eth_bot=  discord.Client()

gold_bot = discord.Client()
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

@gold_bot.event
async def on_ready():
    print('gold started')

@vix_bot.event
async def on_ready():
    print('vix started')

@btc_bot.event
async def on_ready():
    print('btc started')

@eth_bot.event
async def on_ready():
    print('eth started')
    
## change here to whatever 
target_channel_id = 492405515931090964 
# target_channel_id = 644682833511579668
'''
@tasks.loop() can be changed to seconds, minutes, hours
https://discordpy.readthedocs.io/en/latest/ext/tasks/
'''

@tasks.loop(seconds=1)
async def called_second():
    data = scrape_live_ticker()

    print(data)

    ticker_es       = data['es']
    ticker_nas      = data['nas'] 
    ticker_dow      = data['dow'] 
    ticker_vix      = data['vix']
    ticker_dollar   = data['dollar']
    ticker_gold     = data['gold']
    ticker_btc      = data['btc']
    ticker_eth      = data['eth']
    ticker_gold     = data['gold']


    ## es
    name_es = '{:20,.2f}'.format(ticker_es['last'])
    watching_es = ticker_es['change%']
    guild_channel = es_bot.get_guild(target_channel_id)

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

    ##nas
    name_nas = '{:20,.2f}'.format(ticker_nas['last'])
    watching_nas= ticker_nas['change%']
    guild_channel1 = nas_bot.get_guild(target_channel_id)

    red = get(guild_channel1.roles, name='RED')
    green = get(guild_channel1.roles, name='GREEN')

    if "-" in watching_nas:
        discord_bot = guild_channel1.me
        await discord_bot.remove_roles(green)
        await discord_bot.add_roles(red)
    else: 
        discord_bot = guild_channel1.me
        await discord_bot.remove_roles(red)
        await discord_bot.add_roles(green)
    await guild_channel1.me.edit(nick=f"2) {name_nas}")
    await nas_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"NQ {watching_nas}"))

    ## dow
    name_dow = '{:20,.2f}'.format(ticker_dow['last'])
    watching_dow = ticker_dow['change%']
    guild_channel2 = dow_bot.get_guild(target_channel_id)

    red = get(guild_channel2.roles, name='RED')
    green = get(guild_channel2.roles, name='GREEN')

    if "-" in watching_dow:
        discord_bot = guild_channel2.me
        await discord_bot.remove_roles(green)
        await discord_bot.add_roles(red)
    else: 
        discord_bot = guild_channel2.me
        await discord_bot.remove_roles(red)
        await discord_bot.add_roles(green)
    await guild_channel2.me.edit(nick=f"3) {name_dow}")
    await dow_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"DJI {watching_dow}"))

    ## vix 
    name_vix = '{:20,.2f}'.format(ticker_vix['last'])
    watching_vix = ticker_vix['change%']
    guild_channel_vix = vix_bot.get_guild(target_channel_id)

    red = get(guild_channel_vix.roles, name='RED')
    green = get(guild_channel_vix.roles, name='GREEN')

    if "-" in  watching_vix:
        discord_bot = guild_channel_vix.me
        await discord_bot.remove_roles(green)
        await discord_bot.add_roles(red)
    else: 
        discord_bot = guild_channel_vix.me
        await discord_bot.remove_roles(red)
        await discord_bot.add_roles(green)

    await guild_channel_vix.me.edit(nick=f"4) {name_vix}")
    await vix_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"VIX {watching_vix}"))

    ## dollar  
    name_dollar = '{:20,.2f}'.format(ticker_dollar['last'])
    watching_dollar = ticker_dollar['change%']
    guild_channel_dollar = dollar_bot.get_guild(target_channel_id)

    red = get(guild_channel_dollar.roles, name='RED')
    green = get(guild_channel_dollar.roles, name='GREEN')

    if "-" in  watching_dollar:
        discord_bot = guild_channel_dollar.me
        await discord_bot.remove_roles(green)
        await discord_bot.add_roles(red)
    else: 
        discord_bot = guild_channel_dollar.me
        await discord_bot.remove_roles(red)
        await discord_bot.add_roles(green)

    await guild_channel_dollar.me.edit(nick=f"5) {name_dollar}")
    await dollar_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"DXY {watching_dollar}"))

    ## gold  
    name_gold = '{:20,.2f}'.format(ticker_gold['last'])
    watching_gold = ticker_gold['change%']
    guild_channel_gold = gold_bot.get_guild(target_channel_id)

    red = get(guild_channel_gold.roles, name='RED')
    green = get(guild_channel_gold.roles, name='GREEN')

    if "-" in  watching_gold:
        discord_bot = guild_channel_gold.me
        await discord_bot.remove_roles(green)
        await discord_bot.add_roles(red)
    else: 
        discord_bot = guild_channel_gold.me
        await discord_bot.remove_roles(red)
        await discord_bot.add_roles(green)

    await guild_channel_gold.me.edit(nick=f"6) {name_gold}")
    await gold_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"GOLD {watching_gold}"))

    #shit coin stuff
    # btc
    name_btc = '{:20,.2f}'.format(ticker_btc['last'])
    watching_btc = ticker_btc['change%']
    guild_channel3 = btc_bot.get_guild(target_channel_id)

    red = get(guild_channel3.roles, name='RED')
    green = get(guild_channel3.roles, name='GREEN')

    if "-" in watching_btc:
        discord_bot = guild_channel3.me
        await discord_bot.remove_roles(green)
        await discord_bot.add_roles(red)
    else: 
        discord_bot = guild_channel3.me
        await discord_bot.remove_roles(red)
        await discord_bot.add_roles(green)
    await guild_channel3.me.edit(nick=f"7) {name_btc}")
    await btc_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"BTC {watching_btc}"))

    # eth 
    name_eth= '{:20,.2f}'.format(ticker_eth['last'])
    watching_eth = ticker_eth['change%']
    guild_channel4 = eth_bot.get_guild(target_channel_id)

    red = get(guild_channel4.roles, name='RED')
    green = get(guild_channel4.roles, name='GREEN')

    if "-" in  watching_eth:
        discord_bot = guild_channel4.me
        await discord_bot.remove_roles(green)
        await discord_bot.add_roles(red)
    else: 
        discord_bot = guild_channel4.me
        await discord_bot.remove_roles(red)
        await discord_bot.add_roles(green)
    await guild_channel4.me.edit(nick=f"8) {name_eth}")
    await eth_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"ETH {watching_eth}"))

    print(f'updated ')
    # print('something broken')

@called_second.before_loop
async def before():
    await es_bot.wait_until_ready()
    await nas_bot.wait_until_ready()
    await dow_bot.wait_until_ready()

    await dollar_bot.wait_until_ready()
    await vix_bot.wait_until_ready()

    await btc_bot.wait_until_ready()
    await eth_bot.wait_until_ready()

    await gold_bot.wait_until_ready()    
    print("Finished waiting")

called_second.start()

async def create_bots():
    es_task= loop.create_task(es_bot.start(es))
    nas_task = loop.create_task(nas_bot.start(nas))
    dow_task = loop.create_task(dow_bot.start(dow))
    vix_task = loop.create_task(vix_bot.start(vix))
    dollar_task = loop.create_task(dollar_bot.start(dollar))

    gold_task = loop.create_task(gold_bot.start(gold))

    btc_task = loop.create_task(btc_bot.start(btc))
    eth_task = loop.create_task(eth_bot.start(eth))
    

    await es_task 
    await nas_task
    await dow_task
    await vix_task
    await dollar_task 

    await gold_task

    await btc_task 
    await eth_task
    
loop.run_until_complete(create_bots())