from vpython import *
from src import Simulation

TER = (206, 196, 105)
ICE = (76, 134, 168)
GAS = (226, 181, 147)
WHITE = (255, 255, 255)
RICHBLUE = vector(2, 1, 34)

disp_width = 800
disp_height = 600

sim = Simulation.Simulation()

scene = canvas(title='Examples of Tetrahedrons', x=0, y=0, width=disp_width, height=disp_height,
                        center=vector(5, 0, 0), background=RICHBLUE)

position = vector(0,0,0)
Star = sphere(pos=position, radius=100, color=color.white)

while True:
    rate(50)
