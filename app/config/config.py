from typing import Final
import telegram
from goshdb import authenticate, Table
from pathlib import Path

# Take spreadsheet ID from your spreadsheet URL:
# https://docs.google.com/spreadsheets/d/[SPREADSHEET_ID]/edit#gid=0
SPREADSHEET_ID = '1En34KrTyWHCpfHapxWlp0r9FHQWPmhXdMZdlXBdR23M'
# Provide a sheet name. It should be either new sheet or existing one that follows the required structure.
SHEET_NAME = 'scrap_db'

# Authenticate
creds = authenticate(Path('./app/config/'))


# Create a Table object. If you do this for the first time - it'll open a browser window (see Step 3 details)
def get_db_instance():
    return Table(
        creds=creds,
        spreadsheet_id=SPREADSHEET_ID,
        table_name=SHEET_NAME
    )


Token: Final = "7084839341:AAE5pk5zqW0g3n36kTizAlL33zzcRl1aeMk"  ## get this in discord
BOT_USERNAME: Final = "@ethan_test_translate_bot"
OPEN_AI_KEY: Final = ""  ## get this in discord
channel_id = '-1002076231534' #-1001878865896 test-bot-channel

redis_host = 'localhost'
redis_port = 6379
db = 0
password = 'abc123'

# channels = ["unfolded", "ico_analytic", "crypto_fundraising", "Generation_Crypto", "top7ico", "cryptodiffer", "binance_announcements", "icodrops", "WatcherGuru", "chain_broker"]
channels = ["Generation_Crypto", "top7ico", "cryptodiffer", "binance_announcements", "icodrops", "WatcherGuru", "chain_broker"]
# channels = ["cryptodiffer"]

url = 'https://t.me/s/'


def get_telegram_bot():
    return telegram.Bot(token=Token)
