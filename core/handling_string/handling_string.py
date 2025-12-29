import os, sys, random, string
from config.setup import *
from logging_module.handler import logger

CHAR = string.ascii_letters + string.digits


def random_n_chars(n:int)->str:
    """
    Function to generate a random string (n chars).
    """
    return "".join([random.choice(CHAR) for _ in range(n)])
