from gtts import gTTS
import os
import time

def speak(text):
    try:
        filename = "response.mp3"
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except PermissionError:
                print("[ERROR]: File in use, retrying...")
                time.sleep(1)
                return
        tts = gTTS(text=text, lang='en', tld='co.uk')
        tts.save(filename)
        os.system(f'start /min {filename}')
        time.sleep(2)
    except Exception as e:
        print(f"[ERROR in speak()]: {e}")
