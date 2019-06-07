import pygame

#from src.Planet import Planet
#from src.Simulation import Simulation

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RICHBLUE = (2, 1, 34)

#define display size
display_width = 800
display_height = 600
ico = pygame.image.load('../imgs/favicon.ico')
pygame.init()


#open seprate window for simulation, init pygame
def create(simulation):
    global sim
    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
    DISPLAY.fill(RICHBLUE)

    simulation.animatePlanets(DISPLAY, display_width, display_height, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                DISPLAY = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                DISPLAY.fill(RICHBLUE)
                simulation.animatePlanets(DISPLAY, event.dict['w'], event.dict['h'], 1)


if __name__ == '__main__' : create()
