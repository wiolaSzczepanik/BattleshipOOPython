import sys
import os
from board import Board
from player import HumanPlayer
# import ship
# import square

def main():


    while True:
        print("""
===WELCOM IN BATTLESHIP MADE BY BANANY===
* What you want to do?
(1) Play new game
(2) How to play and rules
(3) Exit game
""")
        option = input("Select an option: ")
        if option == "1":
            os.system('clear')
            chosen_mode_game = input("If you want play single player mode press S, if you want play in muliplayer mode press M: ")
            os.system('clear')
            if chosen_mode_game.upper() == "S":
                start_single_player_mode()
                end_of_every_game()
            elif chosen_mode_game.upper() == "M":
                start_multi_player_mode()
                end_of_every_game()
            else:
                print("You pick wrong letter. Try again!")

        elif option == "2":
            os.system('clear')
            print("""
        * You need to set on the board 5 shipes.
        * Ships are: Carrier (occupies 5 spaces),
            Battleship (4), Cruiser (3), Submarine (3),
            and Destroyer (2).
        * You can add only one ship of each kind.
        * The ships can only be placed vertically or horizontally
        * No part of a ship may hang off the edge of the board.
        * Ships may not overlap each other.
        """)
        else:
            break

def start_single_player_mode():
    print("\n","You are starting game in one player mode. GOOD LUCK!!!")
    play_game(HumanPlayer(), ComputerPlayer())

def start_multi_player_mode():
    print("\n","You are starting game in multi player mode. GOOD LUCK!!!")
    play_game(HumanPlayer(), HumanPlayer())

def play_game(player1, player2):

    print("Player1 place ships on his board")
    board1 = player1.place_ships()
    print("Player2 place ships on his board")
    board2 = player2.place_ships()
    while True:
        player1.strike(board2)
        if board2.check_if_every_ship_is_sunken():
            print("Game over. Player2 WON!!!")
            break
        player2.strike(board1)
        if board1.check_if_every_ship_is_sunken():
            print("Game over. Player1 WON!!!")
            break

def end_of_every_game():
    print("\n","You finish game.","\n")
    chosen_to_play_again = input("If you want play again press Y, if you want quit game press Q: ")
    os.system('clear')

    if chosen_to_play_again.upper() == "Q":
        os.system('clear')
        print("Goodbye, see you next time!!!","\n")
        sys.exit()

main()
