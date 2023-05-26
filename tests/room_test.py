import unittest
from src.karaokebar import KaraokeBar
from src.room import Room 
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Standard")
        self.room2 = Room("Premium")
        self.room3 = Room("Deluxe")
    
    def test_room_has_name(self):
        self.assertEqual("Premium", self.room2.name)
