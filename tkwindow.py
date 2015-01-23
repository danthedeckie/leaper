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
from leapmouse import leapinfo
from platforms import platform

def tkgui():
    ''' make a Tk-based diagnostics window '''

    window = Tk()
    #canvas = Canvas(window, width=300, height=300)
    #canvas.grid()

    # mouse:

    Label(window, text='Mouse Info:').grid(row=0, column=0)

    xtext = StringVar()
    xtext.set('X')

    ytext = StringVar()
    ytext.set('Y')

    Label(window, text='x:').grid(row=1, column=0)
    xbox = Label(window, textvariable=xtext)
    xbox.grid(row=1, column=1)

    Label(window, text='y:').grid(row=2, column=0)
    ybox = Label(window, textvariable=ytext)
    ybox.grid(row=2, column=1)

    # leap:
    Label(window, text='Leap Info:').grid(row=0, column=2)

    lxtext = StringVar()
    lxtext.set('X')

    lytext = StringVar()
    lytext.set('Y')

    Label(window, text='x:').grid(row=1, column=2)
    lxbox = Label(window, textvariable=lxtext)
    lxbox.grid(row=1, column=3)

    Label(window, text='y:').grid(row=2, column=2)
    lybox = Label(window, textvariable=lytext)
    lybox.grid(row=2, column=3)

    def update_texts():
        xtext.set(platform.x)
        ytext.set(platform.y)

        lxtext.set(leapinfo.x)
        lytext.set(leapinfo.y)

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
