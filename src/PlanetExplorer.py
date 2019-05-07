#this takes care of displaying a single planet simulation with moons orbiting the planet

from src.Planet import *
from src.Moon import *
from src.Simulation import *
from src.menu import *
from src import explorer_gui
import pygame

# colors definition
WHITE = (255,255,255)
BLACK = (0,0,0)
RICHBLUE = (2, 1, 34)
ORANGY = (255,82,27)
CARROT = (252,158,79)
FLAX = (237, 211, 130)
VANILLA = (242, 243, 174)

# define display size
display_width = 800
display_height = 600
ico = pygame.image.load('../imgs/favicon.ico')

pygame.init()
pygame.font.init()  # for text

# TODO: displays a preview of the planets and after clicking on one it takes u to the richblue screen with planet in
# TODO: the middle and moons orbiting animated
class PlanetExplorer:

    def __init__(self, simulation):
        self.sim = simulation

    def text_object(self, msg, size):
        myfont = pygame.font.SysFont("../imgs/Ubuntu-R.ttf", size)
        textsurface = myfont.render(msg, False, WHITE)
        return textsurface

    # explorer logic
    def pe_events(self, DISPLAY, w, h):
        DISPLAY.fill(RICHBLUE)
        self.sim.drawPlanets(DISPLAY, w, h, 0, 0)
        pygame.display.update()
        msg = "Click on the planet to explore it and its moons."
        textSurf = self.text_object(msg, 20)
        DISPLAY.blit(textSurf, (0.05*w, 0.05*h))

    # main app loop
    def pe_main(self):
        global ico
        DISPLAY = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        pygame.display.set_caption('Planetbox')
        pygame.display.set_icon(ico)
        DISPLAY.fill(RICHBLUE)
        pygame.display.update()

        self.pe_events(DISPLAY, display_width, display_height)

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    DISPLAY = pygame.display.set_mode(event.dict['size'],
                                                      pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                    DISPLAY.fill(RICHBLUE)
                    self.pe_events(DISPLAY, event.dict['w'], event.dict['h'])
                    pygame.display.update()

                # hovering and clicking on the planet
                for p in self.sim.Planets:
                    x = p.cords[0]
                    y = p.cords[1]
                    r = p.cords[2]
                    rad = 10
                    mx, my = pygame.mouse.get_pos()

                    if mx >= x-r and mx <= x+r and my >= y-r and my <= y+r:
                        pygame.draw.circle(DISPLAY, WHITE, [x, y], r)
                        hover = self.text_object(p.name, 15)
                        DISPLAY.blit(hover, (x, (y+r)*0.9))
                        pygame.display.update()

                        # if the planet is clicked then take to a single explorer
                        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                        if p.drawn.collidepoint((mx, my)) and pressed1:
                            explorer_gui.create(p.animation)
                    else:
                        #p.drawPlanet(DISPLAY, x, y)
                        w, h = pygame.display.get_surface().get_size()
                        self.pe_events(DISPLAY, w, h)
                        #pygame.display.update()

            clock.tick(15)


