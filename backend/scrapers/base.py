from abc import ABC, abstractmethod


class ConcertScraper(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_concerts(self, artist: str, start_date: str = None, end_date: str = None, state: str = None):
        pass

    @abstractmethod
    def parse_concerts(self, raw_event_data):
        pass
