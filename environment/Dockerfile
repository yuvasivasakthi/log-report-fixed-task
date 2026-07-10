# >>> ACTION REQUIRED before you build/run this task <<<
# Run these two commands on your own machine, then replace the digest below:
#   docker pull python:3.12-slim
#   docker inspect --format='{{index .RepoDigests 0}}' python:3.12-slim
# Paste the full "python:3.12-slim@sha256:...." string as the FROM line.
FROM python:3.12-slim@sha256:REPLACE_WITH_DIGEST_FROM_DOCKER_INSPECT

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
