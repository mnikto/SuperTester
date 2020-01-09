import time

from logger import Logger
from mouse_listener import MouseListener
from keyboard_listener import KeyboardListener


########################################################################################
class Record:
    def __init__(self):
        self.file_ = open("../src/result.txt", "w")
        self.is_starting_ = False

        timer = time.time()
        mouse_ = MouseListener(self.file_, timer)
        keyboard_ = KeyboardListener(self.file_, timer)

        self.services_ = (mouse_, keyboard_)

        self.logger_ = Logger()
        self.logger_.write_info_log("Record init")

    ####################################################################################
    def __del__(self):
        self.file_.close()

    def is_starting(self):
        return self.is_starting_

    ####################################################################################
    def start(self):
        self.is_starting_ = True
        try:
            for service in self.services_:
                service.start()

            self.logger_.write_debug_log("Record START")
        except Exception as ex:
            self.logger_.write_error_log(ex)

    ####################################################################################
    def stop(self):
        self.is_starting_ = False
        try:
            for service in self.services_:
                service.stop()

            self.logger_.write_debug_log("Record DONE")
        except Exception as ex:
            self.logger_.write_error_log(ex)

########################################################################################