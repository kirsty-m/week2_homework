import unittest
from src.karaokebar import KaraokeBar
from src.room import Room 
from src.song import Song
from src.guest import Guest

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("I Feel Love")
        self.song2 = Song("I Will Survive")
        self.song3 = Song("Young Hearts Run Free")
    
    def test_song_has_title(self):
        self.assertEqual("Young Hearts Run Free", self.song3.title)
    
    
    
    # def setUp(self):
    #     # songs = [self.song1, self.song2, self.song3]
    #     # self.song1 = "I Feel Love"
    #     # self.song2 = "I Will Survive"
    #     # self.song3 = "Young Hearts Run Free"
    #     pass
        

    # def test_song_has_room(self):
    #     pass