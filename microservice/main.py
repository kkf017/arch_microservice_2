import os, sys, json
from microservice.logging_module.handler import logger
import microservice.core.run


if __name__ == "__main__":
    microservice.core.run.run(inputs=sys.argv)

