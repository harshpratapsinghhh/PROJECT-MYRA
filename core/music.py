import os
import random
import threading
from difflib import get_close_matches
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

MUSIC_FOLDER = r"D:\PROJECT-MYRA\Music\MyraSongs"
current_thread = None
current_play_obj = None
current_song_name = ""

def _play(song_path):
    global current_play_obj
    try:
        song = AudioSegment.from_file(song_path, format="mp3")
        current_play_obj = _play_with_simpleaudio(song)
        current_play_obj.wait_done()
    except Exception as e:
        print(f"[ERROR in _play]: {e}")

def play_music(song_name=""):
    """Play a requested or random song and return song name."""
    global current_thread, current_play_obj, current_song_name
    files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
    if not files:
        return None, "No songs found in your music folder."

    if song_name:
        matches = get_close_matches(song_name.lower(), [f.lower().replace(".mp3", "") for f in files], n=1, cutoff=0.5)
        if matches:
            matched_song = [f for f in files if f.lower().startswith(matches[0])][0]
        else:
            matched_song = random.choice(files)
    else:
        matched_song = random.choice(files)

    song_path = os.path.join(MUSIC_FOLDER, matched_song)
    current_song_name = matched_song

    # Stop previous
    if current_play_obj and current_play_obj.is_playing():
        current_play_obj.stop()

    # Play in background
    current_thread = threading.Thread(target=_play, args=(song_path,), daemon=True)
    current_thread.start()

    return matched_song, f"Playing {matched_song}"

def stop_music():
    global current_play_obj, current_song_name
    if current_play_obj and current_play_obj.is_playing():
        current_play_obj.stop()
        stopped_song = current_song_name
        current_song_name = ""
        return True, f"Music '{stopped_song}' stopped."
    return False, "No music is playing right now."
