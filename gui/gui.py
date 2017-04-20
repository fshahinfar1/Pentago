from game.board import *
import pygame
import gui.pygame_resource as rs

# create a board
board = Board()

pygame.init()
rs.set_images_path("images/")
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


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    # draw
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

pygame.quit()
