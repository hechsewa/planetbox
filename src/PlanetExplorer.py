#this takes care of displaying a single planet simulation with moons orbiting the planet


from Planet import *
from Moon import *
from Simulation import *
from menu import *
import explorer_gui
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
ico = pygame.image.load('favicon.ico')
btnH = 50
btnW = 150

pygame.init()
pygame.font.init()  # for text

import sys
class PlanetExplorer:

    def __init__(self, simulation):
        self.sim = simulation

    def quit(self):
        pygame.quit()
        sys.exit()

    def text_object(self, msg, size):
        myfont = pygame.font.SysFont("Ubuntu-R.ttf", size)
        textsurface = myfont.render(msg, False, WHITE)
        return textsurface

    # explorer logic
    def pe_events(self, DISPLAY, w, h, scale):
        DISPLAY.fill(RICHBLUE)
        self.sim.drawPlanets(DISPLAY, w, h, 0, 0, scale)
        pygame.display.update()
        msg = "Click on the planet to explore it and its moons."
        textSurf = self.text_object(msg, 20)
        DISPLAY.blit(textSurf, (0.05*w, 0.05*h))
        pygame.display.update()

    def check_scale(self, scale):
        new_scale = scale
        if scale <= 0:
            new_scale = 0
        elif scale >= 50:
            new_scale = 50
        return new_scale

    # main app loop
    def pe_main(self):
        global ico
        DISPLAY = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        pygame.display.set_caption('Planetbox')
        pygame.display.set_icon(ico)
        DISPLAY.fill(RICHBLUE)
        pygame.display.update()

        scale = 1
        self.pe_events(DISPLAY, display_width, display_height, scale)
        pygame.display.flip()

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
                    self.pe_events(DISPLAY, event.dict['w'], event.dict['h'], scale)
                    pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        scale += 0.1
                        scale = self.check_scale(scale)
                        DISPLAY.fill(RICHBLUE)
                        self.pe_events(DISPLAY, display_width, display_height, scale)
                    if event.key == K_DOWN:
                        scale -= 0.1
                        scale = self.check_scale(scale)
                        DISPLAY.fill(RICHBLUE)
                        self.pe_events(DISPLAY, display_width, display_height, scale)
                    if event.key == K_r:
                        scale = 1
                        DISPLAY.fill(RICHBLUE)
                        self.pe_events(DISPLAY, display_width, display_height, scale)

                # hovering and clicking on the planet
            for p in self.sim.Planets:
                x = p.cords[0]
                y = p.cords[1]
                r = p.cords[2]
                mx, my = pygame.mouse.get_pos()

                if mx >= x-r and mx <= x+r and my >= y-r and my <= y+r:
                    pygame.draw.circle(DISPLAY, WHITE, [x, y], r)
                    hover = self.text_object(p.name, 15)
                    DISPLAY.blit(hover, (x, (y+r)*0.9))
                    pygame.display.update()

                    # if the planet is clicked then take to a single explorer
                    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                    if p.drawn.collidepoint((mx, my)) and pressed1:
                        explorer_gui.create(p.animation, self.sim)
                    else:
                        #p.drawPlanet(DISPLAY, x, y)
                        w, h = pygame.display.get_surface().get_size()
                        self.pe_events(DISPLAY, w, h, 1)
                        pygame.display.update()

            clock.tick(15)

