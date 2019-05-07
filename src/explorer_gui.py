import pygame

from src.Planet import Planet
from src.Moon import *

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RICHBLUE = (2, 1, 34)
GREY = (193, 187, 187)

# define display size
display_width = 800
display_height = 600
ico = pygame.image.load('../imgs/favicon.ico')
pygame.init()


# open seprate window for simulation, init pygame
def create(planetani):
    global ico
    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
    DISPLAY.fill(RICHBLUE)

    planetani.animateMoons(DISPLAY, display_width, display_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                DISPLAY = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                DISPLAY.fill(RICHBLUE)
                planetani.animateMoons(DISPLAY, event.dict['w'], event.dict['h'])


if __name__ == '__main__': create()
