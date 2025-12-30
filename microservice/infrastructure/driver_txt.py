"""Module to read and write .txt files."""

# import datetime, shutil
from typing import List
from microservice.logging_module.handler import logger


def read_by_lines(filename: str) -> List[str]:
    """
    Function to read a file (txt).
    """
    try:
        with open(filename, encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError as err:
        logger.error(f"Error while reading file by line. {err}")
    return []


def read_txt(filename: str) -> str:
    """
    Function to read a file (txt).
    """
    try:
        with open(filename, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError as err:
        logger.error(f"Error while reading file. {err}")
    return ""


def write_txt(filename: str, txt: str) -> None:
    """
    Function to write a file (txt).
    """
    try:
        with open(filename, "w", encoding='utf-8') as f:
            f.write(txt)
    except FileNotFoundError as err:
        logger.error(f"Error while writing file. {err}")


def write_by_lines(filename: str, txt: List[str]) -> None:
    """
    Function to write a file (txt).
    """
    try:
        write_txt(filename=filename, txt="\n".join(txt))
    except FileNotFoundError as err:
        logger.error(f"Error while writing file by line. {err}")
