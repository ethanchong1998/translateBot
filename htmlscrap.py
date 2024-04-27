from lxml import html
import requests
import sched
import time


scheduler = sched.scheduler(time.time, time.sleep)
url = 'https://t.me/s/unfolded'

def scrap_channel():

    page = requests.get(url)
    content = page.content
    parsed_content = html.fromstring(content)
    # tree = html.fromstring(page.content)

    chats_raw = parsed_content.xpath('//div[contains(@class,"tgme_widget_message_text")]')

    # for chat_raw in chats_raw:
    #     print(chat_raw.text)
    last_chat = len(chats_raw) - 1

    print(chats_raw[last_chat].text)


def repeat_task():
    scheduler.enter(5, 1, scrap_channel, ())
    scheduler.enter(5, 1, repeat_task, ())

repeat_task()
scheduler.run()
