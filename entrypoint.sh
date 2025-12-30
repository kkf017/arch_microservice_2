#!/bin/bash

echo "[ENTRYPOINT] Start microservice."

python -m microservice.main $@
