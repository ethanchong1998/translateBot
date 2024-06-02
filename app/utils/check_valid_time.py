from datetime import datetime, timedelta

valid_time_range = 24 #hours


def checkValidTime(chat) -> bool:
    chat_time = chat.xpath('.//a[contains(@class,"tgme_widget_message_date")]/time/@datetime')[0]
    formatted_chat_time = datetime.fromisoformat(chat_time)

    local_tz = datetime.now().astimezone().tzinfo # get local timezone
    local_chat_time = formatted_chat_time.astimezone(local_tz).replace(tzinfo=None) # convert to local datetime
    now = datetime.now()
    time_diff = now - local_chat_time

    return timedelta(hours=valid_time_range) >= time_diff > timedelta(0)