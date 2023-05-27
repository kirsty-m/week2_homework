import unittest
from src.karaokebar import KaraokeBar
from src.room import Room 
from src.song import Song
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Donna", 200)
        self.guest2 = Guest("Gloria", 300)
        self.guest3 = Guest("Candi", 400)

    def test_guest_has_name(self):
        self.assertEqual("Donna", self.guest1.guest_name)

    def test_guest_has_wallet(self):
        self.assertEqual(300, self.guest2.wallet)