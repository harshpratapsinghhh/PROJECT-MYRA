from core.listen import listen
from core.speak import speak

def wait_for_trigger():
    while True:
        command = listen()
        if any(trigger in command for trigger in ["hey myra", "hey mayra", "mayra", "wake up kid"]):
            speak("Boss, I am online.")
            return
        elif command:
            print("Trigger not matched. Listening again...")
