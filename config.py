import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22283740"))
API_HASH = getenv("API_HASH", "e3c4927cbd996aa6b1f6f8bfc776fdfb")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7011958035:AAF-XzO3tGG88IqHh61FL1WzzMaeURBNQwM")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://titlybanerjee302:sayantika@839108@cluster0.xdqrm9p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID","1002036934742"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6404269843"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("sayantikamusictmpcbot")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-18d1801f-4324-47a5-8686-950f9157f6e6")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/abhjkfv")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+XvYOooluvFtkYzdl")

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
STRING1 = getenv("BQFUBdwAhHXGcgR5xVLxLhKJDWtVfc9dGkRJppIm4B27UY6D2ibTAy25FL8DPMRWbzxYNEYi9qpyCEWYcPw1g1oYSx6SZTievabVEmEJhD7GM1Z3ZaS-cavd8M8CMyhDiaxZq1OuvzpEYEpb-nHWpewHQDPnlQz_lcXJ1IKar--1CUNmAnWGqt7ZCaXtdiZkO1G1s4cx9bzwHeMx9jChuC7Py0sgYu_8qco1jCy30C5Z9CPgmG4DX0myBlrz17PbTo2_ShItMDIegmkVrrRar1nvtSAsAJWFETkEr1m-NhzRBBJGNVHWqgWPawF9b5XUVBCXIaQ-nFO_W5GH9Xafd9EsidVarwAAAAF9uWcTAA")
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
    "START_IMG_URL", "https://graph.org/file/3ceff950d08ac1b3c5537.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/2e4866e6d8b9844e09a1c.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
STATS_IMG_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
STREAM_IMG_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b490638fd73cd0ec1d1ad.jpg"


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
