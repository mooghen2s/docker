# Use the official Python image from the Docker Hub
FROM python:3.10

# Install required dependencies
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y \
    xvfb \
    xdotool \
    google-chrome-stable \
    wget \
    unzip
    

# Install Python dependencies
RUN pip install mss requests

# Create a working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Expose ports (if needed)
EXPOSE 8080
RUN google-chrome --version
# Run the Python script when the container launches
# ENTRYPOINT ["python", "main.py"]
CMD ["python", "main.py"]
