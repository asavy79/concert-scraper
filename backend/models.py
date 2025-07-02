from pydantic import BaseModel


class Concert(BaseModel):
    artist: str
    vanue: str
    city: str
    state: str
    event_id: str
    date: str


class ConcertInput(BaseModel):
    artist: str
    state: str
    start_date: str
    end_date: str
