#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:45:27 2019
haha april fools I suck at this :)
@author: hushmans
# TODO: resizable!!
"""
#pip install thorpy, pygame
import thorpy
import pygame
import math
from src import Planet
from src import AlertBox
from src import simulation_gui

#define some colors
from src.Simulation import Simulation
from src.PlanetExplorer import PlanetExplorer


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
DISPLAY = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)

# global planet variables
prad=0
pmass=0
pdist=0 # distance to the sun
pname=""
ptype=""

# def some useful objects
simulation = Simulation()
planetExp = PlanetExplorer(simulation)

# background handling
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# sky prev handling
class SkyPrev(pygame.sprite.Sprite):
    def __init__(self):
        pygame.draw.rect(DISPLAY, BLACK, (350, 250, 415, 315), 0)
        pygame.draw.rect(DISPLAY, WHITE, (350, 250, 415, 315), 2)
        simulation.drawPlanets(DISPLAY, 415, 315, 350, 250)


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

    def radius_check(radius, type):
        if (type == "terrestrial"):
            if (radius < 300):
                return 0
            else:
                return 1
        elif (type == "ice" or type == "gas"):
            if (radius < 200):
                return 0
            else:
                return 1

    # checks if the density is ok
    def density_check(ptype, pmass, prad):
        # pmass: 10^22 kg, prad: km
        rad = prad*100000  # radius in cm
        vol = (4/3)*math.pi*rad*rad*rad  # cm3
        mass = pmass * pow(10,25)  # g
        g = mass/vol  # g/cm3

        if ptype == "terrestrial":
            if (g < 3.6): # not sure about this one
                return 0
            elif (g > 28):
                return 1
            else:
                return 2
        elif ptype == "gas" or ptype == "ice":
            if (g < 0.2): # not sure about this one
                return 0
            elif (g > 17):
                return 1
            else:
                return 2

    #Reading inputs functions

    def read_inserter_func(event):#Reactions functions must take an event as first arg
        global prad, pmass, pname, pdist
        if(event.el == p_rad):
            prad = event.el.get_value()
            prad = int(prad)
            #print(prad)
        elif(event.el== p_dist):
            pdist = event.el.get_value()
            pdist = float(pdist)
            #print(pdist)
        elif(event.el == p_mass):
            pmass = event.el.get_value()
            pmass = int(pmass)
            #print(pmass)
        elif(event.el == p_name):
            pname = event.el.get_value()
            #print(pname)
        elif(event.el== p_kind):
            ptype = event.el.get_value()
            #print(ptype)

    # pressing add planet btn reaction
    def readPlanet():
        global prad, pmass, pname, ptype, simulation, pdist
        ptype = p_kind.get_selected().get_text()
        den_val = density_check(ptype, pmass, prad)
        rad_val = radius_check(prad, ptype)
        if den_val == 0 or den_val == 1: #wrong density
            AlertBox.AlertBox(den_val, "density")
        elif rad_val == 0: #radius too small
            AlertBox.AlertBox(rad_val, "radius")
        else:
            print(ptype)
            #create a new planet
            # clean the inserters
            p_rad.set_value("")
            p_rad.unblit_and_reblit()

            p_dist.set_value("")
            p_dist.unblit_and_reblit()

            p_mass.set_value("")
            p_mass.unblit_and_reblit()

            p_name.set_value("")
            p_name.unblit_and_reblit()

            planet = Planet.Planet(prad, pmass, ptype, pdist, pname)
            simulation.AddPlanet(planet)
            # update preview
            SkyPrev()

    def startExplorer():
        print("Starting explorer...")
        planetExp.pe_main()

    def startSimulation():
        #simulation.CreateMoons()
        print("Starting simulation...")
        print(simulation.PrintPlanets())
        simulation_gui.create(simulation)

    # add button: adds planet to a list and updates prev
    addBtn = thorpy.make_button("Add planet", func=readPlanet)
    addBtn.set_size((120, 20))
    addBtn.set_main_color(RICHBLUE)
    addBtn.set_font_color(WHITE)

    # new window: starts simulation
    startBtn = thorpy.make_button("Start simulation", func=startSimulation)
    startBtn.set_size((120, 20))
    startBtn.set_main_color(RICHBLUE)
    startBtn.set_font_color(WHITE)

    # explore planets: lets u choose a planet and prints info about it and moons simulation
    prevBtn = thorpy.make_button("Explore the planets", func=startExplorer)
    prevBtn.set_size((120, 20))
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

    # distance to the sun input
    p_dist_txt = thorpy.OneLineText(text="Distance to the sun (AU):")
    p_dist = thorpy.Inserter(name="", value="", size=(100, 20))

    distReact = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=read_inserter_func,
                                event_args={"id": thorpy.constants.EVENT_INSERT,
                                           "el": p_dist})

    p_dist.add_reaction(distReact)

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
              thorpy.Checker("terrestrial", type_="radio")]
    p_kind = thorpy.RadioPool(radios, first_value=radios[1], always_value=True)


    # title above the preview
    prev_txt = thorpy.make_text("Preview of the planetary system: ", 24, WHITE)
    prev_txt.set_font("Ubuntu.ttf")
    prev_txt.set_topleft((420, 200))

    # blit thingies
    entries = [p_rad_txt, p_rad, p_mass_txt, p_mass, p_dist_txt, p_dist, p_name_txt, p_name]
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
