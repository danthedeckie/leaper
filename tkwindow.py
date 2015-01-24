'''
    tkwindow.py (c) 2015 Daniel Fairhead
    --------
    Part of Leaper LeapMotion Control software
    GPL3.0
    --------
    This module is responsible for creating the Tk Diagnostics Window,
    and any other Tk GUI stuff, later on.
'''

from Tkinter import Tk, Canvas, Label, mainloop, StringVar
from threading import Thread
import leapmouse
from platforms import platform

def tkgui():
    ''' make a Tk-based diagnostics window '''

    window = Tk()

    position = [0, 0] # row, col

    def column(which):
        position[1] += which * 2
        position[0] = 0

    def add_item(label, variable=None):
        Label(window, text=label).grid(row=position[0], column=position[1])
        if variable:
            Label(window, textvariable=variable).grid(row=position[0], column=position[1]+1)
        position[0] +=1

    m_x = StringVar()
    m_y = StringVar()

    l_x = StringVar()
    l_y = StringVar()
    l_roll = StringVar() # wrist roll
    l_tilt = StringVar()
    l_pinch = StringVar()
    l_grab = StringVar()

    # mouse:

    column(0)

    add_item('Mouse Info:')
    add_item('x:', m_x)

    add_item('y:', m_y)

    # leap:
    column(1)

    add_item('Leap Info:')
    add_item('x:', l_x)
    add_item('y:', l_y)

    add_item('-')

    add_item('roll:', l_roll)
    add_item('tilt:', l_tilt)
    add_item('-')
    add_item('pinch:', l_pinch)
    add_item('grab:', l_grab)

    def update_texts():

        try:
            m_x.set(platform.x)
            m_y.set(platform.y)

            l_x.set(int(leapmouse.leapinfo.x))
            l_y.set(int(leapmouse.leapinfo.y))

            l_roll.set(leapmouse.leapinfo.hand.palm_normal.roll)
            l_tilt.set(leapmouse.leapinfo.hand.palm_normal.yaw)
            l_pinch.set(leapmouse.leapinfo.hand.pinch_strength)
            l_grab.set(leapmouse.leapinfo.hand.grab_strength)

        except Exception as e:
            pass

        window.after(1, update_texts)

    update_texts()

    mainloop()

def do_gui():
    ''' start the gui in it's own thread '''

    gui = Thread(target=tkgui)
    gui.daemon = True
    gui.start()
    return gui


if __name__ == '__main__':
    do_gui().join()
