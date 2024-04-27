from lxml import html
import requests

url = 'https://t.me/s/unfolded'

page = requests.get(url)
content = page.content

parsed_content = html.fromstring(content)
# tree = html.fromstring(page.content)

chats_raw = parsed_content.xpath('//div[contains(@class,"tgme_widget_message_text")]')

# for chat_raw in chats_raw:
#     print(chat_raw.text)
last_chat = len(chats_raw) - 1
print(chats_raw[last_chat].text)

# for chat_raw in chats_raw:
    