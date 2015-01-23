import sys
import lib.Leap as Leap

from threading import Thread

from platforms import platform

class LeapInfo(object):
    x = 200
    y = 300
    z = 100

leapinfo = LeapInfo()

class MouseListener(Leap.Listener):

    pinching = False
    pickup = False

    def on_connect(self, controller):
        print 'connected!'
        controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)

    def on_exit(self, controller):
        print 'disconnected!'

    def on_frame(self, controller):
        global leapinfo

        hands = controller.frame().hands

        if len(hands):
            hand = hands[0]
            leapinfo.x = hand.stabilized_palm_position[0]
            leapinfo.y = hand.stabilized_palm_position[1]
            leapinfo.z = hand.stabilized_palm_position[2]

            # These 'magic numbers' were correct at home, but not the office:
            #platform.set_mouse_pos(
            #    4.4 * (leapinfo.x + 150),
            #    (-2 * leapinfo.y) + 850)

            # and these are right at the office (1920x1080)
            platform.set_mouse_pos(
                10 * (leapinfo.x + 150),
                (-6 * leapinfo.y) + 1400)

            #print hand.palm_normal[2]

            if hand.pinch_strength > 0.6 and not self.pinching:
                self.pinching = True
                if hand.palm_normal[0] > 0: # hand facing downwards
                    platform.click()
                else:
                    platform.mousedown()

            elif hand.pinch_strength < 0.5 and self.pinching:
                self.pinching = False
                if hand.palm_normal[0] < 1:
                    platform.mouseup()


            elif hand.palm_normal[2] > 0.1:
                platform.scroll(y=10*hand.palm_normal[2])
            elif hand.palm_normal[2] < -0.5:
                platform.scroll(y=10*hand.palm_normal[2])



def init():
    listener = MouseListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    # wait...
    sys.stdin.readline()

def do_init():
    leap = Thread(target=init)
    leap.daemon = True
    leap.start()
    return leap
