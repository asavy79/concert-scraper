# Concert Scraper API

This is a FastAPI-based backend service for scraping and retrieving concert event data from multiple sources such as Ticketmaster. A front end will be implemented soon.

## Features

- Retrieve concerts by artist, location, and date range (more coming soon!)
- Pluggable scraper architecture (`ConcertScraper` base class)
- FastAPI backend with Docker support
- Pydantic models for input validation and structured output
- API endpoint returns list of concerts with artist, venue, date, and location

## Dependencies

- Python
- FastAPI
- Pydantic
- Uvicorn
- Docker
- Requests
- Python-dotenv

## Example Usage

Send a POST request to `/` with the following JSON body:

```json
{
  "artist": "Drake",
  "start_date": "2025-06-01",
  "end_date": "2025-09-30",
  "state": "CA"
}
```

Response (200 OK):

```json
[
  {
    "artist": "Drake",
    "venue": "Levis Stadium",
    "city": "Santa Clara",
    "state": "CA",
    "date": "2025-09-01",
    "event_id": "G5diZfkn0B-bh"
  }
]
```

## Project Structure

```
.
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── scrapers/
│   │   ├── base.py
│   │   └── ticketmaster_scraper.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Getting Started

### Running Locally

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn main:app --reload`

### Using Docker

```bash
docker-compose up --build
```
