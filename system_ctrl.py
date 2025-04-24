# skills/system_ctrl.py

import subprocess
import shutil

def handle(text: str) -> str:
    """
    Opens an application based on a command like:
      - "open firefox"
      - "launch code"
    """
    text = text.lower().strip()
    # look for our keywords at the start
    for kw in ("open", "launch"):
        if text.startswith(kw):
            # everything after the keyword
            cmd = text[len(kw):].strip()
            if not cmd:
                return "You said open but didn’t tell me what to open."

            # check if the executable exists in PATH
            exe = shutil.which(cmd)
            if exe is None:
                return f"Sorry, I couldn’t find an application named '{cmd}'."

            # try launching it
            try:
                # shell=True lets us launch GUI apps in your X session
                subprocess.Popen(cmd, shell=True)
                return f"Opened {cmd}."
            except Exception as e:
                return f"Error launching '{cmd}': {e}"

    return "System control: unrecognized command."

