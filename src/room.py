class Room:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.guests = []
        self.song = []



    def guest_count(self):
        return len(self.guests)

    def add_guest_to_room(self, guest):
        self.guests.append(guest)

    def remove_guest_from_room(self, guest):
        for guest in self.guests:
            self.guests.remove(guest)

    def add_song_to_room(self, song):
       self.song.append(song)

    def song_count(self):
        return len(self.song)

    def room_availability(self):
        if len(self.guests) == 0:
            return True

    
        
        