class Guest:
    def __init__(self, guest_name, wallet):
        self.guest_name = guest_name
        self.wallet = wallet
        self.room = []

    def sufficient_funds(self, room_cost):
        return self.wallet >= room_cost
        