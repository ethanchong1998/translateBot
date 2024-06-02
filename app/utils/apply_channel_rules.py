from app.config.channel_rules import top7ico_rules


async def apply_channel_rules(channel, msg):
    formatted_msg = msg
    if channel == "top7ico":
        formatted_msg = top7ico_rules(msg)
    return formatted_msg
