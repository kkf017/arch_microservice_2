"""Module to run __main__."""

import sys
import microservice.core.run

if __name__ == "__main__":
    microservice.core.run.run(inputs=sys.argv)
