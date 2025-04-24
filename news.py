import requests
from config import NEWS_API_KEY

def handle(_: str) -> str:
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    arts = requests.get(url).json().get("articles", [])[:5]
    titles = [a["title"] for a in arts]
    return " | ".join(titles) if titles else "No news right now."

