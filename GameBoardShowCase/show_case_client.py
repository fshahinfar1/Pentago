import socket
from GameBoardShowCase.configuration import *
import threading
from game.board import *
import pygame
import gui.pygame_resource as rs


# create a board
board = Board()

# pygame - gui
pygame.init()
rs.set_images_path("GameBoardShowCase/images/")
clock = pygame.time.Clock()
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pentago")
quarter = rs.get_image("Quarter.png")
red_marble = rs.get_image("Red_Marble.png")
black_marble = rs.get_image("Black_Marble.png")
quarter = pygame.transform.scale(quarter, (190, 190))
red_marble = pygame.transform.scale(red_marble, (30, 30))
black_marble = pygame.transform.scale(black_marble, (30, 30))

#threading
lock = threading.Lock()


def draw():
    screen.fill((0, 0, 0))
    screen.blit(quarter, (10, 10))  # q = 0
    screen.blit(quarter, (195, 10))  # q = 1
    screen.blit(quarter, (10, 195))  # q = 2
    screen.blit(quarter, (195, 195))  # q = 3
    for i in range(6):
        for j in range(6):
            c = board.get_cell(i, j)
            pos = (60 * j + 30, 60 * i + 30)
            if c == 1:  # black
                screen.blit(black_marble, pos)
            elif c == 2:  # red
                screen.blit(red_marble, pos)
    pygame.display.update()
    clock.tick(30)


def update(s):
    # while True:  # while game is on
    print("updateThread")
    data = s.recv(128).decode()
    board.set(data)
    board.show()  # print board to console


class drawThreading(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                        break
            draw()
        pygame.quit()


class updateThreading(threading.Thread):
    def __init__(self, s):
        threading.Thread.__init__(self)
        self.s = s

    def run(self):
        update(self.s)


def run():
    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))  # try to connect to server
    # threading
    drawThread = drawThreading()
    updateThread = updateThreading(s)
    updateThread.start()
    drawThread.start()
    try:
        while True:
            updateThread.join()
            updateThread.run()
    except Exception as e:
        print(e)
        print("Error")
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                        break
    s.close()
    pygame.quit()
    drawThread.stop()
    updateThread.stop()


if __name__ == "__main__":
    run()
