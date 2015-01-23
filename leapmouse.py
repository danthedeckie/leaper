from sys import stdin
import lib.Leap as Leap

from threading import Thread

from xcbmouse import setPosition
from mouse import mouseinfo

class LeapInfo(object):
    x = 200
    y = 300
    z = 100

leapinfo = LeapInfo()

class MouseListener(Leap.Listener):
    def on_connect(self, controller):
        print 'connected!'

    def on_frame(self, controller):
        global leapinfo

        hands = controller.frame().hands

        if len(hands):
            hand = hands[0]
            leapinfo.x = hand.palm_position[0]
            leapinfo.y = hand.palm_position[1]
            leapinfo.z = hand.palm_position[2]

            mouseinfo.x = 4.4 * (leapinfo.x + 150)
            mouseinfo.y = (-2 * leapinfo.y) + 850


            setPosition(mouseinfo.x, mouseinfo.y)

def init():
    listener = MouseListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    # wait...
    stdin.readline()

def do_init():
    leap = Thread(target=init)
    leap.daemon = True
    leap.start()
    return leap
