from datetime import datetime, timezone
import logging
from microservice.logging_module.handling_logger import Logger


logger = Logger()
time = datetime.now(timezone.utc)
logger.set_stream_handler()
# LOGGER_LOGGER .set_file_handler(f"{LOGS}-{(self.time).strftime('%Y%m%d-%H%M%S')}.log")
logger.set_level(logging.DEBUG)
