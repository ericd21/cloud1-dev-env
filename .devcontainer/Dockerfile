FROM mcr.microsoft.com/devcontainers/python:3.11

# Install any additional OS packages you want
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*
