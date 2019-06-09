#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This is the initial file. Launches the main menu.
@author: hushmans
"""
import pygame
from pygame.locals import *

from src import Instructions
from src import main

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RICHBLUE = (2, 1, 34)
ORANGY = (255, 82, 27)
CARROT = (252, 158, 79)
FLAX = (237, 211, 130)
VANILLA = (242, 243, 174)

#def btnW i btnH
btnW = 150
btnH = 50
btn_h1 = 0
btn_h2 = 0
btn_h3 = 0
display_width = 800
display_height = 600

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def blit_logo(DISPLAY, w, h):
    logo = pygame.image.load('../imgs/logo300.png')
    DISPLAY.blit(logo, (w//2-logo.get_width()//1.7, h))
    pygame.display.flip()


def text_object(text, font):
    textSurface = font.render(text, True, RICHBLUE)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, DISPLAY):
    mouse = pygame.mouse.get_pos()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAY, WHITE, (x, y, w, h))
        pygame.display.flip()
    else:
        pygame.draw.rect(DISPLAY, CARROT, (x, y, w, h))
        pygame.display.flip()

    smallText = pygame.font.Font("../imgs/Ubuntu-B.ttf", 18)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ((x+w/2), (y+h/2))
    DISPLAY.blit(textSurf, textRect)


def blit_menu(DISPLAY, display_width, display_height):
    global btnW, btnH, btn_h1, btn_h2, btn_h3
    btn_pos_w = display_width//2 - btnW//2
    btn_h1 = 0.45*display_height
    btn_h2 = 0.57*display_height
    btn_h3 = 0.69*display_height
    button("START", btn_pos_w, btn_h1, btnW, btnH, DISPLAY)
    button("INSTRUCTIONS", btn_pos_w, btn_h2, btnW, btnH, DISPLAY)
    button("QUIT", btn_pos_w, btn_h3, btnW, btnH, DISPLAY)


def mainer(DISPLAY):
    global btnW, btnH, btn_h1, btn_h2, btn_h3, display_height, display_width
    pygame.init()
    clock = pygame.time.Clock()

    # define display size

    ico = pygame.image.load('../imgs/favicon.ico')

    display_height = DISPLAY.get_height()
    display_width = DISPLAY.get_width()

    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY.fill(RICHBLUE)

    # display background
    Bg = Background('../imgs/bg.jpg', [0, 0])
    DISPLAY.blit(pygame.transform.scale(Bg.image, (display_width, display_height)), Bg.rect)

    blit_logo(DISPLAY, display_width, 50)

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            #resizablility
            if event.type == pygame.VIDEORESIZE:
                DISPLAY = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                DISPLAY.blit(pygame.transform.scale(Bg.image, event.dict['size']), (0, 0))
                pygame.display.flip()
                display_width = event.dict['w']
                display_height = event.dict['h']
                mainer(DISPLAY)
                pygame.display.update()

            btn_w = display_width // 2 - btnW // 2
            # start button
            if pygame.mouse.get_pos()[0] >= btn_w and pygame.mouse.get_pos()[1] >= btn_h1:
                if pygame.mouse.get_pos()[0] <= btn_w+btnW and pygame.mouse.get_pos()[1] <= (btn_h1+btnH):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        main.apploop(DISPLAY)
            # quit button
            if pygame.mouse.get_pos()[0] >= btn_w and pygame.mouse.get_pos()[1] >= btn_h3:
                if pygame.mouse.get_pos()[0] <= btn_w+btnW and pygame.mouse.get_pos()[1] <= btn_h3+btnH:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        quit()
            # instructions button
            if pygame.mouse.get_pos()[0] >= btn_w and pygame.mouse.get_pos()[1] >= btn_h2:
                if pygame.mouse.get_pos()[0] <= btn_w+btnW and pygame.mouse.get_pos()[1] <= btn_h2+btnH:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        Instructions.main_loop(DISPLAY)

        blit_menu(DISPLAY, display_width, display_height)
        pygame.display.flip()
        clock.tick(10)


if __name__ == '__main__':
    DISPLAY = pygame.display.set_mode((display_width, display_height), RESIZABLE)
    mainer(DISPLAY)