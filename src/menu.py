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


def blit_logo(DISPLAY, w, h):
    logo = pygame.image.load('../imgs/logo300.png')
    DISPLAY.blit(logo, (w, h))
    pygame.display.flip()


def text_object(text, font):
    textSurface = font.render(text, True, RICHBLUE)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h, DISPLAY):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(DISPLAY, WHITE, (x,y,w,h))
        pygame.display.flip()
    else:
        pygame.draw.rect(DISPLAY, VANILLA, (x, y, w, h))
        pygame.display.flip()

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

    DISPLAY = pygame.display.set_mode((display_width, display_height), RESIZABLE)

    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY.fill(RICHBLUE)

    # display background
    Bg = Background('../imgs/bg.jpg', [0, 0])
    DISPLAY.blit(pygame.transform.scale(Bg.image, (display_width, display_height)), Bg.rect)

    blit_logo(DISPLAY, 220, 50)
    btn_w = 320
    btn_h1 = 270
    btn_h2 = 340
    btn_h3 = 410
    button("START", btn_w, btn_h1, 150, 50, DISPLAY)
    button("ABOUT", btn_w, btn_h2, 150, 50, DISPLAY)
    button("QUIT", btn_w, btn_h3, 150, 50, DISPLAY)
    pygame.display.update()

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
                btnH = 50
                btnW = 150

                logoH = event.dict['h']/8
                logoW = event.dict['w']/3
                spaceH = event.dict['h']/10

                btn_w = logoW + btnW / 2
                btn_h1 = logoH + 3.5 * spaceH
                btn_h2 = logoH + 3.5 * spaceH + btnH + 20
                btn_h3 = logoH + 3.5 * spaceH + 2 * btnH + 40

                blit_logo(DISPLAY, logoW, logoH)
                button("START", btn_w, btn_h1, btnW, btnH, DISPLAY)
                button("ABOUT", btn_w, btn_h2, btnW, btnH, DISPLAY)
                button("QUIT", btn_w, btn_h3, btnW, btnH, DISPLAY)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # start button
                if pygame.mouse.get_pos()[0] >= btn_w and pygame.mouse.get_pos()[1] >= btn_h1:
                    if pygame.mouse.get_pos()[0] <= btn_w+150 and pygame.mouse.get_pos()[1] <= (btn_h1+50):
                        main.apploop()
                # quit button
                if pygame.mouse.get_pos()[0] >= btn_w and pygame.mouse.get_pos()[1] >= btn_h3:
                    if pygame.mouse.get_pos()[0] <= btn_w+150 and pygame.mouse.get_pos()[1] <= btn_h3+50:
                        pygame.quit()
                        quit()

        pygame.display.update()
        clock.tick(15)

if __name__ == '__main__': mainer()