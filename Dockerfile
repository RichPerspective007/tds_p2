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

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jre && \
    apt-get clean;
    
# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Set JAVA_HOME environment variable
#ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
#ENV PATH "$JAVA_HOME/bin:$PATH"

# Install Node.js and npm (for npx)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

RUN apt-get clean;

RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o ~/.local/bin/yt-dlp
RUN chmod a+rx ~/.local/bin/yt-dlp

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
