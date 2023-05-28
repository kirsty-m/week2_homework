import unittest
from src.karaokebar import KaraokeBar
from src.room import Room 
from src.song import Song
from src.karaoke_guest import Guest

class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.karaokebar = KaraokeBar("Disco Queens Karaoke")
        
    def test_karaoke_bar_has_name(self):
        self.assertEqual("Disco Queens Karaoke", self.karaokebar.name)
        