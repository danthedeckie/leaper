import sys

from threading import Thread

def not_implemented():
    print 'not implimented!'

class Platform(object):
    ''' generic base class for platform-specific code.
        if possible, platform specific code should be kept
        as small as possible '''

    def __init__(self, config=None):
        self.init(config)

        self.x, self.y = self.get_mouse_pos()
        self.w, self.h = self.get_screensize()

        print '''Initialise platform.
            Mouse: {}, {}
            Screen Size: {}x{} '''.format(self.x, self.y, self.w, self.h)

    def init(self, config):
        return not_implemented()

    def set_mouse_pos(self, x, y):
        return self._set_mouse_pos(
            max(min(x, self.w), 0),
            max(min(y, self.h), 0))

    def get_mouse_pos(self):
        return not_implemented()

    def click(self, button=0, x=None, y=None):
        x = x if x != None else self.x
        y = y if y != None else self.y

        self._mousedown(button, x, y)
        self._mouseup(button, x, y)

    def mousedown(self, button=0, x=None, y=None):
        x = x if x != None else self.x
        y = y if y != None else self.y
        self._mousedown(button, x, y)

    def mouseup(self, button=0, x=None, y=None):
        x = x if x != None else self.x
        y = y if y != None else self.y
        self._mouseup(button, x, y)

    def _mousedown(self, button, x, y):
        return not_implemented()

    def _mouseup(self, button, x, y):
        return not_implemented()

    def scroll(self, x=0, y=0):
        return not_implemented()

    def get_screensize(self):
        return not_implemented()

if sys.platform == "darwin": # OSX
    import darwin

    platform = darwin.Darwin()

else:

    import x11

    platform = x11.X11()
