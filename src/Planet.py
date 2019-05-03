import random, math
from src.MathEquations import *
from src.Sun import *
import pygame

#planet colors
TER = (206, 196, 105)
ICE = (76, 134, 168)
GAS = (226, 181, 147)
WHITE = (255, 255, 255)
RICHBLUE = (2, 1, 34)

class Planet:

    def __init__(self, radius, myMass, type, distance, name):
        self.radius = radius
        self.mass = myMass
        self.type = type
        self.distance = distance
        self.name = name
        self.gravity = self.GravityCalculator(self.mass)
        self.nrMoons = self.RandomizeMoons()
        self.year = self.KeplersThirdLaw()
        self.moons = []
        self.degree = 0

    def KeplersThirdLaw(self):
        # T^2 / a^3 is const for every planet in this system -> check with good ol' Earth (Sun is in center, so why not?)
        # therefore (1AU)^3 and (1year)^2
        return math.sqrt(pow(self.distance,3)) # Earth years

    def RandomizeMoons(self):
        if self.type == "terrestrial":
            return random.randint(0, round(self.gravity / 2))
        if self.type == "gas":
            return random.randint(round(self.gravity * 2), round(self.gravity * 4))
        if self.type == "ice":
            return random.randint(round(self.gravity * 1.5), round(self.gravity * 3)) # all of the numbers are based on the actual
                                                                  # number of moons for each planet in solar system

    def GravityCalculator(self, massFirst):
        return ((6.674 * massFirst * pow(10, 11))/ (pow(self.radius*1000, 2))) # 10^11 'cause 10^-11 from G and 10^22 from mass


    #for drawing purposes
    def drawOrbit(self, screen, x, y):
        # planet distance from sun, draw orbit
        w, h = pygame.display.get_surface().get_size()
        dist = int(self.distance * (h / 3));
        pygame.draw.circle(screen, WHITE, [x, y], dist, 1)

    #draw planet on simulation
    def drawPlanet(self, screen, x, y):

        #planet size (w/ resize)
        w, h = pygame.display.get_surface().get_size()
        size = int(self.radius/h)

        if self.type == "terrestrial":
            pygame.draw.circle(screen, TER, [x, y], size)
        elif self.type == "ice":
            pygame.draw.circle(screen, ICE, [x, y], size)
        elif self.type == "gas":
            pygame.draw.circle(screen, GAS, [x, y], size)

        return

    def animate(self, screen, star_x, star_y, h):
        self.degree += self.gravity;
        if self.degree == 360:
            self.degree = 0

        dist = int(self.distance * (h / 3))
        x = int(math.cos(self.degree * 2 * math.pi / 360) * dist) + star_x
        y = int(math.sin(self.degree * 2 * math.pi / 360) * dist) + star_y

        self.drawOrbit(screen, star_x, star_y)
        self.drawPlanet(screen, x, y)
        pygame.display.flip()
