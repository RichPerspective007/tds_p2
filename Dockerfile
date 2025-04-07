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

# 1. Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        gpg \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 2. Download and install Corretto 8 .deb package
RUN wget https://corretto.aws/downloads/latest/amazon-corretto-8-x64-linux-jdk.deb -O corretto.deb && \
    apt-get update && \
    apt-get install -y ./corretto.deb && \
    rm corretto.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 3. Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-amazon-corretto-amd64

# 4. Verify installation
RUN java -version

# Install Node.js and npm (for npx)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

RUN apt-get clean;

# Copy only the required files
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install --no-deps sentence-transformers
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install numpy scipy scikit-learn tqdm transformers

COPY . .

# Run the FastAPI application using Uvicorn
CMD ["sh", "-c", "uvicorn agent:app --host 0.0.0.0 --port ${PORT}"]
