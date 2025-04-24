# main.py

from utils.voice import speak, listen
from utils.intent_parser import parse_intent
import importlib

speak("Jarvis online. How can I assist you?")

while True:
    text = listen()  # now Whisper-driven
    if not text:
        text = input("I didn’t catch that. Please type your command: ").strip().lower()

    if text in ("exit jarvis", "goodbye"):
        speak("Shutting down. Bye!")
        break

    intent = parse_intent(text)
    try:
        skill = importlib.import_module(f"skills.{intent}")
        resp = skill.handle(text)
    except ModuleNotFoundError:
        from skills.chat import handle as chat_handle
        resp = chat_handle(text)

    speak(resp)

