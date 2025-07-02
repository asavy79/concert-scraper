from fastapi import FastAPI, HTTPException
import uvicorn
from models import ConcertInput
from scrapers.ticketmaster import TicketMasterScraper
from main import ConcertFinder


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/")
def get_concerts(params: ConcertInput):

    try:
        scraper = ConcertFinder([TicketMasterScraper])
        data = scraper.get_concerts(
            artist=params.artist, start_date=params.start_date, end_date=params.end_date, state=params.state)
        return data
    except Exception as err:
        raise HTTPException(
            status_code=401, detail=f"An error occurred finding data! {err}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
