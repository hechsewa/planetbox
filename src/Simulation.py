class Simulation:
    def __init__(self):
        self.Planets = []


    def AddPlanet(self, planet):
        self.Planets.append(planet)

    def PrintPlanets(self):
        i = 1
        for planet in self.Planets:
            print("Planet nb: " + str(i) + ", name: " + planet.name)
            i = i+1
