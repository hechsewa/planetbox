from src.Planet import *
from src.Moon import *

#global var for controlling the simulation
sim = True

class Simulation:

    def __init__(self):
        self.Planets = []


    #draws static planets (for preview)
    def drawPlanets(self, screen, w, h, xs, ys):
        #x, y point to where in starts, usually (0,0) but preview :<
        star_pos_x = xs + int(w / 2)
        star_pos_y = ys + int(h / 2)
        # display main star
        pygame.draw.circle(screen, WHITE, [star_pos_x, star_pos_y], 15)
        for p in self.Planets:
            dist = int(p.distance * (h / 3))
            x = int(math.cos(0 * 2 * math.pi / 360)*dist) + star_pos_x
            y = int(math.sin(0 * 2 * math.pi / 360) * dist) + star_pos_y
            p.drawPlanet(screen, x, y)
            pygame.display.update()


    #animates the planets
    def animatePlanets(self, screen, w, h, degree):
        global sim
        star_pos_x = int(w / 2)
        star_pos_y = int(h / 2)
        clock = pygame.time.Clock()

        sim = True
        while sim:
            #closes the simulation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode(event.dict['size'],
                                                     pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                    screen.fill(RICHBLUE)
                    sim = False
                    self.animatePlanets(screen, event.dict['w'], event.dict['h'], degree)

            screen.fill(RICHBLUE)
            degree += 10
            if degree == 360:
                degree = 0
            pygame.draw.circle(screen, WHITE, [star_pos_x, star_pos_y], 15)
            for p in self.Planets:
                dist = int(p.distance * (h / 3))
                x = int(math.cos(degree * 2 * math.pi / 360) * dist) + star_pos_x
                y = int(math.sin(degree * 2 * math.pi / 360) * dist) + star_pos_y

                p.drawOrbit(screen, star_pos_x, star_pos_y)
                p.drawPlanet(screen, x, y)

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

