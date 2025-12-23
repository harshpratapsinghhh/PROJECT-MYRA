import os
import random
import threading
from difflib import get_close_matches
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

MUSIC_FOLDER = r"D:\PROJECT-MYRA\Music\MyraSongs"  # your music folder
current_thread = None
current_play_obj = None


def _play(song_path):
    """Internal threaded player using pydub + simpleaudio."""
    global current_play_obj
    try:
        song = AudioSegment.from_file(song_path, format="mp3")
        current_play_obj = _play_with_simpleaudio(song)
        current_play_obj.wait_done()
    except Exception as e:
        print(f"[ERROR in _play]: {e}")


def play_music(speak, song_name=""):
    """Play a requested or random song."""
    global current_thread, current_play_obj
    try:
        files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
        if not files:
            speak("No songs found in your music folder.")
            return

        if song_name:
            # fuzzy match for song name
            matches = get_close_matches(song_name.lower(), [f.lower().replace(".mp3", "") for f in files], n=1, cutoff=0.5)
            if matches:
                matched_song = [f for f in files if f.lower().startswith(matches[0])][0]
                song_path = os.path.join(MUSIC_FOLDER, matched_song)
                speak(f"Playing {matched_song}")
            else:
                speak("Couldn't find that song. Playing a random one.")
                song_path = os.path.join(MUSIC_FOLDER, random.choice(files))
        else:
            song_path = os.path.join(MUSIC_FOLDER, random.choice(files))
            speak("Playing a random song for you.")

        # Stop any previous playback first
        if current_play_obj and current_play_obj.is_playing():
            current_play_obj.stop()

        # Run in background thread
        current_thread = threading.Thread(target=_play, args=(song_path,), daemon=True)
        current_thread.start()

    except Exception as e:
        speak(f"Error while playing music: {e}")


def stop_music(speak):
    """Stop any currently playing song."""
    global current_play_obj
    try:
        if current_play_obj and current_play_obj.is_playing():
            current_play_obj.stop()
            speak("Music stopped.")
        else:
            speak("No music is playing right now.")
    except Exception as e:
        speak(f"Error stopping music: {e}")
