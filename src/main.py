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

#background handling
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class SkyPrev(pygame.sprite.Sprite):
    def __init__(self):
        pygame.draw.rect(DISPLAY, BLACK, (350, 250, 415, 315), 0)
        pygame.draw.rect(DISPLAY, WHITE, (350, 250, 415, 315), 2)

#main app loop
pygame.init()
DISPLAY = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Planetbox')
DISPLAY.fill(RICHBLUE)

#display background
Bg = Background('../imgs/bg.jpg',[0,0])
DISPLAY.blit(Bg.image, Bg.rect)

#display sky preview
Skyprev = SkyPrev()

#update
pygame.display.update()

#thorpy elements
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
p_rad = thorpy.Inserter(name="Radius of the planet(km2)", value="", size=(100,20))
p_name = thorpy.Inserter(name="Name of the planet: ", value="", size=(100,20))
p_weight = thorpy.Inserter(name="Weight of the planet: ", value="", size=(100,20))
radios = [thorpy.Checker("gas", type_="radio"),
          thorpy.Checker("rock", type_="radio")]
p_kind = thorpy.RadioPool(radios, first_value=radios[1], always_value=True)


#blit thingies
entries = [p_rad, p_weight, p_name]
buttons = [addBtn, startBtn]
boxBtn = thorpy.Box.make(elements=entries+radios+buttons)
boxBtn.set_main_color(WHITE)
boxBtn.set_size((260,500))
menu = thorpy.Menu(elements=[boxBtn])

for element in menu.get_population():
    element.surface = DISPLAY
    
boxBtn.set_topleft((40,50))
boxBtn.blit()
boxBtn.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        menu.react(event)
                              


