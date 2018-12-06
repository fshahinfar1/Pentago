import socket
from server.configuration import *
from game.board import Board, GameException


def run():
    # setting up server socket
    #host = "localhost"
    #port = 1234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("starting server on host:{0} port:{1}".format(host, port))
    s.bind((host, port))
    s.listen(5)

    # setting up game board
    board = Board()
    turn = 1

    # setting the show case
    print("waiting for show case to connect")
    show_case_connection, show_case_add = s.accept()
    print("show case connected")

    # while True:
    print("Waiting for connection")
    connection1, client1_address = s.accept()
    connection1.settimeout(10)
    print("A new connection form: " + str(client1_address))
    connection2, client2_address = s.accept()
    connection2.settimeout(10)
    print("A new connection form: " + str(client2_address))
    try:
        while board.state() == -1:  # until game is over
            if turn == 1:
                player_number = 1  # playing player number
                while True:
                    data = connection1.recv(128).decode()  # get request
                    print("get/send: ", data)
                    if data == "":
                        raise Exception("lost connection")
                    if data == "GET":
                        print("sending board to: " + str(client1_address))
                        connection1.sendall(str(board).encode())
                        show_case_connection.sendall(str(board).encode())  # update show case
                    elif data == "SEND":
                        print("receiving the move from: " + str(client1_address))
                        data = connection1.recv(128).decode()  # get input data
                        print("parsing: " + data)
                        entry = eval(data)
                        board.insert(entry[0], entry[1], player_number)  # insert marble
                        board.rotate(entry[2], entry[3])  # rotate marble
                        turn += 1
                        print("Turn: ", turn)
                        break  # his turn is over
            elif turn == 2:
                player_number = 2  # playing player number
                while True:
                    data = connection2.recv(128).decode()  # get request
                    print("get/send: ", data)
                    if data == "":
                        raise Exception("lost connection")
                    if data == "GET":
                        print("sending board to: " + str(client2_address))
                        connection2.sendall(str(board).encode())
                        show_case_connection.sendall(str(board).encode())  # update show case
                    elif data == "SEND":
                        print("receiving the move from: " + str(client1_address))
                        data = connection2.recv(128).decode()  # get input data
                        print("parsing: " + data)
                        entry = eval(data)
                        board.insert(entry[0], entry[1], player_number)  # insert marble
                        board.rotate(entry[2], entry[3])  # rotate marble
                        turn -= 1
                        print("Turn: ", turn)
                        break  # his turn is over
        state = board.state()
        show_case_connection.sendall(str(board).encode())  # update show case
        if state == 0:
            print("it is a tie")
        else:
            print("winner is: " + str(state))
    except GameException as e:
        print(e)
    except Exception as e:
        print("Unknown Error:")
        print(e)
    finally:
            print("Closing connection")
            connection1.close()
            connection2.close()


if __name__ == "__main__":
    run()

