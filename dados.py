from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
BOT_TOKEN = getenv("BOT_TOKEN", "1978585012:AAH5twyVYxgpKkF1QDMSBbZoJBayLpf9TSs")
POST_CANAL = getenv("POST_CANAL", "1490373082")