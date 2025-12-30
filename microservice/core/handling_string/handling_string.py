"""Module to generate random strings."""

import random
import string
from microservice.logging_module.handler import logger

CHAR = string.ascii_letters + string.digits


def random_n_chars(n: int) -> str:
    """
    Function to generate a random string (n chars).
    """
    #try:
        #return "".join([random.choice(CHAR) for _ in range(n)])
    #except TypeError as err:
        #logger.error(f"Error while generating random string. {err}")
    #return ""
    return "".join([random.choice(CHAR) for _ in range(n)])
