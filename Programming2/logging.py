import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    num = int("abc")  # Invalid conversion
except ValueError as e:
    logging.error("ValueError occurred: %s", e)
