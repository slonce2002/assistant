import schedule, time
from threading import Thread
from utils.voice import speak

def set_timer(minutes: int, note: str):
    def job():
        speak(f"Reminder: {note}")
    schedule.every(minutes).minutes.do(job)

    def run_sched():
        while True:
            schedule.run_pending()
            time.sleep(1)

    Thread(target=run_sched, daemon=True).start()
    return f"Timer set for {minutes} minutes: {note}"

def handle(text: str) -> str:
    # parse “timer for 5 minutes to stretch”
    import re
    m = re.search(r"timer for (\d+) minutes? to (.+)", text)
    if m:
        mins, note = int(m.group(1)), m.group(2)
        return set_timer(mins, note)
    return "Usage: set timer for X minutes to [note]."

