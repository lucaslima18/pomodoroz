from pygame import mixer

def sound_notification(mp3_path: str):
    mixer.init()
    mixer.music.load(mp3_path)
    mixer.music.play()
    # while mixer.music.get_busy():  # wait for music to finish playing
    #     time.sleep(1)