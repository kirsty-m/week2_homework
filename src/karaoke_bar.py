from src.guest import Guest
from src.room import Room 
from src.song import Song

class KaraokeBar:
    def __init__(self, name, rooms, songs, guests):
        self.name = name
        self.rooms = [rooms]
        self.songs = [songs]
        self.guests = [guests]


