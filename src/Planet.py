import random, math


class Planet:

    def __init__(self, radius, mass, type, name):
        self.radius = radius
        self.mass = mass
        self.type = type
        self.name = name
        self.gravity = 6.674 * self.mass # / pow(self.radius, 2)  #TODO:  G*m / R^2 WRONG!!!!
        # TODO: its not self.radius, its the freaking distance which i dont know how to calcualte without parallax
        # maybe we should let the person place the planet? :thinking_emoji:
        self.nrMoons = random.randint(0, round(self.gravity)) # the bigger the mass, the more (but its not a rule, f.e. Earth is bigger
                                            # and heavier than Mars but has less moons /shrug
        self.day = self.KeplersThirdLaw()
        # self.distance = my ass, we should do the "pick a spot" thingy

    def KeplersThirdLaw(self):
        # T^2 / a^3 is const for every planet in this system -> check with good ol' Earth (Sun is in center, so why not?)
        return math.sqrt(1 / pow(self.distance,3) * pow(149598,3)) # 1 AU = 149 587 870 700 m