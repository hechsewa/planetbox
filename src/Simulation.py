from Planet import *
from Moon import *
import menu
import main
import pygame

# FIXME: resizablity not working
# TODO: go from simulation to adding new planets and explorer

# global var for controlling the simulation
sim = True
pause = False
#planet colors
TER = (206, 196, 105)
ICE = (76, 134, 168)
GAS = (226, 181, 147)
WHITE = (255, 255, 255)
RICHBLUE = (2, 1, 34)

ico = pygame.image.load('favicon.ico')
pygame.init()
import sys
class Simulation:

    def __init__(self):
        self.Planets = []
        self.PlanetsCord = []  # stores planets initial (x, y, radius)

    def quit(self):
        pygame.quit()
        sys.exit()
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


    def check_scale(self, scale):
        new_scale = scale
        if scale <= 0.2:
            new_scale = 0.2
        elif scale >= 50:
            new_scale = 50
        return new_scale

    # animates the planets
    def animatePlanets(self, screen, w, h, scale):
        global sim, pause, ico
        pygame.display.set_caption('Planetbox')
        pygame.display.set_icon(ico)
        screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
        screen.fill(RICHBLUE)

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
                    self.animatePlanets(screen, event.dict['w'], event.dict['h'], scale)
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
                    if event.key == pygame.K_UP:
                        scale += 0.1
                        scale = self.check_scale(scale)
                        self.animatePlanets(screen, w, h, scale)
                    if event.key == pygame.K_DOWN:
                        scale -= 0.1
                        scale = self.check_scale(scale)
                        self.animatePlanets(screen, w, h, scale)
                    if event.key == pygame.K_r:
                        scale = 1
                        self.animatePlanets(screen, w, h, scale)

            screen.fill(RICHBLUE)

            pygame.draw.circle(screen, WHITE, [star_pos_x, star_pos_y], int(15*scale))
            for p in self.Planets:
                p.animate(screen, star_pos_x, star_pos_y, h, scale)

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
