import pdb
import unittest
from src.karaokebar import KaraokeBar
from src.room import Room 
from src.song import Song
from src.karaoke_guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Standard", 30)
        self.room2 = Room("Premium", 50)
        self.room3 = Room("Deluxe", 70)
        self.guest_count = [0]
        self.song_count = [0]
        
    
        self.song1 = "Hot Stuff"
        self.song2 = "I Will Survive"
        self.song3 = "Young Hearts Run Free"

        self.guest1 = ("Donna", 200)
        self.guest2 = ("Gloria", 300)
        self.guest3 = ("Candi", 400)


    
    def test_room_has_name(self):
        self.assertEqual("Premium", self.room2.name)

    def test_check_if_room_is_free(self):        
        self.assertEqual(True, self.room1.room_availability())

    def test_check_in_guest_to_room(self):
        self.room1.add_guest_to_room(self.room1)
        self.assertEqual(1, self.room1.guest_count())

    def test_check_out_guest_from_room(self):
        self.room1.remove_guest_from_room(self.room1)
        self.assertEqual(0, self.room1.guest_count())

    def test_add_song_to_room(self): 
        self.room3.add_song_to_room(self.room3)
        self.assertEqual(1, self.room3.song_count())

    def test_customer_books_room_and_song(self):
        self.room3.add_guest_to_room(self.room3)
        self.room3.add_song_to_room(self.room3)
        self.assertEqual(1, self.room3.guest_count())
        self.assertEqual(1, self.room3.song_count())

    def test_room_has_cost(self):
        self.assertEqual(30, self.room1.cost)


