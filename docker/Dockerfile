# Use a minimal base image for Python 3.12
FROM python:3.12

# Set working directory
RUN mkdir /app
WORKDIR /app
ADD ./ /app/


# Copy requirements file and application code
COPY requirements.txt ./
COPY .env ./app/

# Install dependencies
RUN pip install -r requirements.txt


