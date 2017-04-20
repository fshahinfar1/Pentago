import socket
from client.configuration import *
from game.board import Board
from random import randrange, choice
from time import sleep


# setting up board
board = Board()


def ai():
    # a Random AI
    while True:
        row = randrange(6)
        col = randrange(6)
        if not board.is_cell_filled(row, col):
            break
    quarter = randrange(4)
    direction = choice((1, -1))
    return row, col, quarter, direction

def run():
    # setting up connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))  # try to connect to server
    while True:  # while game is on
        try:
            print("sending GET request")
            s.sendall("GET".encode())
            sleep(1)
            print("receiving the board")
            data = s.recv(128).decode()  # get last board state
            if data == "":
                print("connection closed")
                break
            board.set(data)  # set board
            entry = ai()  # decide your move
            print("sending SEND request")
            s.sendall("SEND".encode())
            sleep(1)
            print("sending the move")
            s.sendall(str(entry).encode())  # send your move
            sleep(2)
            # Now it's the other player's turn
        except Exception as e:
            print(e)
            break  # out of while

    s.close()



if __name__ == "__main__":
    run()
