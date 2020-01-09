import time
from logger import Logger
from pynput.mouse import Button, Controller


########################################################################################
class MouseController:
    def __init__(self):
        self.mouse_ = Controller()

        self.logger_ = Logger()
        self.logger_.write_info_log("Mouse controller init")

    ########################################################################################
    def __del__(self):
        pass

    ########################################################################################
    def move(self, x, y, timer):
        time.sleep(timer)
        self.mouse_.position = (x, y)
        self.logger_.write_debug_log("move x = {0}, y = {1}".format(x, y))

    ########################################################################################
    def press(self, x, y, button, timer):
        time.sleep(timer)
        self.mouse_.position = (x, y)
        if "left" in button:
            self.mouse_.press(Button.left)
        elif "right" in button:
            self.mouse_.press(Button.right)
        elif "middle" in button:
            self.mouse_.press(Button.middle)

        self.logger_.write_debug_log("Mouse button press {0}".format(button))

    ########################################################################################
    def release(self, button, timer):
        time.sleep(timer)
        if "left" in button:
            self.mouse_.release(Button.left)
        elif "right" in button:
            self.mouse_.release(Button.right)
        elif "middle" in button:
            self.mouse_.release(Button.middle)

        self.logger_.write_debug_log("Mouse button release {0}".format(button))

    ########################################################################################
    def scroll(self, x, y, route):
        self.mouse_.position = (x, y)
        if "up" in route:
            self.mouse_.scroll(0, 1)
        elif "down" in route:
            self.mouse_.scroll(0, -1)

        self.logger_.write_debug_log("Mouse scroll {0}".format(route))

########################################################################################
