from src.Planet import *
from src.Moon import *
from src import menu
from src import main

# FIXME: resizablity not working
# TODO: go from simulation to adding new planets and explorer

# global var for controlling the simulation
sim = True
pause = False


class Simulation:

    def __init__(self):
        self.Planets = []
        self.PlanetsCord = []  # stores planets initial (x, y, radius)

    # calculates planets' position and size (for preview)
    def calcPlanetCord(self, x, y, p, h):
        rad = int(p.radius / h)
        self.PlanetsCord.append((x, y, rad))

    # draws static planets (for preview)
    def drawPlanets(self, screen, w, h, xs, ys, scale):
        self.orderSystem()
        self.PlanetsCord = []
        #x, y point to where in starts, usually (0,0) but preview :<
        star_pos_x = xs + int(w / 2)
        star_pos_y = ys + int(h / 2)
        # display main star
        pygame.draw.circle(screen, WHITE, [star_pos_x, star_pos_y], int(15*scale))
        if len(self.Planets) != 0:
            dist = int(300/len(self.Planets))*scale  # distance between planets
        else:
            return
        i = 1
        for p in self.Planets:
            x = i*dist + star_pos_x
            i = i + 1
            y = star_pos_y
            p.drawPlanet(screen, x, y, scale)
            self.calcPlanetCord(x, y, p, h)
            pygame.display.update()

    #unpause function
    def unpause(self):
        global pause
        pause = False

    #pause function
    def paused(self, screen):
        global pause

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.unpause()
                    #return to menu from pause
                    if event.key == pygame.K_m: #if m then stop and go to menu
                        menu.mainer(screen)
                    if event.key == pygame.K_a: #if a then go to adding planets screen
                        main.apploop(screen)
                    if event.key == pygame.K_s:
                        self.WriteSimToFile()

    def orderSystem(self):
        self.Planets.sort(key=lambda x: x.distance)


    # animates the planets
    def animatePlanets(self, screen, w, h):
        global sim, pause
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
                    self.animatePlanets(screen, event.dict['w'], event.dict['h'])
                # KEY EVENTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # if space pressed then pause
                        pause = True
                        self.paused(screen)
                    if event.key == pygame.K_m:  # if m then stop and go to menu
                        menu.mainer(screen)
                    if event.key == pygame.K_a: #if a then go to adding planets screen
                        main.apploop(screen)
                    if event.key == pygame.K_s:
                        self.WriteSimToFile()

            screen.fill(RICHBLUE)

            pygame.draw.circle(screen, WHITE, [star_pos_x, star_pos_y], 15)
            for p in self.Planets:
                p.animate(screen, star_pos_x, star_pos_y, h)

            pygame.display.flip()
            clock.tick(10)

    def AddPlanet(self, planet):
        self.Planets.append(planet)

    def PrintPlanets(self):
        i = 1
        for planet in self.Planets:
            print("Planet nb: " + str(i))
            print(planet.printPlanet())
            i = i+1

    def WriteSimToFile(self):
        f = open("Statistics.txt", "w+")
        for planet in self.Planets:
            f.write(planet.printPlanet())
            i = 1
            for moon in planet.moons:
                f.write("\nMoon number %s:" % i)
                f.write(moon.printMoon())
                i = i + 1
            f.write("\n--------\n")
        f.close()
