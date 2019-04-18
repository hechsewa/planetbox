import random


class Planet:

    def __init__(self, radius, mass, type, name):
        self.radius = radius
        self.mass = mass
        self.type = type
        self.name = name
        self.gravity = 6.674 * self.mass / pow(self.radius, 2)  # G*m / r^2
        self.nrMoons = random.randint(0, 4)


