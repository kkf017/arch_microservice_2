import os, sys, json
from logging_module.handler import logger
import core.run

#input_file = os.getenv("INPUT_FILE", os.path.join(".", "input"))
#inputs = json.load(open(input_file, 'r'))

if __name__ == "__main__":
	core.run.run(inputs=sys.argv)
