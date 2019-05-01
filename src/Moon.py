import random, math
from src.MathEquations import *

class Moon:
    def __init__(self, radius, mass, motherPlanet):
        self.radius = radius
        self.mass = mass
        self.motherPlanet = motherPlanet
        self.distance = self.GenerateDistance() #TODO wymysl cos bo sie nie kompiluje; pewnie jakis rand i na podstawie jego
        #TODO sprawdzaj tez z predkoscia minimalna (v=pierwiatek 3. stopnia z (G * M(centralny)/R)
        self.gravity = motherPlanet.GravityCalculator(self.mass)



    def GenerateDistance(self):
        dist = random.randint(self.radius * 5, self.radius * 20)
        v = int(round((6.67 * self.motherPlanet.mass / dist) ** (1. / 3)) ** 3)
        return dist



