import os
from dotenv import load_dotenv

load_dotenv()  # loads .env in project root

OPENAI_API_KEY   = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY  = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY     = os.getenv("NEWS_API_KEY")
EMAIL_ADDRESS    = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD   = os.getenv("EMAIL_PASSWORD")
DEFAULT_CITY     = "Mumbai,IN"

