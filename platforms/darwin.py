'''
    darwin.py (C) 2015 Daniel Fairhead
    Part of 'leaper' LeapMotion mouse/computer control software
    GPL3.0
    -------------------
    darwin (OSX) specific platform stuff.
    implemented using Quartz.CoreGraphics
'''

from Quartz.CoreGraphics import (
    CGEventPost, kCGHIDEventTap, # To 'post' events to Quartz
    CGDisplayBounds, CGMainDisplayID, # for getting screen size
    kCGEventMouseMoved, CGEventCreateMouseEvent, # Mouse Events
    kCGEventLeftMouseDown, kCGEventLeftMouseUp,
    )

from platforms import Platform

################################################################################
# Convenience:

Event = CGEventCreateMouseEvent

def Post(event):
    ''' wrapper for CGEventPost(kHIDEventTap, ...) to save typing '''
    return CGEventPost(kCGHIDEventTap, event)

################################################################################
# Actual implimentation

class Darwin(Platform):
    ''' X11 Implementation of Mouse and Screen stuff '''

    def get_screensize(self):
        # TODO: multiple screens!  This only finds the primary display
        bounds = CGDisplayBounds(CGMainDisplayID()).size
        return (bounds.width, bounds.height)

    def _set_mouse_pos(self, x, y):
        self.x, self.y = x, y

        Post(Event(None, kCGEventMouseMoved, (x, y), 0))

    def get_mouse_pos(self):
        # TODO
        return 100, 100

    def _mousedown(self, button, x, y):
        Post(Event(None, kCGEventLeftMouseDown, (x, y), 0))

    def _mouseup(self, button, x, y):
        Post(Event(None, kCGEventLeftMouseUp, (x, y), 0))



if __name__ == '__main__':
    print 'hi'

    plat = X11()
    X11.set_mouse_pos(10, 10)
    print '10, 10'

    X11.set_mouse_pos(100, 100)
    print '10, 10'



