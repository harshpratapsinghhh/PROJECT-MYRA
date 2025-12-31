from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def speak(text):
    try:
        filename = "response.mp3"
        if os.path.exists(filename):
            os.remove(filename)
        tts = gTTS(text=text, lang='en', tld='co.uk')
        tts.save(filename)

        # Pydub play
        song = AudioSegment.from_file(filename)
        play(song)
        
    except Exception as e:
        print(f"[ERROR in speak()]: {e}")
