from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
import telegram
from app.config import Token, channel_id
from app.utils import translate_message

bot = telegram.Bot(token=Token)

async def send_message(text: str):

    print(text)
    response: str = translate_message(text)
    if not response == "":
        print("Sending message....")
        emoji: str = "\u26a1" * 8
        post_message: str = emoji + "\n \n" + response + "\n\n\U000027a1 <a href='https://t.me/telonews_cn/'>Telegram</a> \U000027a1 <a href='https://twitter.com/telo_official/'>Twitter</a> \n\U0001F4AC <a href='https://t.me/telochat_cn/'>社区</a>"
        await bot.send_message(chat_id=channel_id, text=post_message, parse_mode=ParseMode.HTML)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
