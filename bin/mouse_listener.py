import time
from pynput import mouse
from logger import Logger


########################################################################################
class MouseListener:
    def __init__(self, file, timer):
        self.file_ = file
        self.start_ = timer
        self.is_starting_ = False

        self.listener_ = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)

        self.logger_ = Logger()
        self.logger_.write_info_log("Mouse listener init")

    ########################################################################################
    def __del__(self):
        pass

    ########################################################################################
    def is_starting(self):
        return self.is_starting_

    ########################################################################################
    def on_move(self, x, y):
        text = "action=move&x={0}&y={1}&timer={2}\n".format(x, y, str(time.time() - self.start_))
        self.logger_.write_debug_log("Mouse move x = {0}, y = {1}".format(x, y))
        self.start_ = time.time()
        self.file_.write(text)

    ########################################################################################
    def on_click(self, x, y, button, pressed):
        text = "x={0}&y={1}&timer={2}\n".format(x, y, str(time.time() - self.start_))
        text = "action={0}&key={1}&".format('press=' if pressed else 'release=', button) + text

        self.logger_.write_debug_log("Mouse click x = {0}, y = {1}, button = ".format(x, y, button))
        self.start_ = time.time()
        self.file_.write(text)

    ########################################################################################
    def on_scroll(self, x, y, dx, dy):
        text = "action=scroll&key={0}&x={1}&y={2}\n".format('down' if dy < 0 else 'up', x, y,
                                                            str(time.time() - self.start_))

        self.logger_.write_debug_log("Mouse scroll route {0}".format('down' if dy < 0 else 'up'))
        self.start_ = time.time()
        self.file_.write(text)

    ########################################################################################
    def start(self):
        self.is_starting_ = True
        try:
            self.logger_.write_info_log("Mouse listener START")
            self.listener_.start()
        except Exception as ex:
            self.logger_.write_error_log(ex)

    ########################################################################################
    def stop(self):
        self.is_starting_ = False
        try:
            self.logger_.write_info_log("Mouse listener DONE")
            self.listener_.stop()
        except Exception as ex:
            self.logger_.write_error_log(ex)
########################################################################################
