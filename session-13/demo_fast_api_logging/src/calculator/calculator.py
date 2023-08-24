

###########################################
###########################################

import string
import numpy as np
import logging
from utilities.custom_logging import CustomLogging

# logger for the calculator module
# Create an instance of CustomLogging
logger_instance = CustomLogging(__name__, 'calculator.log')
logger = logger_instance.logger
logger.setLevel(logging.DEBUG)

# formatter for log messages
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# file handler for logging to a file
file_handler = logging.FileHandler('calculator.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# stream handler to visualize logs on the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

class Calculator:
    def get_fractions(self, frac_str: (int or float or string)) -> (int or float):
        """Checks a number and returns to float type."""
        # ... (rest of the function remains unchanged)

    def sum(self, a: any, b: any) -> (int or float):
        """Gets two numbers, adds them, and returns the result."""
        sum_a = self.get_fractions(a)
        sum_b = self.get_fractions(b)
        return np.sum([sum_a, sum_b])

    def subtract(self, a: any, b: any) -> (int or float):
        """Gets two numbers, subtracts the second from the first, and returns the result."""
        minuend = self.get_fractions(a)
        subtrahend = self.get_fractions(b)
        return minuend - subtrahend

    def multiply(self, a: any, b: any) -> (int or float):
        """Gets two numbers, multiplies them, and returns the result."""
        multiplicand = self.get_fractions(a)
        multiplier = self.get_fractions(b)
        return multiplicand * multiplier

    def divide(self, a: any, b: any) -> (int or float):
        """Gets two numbers, divide the first by the second, and returns the result."""
        dividend = self.get_fractions(a)
        divider = self.get_fractions(b)
        
        try:
            return np.divide(dividend, divider)
        except ZeroDivisionError:
            logger.exception('Tried to divide by zero')  # Log the exception
            return "Division by zero is not allowed!"


# Ensure that this code block is executed only when the script is run directly
if __name__ == "__main__":
    # Your calculator instance creation and operations go here
    pass
