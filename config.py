import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("24233765"))
API_HASH = getenv("519019f681bf355123c3422a7379bc02")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7396064045:AAGWwVUcgWcu_WirDlBXs0rdE4xEqob1pCo")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://Sawn02:Sawn02@cluster0.twinbpi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("1002162980134))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("7408682347"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("3a57e70f-f56c-477f-861d-7eb0e446b598")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

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
STRING1 = getenv("BQFxxyUAttj3mGtobg9lipwUGa9CsksS8EmY8JPf-6x6nMVoM8pJ1fPSFsOoxnYwR6lp6Vw8jzmpnl4q-QKkz441vwwt9YoEKqeCs7ne4HZhAeblegrdHpo2daChUP9YaOwngk3NqWPz1yrZ2o_TeBDLXUMtHUzkagAyCXzvo98ZySB-xD_PYU84viAW9LzUuPaWFcEiwopnYJHgJIlSCal8cM9iy7EyKz3VoxZnpy1QIw0el_MmJdwZ5QAklyTH4NNKzTzy8CiVJeYnxzelmrbHFd5ylFvJqmMgIFvAa5BOZHvuEsOm8dbS5iuTHWJacfJ0flQv-SkDRrq-pdVkJvUpPXbAbQAAAAFfgjemAA")
STRING2 = getenv("BQFxxyUAttj3mGtobg9lipwUGa9CsksS8EmY8JPf-6x6nMVoM8pJ1fPSFsOoxnYwR6lp6Vw8jzmpnl4q-QKkz441vwwt9YoEKqeCs7ne4HZhAeblegrdHpo2daChUP9YaOwngk3NqWPz1yrZ2o_TeBDLXUMtHUzkagAyCXzvo98ZySB-xD_PYU84viAW9LzUuPaWFcEiwopnYJHgJIlSCal8cM9iy7EyKz3VoxZnpy1QIw0el_MmJdwZ5QAklyTH4NNKzTzy8CiVJeYnxzelmrbHFd5ylFvJqmMgIFvAa5BOZHvuEsOm8dbS5iuTHWJacfJ0flQv-SkDRrq-pdVkJvUpPXbAbQAAAAFfgjemAA"")
STRING3 = getenv("BQFxxyUAttj3mGtobg9lipwUGa9CsksS8EmY8JPf-6x6nMVoM8pJ1fPSFsOoxnYwR6lp6Vw8jzmpnl4q-QKkz441vwwt9YoEKqeCs7ne4HZhAeblegrdHpo2daChUP9YaOwngk3NqWPz1yrZ2o_TeBDLXUMtHUzkagAyCXzvo98ZySB-xD_PYU84viAW9LzUuPaWFcEiwopnYJHgJIlSCal8cM9iy7EyKz3VoxZnpy1QIw0el_MmJdwZ5QAklyTH4NNKzTzy8CiVJeYnxzelmrbHFd5ylFvJqmMgIFvAa5BOZHvuEsOm8dbS5iuTHWJacfJ0flQv-SkDRrq-pdVkJvUpPXbAbQAAAAFfgjemAA"")
STRING4 = getenv("BQFxxyUAttj3mGtobg9lipwUGa9CsksS8EmY8JPf-6x6nMVoM8pJ1fPSFsOoxnYwR6lp6Vw8jzmpnl4q-QKkz441vwwt9YoEKqeCs7ne4HZhAeblegrdHpo2daChUP9YaOwngk3NqWPz1yrZ2o_TeBDLXUMtHUzkagAyCXzvo98ZySB-xD_PYU84viAW9LzUuPaWFcEiwopnYJHgJIlSCal8cM9iy7EyKz3VoxZnpy1QIw0el_MmJdwZ5QAklyTH4NNKzTzy8CiVJeYnxzelmrbHFd5ylFvJqmMgIFvAa5BOZHvuEsOm8dbS5iuTHWJacfJ0flQv-SkDRrq-pdVkJvUpPXbAbQAAAAFfgjemAA"")
STRING5 = getenv("BQFxxyUAttj3mGtobg9lipwUGa9CsksS8EmY8JPf-6x6nMVoM8pJ1fPSFsOoxnYwR6lp6Vw8jzmpnl4q-QKkz441vwwt9YoEKqeCs7ne4HZhAeblegrdHpo2daChUP9YaOwngk3NqWPz1yrZ2o_TeBDLXUMtHUzkagAyCXzvo98ZySB-xD_PYU84viAW9LzUuPaWFcEiwopnYJHgJIlSCal8cM9iy7EyKz3VoxZnpy1QIw0el_MmJdwZ5QAklyTH4NNKzTzy8CiVJeYnxzelmrbHFd5ylFvJqmMgIFvAa5BOZHvuEsOm8dbS5iuTHWJacfJ0flQv-SkDRrq-pdVkJvUpPXbAbQAAAAFfgjemAA"")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/25efe6aa029c6baea73ea.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(https://t.me/A
    ZTX_ORG):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(https://t.me/Anime_Chat_Unite):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
