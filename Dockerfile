FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (chromium only to keep image smaller, or with-deps for system libs)
RUN playwright install --with-deps chromium

COPY . .

# Default command (can be overridden)
CMD ["python", "smart_scraper_graph.py"]
