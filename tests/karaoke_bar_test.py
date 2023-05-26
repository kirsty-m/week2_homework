import unittest
from src.karaoke_bar import KaraokeBar
from src.room import Room 
from src.song import Song
from src.guest import Guest

class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.karaoke_bar = KaraokeBar("Disco Karaoke", [rooms], [songs], [guests])
   
def test_karaoke_bar_has_name(self):
    # self.assertEqual("Disco Karaoke", self.karaoke_bar.name)
    pass