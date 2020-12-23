import asyncio
from time import sleep
import discord
import discord.ext.commands
from discord.ext import tasks
from discord.utils import get
from live_ticker_scrape import scrape_live_ticker

class Bot(object):
    client: discord.Client

    task = None

    guild_id = None

    guild_channel = None

    red = None

    green = None

    token = ""

    loop = None
    
    data = None
    print(data)

    def start(self):
        self.client = discord.Client()
        self.on_ready = self.client.event(self.on_ready)
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.__start())

    async def __start(self):
        await self.create()
        await self.client.wait_until_ready()

    async def on_ready(self):
        print("started")
        self.guild_channel = self.client.get_guild(self.guild_id)
        self.red = get(self.guild_channel.roles, name='RED')
        self.green = get(self.guild_channel.roles, name='GREEN')
        self.process.start()

    async def create(self):
        self.task = self.loop.create_task(self.client.start(self.token))
        await self.task

    @tasks.loop(seconds=1)
    async def process(self):
        if self.data:
            print(self.data)
            print('hello world')
            name = '{:20,.2f}'.format(self.data['last'])
        print('outside if')
        print(self.data)
        # change_percent = key['change%']
        # if "-" in change_percent:
        #     discord_bot = self.guild_channel.me
        #     await discord_bot.remove_roles(self.green)
        #     await discord_bot.add_roles(self.red)
        # else:
        #     discord_bot = self.guild_channel.me
        #     await discord_bot.remove_roles(self.red)
        #     await discord_bot.add_roles(self.green)
        # await self.guild_channel.me.edit(nick=f"{value} - {name}")
        # await self.client.change_presence(activity=discord.Activity(
        #     type=discord.ActivityType.watching,
        #     name=f"{value} {change_percent}"))