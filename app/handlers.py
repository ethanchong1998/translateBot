from telegram import Update
from telegram.ext import ContextTypes
import telegram
from app.config import Token, channel_id
from app.utils import translate_message

bot = telegram.Bot(token=Token)

async def send_message(text: str):

    # prevent scrapping some nonsense

    response: str = translate_message(text)
    print("Sending message....")
    await bot.send_message(chat_id=channel_id, text=response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
