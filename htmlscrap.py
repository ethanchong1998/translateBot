import asyncio
import time
import requests
import redis
import telegram
from lxml import html
from app.config import Token, url, channels, channel_id
from app.handlers import send_message, error

r = redis.StrictRedis(host='localhost', port=6379, db=0, password="abc123", decode_responses=True)
bot = telegram.Bot(token=Token)

async def scrap_channel(channel):
    print("Scraping " + channel)
    page = requests.get(url + channel)
    content = page.content
    parsed_content = html.fromstring(content)
    chats_raw = parsed_content.xpath('//div[contains(@class,"tgme_widget_message_text")]/text()')
    if chats_raw:
        last_chat_value = chats_raw[-1]  # Get the last message
        if getPreviousChannelValue(channel, last_chat_value):
            if len(last_chat_value.split()) < 1000:
                await bot.send_message(chat_id=channel_id, text="Something is wrong with " + channel)
                print("Something is wrong with " + channel)
            else:
                r.set(channel, last_chat_value)
                await send_message(last_chat_value)
                print(last_chat_value)

def getPreviousChannelValue(channel: str, current_scrap_value: str) -> bool:
    prev_value = r.get(channel)
    return current_scrap_value != prev_value

async def repeat_task():
    while True:
        for channel in channels:
            await scrap_channel(channel)
        await asyncio.sleep(10)

async def main():
    print("Starting bot...")
    await repeat_task()

if __name__ == '__main__':
    print("Polling...")
    asyncio.run(main())
