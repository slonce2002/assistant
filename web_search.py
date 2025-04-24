import requests
from bs4 import BeautifulSoup

def handle(text: str) -> str:
    query = text.replace("search", "").strip().replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent":"Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    results = soup.select(".kCrYT a")[:3]
    outs = []
    for a in results:
        href = a.get("href")
        title = a.get_text()
        outs.append(title)
    return " | ".join(outs) if outs else "No results found."

