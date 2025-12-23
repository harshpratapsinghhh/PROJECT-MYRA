import os
import webbrowser
import datetime
import wikipedia
import psutil
from core.music import play_music, stop_music
from core.speak import speak
from core.listen import listen

def execute_command(command):
    if "play music" in command:
        song_name = command.replace("play music", "").strip()
        play_music(speak, song_name)

    elif "stop music" in command or "pause music" in command:
        stop_music(speak)

    elif "open" in command:
        if "chrome" in command:
            speak("Opening Chrome")
            os.system("start chrome")
        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("start notepad")
        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        else:
            app = command.replace("open", "").strip()
            speak(f"Opening {app}")
            os.system(f"start {app}")

    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching for {query}")
        webbrowser.open(url)

    elif "wikipedia" in command or "who is" in command or "what is" in command:
        try:
            topic = command.replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
            result = wikipedia.summary(topic, sentences=2)
            speak(f"According to Wikipedia, {result}")
        except Exception:
            speak("Sorry, I couldn't find anything on Wikipedia.")

    elif "battery" in command:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = "charging" if battery.power_plugged else "not charging"
            speak(f"Battery is at {percent} percent and is {plugged}.")
        else:
            speak("Battery status not available.")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Boss, the time is {now}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}")

    else:
        speak("Sorry boss, I didn’t get that. Should I search it online?")
        response = listen()
        if "yes" in response or "search" in response or "go for it" in response:
            speak("Okay boss, searching it for you.")
            webbrowser.open(f"https://www.google.com/search?q={command}")
        else:
            speak("Okay boss, skipping search.")
