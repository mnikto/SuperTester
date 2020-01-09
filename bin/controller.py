from play import Play
from record import Record
from logger import Logger
from tkinter import Tk, Button

########################################################################################
class Controller:
    def __init__(self):
        self.root = Tk()
        self.flag = True

        self.play = Play()
        self.record = Record()

        self.logger = Logger()
        self.logger.write_info_log("Controller init")

    ####################################################################################
    def __del__(self):
        pass

    ####################################################################################
    def do_play(self):
        self.logger.write_debug_log("Do play start")
        if self.flag is True:
            self.flag = False
            self.play.start()
            self.flag = True
        else:
            pass

    ####################################################################################
    def do_record(self):
        self.logger.write_debug_log("Do record start")
        if self.flag is True:
            self.flag = False
            self.record.start()
            self.flag = True
        else:
            pass

    ####################################################################################
    def create_button(self, name):
        self.logger.write_debug_log("Create button " + name)
        button = Button(text = name, width=15, height=3)
        button.pack()
        return button


    ####################################################################################
    def run(self):
        self.logger.write_debug_log("Controller start")

        play_button = self.create_button("Play")
        play_button.config(command = self.do_play())

        record_button = self.create_button("Record")
        record_button.config(command = self.do_record())

        play_button.pack()
        record_button.pack()

        self.root.mainloop()
        self.logger.write_debug_log("Controller stop")

########################################################################################