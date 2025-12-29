import os, sys, time, datetime
from config.loader import *
from logging_module.handler import logger
import infrastructure.driver_txt, core.handling_string.handling_string
from typing import Dict


def function(inputs:Dict[str, bool])->None:
	"""
	Function to execute main code.
	"""
	start_time = datetime.datetime.now()

	x = core.handling_string.handling_string.random_n_chars(n=16)
	logger.info(f"Random string: {x}")

	end_time = datetime.datetime.now()
	logger.info(f"Execution Time: {end_time - start_time}s.")



