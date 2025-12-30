"""Module to manage global paths and environment variables."""

import os

MAIN_DIR = os.getenv("ROOT_DIR", os.getcwd())
