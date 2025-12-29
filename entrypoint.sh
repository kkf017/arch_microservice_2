#!/bin/bash

echo "[ENTRYPOINT] Start microservice."

python3 ./app/main.py $@
