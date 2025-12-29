import os, sys, time, datetime
from config.loader import *
from logging_module.handler import logger
import infrastructure.driver_txt
from typing import Dict


def function(inputs:Dict[str, bool])->None:
	"""
	Function to execute main code.
	"""
	start_time = datetime.datetime.now()

	pass

	end_time = datetime.datetime.now()
	logger.info(f"Execution Time: {end_time - start_time}s.")



