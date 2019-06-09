import thorpy
import pygame
import math
from src import menu

WHITE = (255,255,255)
BLACK = (0,0,0)
RICHBLUE = (2, 1, 34)
ORANGY = (255,82,27)
CARROT = (252,158,79)
FLAX = (237, 211, 130)
VANILLA = (242, 243, 174)
btnH = 50
btnW = 150
display_height = 600
display_width = 800

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def multiline_centered_txt(DISPLAY, text, font, size, height):
    lines = text.splitlines()
    w_width, w_height = DISPLAY.get_size()
    i=0
    for line in lines:
        kern = font.render(line, True, WHITE)
        DISPLAY.blit(kern, (w_width/2 - kern.get_width() // 2, height - kern.get_height() // 2 + i))
        i += size+size/4


def blit_logo(DISPLAY, w, h):
    logo = pygame.image.load('../imgs/logo150.png')
    DISPLAY.blit(logo, (w//2 - logo.get_width()//1.7, h))
    pygame.display.flip()


def text_object(text, font):
    textSurface = font.render(text, True, RICHBLUE)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, DISPLAY):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(DISPLAY, WHITE, (x, y, w, h))
        pygame.display.flip()
    else:
        pygame.draw.rect(DISPLAY, CARROT, (x, y, w, h))
        pygame.display.flip()

    smallText = pygame.font.Font("../imgs/Ubuntu-B.ttf", 18)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ((x+w/2), (y+h/2))
    DISPLAY.blit(textSurf, textRect)


def blit_all_info(DISPLAY, display_width, display_height):
    global btnW, btnH
    instr = "Planetbox is a simple, custom planetary system simulation. \n" \
            "It can simulate a whole planetary system and single planets and it's moons. \n" \
            "Planetbox allows you to add your own planets to the simulation, lets you name them, \n" \
            "and checks if the parameters are correct for the chosen type of a planet. \n"

    instr_sim = "Planetary system simulation: "
    instr_sim2 = "SPACE to pause/unpause simulation \n" \
                 "S to save information about your planetary system to a file containing all the calculations \n" \
                 "M to go to the menu\n" \
                 "A to go back to adding more planets \n"

    instr_exp = "Single planet simulation: "
    instr_exp2 = "SPACE to pause/unpause simulation \n" \
                 "E to go back to the explorer \n" \
                 "M to go to the menu\n" \
                 "A to go back to adding more planets \n \n" \
                 "UP to zoom in, DOWN to zoom out \n"

    credit = "© Ewa Hechsman, Laura Żuchowska"

    regular = pygame.font.Font("../imgs/Ubuntu-R.ttf", 14)
    small = pygame.font.Font("../imgs/Ubuntu-R.ttf", 10)
    bold = pygame.font.Font("../imgs/Ubuntu-B.ttf", 14)

    btn_pos_w = display_width//2 - btnW//2
    btn_pos_h = 0.8*display_height

    blit_logo(DISPLAY, display_width, 0.1*display_height)
    multiline_centered_txt(DISPLAY, instr, regular, 14, 0.3*display_height)
    multiline_centered_txt(DISPLAY, instr_sim, bold, 14, 0.43*display_height)
    multiline_centered_txt(DISPLAY, instr_sim2, regular, 14, 0.46*display_height)
    multiline_centered_txt(DISPLAY, instr_exp, bold, 14, 0.59*display_height)
    multiline_centered_txt(DISPLAY, instr_exp2, regular, 14, 0.62*display_height)
    button("BACK TO MENU", btn_pos_w, btn_pos_h, btnW, btnH, DISPLAY)

    multiline_centered_txt(DISPLAY, credit, small, 10, 0.9*display_height)

    pygame.display.update()


def main_loop(DISPLAY):
    global btnW, btnH, display_height, display_width
    pygame.init()
    clock = pygame.time.Clock()

    ico = pygame.image.load('../imgs/favicon.ico')

    display_width, display_height = DISPLAY.get_size()

    pygame.display.set_caption('Planetbox')
    pygame.display.set_icon(ico)
    DISPLAY.fill(RICHBLUE)

    # display background
    Bg = Background('../imgs/bg.jpg', [0, 0])
    DISPLAY.blit(pygame.transform.scale(Bg.image, (display_width, display_height)), Bg.rect)
    blit_all_info(DISPLAY, display_width, display_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                DISPLAY = pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
                DISPLAY.blit(pygame.transform.scale(Bg.image, event.dict['size']), (0, 0))
                pygame.display.flip()
                display_width = event.dict['w']
                display_height = event.dict['h']
                blit_all_info(DISPLAY, display_width, display_height)

            btn_w = display_width // 2 - btnW // 2
            btn_h = 0.77 * display_height
            #back to menu button
            if pygame.mouse.get_pos()[0] >= btn_w and pygame.mouse.get_pos()[1] >= btn_h:
                if pygame.mouse.get_pos()[0] <= btn_w + btnW and pygame.mouse.get_pos()[1] <= (btn_h + btnH):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        menu.mainer(DISPLAY)

        btn_pos_w = display_width // 2 - btnW // 2
        btn_pos_h = 0.8 * display_height
        button("BACK TO MENU", btn_pos_w, btn_pos_h, btnW, btnH, DISPLAY)
        pygame.display.flip()
        clock.tick(20)