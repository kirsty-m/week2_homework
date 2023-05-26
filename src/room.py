class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.song = []

    # def add_guest_to_room(self, guest):
    def guest_count(self):
        return len(self.guests)
