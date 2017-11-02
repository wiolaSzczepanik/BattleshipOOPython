class Board:

    def __init__(self):
        self.board = []
        i = 0
        while  i < 10:
            self.board.append(["_"]*10)
            i += 1

    def check_if_every_ship_is_sunken(self):
        pass

    def check_if_can_strike(self, spot_x, spot_y):
        pass

    def strike(self, spot_x, spot_y):
        pass

    def convert_to_str(self):
        str_board = ""
        for row in self.board:
            str_board += " ".join(row) +"\n"
        return str_board

    def check_if_ship_is_ok(self, ship):
        # musi się znajdowac na tablicy
        # czy cały się mieści na tablicy
        # nie może się stykać z już postawionym statskiem

        if ship.spot_x > 10 or ship.spot_x < 1:
            return False
        if ship.spot_y > 10 or ship.spot_y <1:
            return False
        if ship.position == "h":
            if ship.spot_x + ship.lenght - 1 > 10:
                return False
        if ship.position == "v":
            if ship.spot_y + ship.lenght - 1 > 10:
                print("d")
                return False


        return True



    def place_ship(self, ship):
        if ship.position == "h":
            i = 0
            while i < ship.lenght:
                self.board[ship.spot_y-1][ship.spot_x + i -1]= "S"
                i += 1

        if ship.position == "v":
            i = 0
            while i < ship.lenght:
                print(ship.spot_x-1,ship.spot_y + i-1)
                self.board[ship.spot_y + i-1][ship.spot_x-1]= "S"
                i += 1
