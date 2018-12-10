"""
Farbod Shahinfar
Pentago Game

"""
from board import Board
from player import *
import os

def game_main():
    # create the games board
    game_board = Board()
    # create two players
    players = [Player(False), Player(False)]
    # player one starts the game
    game_board.show()  # print out game board to console
    while True:
        for p in players:
            p.is_turn = True
            entry = tuple(p.your_turn()) 
            game_board.insert(entry[0], entry[1], p.player_number)
            game_board.rotate(entry[2], entry[3])
            p.is_turn = False
            os.system("clear")
            game_board.show()

if __name__ == "__main__":
    game_main()
