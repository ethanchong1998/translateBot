from app.config.config import get_db_instance
from app.utils.scrap_tg import scrap_tg_post_content

db_instance = get_db_instance()


async def check_previous_post(channel, posts):
    for post_index, post in enumerate(posts):
        if not not_previous_post_value(channel, post):
            return post_index + 1

    return 0


def not_previous_post_value(channel: str, post: str) -> bool:
    current_scrap_value = scrap_tg_post_content(post)
    try:
        prev_value = db_instance.get_string(channel)
    except ValueError:
        prev_value = ""
    return current_scrap_value != prev_value
