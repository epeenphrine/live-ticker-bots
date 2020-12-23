#%%
from Bot import Bot
import asyncio
from live_ticker_scrape import  scrape_live_ticker
from tokens import dev1
import time

data = None
async def run_scrape():
    global data
    data = scrape_live_ticker()

async def run_job():
    while True:
        await run_scrape() 
        print(data)
        time.sleep(1)

#prod
guild_id = 492405515931090964

#test 
guild_id = 644682833511579668
es = dev1
nas = "Nzg2MTUxNjQ5Njc1NzA2Mzcw.X9COxw._rAVVXrj65ypBNjbP8aMEII7e-s"

es_bot = Bot()
es_bot.data = data
es_bot.guild_id = guild_id
es_bot.token = es
es_bot.start()

# nas_bot = Bot()
# nas_bot.guild_id = guild_id
# nas_bot.token = nas
# nas_bot.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(run_job())
print(data)