import random, math
import pygame
from MathEquations import *

#colors
WHITE = (255, 255, 255)
RICHBLUE = (2, 1, 34)
GREY = (193, 187, 187)

# TODO: co jak np. dwa ksiezyce zachodza na siebie? tzn maja ten sam distance albo bardzo bliski
# todo: zroznicowac jakos radius bo troche to kiepsko wyglada + ogarnac co z tym distancem do planety
# todo: bo teraz moze sie np zdarzyc ze ksiezyc wyladuje w srodku planety. zrobic zalezne od motherplanet radius??
# todo: a no i ogarnac z iloscia ksiezycy bo jak chujnia z grzybnia to wyglada teraz (: (:

class Moon:
    def __init__(self, radius, mass, motherPlanet):
        self.radius = radius
        self.mass = mass
        self.motherPlanet = motherPlanet
        self.distance = self.GenerateDistance() #TODO wymysl cos bo sie nie kompiluje; pewnie jakis rand i na podstawie jego
        #TODO sprawdzaj tez z predkoscia minimalna (v=pierwiatek 3. stopnia z (G * M(centralny)/R)
        self.gravity = motherPlanet.GravityCalculator(self.mass)
        self.degree = 0  # for animation purposes
        self.day = math.sqrt(4*math.pi*(self.distance*self.distance*self.distance)/6.67)

    # TODO: !! ! ! !
    def GenerateDistance(self):
        ld = 0.00257  # 1 ld = 0.00257 au
        dist = random.uniform(0.2, 2) #distance in LD units (lunar distance)
        return dist

    # drawing functions
    def drawMoon(self, screen, x, y, scale):
        # moon size (w/ resize)
        w, h = pygame.display.get_surface().get_size()
        size = int(self.radius*(0.01*h)*scale)

        pygame.draw.circle(screen, GREY, [x, y], size)  # previously 3

    def drawOrbit(self, screen, x, y, scale):
        # moon distance from planet, draw orbit
        w, h = pygame.display.get_surface().get_size()
        dist = int(self.distance * (h / 3)*scale)
        pygame.draw.circle(screen, WHITE, [x, y], dist, 1)

    def animate(self, screen, planet_x, planet_y, h, scale):
        self.degree += 1/self.day  # change speed according to gravity
        if self.degree == 360:
            self.degree = 0

        dist = int(self.distance * (h / 3)*scale)
        x = int(math.cos(self.degree * 2 * math.pi / 360) * dist) + planet_x
        y = int(math.sin(self.degree * 2 * math.pi / 360) * dist) + planet_y

        # self.drawOrbit(screen, planet_x, planet_y)
        self.drawMoon(screen, x, y, scale)
        pygame.display.flip()

    # for printing to file
    def printMoon(self):
        msg = "\nDistance to the planet: " + str(self.distance) + "LD\n" \
              "Mass: " + str(self.mass) + "*10^22 kg\nGravitational field: " + str(self.gravity) + " N/kg\n" \
              "Radius: " + str(self.radius) + " km"
        return msg