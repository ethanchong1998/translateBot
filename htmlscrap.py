import asyncio
import time
import requests
import redis
import telegram
from lxml import html
from app.config import Token, url, channels, channel_id
from app.handlers import send_message, error
from datetime import datetime, timedelta

r = redis.StrictRedis(host='localhost', port=6379, db=0, password="abc123", decode_responses=True)
bot = telegram.Bot(token=Token)
valid_time_range = 24 #hours

async def checkPreviousPost(channel):
    print("Checking channel " + channel)
    page = requests.get(url + channel)
    content = page.content
    parsed_content = html.fromstring(content)
    chats_raw = parsed_content.xpath('//div[contains(@class,"tgme_widget_message_bubble")]')
    
    last_index = len(chats_raw) - 1

    for x, chat_raw in enumerate(chats_raw):
        chat_content = chat_raw.xpath('.//div[contains(@class,"tgme_widget_message_text")]/text()')[0]
        print('Checking post no.{}'.format(x))
        if not getPreviousChannelValue(channel, chat_content): # last scrapped message
            if not x == last_index:
                print("Missed message detected")
                for chat_raw in chats_raw[x+1:]:
                    if(checkValidTime(chat_raw)):
                        print("Posting missed message in channel {}".format(channel))
                        chat_content = chat_raw.xpath('.//div[contains(@class,"tgme_widget_message_text")]/text()')[0]
                        r.set(channel, chat_content)
                        await send_message(chat_content)
                        print('posting: {}\n'.format(chat_content))
            break
        elif x == last_index: # All 20 message missed
            for chat_raw in chats_raw:
                if(checkValidTime(chat_raw)):
                    print("finding missed posts")
                    chat_content = chat_raw.xpath('.//div[contains(@class,"tgme_widget_message_text")]/text()')[0]
                    print('posting: {}\n'.format(chat_content))
                    r.set(channel, chat_content)
                    await send_message(chat_content)
            
    
async def scrap_channel(channel):
    print("Scraping " + channel)
    page = requests.get(url + channel)
    content = page.content
    parsed_content = html.fromstring(content)
    chats_raw = parsed_content.xpath('//div[contains(@class,"tgme_widget_message_bubble")]')
     
    if chats_raw:
        last_chat = chats_raw[-1]
        last_chat_value = last_chat.xpath('.//div[contains(@class,"tgme_widget_message_text")]/text()')[0] # Get the last message

        if getPreviousChannelValue(channel, last_chat_value):
            if len(last_chat_value.split()) > 1000:
                print("Something is wrong with " + channel)
            else:
                r.set(channel, last_chat_value)
                await send_message(last_chat_value)
                print('Posted in channel {}: {}',format(channel,last_chat_value))

def getPreviousChannelValue(channel: str, current_scrap_value: str) -> bool:
    prev_value = r.get(channel)
    return current_scrap_value != prev_value

def checkValidTime(chat) -> bool:
    chat_time = chat.xpath('.//a[contains(@class,"tgme_widget_message_date")]/time/@datetime')[0]
    formatted_chat_time = datetime.fromisoformat(chat_time)

    local_tz = datetime.now().astimezone().tzinfo # get local timezone
    local_chat_time = formatted_chat_time.astimezone(local_tz).replace(tzinfo=None) # convert to local datetime
    now = datetime.now()
    time_diff = now - local_chat_time

    return timedelta(hours=valid_time_range) >= time_diff > timedelta(0)

async def repeat_task():
    while True:
        for channel in channels:
            await scrap_channel(channel)
        await asyncio.sleep(10)

async def main():
    print("Starting bot...")
    for channel in channels: # initially run one time only
        await checkPreviousPost(channel)
    await repeat_task()

if __name__ == '__main__':
    print("Polling...")
    asyncio.run(main())
