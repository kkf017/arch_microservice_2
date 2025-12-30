"""Interface between main.py and core/."""

from typing import List
from microservice.logging_module.handler import logger
import microservice.core.handling_functions



def run(inputs: List[str]) -> None:
    """
    Function to run main function.
    """
    logger.info("Start of task.")

    microservice.core.handling_functions.function(inputs=inputs)

    logger.info("End of task.")
