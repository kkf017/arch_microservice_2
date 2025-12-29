import os, configparser

MAIN_DIR = os.getenv("ROOT_DIR", os.getcwd())
VAR = os.getenv("VAR", "default")

FILENAME = os.path.join(MAIN_DIR, "helpers", "test_1.txt")
