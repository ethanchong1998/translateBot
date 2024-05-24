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
        post_message: str = emoji + "\n \n" + response + "\n\n <a href='https://www.google.com/'>Google</a> <a href='https://www.google.com/'>Google</a> <a href='https://www.google.com/'>Google</a>"
        await bot.send_message(chat_id=channel_id, text=post_message, parse_mode=ParseMode.HTML)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
