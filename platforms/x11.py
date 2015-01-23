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

from platforms import Platform

# is is worth dropping xcffib and going straight to ctypes?

#from ctypes import cdll, c_int, c_voidp, byref
#xlib = cdll.LoadLibrary('libX11-xcb.so')


class X11(Platform):
    ''' X11 Implementation of Mouse and Screen stuff '''
    def init(self):
        self.connection = x.connect()
        self.setup = self.connection.get_setup()
        self.root = self.setup.roots[0].root

    def _set_mouse_pos(self, x, y):
        self.connection.core.WarpPointer(0, self.root, 0, 0, 0, 0, x, y)
        self.connection.flush()

if __name__ == '__main__':
    print 'hi'

    plat = X11()
    X11.set_mouse_pos(10, 10)
    print '10, 10'

    X11.set_mouse_pos(100, 100)
    print '10, 10'



