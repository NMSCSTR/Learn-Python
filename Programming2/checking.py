
# c-familia-tutorial-services.myshopify.com

import logging


logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    return a / b

divide(10, 2)
