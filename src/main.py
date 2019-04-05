#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:45:27 2019
haha april fools I suck at this :)
@author: hushmans
"""
#pip install thorpy, pygame
import thorpy, pygame

#define some colors
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


#main app loop
pygame.init()
DISPLAY = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Planetbox')
pygame.display.set_icon(ico)
DISPLAY.fill(RICHBLUE)

#display background
Bg = Background('../imgs/bg.jpg',[0,0])
DISPLAY.blit(Bg.image, Bg.rect)

#display sky preview
Skyprev = SkyPrev()

#update
pygame.display.update()

#thorpy elements

#logo
logo = pygame.image.load('../imgs/logo300.png')

#add button: adds planet to a list and updates prev
addBtn = thorpy.make_button("Add planet") #param2: func=...
addBtn.set_main_color(RICHBLUE)
addBtn.set_font_color(WHITE)
#addBtn.set_size((100,20))

#new window: starts simulation
startBtn = thorpy.make_button("Start simulation")
startBtn.set_main_color(RICHBLUE)
startBtn.set_font_color(WHITE)
#startBtn.set_size((100,20))


#entries
p_rad_txt = thorpy.OneLineText(text="Radius of the planet(km2):")
p_rad = thorpy.Inserter(name="", value="", size=(100,20))

p_name_txt = thorpy.OneLineText(text="Name of the planet: ")
p_name = thorpy.Inserter(name="", value="", size=(100,20))

p_mass_txt = thorpy.OneLineText(text="Mass of the planet (10^26 kg):")
p_mass = thorpy.Inserter(name="", value="", size=(100,20))

radio_txt = thorpy.make_text("Type of the planet: ")
radios = [thorpy.Checker("gas", type_="radio"),
          thorpy.Checker("ice", type_="radio"),
          thorpy.Checker("therestial", type_="radio")]
p_kind = thorpy.RadioPool(radios, first_value=radios[1], always_value=True)


prev_txt = thorpy.make_text("Preview of the planetary system: ", 24, WHITE)
prev_txt.set_font("Ubuntu.ttf")
prev_txt.set_topleft((420,200))

#blit thingies
entries = [p_rad_txt, p_rad, p_mass_txt, p_mass, p_name_txt, p_name]
txts = [radio_txt]
buttons = [addBtn, startBtn]
boxBtn = thorpy.Box.make(elements=entries+txts+radios+buttons)
boxBtn.set_main_color(WHITE)
boxBtn.set_size((260,500))
menu = thorpy.Menu(elements=[prev_txt,boxBtn])

for element in menu.get_population():
    element.surface = DISPLAY
    
boxBtn.set_topleft((40,50))
boxBtn.blit()
boxBtn.update()
prev_txt.blit()
prev_txt.update()
DISPLAY.blit(logo,(390,20))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        menu.react(event)
                              


