#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This is the initial file. Launches the main menu.
@author: hushmans
"""
import pygame
import time
from pygame.locals import *
from src import main

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RICHBLUE = (2, 1, 34)
ORANGY = (255, 82, 27)
CARROT = (252, 158, 79)
FLAX = (237, 211, 130)
VANILLA = (242, 243, 174)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def blit_logo(DISPLAY):
    logo = pygame.image.load('../imgs/logo300.png')
    DISPLAY.blit(logo, (220, 50))
    pygame.display.flip()


def text_object(text, font):
    textSurface = font.render(text, True, RICHBLUE)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h, DISPLAY):
    mouse = pygame.mouse.get_pos()

    if x+w> mouse[0] > x and y+h>mouse[1] > y:
        pygame.draw.rect(DISPLAY, WHITE, (x,y,w,h))
    else:
        pygame.draw.rect(DISPLAY, VANILLA, (x, y, w, h))

    smallText = pygame.font.Font("../imgs/Ubuntu-B.ttf", 18)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ((x+w/2), (y+h/2))
    DISPLAY.blit(textSurf, textRect)

def mainer():
    pygame.init()
    clock = pygame.time.Clock()

    # define display size
    display_width = 800
    display_height = 600
    ico = pygame.image.load('../imgs/favicon.ico')

    DISPLAY = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY.fill(RICHBLUE)


    # display background
    Bg = Background('../imgs/bg.jpg', [0, 0])
    DISPLAY.blit(Bg.image, Bg.rect)


    blit_logo(DISPLAY)

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start button
                if pygame.mouse.get_pos()[0] >= 320 and pygame.mouse.get_pos()[1] >= 270:
                    if pygame.mouse.get_pos()[0] <= 470 and pygame.mouse.get_pos()[1] <= 320:
                        main.apploop()
                # quit button
                if pygame.mouse.get_pos()[0] >= 320 and pygame.mouse.get_pos()[1] >= 410:
                    if pygame.mouse.get_pos()[0] <= 470 and pygame.mouse.get_pos()[1] <= 460:
                        pygame.display.flip()
                        return

        button("START", 320, 270, 150, 50, DISPLAY)
        button("ABOUT", 320, 340, 150, 50, DISPLAY)
        button("QUIT", 320, 410, 150, 50, DISPLAY)

        pygame.display.update()
        clock.tick(15)

if __name__ == '__main__': mainer()