from board import Board
from ship import Ship

# {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}

class Player:

    def place_ships(self):
        pass

    def strike(self, board):
        pass

class HumanPlayer(Player):

    def place_ships(self):
        i = 0
        board = Board()
        print(board.convert_to_str()) # masz po to __str___

        ships = Ship.create_game_ships()

        while i < len(ships):
            ship = ships[i]
            self.choose_position_and_spot(ship)
            if not board.check_if_ship_is_ok(ship):
                print("Try again")
                continue
            board.place_ship(ship)
            print(board.convert_to_str())
            i += 1
        return board

    def strike(self, board):
        while True:
            spot_x = int(input("Pick spot x to strike: "))
            spot_y = int(input("Pick spot y to strike: "))
            if board.check_if_can_strike(spot_x, spot_y): # returnTrue/False
                board.strike(spot_x, spot_y)
                break
            else:
                print("Invalid / already taken spot. Try agin")

    def choose_position_and_spot(self, ship):
        spot_x = int(input("Pick spot x to place ship {} lenght {}: ".format(
                            ship.name, ship.lenght)))
        spot_y = int(input("Pick spot y to place this ship: "))
        ship.set_spot(spot_x, spot_y)
        position = input("Pick position: ")
        ship.set_position(position)




class ComputerPlayer(Player):
    pass
