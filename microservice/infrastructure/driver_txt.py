import os, sys, datetime, shutil
from microservice.config.loader import *
from microservice.logging_module.handler import logger
from typing import List


def read_by_lines(filename: str) -> List[str]:
    """
    Function to read a file (txt).
    """
    try:
        with open(filename) as f:
            return f.readlines()
    except Exception as err:
        logger.error(f"Error while reading file by line.")
    return None


def read_txt(filename: str) -> str:
    """
    Function to read a file (txt).
    """
    try:
        with open(filename) as f:
            return f.read()
    except Exception as err:
        logger.error(f"Error while reading file.")
    return None


def write_txt(filename: str, txt: str) -> None:
    """
    Function to write a file (txt).
    """
    try:
        with open(filename, "w") as f:
            f.write(txt)
    except Exception as err:
        logger.error(f"Error while writing file.")


def write_by_lines(filename: str, txt: List[str]) -> None:
    """
    Function to write a file (txt).
    """
    try:
        write_txt(filename=filename, txt="\n".join(txt))
    except Exception as err:
        logger.error(f"Error while writing file by line.")
