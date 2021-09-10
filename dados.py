from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
BOT_TOKEN = getenv("BOT_TOKEN", "")
POST_CANAL = getenv("POST_CANAL", "")
