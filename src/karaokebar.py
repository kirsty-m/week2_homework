from src.karaoke_guest import Guest
from src.room import Room 
from src.song import Song

class KaraokeBar:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.songs = []
        self.guests = []


