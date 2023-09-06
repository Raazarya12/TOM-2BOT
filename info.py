import re
from os import environ
from Script import script

from time import time


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']


# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
BOT_START_TIME = time()

PICS = (environ.get('PICS', 'https://telegra.ph/file/6a0726f79acd8300e9a04.jpg https://telegra.ph/file/68289fefb76dbc43b766d.jpg https://telegra.ph/file/0caad29c0cf91c23fb1b6.jpg https://telegra.ph/file/8c34c755dd16581c1c6b5.jpg https://telegra.ph/file/365e35b554e5a3ea83857.jpg https://telegra.ph/file/07f185825c5b7bfd6fbfb.jpg https://telegra.ph/file/85f95494565a762edb3e7.jpg https://telegra.ph/file/708a1d6ce805fcc6a46d0.jpg https://telegra.ph/file/d799c1a964f211028cc97.jpg https://telegra.ph/file/b987425b80bca0cf45c7e.jpg https://telegra.ph/file/2a8b3779760289b76de24.jpg https://telegra.ph/file/47961be968719b3e24cf0.jpg https://telegra.ph/file/2e127b0f6b1810d733c09.jpg https://telegra.ph/file/281b18770a43a29120252.jpg https://telegra.ph/file/2086dd2aa8382e758a599.jpg https://telegra.ph/file/fcc849db4bf5c517f0f8d.jpg')).split()
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/f7f2a532fe4b990044507.mp4")
NOR_IMG = (environ.get("NOR_IMG","")).split()
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/6bb65e84e95b708f7be7a.jpg")
CLOSE_IMG = (environ.get('CLOSE_IMG', 'https://telegra.ph/file/6e9dd701bac49632cf79a.jpg https://telegra.ph/file/998d2b84e1411ed5189e3.jpg https://telegra.ph/file/c199babd469011d07f139.jpg https://telegra.ph/file/31b6d3d2c70bbe52b5300.jpg https://telegra.ph/file/77744524fbb6305298d45.jpg https://telegra.ph/file/9d79d990674166a2a2364.jpg')).split()
JOIN_IMG = (environ.get('JOIN_IMG', 'https://telegra.ph/file/2718e562b65da275a7c56.jpg https://telegra.ph/file/a32c89628fa5444dc4a49.jpg https://telegra.ph/file/03bd753c7d9ca801ef5c3.jpg https://telegra.ph/file/ef824cc41a4795ddb1053.png https://telegra.ph/file/45c5df081bd4c631aca0d.jpg')).split()
                    
# Admins, Log, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5554564210 1985196029 5069888600').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001572383457').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5554564210').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
login_channel = environ.get('LOGIN_CHANNEL')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
LOGIN_CHANNEL = int(login_channel) if login_channel and id_pattern.search(login_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# Custom Chats
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', '0'))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', '0')

#VALUES
HRK_APP_NAME = environ.get('HRK_APP_NAME', 'mybots')
HRK_API = environ.get('HRK_API', '0')

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', '')

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", False)
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)
group_sub = environ.get('GROUP_SUB')
GROUP_SUB = int(group_sub) if group_sub and id_pattern.search(group_sub) else None

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnlink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '826eb92e893f6fdb42920983bba04c409bdc0b5d')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "False")), False)
S_GROUP = environ.get('S_GROUP',"https://t.me/Mix_Cinema_Box")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/Latest_movies_freeOnNet")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Mix_Cinema_Box')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Latest_movies_freeOnNet')
MSG_ALRT = environ.get('MSG_ALRT', 'Piracy Is Crime')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001801990402))
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Request_Corner1')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada"]

# Delete Time
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB_DLT_TIME = int(environ.get('IMDB_DLT_TIME', 300))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
