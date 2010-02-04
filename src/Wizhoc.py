#! /usr/bin/python
import sys, pygame
pygame.init()

window_size = width, height = 800, 680

screen = pygame.display.set_mode(window_size)

fill_color = 0, 28, 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        screen.fill(fill_color)
        pygame.display.flip()
