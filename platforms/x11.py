'''
    x11.py (C) 2015 Daniel Fairhead
    Part of 'leaper' LeapMotion mouse/computer control software
    GPL3.0
    -------------------
    x11 specific platform stuff.
    implemented using xcffib (modern python xcb library, drop in replacement
        for xpyb)
'''

import xcffib as x
import xcffib.xproto
import Xlib

from platforms import Platform

# is is worth dropping xcffib and going straight to ctypes?

#from ctypes import cdll, c_int, c_voidp, byref
#xlib = cdll.LoadLibrary('libX11-xcb.so')

class X11(Platform):
    ''' X11 Implementation of Mouse and Screen stuff '''
    def init(self, config):
        self.connection = x.connect()
        self.setup = self.connection.get_setup()
        self.root = self.setup.roots[0].root

    def _set_mouse_pos(self, x, y):
        self.connection.core.WarpPointer(0, self.root, 0, 0, 0, 0, x, y)
        self.connection.flush()

    def get_mouse_pos(self):
        # TODO
        return 100,100

    def get_screensize(self):
        # TODO
        return 1920, 1080

    def _mousedown(self, button, x, y):
        self.connection.
        pass

    def _mouseup(self, button, x, y):
        pass
