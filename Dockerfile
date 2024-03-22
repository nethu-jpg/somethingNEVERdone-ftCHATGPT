FROM python:3.10.12-slim-buster

# Update and install necessary packages
RUN apt update && apt upgrade -y \
    && apt install -y git

# Copy requirements.txt and install dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Create directory and set it as working directory
RUN mkdir /somethingNEVERdone-ftCHATGPT
WORKDIR /somethingNEVERdone-ftCHATGPT

# Copy start.sh
COPY start.sh /start.sh

# Set the command to execute when the container starts
CMD ["/bin/bash", "/start.sh"]
