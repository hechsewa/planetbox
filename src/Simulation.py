from src.Planet import *
from src.Moon import *

class Simulation:
    def __init__(self):
        self.Planets = []


    def AddPlanet(self, planet):
        self.Planets.append(planet)

    def PrintPlanets(self):
        i = 1
        for planet in self.Planets:
            print("Planet nb: " + str(i) + ", Name: " + planet.name + ", Distance: " + str(planet.distance) +", Mass: " + str(planet.mass))
            print("Gravitational field: " + str(planet.gravity) + "N/kg, Year time: " + str(planet.year))
            print("Number of moons: " + str(planet.nrMoons))
            i = i+1


    def CreateMoons(self):
        for planet in self.Planets:
            for nbMoon in range(planet.nrMoons):
                if(len(str(planet.mass)) <= 8):
                    mass = random.randint(round(planet.mass / 10000), round(planet.mass / 100)) # for now its hardcoded, may think
                else:                                                                   # about change later
                    mass = random.randint(round(planet.mass / 1000000), round(planet.mass / 1000))
                if mass == 0:
                    mass = 1
                highBorderDistance = int(round((mass / 4.8 * math.pi) ** (1. / 3)) ** 3)
                lowBorderDistance = int(round((mass / 97.2 * math.pi) ** (1. / 3)) ** 3)
                if lowBorderDistance == 0:
                    lowBorderDistance = 1
                radius = random.randint(lowBorderDistance, highBorderDistance)
                moon = Moon(radius, mass, planet)
                planet.moons.append(moon)

