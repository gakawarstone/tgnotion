from lib.bot import Bot
from lib.schedule import Schedule
import os

# VARS
IN_HEROKU = os.environ.get('IN_HEROKU')
if IN_HEROKU:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
    NOTION_API_TOKEN = os.environ.get('NOTION_API_TOKEN')
    # Heroku PostgreSQL server
    DATABASE_URL = os.environ.get('DATABASE_URL')
else:
    import env
    BOT_TOKEN = env.BOT_TOKEN
    NOTION_TOKEN = env.NOTION_TOKEN
    NOTION_API_TOKEN = env.NOTION_API_TOKEN
    LOCAL_DB_USER_PSWD = env.LOCAL_DB_USER_PSWD

# main objects
bot = Bot(BOT_TOKEN)
schedule = Schedule()
