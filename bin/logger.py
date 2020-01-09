import logging


########################################################################################
class Logger:
    def __init__(self):
        logging.basicConfig(format=u"%(levelname)-8s [%(asctime)s] %(message)s",
                            filename="../log/application.log",
                            level=logging.DEBUG)

    ###################################################################################
    @staticmethod
    def write_info_log(msg):
        logging.info(msg)

    ###################################################################################
    @staticmethod
    def write_error_log(msg):
        logging.error(msg)

    ###################################################################################
    @staticmethod
    def write_debug_log(msg):
        logging.debug(msg)

#######################################################################################
