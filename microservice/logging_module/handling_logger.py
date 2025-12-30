"""Class to manage logging."""

import logging


DEBUG = "%(asctime)s | \033[0;34m %(levelname)s \033[0m | %(message)s"
INFO = "%(asctime)s | \033[0;32m %(levelname)s \033[0m  | %(message)s"
WARNING = "%(asctime)s | \033[0;33m %(levelname)s \033[0m | %(message)s"
ERROR = "%(asctime)s | \033[0;31m %(levelname)s \033[0m | %(message)s"
CRITICAL = "%(asctime)s | \033[0;35m %(levelname)s \033[0m | %(message)s"
DATE = "%Y-%m-%d %H:%M:%S"

class Logger:
    """Class to manage logging_module."""
    def __init__(
        self,
    ):
        self.logger = logging.getLogger(__name__)
        self.set_stream_handler()
        self.handler = None

    def set_level(self, level: int) -> None:
        """Function to set level of logs."""
        self.logger.setLevel(level)

    def set_stream_handler(
        self,
    ) -> None:
        """Function to print logs."""
        self.handler = logging.StreamHandler()
        self.logger.addHandler(self.handler)

    def set_file_handler(self, filename) -> None:
        """Function to write logs in file .log."""
        self.handler = logging.FileHandler(filename, mode="w", encoding="utf-8")
        self.logger.addHandler(self.handler)

    def debug(self, msg: str) -> None:
        """Message level debug."""
        form = logging.Formatter(DEBUG, datefmt=DATE)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        """Message level info."""
        form = logging.Formatter(INFO, datefmt=DATE)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        """Message level warning."""
        form = logging.Formatter(WARNING, datefmt=DATE)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """Message level error."""
        form = logging.Formatter(ERROR, datefmt=DATE)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        """Message level critical."""
        form = logging.Formatter(CRITICAL, datefmt=DATE)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.critical(msg)
