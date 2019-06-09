import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'D:\Users\ewahe\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Users\ewahe\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

base = "Win32GUI"

path="C:/Users/ewahe/OneDrive/Dokumenty/planetbox-master/imgs/"
executables = [cx_Freeze.Executable("menu.py", base=base, targetName="Planetbox.exe", icon=path+"favicon.ico")]

cx_Freeze.setup(
    name="Planetbox",
    options={"build_exe": { "packages": ["tkinter", "pygame", "thorpy", "math"],
                              "include_files": [
                                  path+"favicon.ico",
                                  path+"Ubuntu-R.ttf",
                                  path+"Ubuntu-B.ttf",
                                  path+"logo300.png",
                                  path+"bg.jpg",
                                  path+"logo.png",
                                  path+"logo150.png"
                              ]}},
    executables=executables
)
