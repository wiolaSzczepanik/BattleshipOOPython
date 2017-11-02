from board import Board

class Ship:

    def __init__(self, name, lenght):
        self.name = name
        self.lenght = lenght


    def set_spot(self, spot_x, spot_y):
        self.spot_x = spot_x
        self.spot_y = spot_y


    def set_position(self, position):
        self.position = position


    @staticmethod
    def create_game_ships():
        return [Ship('Carrier', 5), Ship('Battleship', 4), Ship('Cruiser', 3),
                                    Ship('Submarine', 3), Ship('Destroyer', 2)]
