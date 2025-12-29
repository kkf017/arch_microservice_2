import os
from config.loader import *
from logging_module.handler import logger
import core.handling_functions
from typing import Dict, List, Any


def run(inputs: List[str])->None:
	"""
	Function to run main function.
	"""
	logger.info(f"Start of task.")

	core.handling_functions.function(inputs=inputs)

	logger.info(f"End of task.")
