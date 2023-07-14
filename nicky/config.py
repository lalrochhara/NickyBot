from nicky.sample_config import Config


class Development(Config):
    OWNER_ID = "894380120" # your telegram ID; easiest way is to search and start 'userinfobot' from Telegram directory
    OWNER_USERNAME = "nickylrca"  # your telegram username; if you don't have one, set one
    API_KEY = ""  # bot api token, as provided by the botfather (yes, daddy)
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = "" # group-chat/channel id; dumps logs as messages in dedicated room
    USE_MESSAGE_DUMP = True # set true/false to log or not
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = [] # choose which modules to load
    NO_LOAD = [android.py, memes.py, webtools.py] # choose which modules to exclude
    TELETHON_HASH = "" # api_hash from my.telegram.org
    TELETHON_ID = "" # api_id from my.telegram.org
