from src.Planet import *
from src.Moon import *

class Simulation:

    def __init__(self):
        self.Planets = []

    def drawPlanets(self, screen, w, h):
        star_pos_x = int(w / 2)
        star_pos_y = int(h / 2)
        # display main star
        pygame.draw.circle(screen, WHITE, [star_pos_x, star_pos_y], 15)
        for p in self.Planets:
            dist = int(p.distance * (h / 3))
            x = int(math.cos(0 * 2 * math.pi / 360)*dist) + star_pos_x
            y = int(math.sin(0 * 2 * math.pi / 360) * dist) + star_pos_y
            p.drawOrbit(screen, star_pos_x, star_pos_y)
            p.drawPlanet(screen, x, y)
            pygame.display.update()


    def animatePlanets(self, screen, w, h):
        # w, h = pygame.display.get_surface().get_size()
        star_pos_x = int(w / 2)
        star_pos_y = int(h / 2)

        clock = pygame.time.Clock()

        for degree in range(0, 360, 10):
            # display main star
            pygame.draw.circle(screen, WHITE, [star_pos_x, star_pos_y], 15)
            for p in self.Planets:
                dist = int(p.distance * (h / 3))
                xRadius = dist
                yRadius = dist
                x1 = int(math.cos(degree * 2 * math.pi / 360) * xRadius) + star_pos_x
                y1 = int(math.sin(degree * 2 * math.pi / 360) * yRadius) + star_pos_y
                screen.fill(RICHBLUE)


                p.drawOrbit(screen, star_pos_x, star_pos_y)
                p.drawPlanet(screen, x1, y1)
            pygame.display.flip()
            clock.tick(5)



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

