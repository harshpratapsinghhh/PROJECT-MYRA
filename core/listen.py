import speech_recognition as sr

def listen(use_microphone=True):
    """
    Listens to user's voice and returns the recognized text.
    use_microphone=False => skips listening, useful for WebSocket input
    """
    if not use_microphone:
        return ""  # Web interface will provide input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return ""  # optional: CLI can speak("Sorry boss...") if needed
    except sr.RequestError:
        return ""
