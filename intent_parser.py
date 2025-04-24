from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

INTENTS = {
    "weather": ["weather", "temperature", "forecast"],
    "news":    ["news", "headlines"],
    "timer":   ["timer", "remind me", "alarm"],
    "open_app":["open", "launch"],
    "search":  ["search", "look up", "find"],
    "email":   ["email", "send mail"],
}

def parse_intent(text: str) -> str:
    for intent, keywords in INTENTS.items():
        for kw in keywords:
            if kw in text:
                return intent
    return "chat"

