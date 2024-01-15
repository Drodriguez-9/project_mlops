# Base image
FROM python:3.11-slim

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml
COPY tbd/ tbd/
COPY data/ data/
COPY models/ models/

WORKDIR /
RUN pip install -r requirements.txt
RUN pip install . --no-deps

ENTRYPOINT ["python", "-u", "tbd/models/train_model.py"]
