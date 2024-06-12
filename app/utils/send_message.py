from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from urlextract import URLExtract

from app.config.config import get_telegram_bot
from app.config.config import channel_id

bot = get_telegram_bot()


async def send_message(response: str):
    if not response == "":
        print("Sending message....")
        emoji: str = "\u26a1" * 8
        modified_response = replace_urls(response)
        post_message: str = emoji + "\n \n" + modified_response + "\n\n\U000027a1 <a href='https://t.me/telonews_cn/'>Telegram</a> \U000027a1 <a href='https://twitter.com/telo_official/'>Twitter</a> \n\U0001F4AC <a href='https://t.me/telochat_cn/'>社区</a>"
        await bot.send_message(chat_id=channel_id, text=post_message, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        print('posting: {}\n'.format(post_message))


def replace_urls(text: str) -> str:
    extractor = URLExtract()
    urls = extractor.find_urls(text)
    for url in urls:
        text = text.replace(url, f"<a href='{url}'>— link</a>")
        print("replaced:", text)

    return text


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
