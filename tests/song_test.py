import unittest
from src.karaokebar import KaraokeBar
from src.room import Room 
from src.song import Song
from src.karaoke_guest import Guest

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Hot Stuff")
        self.song2 = Song("I Will Survive")
        self.song3 = Song("Young Hearts Run Free")

        
    
    def test_song_has_title(self):
        self.assertEqual("Young Hearts Run Free", self.song3.title)