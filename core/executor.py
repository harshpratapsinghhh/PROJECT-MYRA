import os
import webbrowser
import datetime
import wikipedia
import psutil
from core.music import play_music, stop_music
from core.speak import speak
from core.listen import listen

def execute_command(command):
    response = ""

    if "play music" in command:
        song_name = command.replace("play music", "").strip()
        song, msg = play_music(song_name)
        response = msg

    elif "stop music" in command or "pause music" in command:
        _, msg = stop_music()
        response = msg

    elif "open" in command:
        app_name = command.replace("open", "").strip()
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
            speak(f"Opening {app_name}")
            os.system(f"start {app_name}")
        response = f"Opened {app_name}"

    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        response = f"Searching for {query}"

    elif "wikipedia" in command or "who is" in command or "what is" in command:
        try:
            topic = command.replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
            result = wikipedia.summary(topic, sentences=2)
            response = f"According to Wikipedia, {result}"
        except Exception:
            response = "Sorry, I couldn't find anything on Wikipedia."

    elif "battery" in command:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = "charging" if battery.power_plugged else "not charging"
            response = f"Battery is at {percent} percent and is {plugged}."
        else:
            response = "Battery status not available."

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The time is {now}"

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        response = f"Today is {today}"

    else:
        response = "Sorry boss, I didn’t get that. Should I search it online?"
        speak(response)
        user_resp = listen()
        if "yes" in user_resp or "search" in user_resp:
            webbrowser.open(f"https://www.google.com/search?q={command}")
            response = f"Searching online for '{command}'"
        else:
            response = "Skipping search."

    speak(response)
    return response
