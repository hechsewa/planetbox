import pygame, thorpy
import tkinter as tk

WHITE = '#ffffff'
BLACK = '#000000'
RICHBLUE = '#020122'
FONT=("Ubuntu", 12)

class AlertBox:

    def __init__(self, val, type):
        alert = tk.Tk()
        alert['background']=RICHBLUE
        alert.wm_title("Density is not right")
        if(type == "density"):
            if(val==0):
                text_small = "Density of the planet is too small for that type of planet. " \
                             "\n Please change the type of planet or planet's attributes."
                label = tk.Label(alert, text=text_small, font=FONT, fg=WHITE)
            if(val==1):
                text_big = "Density of the planet is too big for that type of planet. " \
                           "\n Please change the type of planet or planet's attributes."
                label = tk.Label(alert, text=text_big, font=FONT, fg=WHITE)
        elif(type == "radius"):
            if(val==0):
                text_rad = "Radius of the planet is too small for that type of planet. "\
                           "\n Please change the type of planet or planet's attributes."
                label = tk.Label(alert, text=text_rad, font=FONT, fg=WHITE)
        elif(type == "valueError"):
            text_err = "Please insert only numeric (int or float) values" \
                        "\n for planet's radius, distance and mass."
            label = tk.Label(alert, text=text_err, font=FONT, fg=WHITE)

        label['background'] = RICHBLUE
        label.pack(side="top", fill="x", pady=10)
        ok_btn = tk.Button(alert, text="okay", command=alert.destroy, font=FONT)
        ok_btn.config(fg=WHITE)
        ok_btn['background'] = RICHBLUE
        ok_btn.pack()
        alert.mainloop()