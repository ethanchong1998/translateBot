from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from app.config.config import get_telegram_bot
from app.config.config import channel_id
from app.utils.format_mesasge import get_extracted_url


bot = get_telegram_bot()


async def send_message(response: str):
    extracted_url = get_extracted_url()
    if not response == "":
        print("Sending message....")
        emoji: str = "\u26a1" * 8
        post_message: str = "Daily News" + "\n \n" + response + (f"\n\n<a href='{extracted_url}'>— link</a>" if extracted_url else "")
        await bot.send_message(chat_id=channel_id, text=post_message, parse_mode=ParseMode.HTML,
                               disable_web_page_preview=True)
        print('posting: {}\n'.format(post_message))


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
