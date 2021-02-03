from discord.ext import commands, tasks
from discord import Member
import discord
import re
import json 
import time 
import random
import asyncio
import requests
import os
import datetime

from tokens import optional_ticker_1, silver

optional_bot_1 = commands.Bot(command_prefix='.')
optional_bot_2 = commands.Bot(command_prefix='..')
optional_bot_3 = commands.Bot(command_prefix='...')

## for testing new stuff in another server without having to restart the main bot 


@optional_bot_1.event
async def on_ready():
    print('option 1 ready')

# @optional_bot_2.event
# async def on_ready():
#     print('option 2 ready')

# @optional_bot_3.event
# async def on_ready():
#     print('option 3 ready')

# target_channel_id = 492405515931090964 
target_channel_id = 644682833511579668
@optional_bot_1.command()
async def track(ctx, *arg):
    if arg and len(arg) == 2:
        print('in track for optional bot 1 and condition have been met')

# for getting guild id for every server the bot has joined
@optional_bot_1.command()
async def test(ctx, *arg):
    guilds = [guild.id for guild in optional_bot_1.guilds]
    print(guilds)
    
    

optional_bot_1.run(silver)
