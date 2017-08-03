import logging
import bot_define

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Telegram'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_IDENTITY = {
        'token': TELEGRAM_BOT_TOKEN
        }

BOT_DATA_DIR = BOT_HOME_DIR + r'/data'
BOT_EXTRA_PLUGIN_DIR = BOT_HOME_DIR + '/plugins'

BOT_LOG_FILE = BOT_HOME_DIR + r'/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = (BOT_ADMIN_ID, )  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!

CHATROOM_PRESENCE = ()

BOT_PREFIX = '/'
