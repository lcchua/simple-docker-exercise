# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

# EXPOSE 5000

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app_v1.py"]
