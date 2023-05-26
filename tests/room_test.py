import pdb
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
        self.guest_count = [0]
    
    def test_room_has_name(self):
        self.assertEqual("Premium", self.room2.name)

    def test_check_if_room_is_free(self):        
        self.assertEqual(0, self.room1.guest_count())