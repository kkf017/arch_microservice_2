# BUILDER STAGE
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install system dependencies and Python packages
RUN apt update && apt upgrade -y &&\
  apt clean &&\
  pip install -U pip &&\
  pip install -r requirements.txt

COPY . /app/

# RUNTIME STAGE
FROM python:${PYTHON_VERSION}-slim-buster AS runtime

COPY --from=builder /app /app

RUN chmod u+x ./app/entrypoint.sh
ENTRYPOINT ["bash", "./app/entrypoint.sh" ]

#  command: docker run --name "sync_{{ app_name }}_validator_1" -d
# -v "{{ base_path }}/92_DATA_LAKE/:/data/92_DATA_LAKE/"
# -e NAS_USER='{{ NAS_USER }}'
# ghcr.io/wattabase/synology-sync:0.2.0 'pull {{ filepath }}/{{ filename }} --dest-path=/data{{ filepath }}'

#  podman run --name "arch_microservice_2"  microservice2:latest '-n 32'
