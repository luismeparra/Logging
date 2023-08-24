import logging

class CustomLogging:
    def __init__(self, logger_name, log_filename):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')

        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
