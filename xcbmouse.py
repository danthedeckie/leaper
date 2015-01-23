import xcffib as x
import xcffib.xproto

#from ctypes import cdll, c_int, c_voidp, byref

#xlib = cdll.LoadLibrary('libX11-xcb.so')

_CONN = x.connect()
_SETUP = _CONN.get_setup()
_ROOT = _SETUP.roots[0].root

def setPosition(x, y):
    _CONN.core.WarpPointer(0, _ROOT, 0,0,0,0,x,y)
    _CONN.flush()

if __name__ == '__main__':
    print 'hi'
    setPosition(200, 300)
