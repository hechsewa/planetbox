#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:45:27 2019
haha april fools I suck at this :)
@author: hushmans
"""
#pip install thorpy, pygame
import thorpy, pygame, math, ctypes
from src import Planet
from src import AlertBox

#define some colors
from src.Simulation import Simulation

WHITE = (255,255,255)
BLACK = (0,0,0)
RICHBLUE = (2, 1, 34)
ORANGY = (255,82,27)
CARROT = (252,158,79)
FLAX = (237, 211, 130)
VANILLA = (242, 243, 174)

#define display size
display_width = 800
display_height = 600
ico = pygame.image.load('../imgs/favicon.ico')
pygame.init()
DISPLAY = pygame.display.set_mode((display_width, display_height))
#global planet variables
prad=0
pmass=0
pname=""
ptype=""

simulation = Simulation()

#background handling
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#sky prev handling
class SkyPrev(pygame.sprite.Sprite):
    def __init__(self):
        pygame.draw.rect(DISPLAY, BLACK, (350, 250, 415, 315), 0)
        pygame.draw.rect(DISPLAY, WHITE, (350, 250, 415, 315), 2)

def apploop():
    #main app loo
    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY.fill(RICHBLUE)

    #display background
    Bg = Background('../imgs/bg.jpg', [0, 0])
    DISPLAY.blit(Bg.image, Bg.rect)

    #display sky preview
    Skyprev = SkyPrev()

    #update
    pygame.display.update()

    #thorpy elements

    #logo
    logo = pygame.image.load('../imgs/logo300.png')

    # checks if the density is ok
    def density_check(ptype, pmass, prad):
        # pmass: 10^22 kg, prad: km
        rad = prad*100000  # radius in cm
        vol = (4/3)*math.pi*rad*rad*rad  # cm3
        mass = pmass * 10 ^ 25  # g
        g = mass/vol  # g/cm3

        if ptype == "terrestial":
            if (g<3.8):
                return 0
            elif (g>5.5):
                return 1
            else:
                return 2
        elif ptype == "gas" or ptype == "ice":
            if (g<0.2):
                return 0
            elif (g>2.0):
                return 1
            else:
                return 2

    #Reading inputs functions
    #TODO: check conditions for inserted values, eg. if is bigger than 0 if mass is proportional to radius etc


    def read_inserter_func(event):#Reactions functions must take an event as first arg
        global prad, pmass, pname
        if(event.el == p_rad):
            prad = event.el.get_value()
            prad = int(prad)
            print(prad)
        elif(event.el == p_mass):
            pmass = event.el.get_value()
            pmass = int(pmass)
            print(pmass)
        elif(event.el == p_name):
            pname = event.el.get_value()
            print(pname)
        elif(event.el== p_kind):
            ptype = event.el.get_value()
            print(ptype)


    # pressing add planet btn reaction
    def readPlanet():
        global prad, pmass, pname, ptype, simulation
        ptype = p_kind.get_selected().get_text()
        val = density_check(ptype, pmass, prad)
        if val == 0 or val == 1:
            AlertBox.AlertBox(val)
        else:
            print(ptype)
            #create a new planet
            # clean the inserters
            p_rad.set_value("")
            p_rad.unblit_and_reblit()
            p_mass.set_value("")
            p_mass.unblit_and_reblit()
            p_name.set_value("")
            p_name.unblit_and_reblit()
            planet = Planet.Planet(prad, pmass, ptype, pname)
            simulation.AddPlanet(planet)

    def startSimulation():
        print("Starting simulation...")
        print(simulation.PrintPlanets())


    # add button: adds planet to a list and updates prev
    addBtn = thorpy.make_button("Add planet", func=readPlanet)
    addBtn.set_size((100, 20))
    addBtn.set_main_color(RICHBLUE)
    addBtn.set_font_color(WHITE)

    # new window: starts simulation
    startBtn = thorpy.make_button("Start simulation", func=startSimulation)
    startBtn.set_size((100, 20))
    startBtn.set_main_color(RICHBLUE)
    startBtn.set_font_color(WHITE)

    # update preview: adds newly added planets to the preview and rearranges the orbits
    prevBtn = thorpy.make_button("Update preview")
    prevBtn.set_size((100, 20))
    prevBtn.set_main_color(RICHBLUE)
    prevBtn.set_font_color(WHITE)

    # radius input
    p_rad_txt = thorpy.OneLineText(text="Radius of the planet(km):")
    p_rad = thorpy.Inserter(name="", value="", size=(100, 20))

    radReact = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                               reac_func=read_inserter_func,
                               event_args={"id":thorpy.constants.EVENT_INSERT,
                                              "el":p_rad})

    p_rad.add_reaction(radReact)

    # name input
    p_name_txt = thorpy.OneLineText(text="Name of the planet: ")
    p_name = thorpy.Inserter(name="", value="", size=(100, 20))
    nameReact = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=read_inserter_func,
                                event_args={"id":thorpy.constants.EVENT_INSERT,
                                            "el":p_name})

    p_name.add_reaction(nameReact)

    # mass input
    p_mass_txt = thorpy.OneLineText(text="Mass of the planet (10^22 kg):")
    p_mass = thorpy.Inserter(name="", value="", size=(100, 20))
    massReact = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=read_inserter_func,
                                event_args={"id":thorpy.constants.EVENT_INSERT,
                                              "el":p_mass})

    p_mass.add_reaction(massReact)

    # type of planet input
    radio_txt = thorpy.make_text("Type of the planet: ")
    radios = [thorpy.Checker("gas", type_="radio"),
              thorpy.Checker("ice", type_="radio"),
              thorpy.Checker("therestial", type_="radio")]
    p_kind = thorpy.RadioPool(radios, first_value=radios[1], always_value=True)


    # title above the preview
    prev_txt = thorpy.make_text("Preview of the planetary system: ", 24, WHITE)
    prev_txt.set_font("Ubuntu.ttf")
    prev_txt.set_topleft((420, 200))

    # blit thingies
    entries = [p_rad_txt, p_rad, p_mass_txt, p_mass, p_name_txt, p_name]
    txts = [radio_txt]
    buttons = [addBtn, prevBtn, startBtn]
    elements = entries+txts+radios+buttons
    boxBtn = thorpy.Box.make(elements=elements)
    boxBtn.set_main_color(WHITE)
    boxBtn.set_size((260, 500))

    thorpy.store(boxBtn, elements, align="center")

    menu = thorpy.Menu(elements=[prev_txt, boxBtn])

    for element in menu.get_population():
        element.surface = DISPLAY

    boxBtn.set_topleft((40, 50))
    boxBtn.blit()
    boxBtn.update()
    prev_txt.blit()
    prev_txt.update()
    DISPLAY.blit(logo, (390, 20))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            menu.react(event)


if __name__ == '__main__': apploop()
