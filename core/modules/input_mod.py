import logging
from datetime import datetime


def take_input():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return input(f"{now} - {logging.getLevelName(logging.INFO)} - Master: ")
