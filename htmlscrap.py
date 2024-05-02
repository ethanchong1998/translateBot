from lxml import html
from typing import Final
from telegram import Update
import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN: Final = '7084839341:AAE5pk5zqW0g3n36kTizAlL33zzcRl1aeMk'
BOT_USERNAME: Final = '@ethan_test_translate_bot'
url1 = 'https://t.me/s/unfolded'
url2 = 'https://t.me/s/crypto_fundraising'
url3 = 'https://t.me/s/ico_analytic'

#posting channel can change here
channel_id = '-1001878865896'

bot = telegram.Bot(token=TOKEN)
async def scrapMessage(url):
    page = requests.get(url)
    content = page.content
    parsed_content = html.fromstring(content)

    chats_raw = parsed_content.xpath('//div[contains(@class,"tgme_widget_message_text")]/text()')

    last_chat_index = len(chats_raw) - 1
    last_message = chats_raw[last_chat_index]
    print(last_message)
    return last_message

async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.channel_post.text #text content
    print(text)

    if 'scrap' in text:
        await bot.send_message(chat_id=channel_id, text="Scraping, please wait...")
        response1: str = await scrapMessage(url1)
        response2: str = await scrapMessage(url2)
        response3: str = await scrapMessage(url3)

        await bot.send_message(chat_id=channel_id, text=response1)
        await bot.send_message(chat_id=channel_id, text=response2)
        await bot.send_message(chat_id=channel_id, text=response3)
    else:
        return

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT, send_message))

    #Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)
