# Use an official lightweight Python image
FROM python:3.12-slim-bookworm

# Set the working directory inside the container
WORKDIR /project2

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    unzip \
    p7zip-full \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js and npm (for npx)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Copy only the required files
COPY . .

RUN pip install -r requirements.txt
RUN pip install --no-deps sentence-transformers
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install numpy scipy scikit-learn tqdm transformers

# Expose the port FastAPI runs on
EXPOSE 8080

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8080"]
