import os, sys, time, datetime
from microservice.config.loader import *
from microservice.logging_module.handler import logger
import microservice.core.handling_string.handling_string
from typing import Dict, List, Any


def argparse(inputs: List[str]) -> Dict[str, Any]:
    """
    Function to parse args (command).
    """
    args = {"-n": 8, "default": None}
    try:
        if "-n" in inputs:
            args["-n"] = int(inputs[inputs.index("-n") + 1])
    except Exception as err:
        logger.warning(f"Error while getting -n arg from command.")
    return args


def function(inputs: List[str]) -> None:
    """
    Function to execute main code.
    """
    start_time = datetime.datetime.now()

    logger.info(f"Argv: {inputs}")

    args = argparse(inputs=inputs)
    logger.info(f"Arguments: {args}")

    x = microservice.core.handling_string.handling_string.random_n_chars(n=args["-n"])
    logger.info(f"Random string: {x}")

    end_time = datetime.datetime.now()
    logger.info(f"Execution Time: {end_time - start_time}s.")
