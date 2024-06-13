from app.config.config import get_redis_instance
from app.utils.check_previous_post import check_previous_post, not_previous_post_value
from app.utils.check_valid_time import checkValidTime
from app.utils.scrap_tg import scrap_tg_channel, scrap_tg_post_content
from app.utils.send_message import send_message
from app.utils.translator import translate_message
from app.utils.format_mesasge import format_message

redis_instance = get_redis_instance()


async def scrap_channel(channel, first_start=False):
    channel_posts = scrap_tg_channel(channel)
    if channel_posts and len(channel_posts) > 1:
        print("Scraping " + channel)
        if first_start:
            print("First start....")
            index = await check_previous_post(channel, channel_posts)
            for post in channel_posts[index:]:
                await translate_and_send(channel, post)
        else:
            latest_post = channel_posts[-1]
            if not_previous_post_value(channel, latest_post):
                await translate_and_send(channel, latest_post)


async def translate_and_send(channel, post):
    post_content = scrap_tg_post_content(post)
    if checkValidTime(post) and content_check(post_content):
        redis_instance.set(channel, post_content)
        translated_msg = translate_message(post_content)
        formatted_msg = format_message(translated_msg, channel)
        await send_message(formatted_msg)
        print('Posted in channel {}: {}'.format(channel, formatted_msg))


def content_check(chat_content: str):  # to prevent translating garbage
    if chat_content and not chat_content.strip() == "" and len(chat_content.split()) < 1000:
        return True
    else:
        return False
