import time
from logger import Logger
from pynput.keyboard import Key, Controller


#######################################################################################
class KeyboardController:
    def __init__(self):
        self.keyboard_ = Controller()
        self.logger_ = Logger()
        self.logger_.write_info_log("Keyboard controller init")

    ####################################################################################
    def __del__(self):
        pass

    ###################################################################################
    def press(self, key, timer):
        time.sleep(timer)
        value = self.converter(key)
        self.keyboard_.press(value)
        self.logger_.write_debug_log("Keyboard press key = {0}".format(key))

    ####################################################################################
    def release(self, key, timer):
        time.sleep(timer)
        value = self.converter(key)
        self.keyboard_.release(value)
        self.logger_.write_debug_log("Keyboard release key = {0}".format(key))

    ####################################################################################
    @staticmethod
    def converter(key):

        if "left" in key:
            return Key.left
        elif "right" in key:
            return Key.right
        elif "up" in key:
            return Key.up
        elif "down" in key:
            return Key.down
        elif "shift" in key:
            return Key.shift
        elif "ctrl" in key:
            return Key.ctrl
        elif "esc" in key:
            return Key.ctrl
        elif "enter" in key:
            return Key.enter
        elif "space" in key:
            return Key.space
        elif "tab" in key:
            return Key.tab
        elif "home" in key:
            return Key.home
        elif "alt" in key:
            return Key.alt
        elif "backspace" in key:
            return Key.backspace
        elif "caps_lock" in key:
            return Key.caps_lock
        elif "esc" in key:
            return Key.esc
        elif "f1" in key:
            return Key.f1
        elif "f2" in key:
            return Key.f2
        elif "f3" in key:
            return Key.f3
        elif "f4" in key:
            return Key.f4
        elif "f5" in key:
            return Key.f5
        elif "f6" in key:
            return Key.f6
        elif "f7" in key:
            return Key.f7
        elif "f8" in key:
            return Key.f8
        elif "f9" in key:
            return Key.f9
        elif "f10" in key:
            return Key.f10
        elif "f11" in key:
            return Key.f11
        elif "f12" in key:
            return Key.f12
        elif "f13" in key:
            return Key.f13
        elif "f14" in key:
            return Key.f14
        elif "f15" in key:
            return Key.f15
        elif "f16" in key:
            return Key.f16
        elif "f17" in key:
            return Key.f17
        elif "f18" in key:
            return Key.f18
        else:
            return key.replace('\'', '')

#######################################################################################
