# Scraper Project

This project uses `scrapegraphai` to scrape travel destinations.

## Setup

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Set up env:
    create `.env` with `OPENAI_API_KEY` if using paid models.
    
## Docker

Build and run:
```bash
docker build -t scraper-app .
docker run --network host scraper-app
```
