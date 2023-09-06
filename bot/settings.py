import os
import logging
# import logging.config

from dotenv import load_dotenv


# Logging config
logging.basicConfig(level=logging.WARNING,
                    format='%(name)s::%(levelname)s::%(message)s')
logger = logging.getLogger(__name__)


# Environmental variables
load_dotenv()

try:
    BOT_TOKEN = os.environ['BOT_TOKEN']
    NOTION_API_TOKEN = os.environ['NOTION_API_TOKEN']
    DB_URL = os.environ['DB_URL']
    API_SERVER_URL = os.environ['API_SERVER_URL']
except KeyError:
    raise ValueError('Please set env variables')


BOT_API_DIR = '/var/lib/telegram-bot-api'
CACHE_DIR = '~/.cache/gkbot'


ADMINS = [
    897651738
]


MODELS = [
    'models.users',
    'models.road',
    'models.books',
    'models.timezone',
    'models.tasks',
]


DEFAULT_COMMANDS = {
    'list': 'list of possible bot commands',
    'road': 'road to the dream',
    'bomber': 'use it for call someone',
    'add_remind': 'add remind',
    'start_timer': 'start timer',
    'admins': 'tag all admins',
    'books': 'personal book shelf',
    'platonus2indigo': 'convert test',
    'dl': 'download file',
}
