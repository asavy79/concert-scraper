from scrapers.base import ConcertScraper
from typing import List


class ConcertFinder:

    def __init__(self, parsers: List[ConcertScraper]):
        self.parsers = parsers

    def get_concerts(self, artist: str, start_date: str, end_date: str, state: str):
        concert_list = []

        for Parser in self.parsers:
            try:
                parser = Parser()
                data = parser.get_concerts(artist, start_date, end_date, state)
                concert_list += data
            except Exception as err:
                print(f"Error on parser: {err}")

        return concert_list
