from ocean import Ocean
from ship import Ship


class Player:

    def place_ships(self):
        pass

    def strike(self, board):
        pass

class HumanPlayer(Player):

    def place_ships(self):
        i = 5
        board = Ocean()
        print(board.convert_to_str()) # masz po to __str___

        while i > 0:
            ship = pick_ship() # zastanowić się jak to ma działać
            self.choose_position_and_spot(ship)
            if not board.check_if_ship_is_ok(ship):
                print("Try again")
                continue
            board.place_ship(ship)
            print(board.convert_to_str())
            i -= 1
        return board

    def strike(self, board):
        pass

    def choose_position_and_spot(self, ship):
        spot_x = int(input("Pick spot x to place ship 5: "))
        spot_y = int(input("Pick spot y to place ship 5: "))
        ship.set_spot(spot_x, spot_y)
        position = input("Pick position: ")
        ship.set_position(position)
