import re
from os import environ

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
API_ID = int(environ.get('API_ID','6595979'))
API_HASH = environ.get('API_HASH','b9625545e9f261a600a049de0b0c310f')
BOT_TOKEN = environ.get('BOT_TOKEN','5446097446:AAFsqwv4C_xXAIrYGrWhaWEXsakLmdAdooc')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/409aa76ac48880b9ec372.jpg https://telegra.ph/file/8b1667c39b2f7ae3a098a.jpg https://telegra.ph/file/ba5a1c44b0b539a3833f3.jpg https://telegra.ph/file/d953c8b31ae4366a13a39.jpg https://telegra.ph/file/a7fc7fa687ee022ed853e.jpg https://telegra.ph/file/91ea6b58ab3dce3406d8e.jpg https://telegra.ph/file/5a8d1dead0a522c4cab95.jpg https://telegra.ph/file/4d840087dc3a1e1d08b2c.jpg https://telegra.ph/file/7d3401b366294fbee7dc7.jpg https://telegra.ph/file/d288630be65014ae293f1.jpg https://telegra.ph/file/1e8633bd9a318bef75e49.jpg https://telegra.ph/file/4879e36e11b66215a239c.jpg https://telegra.ph/file/7b9a03a3a72f1d8780f1c.jpg https://telegra.ph/file/b2f835904130fa125fdc3.jpg https://telegra.ph/file/347e209d961ad14dd1c51.jpg https://telegra.ph/file/854cdc547322b546e2129.jpg https://telegra.ph/file/c4761a91947fb9fe3bf21.jpg https://telegra.ph/file/570b9488a925baf24574e.jpg https://telegra.ph/file/e7df0a5fb705e65988a68.jpg https://telegra.ph/file/4326c264ace2262182119.jpg https://telegra.ph/file/990256fc14e3bf0bf1022.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1573108290 1167310327').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002080383910 -1001396095544 -1001620200646 -1001732737927 -1001551816705 -1001690448036 -1001622478032 -1001566642237 -1001705433155 -1001584832671 -1001519694012 -1001565676692 -1001586913070 -1001784709266 -1001793950262 -1001645647150 -1001509224438 -1001537303459 -1001797222352').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '').split()]
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
NON_AUTH_GROUPS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('NON_AUTH_GROUPS', '').split()]


# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "sahan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Narutoo:Narutoo111@cluster0.axhiqdd.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
FILES_DB_URL = environ.get('FILES_DB_URL', "mongodb+srv://sinhalasub:sinhalasubbot@cluster0.cfk9dts.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001514899549'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<code>{file_name}</code>\n‌‌‌‌\n<b>BOT PROBLEM? <a href='https://t.me/SECL4U/54'>USE ANOTHER</a></b> \n‌‌‌‌<b>HOW TO USE ? <a href='https://t.me/SECOfficial_Bot'>WATCH THIS</a></b>\n‌‌‌‌\n<b>- @SECLK | @CeylonCryptoSL -</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🎬 <b><a href={url}>{title}</a> ({year})</b>\n‌‌‌‌<b>{runtime}min | {release_date}</b>\n‌‌‌‌\n‌‌‌‌<b>⭐️ IMDB</b> ➠ <b><i>{rating}/10 ({votes})</i></b>\n‌‌‌‌<b>🌏 Country</b> ➠ <b><i>{countries}</i></b>\n<b>🔉 Language</b> ➠ <b><i>{languages}</i></b>\n‌‌‌‌‌‌‌‌‌‌‌‌<b>⚙️ Genres</b> ➠ <b><i>{genres}</i></b>\n‌‌‌‌\n‌‌‌‌®️ <b><a href='https://t.me/SECL4U'>Mαιɴ Cнαɴɴel</a></b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
