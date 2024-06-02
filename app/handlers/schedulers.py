from app.config.config import channels
from app.handlers.scrap_and_send import scrap_channel
import asyncio


async def repeat_task():
    first_start = True
    while True:
        for channel in channels:
            await scrap_channel(channel, first_start)
        first_start = False
        await asyncio.sleep(10)


async def run_scheduler():
    print("Starting bot...")
    await repeat_task()
