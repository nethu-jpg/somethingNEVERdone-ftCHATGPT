FROM python:3.10.12-slim-buster

# Update and install necessary packages
RUN apt update && apt upgrade -y \
    && apt install -y git

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

# Set the command to execute when the container starts
CMD ["python3", "bot.py"]
