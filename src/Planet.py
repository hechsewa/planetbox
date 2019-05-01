import random, math
from src.MathEquations import *
from src.Sun import *

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
