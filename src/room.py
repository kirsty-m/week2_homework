class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.song = []

    def guest_count(self):
        return len(self.guests)

    def add_guest_to_room(self, guest):
        self.guests.append(guest)

    def remove_guest_from_room(self, guest):
        for guest in self.guests:
            self.guests.remove(guest)