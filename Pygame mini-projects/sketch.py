import pygame
from pygame.locals import *
import sys

# 2 CONSTANTS
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
COLOR = (0,0,0)

# 3 INITIALIZE THE WORLD
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 LOAD ASSETS
window.fill("White")

# 5 INITIALIZE VARIABLES
drawing = False
previous_pos = None

# 6 MAIN LOOP
while True:
    #7 check for and handle events
    """
    Allow to draw continously while the mouse button is down
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            previous_pos = event.pos
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing and previous_pos:
                current_pos = event.pos
                pygame.draw.line(window, COLOR, previous_pos, current_pos, 2)
                previous_pos = current_pos
    
    pygame.display.flip()
    clock.tick(30)


