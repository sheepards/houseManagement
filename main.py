# imports
from tkinter import *
import time
import os
from os import _exit
import json
import bimpy
import getpass
from datetime import datetime
import classes

# gui setup with tkinter
win = Tk()
win.title = "Haus Management"
win.geometry("1000x720")

# start drawing of the gui
#win.mainloop()

# get logged in user
system_user = getpass.getuser()

# gui setup with bimpy
# render new window
ctx = bimpy.Context()
# init main window
ctx.init(1280, 720, "Haus Management")
max_height = ctx.height()
max_width = ctx.width()

string = bimpy.String()
f = bimpy.Float()
i = bimpy.Int()

while(not ctx.should_close()):
    # display new window and set pos and size
    ctx.new_frame()

    bimpy.set_next_window_pos(bimpy.Vec2(10, 10), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(max_width - 20, max_height - 20), bimpy.Condition.Once)


    bimpy.begin("Willkommen {} es ist der {}".format(system_user, datetime.now().strftime('%d.%m.%Y um %H:%M:%S')))

    bimpy.input_text('Besitzer', string, 25)

    bimpy.end()
    ctx.render()
