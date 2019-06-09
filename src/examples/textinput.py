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

scene = canvas(title='Planetbox', x=0, y=0, width=disp_width, height=disp_height,
               center=vector(5, 0, 0), background=RICHBLUE)

position = vector(0,0,0)
Star = sphere(pos=position, radius=50, color=color.white)

G = 6.7e-11 # Newton gravitational constant

giant = sphere(pos=vector(-1e11,0,0), radius=2e10, color=color.red,
               make_trail=True, trail_type='points', interval=10, retain=50)
giant.mass = 2e30
giant.p = vector(0, 0, -1e4) * giant.mass

dwarf = sphere(pos=vector(1.5e11, 0, 0), radius=1e10, color=RICHBLUE,
               make_trail=True, interval=10, retain=50)
dwarf.mass = 1e30
dwarf.p = -giant.p

dt = 1e5
while True:
    rate(200)
    r = dwarf.pos - giant.pos
    F = G * giant.mass * dwarf.mass * r.hat / mag2(r)
    giant.p = giant.p + F*dt
    dwarf.p = dwarf.p - F*dt
    giant.pos = giant.pos + (giant.p/giant.mass) * dt
    dwarf.pos = dwarf.pos + (dwarf.p/dwarf.mass) * dt

