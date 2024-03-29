# this animates a single planet and its moons

import pygame
from src.Planet import *
from src.Moon import *
from src.menu import *
from src.PlanetExplorer import PlanetExplorer
from src import main
from src import menu
# from OpenGL.GL import *

# TODO: zooooooomiiiin

# some imports and globals
# define display size
display_width = 800
display_height = 600
ico = pygame.image.load('../imgs/favicon.ico')

pygame.init()
pygame.font.init()  # for text

# globals for controlling the animation
sim = True
pause = False

class PlanetAnimation:

    def __init__(self, planet):
        self.planet = planet
        self.CreateMoons()  # init the moons

    def setSimulation(self, simulation):
        self.exp = PlanetExplorer(simulation)

    def CreateMoons(self):
        for nbMoon in range(self.planet.nrMoons):
            if(len(str(self.planet.mass)) <= 8):
                mass = random.randint(round(self.planet.mass / 10000), round(self.planet.mass / 100)) # for now its hardcoded, may think
            else:                                                                   # about change later
                mass = random.randint(round(self.planet.mass / 1000000), round(self.planet.mass / 1000))
            if mass == 0:
                mass = 1

            highBorderDistance = int(round((mass / 4.8 * math.pi) ** (1. / 3)) ** 3)
            lowBorderDistance = int(round((mass / 97.2 * math.pi) ** (1. / 3)) ** 3)
            if lowBorderDistance == 0:
                lowBorderDistance = 1
            radius = random.randint(lowBorderDistance, highBorderDistance)
            moon = Moon(radius, mass, self.planet)
            self.planet.moons.append(moon)

    def unpause(self):
        global pause
        pause = False

        # pause function

    def paused(self, DISPLAY):
        global pause

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.unpause()
                    # return to menu from pause
                    if event.key == pygame.K_e:
                        self.exp.pe_main()
                    if event.key == pygame.K_m:  # if m then stop and go to menu
                        # self.planet.moons = []
                        menu.mainer(DISPLAY)
                    if event.key == pygame.K_a:
                        main.apploop(DISPLAY)

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
        myfont = pygame.font.Font("../imgs/Ubuntu-R.ttf", 15)
        info = self.planet.printPlanet()
        self.multiline_txt(DISPLAY, info, (0.05*w+20, 0.05*h+20), myfont)
        pygame.display.update()

    def planet_events(self, DISPLAY, w, h, x, y, scale):
        #DISPLAY.fill(RICHBLUE)
        self.planet.drawBigPlanet(DISPLAY, int(h*0.1), scale)

        maintxt = "Planet Information"
        textSurf = self.text_object(maintxt, 20)
        DISPLAY.blit(textSurf, (0.05 * w, 0.05 * h))

        for m in self.planet.moons:
            m.drawOrbit(DISPLAY, x, y, scale)

        self.printPlanetInfo(DISPLAY, w, h)
        #pygame.display.update()

    def planet_anim(self, screen, w, h, x, y, scale):
        self.planet_events(screen, w, h, x, y, scale)
        for m in self.planet.moons:
            m.animate(screen, x, y, h, scale)

    def check_scale(self, scale):
        new_scale = scale
        if scale <= 0.2:
            new_scale = 0.2
        elif scale >= 50:
            new_scale = 50
        return new_scale

    # animates the moons
    def animateMoons(self, screen, w, h, scale):
        global sim, pause
        #screen = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
        pygame.display.set_caption('Planetbox')
        pygame.display.set_icon(ico)
        screen.fill(RICHBLUE)
        pygame.display.update()

        planet_pos_x = int(w / 2)
        planet_pos_y = int(h / 2)
        clock = pygame.time.Clock()

        sim = True
        while sim:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode(event.dict['size'],
                                                     pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                    screen.fill(RICHBLUE)
                    sim = False
                    scale = 1
                    self.animateMoons(screen, event.dict['w'], event.dict['h'], scale)
                # KEY EVENTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # if space pressed then pause
                        pause = True
                        self.paused(screen)
                    if event.key == pygame.K_e:  # back to explorer
                        self.exp.pe_main()
                    if event.key == pygame.K_m:  # if m then stop and go to menu
                        menu.mainer(screen)
                    if event.key == pygame.K_a:
                        main.apploop(screen)
                    if event.key == pygame.K_r:  # resets zoom
                        scale = 1
                        screen.fill(RICHBLUE)
                        self.animateMoons(screen, display_width, display_height, scale)
                    if event.key == pygame.K_UP:  # zoom up
                        scale += 0.1
                        scale = self.check_scale(scale)
                        screen.fill(RICHBLUE)
                        self.animateMoons(screen, display_width, display_height, scale)
                    if event.key == pygame.K_DOWN:  # zoom down
                        scale -= 0.1
                        scale = self.check_scale(scale)
                        screen.fill(RICHBLUE)
                        self.animateMoons(screen, display_width, display_height, scale)

            screen.fill(RICHBLUE)

            # draw the planet and the planet's info
            self.planet_anim(screen, w, h, planet_pos_x, planet_pos_y, scale)

            pygame.display.flip()
            clock.tick(100)
