import requests
from app.config.config import url
from lxml import html


def scrap_tg_channel(channel: str) -> str:
    print("Checking channel " + channel)
    page = requests.get(url + channel)
    content = page.content
    parsed_content = html.fromstring(content)
    chats_raw = parsed_content.xpath('//div[contains(@class,"tgme_widget_message_bubble")]')
    return chats_raw


def scrap_tg_post_content(post: str) -> str:
    chat_content = post.xpath('.//div[contains(@class,"tgme_widget_message_text")]//text()')
    chat_content = ''.join(chat_content).strip()
    return chat_content
