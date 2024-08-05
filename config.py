import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("20183627"))
API_HASH = getenv("6ee2647119abfb228e59ce5254157963")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7437976710:AAG7qFTRJaIPtHEU1UD0m3DXTjgOpJDRorA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://GOKU:MISSBHOPALI@goku.pzzsl8d.mongodb.net/?retryWrites=true&w=majority", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("1002186923374"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("7089408502"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ZTX_ORG")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Anime_Chat_Unite")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("BQEz-ksAcux1w6sWaygBXWjJbAtZpcBEROCbS6u8iq3lO-SDsSIEQ4fYWAIBOyCzgR2ny_5yrC98kC1skKx4U5lGjhDGovjtnH5eQT2x6_BXGyKNbMBHRznQq229tCbLqWGa8tiFjjL73gz8UTIHBUVHgaEmpa2NvBGejMFi4iI6hNplW6GN8IB7tGYJmX4SVLuQMWWMMqkzfyYUBC2SwwPdJHCqDbyx4rmJoJOkd3YDM1Vn0bUmTDBATdD0IiNFJnR-TISh47oN9j2dpasuvdoILjNUWZUPwShsd4018CLqMGYkzWTSVZEgv-cfOkvXJ5s3Nb2Fztkx-NL3e3MTkOeqJ5f3mAAAAAGU3GBtAA")
STRING2 = getenv("BQEz-ksAcux1w6sWaygBXWjJbAtZpcBEROCbS6u8iq3lO-SDsSIEQ4fYWAIBOyCzgR2ny_5yrC98kC1skKx4U5lGjhDGovjtnH5eQT2x6_BXGyKNbMBHRznQq229tCbLqWGa8tiFjjL73gz8UTIHBUVHgaEmpa2NvBGejMFi4iI6hNplW6GN8IB7tGYJmX4SVLuQMWWMMqkzfyYUBC2SwwPdJHCqDbyx4rmJoJOkd3YDM1Vn0bUmTDBATdD0IiNFJnR-TISh47oN9j2dpasuvdoILjNUWZUPwShsd4018CLqMGYkzWTSVZEgv-cfOkvXJ5s3Nb2Fztkx-NL3e3MTkOeqJ5f3mAAAAAGU3GBtAA")
STRING3 = getenv("BQEz-ksAcux1w6sWaygBXWjJbAtZpcBEROCbS6u8iq3lO-SDsSIEQ4fYWAIBOyCzgR2ny_5yrC98kC1skKx4U5lGjhDGovjtnH5eQT2x6_BXGyKNbMBHRznQq229tCbLqWGa8tiFjjL73gz8UTIHBUVHgaEmpa2NvBGejMFi4iI6hNplW6GN8IB7tGYJmX4SVLuQMWWMMqkzfyYUBC2SwwPdJHCqDbyx4rmJoJOkd3YDM1Vn0bUmTDBATdD0IiNFJnR-TISh47oN9j2dpasuvdoILjNUWZUPwShsd4018CLqMGYkzWTSVZEgv-cfOkvXJ5s3Nb2Fztkx-NL3e3MTkOeqJ5f3mAAAAAGU3GBtAA")
STRING4 = getenv("BQEz-ksAcux1w6sWaygBXWjJbAtZpcBEROCbS6u8iq3lO-SDsSIEQ4fYWAIBOyCzgR2ny_5yrC98kC1skKx4U5lGjhDGovjtnH5eQT2x6_BXGyKNbMBHRznQq229tCbLqWGa8tiFjjL73gz8UTIHBUVHgaEmpa2NvBGejMFi4iI6hNplW6GN8IB7tGYJmX4SVLuQMWWMMqkzfyYUBC2SwwPdJHCqDbyx4rmJoJOkd3YDM1Vn0bUmTDBATdD0IiNFJnR-TISh47oN9j2dpasuvdoILjNUWZUPwShsd4018CLqMGYkzWTSVZEgv-cfOkvXJ5s3Nb2Fztkx-NL3e3MTkOeqJ5f3mAAAAAGU3GBtAA")
STRING5 = getenv("BQEz-ksAcux1w6sWaygBXWjJbAtZpcBEROCbS6u8iq3lO-SDsSIEQ4fYWAIBOyCzgR2ny_5yrC98kC1skKx4U5lGjhDGovjtnH5eQT2x6_BXGyKNbMBHRznQq229tCbLqWGa8tiFjjL73gz8UTIHBUVHgaEmpa2NvBGejMFi4iI6hNplW6GN8IB7tGYJmX4SVLuQMWWMMqkzfyYUBC2SwwPdJHCqDbyx4rmJoJOkd3YDM1Vn0bUmTDBATdD0IiNFJnR-TISh47oN9j2dpasuvdoILjNUWZUPwShsd4018CLqMGYkzWTSVZEgv-cfOkvXJ5s3Nb2Fztkx-NL3e3MTkOeqJ5f3mAAAAAGU3GBtAA")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/7d23c8eeaf6a91e82b7ac.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/53e0f4fad846697d68265.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org//file/3dfcffd0c218ead96b102.png"
STATS_IMG_URL = "https://telegra.ph/file/57cea313906cbb2e562ad.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
)
