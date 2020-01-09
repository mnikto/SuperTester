import time
from logger import Logger
from pynput import keyboard


########################################################################################
class KeyboardListener:
    def __init__(self, file, timer):
        self.file_ = file
        self.start_ = timer
        self.is_starting_ = False

        self.listener_ = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)

        self.logger_ = Logger()
        self.logger_.write_info_log("Keyboard listener init")

    ####################################################################################
    def __del__(self):
        pass

    ####################################################################################
    def on_press(self, key):
        try:
            text = "action=press&key={0}&timer={1}\n".format(key.char, str(time.time() - self.start_))
            self.logger_.write_debug_log("Keyboard listen press key = {0}".format(key))
            self.start_ = time.time()
            self.file_.write(text)

        except AttributeError:
            text = "action=press&key={0}&timer={1}\n".format(key, str(time.time() - self.start_))
            self.logger_.write_debug_log("Keyboard listen press key = {0}".format(key))
            self.start_ = time.time()
            self.file_.write(text)
        except Exception as ex:
            self.logger_.write_error_log(ex)

    ####################################################################################
    def on_release(self, key):
        text = "action=release&key={0}&timer={1}\n".format(key, str(time.time() - self.start_))
        self.logger_.write_debug_log("Keyboard listen release key = {0}".format(key))
        self.start_ = time.time()
        self.file_.write(text)

    ####################################################################################
    def start(self):
        self.is_starting_ = True
        try:
            self.listener_.start()
            self.logger_.write_info_log("Keyboard listener START")
        except Exception as ex:
            self.logger_.write_error_log(ex)

    ####################################################################################
    def stop(self):
        self.is_starting_ = False
        try:
            self.listener_.stop()
            self.logger_.write_info_log("Keyboard listener DONE")
        except Exception as ex:
            self.logger_.write_error_log(ex)
########################################################################################
