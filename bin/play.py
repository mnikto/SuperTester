from logger import Logger
from mouse_controller import MouseController
from keyboard_controller import KeyboardController


########################################################################################
class Play:
    def __init__(self):
        self.is_starting_ = False
        self.file_ = open("../src/result.txt", "r")

        self.mouse_ = MouseController()
        self.keyboard_ = KeyboardController()

        self.logger_ = Logger()
        self.logger_.write_info_log("Play init")

    ####################################################################################
    def __del__(self):
        pass

    ####################################################################################
    def is_starting(self):
        return self.is_starting_

    ####################################################################################
    def parse(self, line):
        result = line.split("&")

        dictionary = {}
        for res in result:
            values = res.split("=")
            dictionary[values[0]] = values[1]

        self.controller(dictionary)

    ####################################################################################
    def controller(self, dictionary):
        action = dictionary["action"]
        self.logger_.write_debug_log("Controller action = {0}".format(action))

        if action == "move":
            x = int(dictionary["x"])
            y = int(dictionary["y"])
            timer = float(dictionary["timer"])
            self.mouse_.move(x, y, timer)

        elif action == "press":
            key = dictionary["key"]
            timer = float(dictionary["timer"])
            if "Key" in key:
                self.keyboard_.press(key, timer)
            elif "Button" in key:
                x = int(dictionary["x"])
                y = int(dictionary["y"])
                self.mouse_.press(x, y, key, timer)
            else:
                self.keyboard_.press(key, timer)

        elif action == "release":
            key = dictionary["key"]
            timer = float(dictionary["timer"])
            if "Key" in key:
                self.keyboard_.release(key, timer)
            elif "Button" in key:
                x = int(dictionary["x"])
                y = int(dictionary["y"])
                self.mouse_.release(key, timer)
            else:
                self.keyboard_.release(key, timer)

        elif action == "scroll":
            key = dictionary["key"]
            x = int(dictionary["x"])
            y = int(dictionary["y"])
            self.mouse_.scroll(x, y, key)

    ####################################################################################
    def start(self):
        self.is_starting_ = True
        try:
            for line in self.file_:
                self.parse(line)
        except Exception as ex:
            self.logger_.write_error_log(ex)

    ####################################################################################
    def stop(self):
        self.is_starting_ = False
        self.logger_.write_info_log("Play DONE")
        raise


########################################################################################