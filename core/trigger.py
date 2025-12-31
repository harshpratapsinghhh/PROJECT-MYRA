from core.listen import listen
from core.speak import speak

def wait_for_trigger():
    """
    Continuously listens for trigger words like 'hey myra' or 'wake up kid'.
    Returns True when triggered.
    """
    triggers = ["hey myra", "hey mayra", "mayra", "wake up kid"]

    while True:
        command = listen()
        if any(trigger in command for trigger in triggers):
            speak("Boss, I am online.")
            return True  # Trigger detected
        elif command:
            print(f"Trigger not matched: '{command}'. Listening again...")
