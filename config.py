import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7011958035:AAF-XzO3tGG88IqHh61FL1WzzMaeURBNQwM")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://titlybanerjee302:sayantika@839108@cluster0.xdqrm9p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "1002036934742"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6404269843"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/abhjkfv")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/abhjkfv")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
STATS_IMG_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
STREAM_IMG_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/5705ec3e3c9acfa2c32ff.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
