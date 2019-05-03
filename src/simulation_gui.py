import pygame

from src import Planet
from src import Simulation

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RICHBLUE = (2, 1, 34)

#define display size
display_width = 800
display_height = 600
ico = pygame.image.load('../imgs/favicon.ico')
pygame.init()

#new simulation
simulation = Simulation.Simulation()

#open seprate window for simulation, init pygame
def create():
    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
    DISPLAY.fill(RICHBLUE)

    tester = Planet.Planet(6371, 597, "terrestrial", 1, "earth")
    merc = Planet.Planet(2440, 33, "gas", 0.39, "merc")
    gwen = Planet.Planet(7440, 600, "gas", 2, "gwen")
    DISPLAY.fill(RICHBLUE)
    simulation.AddPlanet(tester)
    simulation.AddPlanet(merc)
    simulation.AddPlanet(gwen)

    simulation.drawPlanets(DISPLAY, display_width, display_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                DISPLAY = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                DISPLAY.fill(RICHBLUE)
                simulation.drawPlanets(DISPLAY, event.dict['w'], event.dict['h'])



if __name__ == '__main__': create()