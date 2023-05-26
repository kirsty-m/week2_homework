import unittest
from src.karaokebar import KaraokeBar
from src.room import Room 
from src.song import Song
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Donna")
        self.guest2 = Guest("Gloria")
        self.guest3 = Guest("Candi")

    def test_guest_has_name(self):
        self.assertEqual("Donna", self.guest1.guest_name)