import pygame

# from src.Planet import Planet
from Moon import *
import sys

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RICHBLUE = (2, 1, 34)
GREY = (193, 187, 187)

# define display size
display_width = 800
display_height = 600
ico = pygame.image.load('favicon.ico')
pygame.init()

def quit():
    pygame.quit()
    sys.exit()

# open seprate window for simulation, init pygame
def create(planetani, simulation):
    global ico, display_height, display_width
    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
    DISPLAY.fill(RICHBLUE)

    planetani.setSimulation(simulation)
    planetani.animateMoons(DISPLAY, display_width, display_height, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                DISPLAY = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                DISPLAY.fill(RICHBLUE)
                scale = 1
                planetani.animateMoons(DISPLAY, event.dict['w'], event.dict['h'], scale)


if __name__ == '__main__': create()
