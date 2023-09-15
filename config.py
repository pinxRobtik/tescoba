import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(os.environ.get("API_ID", None))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
SESSION = os.environ.get("SESSION", None)
SUDOERS = list(map(int, os.environ.get("SUDOERS", "").split()))
BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001861414061]
BLACKLIST_GCAST = {int(x) for x in os.environ.get("BLACKLIST_GCAST", "").split()}
BRANCH = os.environ.get("BRANCH", "magic")
DB_URL = os.environ.get("DATABASE_URL", None)
HEROKU_API = os.environ.get("HEROKU_API", None)
HEROKU_NAME = os.environ.get("HEROKU_NAME", None)
REPO_URL = os.environ.get("REPO_URL", "https://github.com/Team-Pesulap/MagicProject")
