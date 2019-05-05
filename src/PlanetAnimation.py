# this animates a single planet and its moons

import pygame
from src.Planet import *
from src.Moon import *

#some imports and globals
# define display size
display_width = 800
display_height = 600
ico = pygame.image.load('../imgs/favicon.ico')

pygame.init()
pygame.font.init()  # for text


class PlanetAnimation:

    def __init__(self, planet):
        self.planet = planet

    def text_object(self, msg, size):
        myfont = pygame.font.SysFont("../imgs/Ubuntu-R.ttf", size)
        textsurface = myfont.render(msg, False, WHITE)
        return textsurface

    def multiline_txt(self, DISPLAY, text, pos, font):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = DISPLAY.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, WHITE)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                DISPLAY.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def printPlanetInfo(self, DISPLAY, w, h):
        myfont = pygame.font.SysFont("../imgs/Ubuntu-R.ttf", 15)
        info = self.planet.printPlanet()
        self.multiline_txt(DISPLAY, info, (0.05*w+20, 0.05*h+20), myfont)
        pygame.display.update()


    def planet_events(self, DISPLAY, w, h):
        DISPLAY.fill(RICHBLUE)
        self.planet.drawBigPlanet(DISPLAY, int(h*0.1))

        maintxt = "Planet Information"
        textSurf = self.text_object(maintxt, 20)
        DISPLAY.blit(textSurf, (0.05 * w, 0.05 * h))

        self.printPlanetInfo(DISPLAY, w, h)
        pygame.display.update()

    def planet_loop(self):
        global ico
        DISPLAY = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        pygame.display.set_caption('Planetbox')
        pygame.display.set_icon(ico)
        DISPLAY.fill(RICHBLUE)
        pygame.display.update()

        self.planet_events(DISPLAY, display_width, display_height)

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    DISPLAY = pygame.display.set_mode(event.dict['size'],
                                                      pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                    DISPLAY.fill(RICHBLUE)
                    self.planet_events(DISPLAY, event.dict['w'], event.dict['h'])
                    pygame.display.update()
