from os import getenv

from dotenv import load_dotenv

load_dotenv()


SCREENSHOTS_PATH = "artifacts/screenshots"
VIDEOS_PATH = "artifacts/videos"

BASE_URL = getenv("BASE_URL", "https://www.twitch.tv")
LONG_TIMEOUT = 10_000
SHORT_TIMEOUT = 5_000
