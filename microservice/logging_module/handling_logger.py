"""Class to manage logging."""

import logging


class Logger:
    """Class to manage logging_module."""
    def __init__(
        self,
    ):
        self.logger = logging.getLogger(__name__)
        self.set_stream_handler()
        self.handler = None

        self.level_debug = "%(asctime)s | \033[0;34m %(levelname)s \033[0m | %(message)s"
        self.level_info = "%(asctime)s | \033[0;32m %(levelname)s \033[0m  | %(message)s"
        self.level_warning = "%(asctime)s | \033[0;33m %(levelname)s \033[0m | %(message)s"
        self.level_error = "%(asctime)s | \033[0;31m %(levelname)s \033[0m | %(message)s"
        self.level_critical = "%(asctime)s | \033[0;35m %(levelname)s \033[0m | %(message)s"

        self.date = "%Y-%m-%d %H:%M:%S"

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
        form = logging.Formatter(self.level_debug, datefmt=self.date)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        """Message level info."""
        form = logging.Formatter(self.level_info, datefmt=self.date)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        """Message level warning."""
        form = logging.Formatter(self.level_warning, datefmt=self.date)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """Message level error."""
        form = logging.Formatter(self.level_error, datefmt=self.date)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        """Message level critical."""
        form = logging.Formatter(self.level_critical, datefmt=self.date)
        self.handler.setFormatter(form)
        # msg = f"{filename.split('/')[-1]} | {msg}"
        self.logger.critical(msg)
