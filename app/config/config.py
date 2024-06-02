from typing import Final
import redis
import telegram

Token: Final = ""  ## get this in discord
BOT_USERNAME: Final = "@ethan_test_translate_bot"
OPEN_AI_KEY: Final = ""  ## get this in discord
channel_id = '-1001878865896'

redis_host = 'localhost'
redis_port = 6379
db = 0
password = 'abc123'

# channels = ["unfolded", "ico_analytic", "crypto_fundraising", "Generation_Crypto", "top7ico", "cryptodiffer", "binance_announcements", "icodrops", "WatcherGuru", "chain_broker"]
# channels = ["Generation_Crypto", "top7ico", "cryptodiffer", "binance_announcements", "icodrops", "WatcherGuru", "chain_broker"]
channels = ["top7ico", "WatcherGuru", "chain_broker"]

url = 'https://t.me/s/'


# Connect to Redis
def get_redis_instance():
    return redis.StrictRedis(host='localhost', port=6379, db=0, password="abc123", decode_responses=True)


def get_telegram_bot():
    return telegram.Bot(token=Token)
