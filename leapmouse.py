import sys
import lib.Leap as Leap

from threading import Thread

from platforms import platform

leapinfo = None

class MouseListener(Leap.Listener):

    x = 0
    y = 0
    z = 0
    pinching = False
    pickup = False

    def on_connect(self, controller):
        print 'connected!'
        controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)

    def on_exit(self, controller):
        print 'disconnected!'

    def on_frame(self, controller):

        hands = controller.frame().hands

        if len(hands):
            hand = hands[0]
            self.hand = hand
            self.x = hand.stabilized_palm_position[0]
            self.y = hand.stabilized_palm_position[1]
            self.z = hand.stabilized_palm_position[2]

            # these 'magic numbers' seem right at (1920x1080)
            # TODO: make less magic.
            platform.set_mouse_pos(
                10 * (self.x + 150),
                (-6 * self.y) + 1400)

            if hand.pinch_strength > 0.6 and not self.pinching and hand.grab_strength < 0.3:
                if hand.palm_normal.roll < -0.4: # hand not facing downwards
                    if not self.pinching:
                        platform.click()
                        self.pinching = True
                else:
                    self.pinching = True
                    platform.mousedown()

            elif hand.pinch_strength < 0.7 and self.pinching:
                self.pinching = False
                platform.mouseup()

            # Scrolling.  Doesn't work well (yet).
            # I think probably this style (whole wrist direction) isn't a 
            # good idea for my tendonitis, anyway.

            #elif hand.palm_normal.roll > -0.1: # hand horizontal
            #    if hand.palm_normal.pitch > 0.1 and not self.pinching:
            #        platform.scroll(y=2) # TODO Do variable scrolling?
            #    elif hand.palm_normal.pitch < -0.5 and not self.pinching:
            #        platform.scroll(y=-2)



def init():
    global leapinfo

    leapinfo = MouseListener()
    controller = Leap.Controller()
    controller.add_listener(leapinfo)

    # wait...
    sys.stdin.readline()

def do_init():
    leap = Thread(target=init)
    leap.daemon = True
    leap.start()
    return leap
