import requests
from .base import ConcertScraper
from dotenv import load_dotenv
import os
from .utils.dates import format_sz_time


load_dotenv()


class TicketMasterScraper(ConcertScraper):

    def __init__(self):
        super().__init__()
        API_KEY = os.getenv("TICKETMASTER_API_KEY")

        if not API_KEY:
            raise ValueError("Invalid API Key!")
        self.api_route = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}"

    def get_concerts(self, artist: str, start_date: str = None, end_date: str = None, state: str = None):
        raw_data = self._get_raw_concert_data(
            artist, start_date, end_date, state)
        parsed_data = self.parse_concerts(raw_data)
        return parsed_data

    def parse_concerts(self, raw_event_data):

        events = []
        try:

            for event in raw_event_data:
                new_event = {}

                attractions = event.get('_embedded', {}).get('attractions', [])
                artist = attractions[0]['name'] if attractions else "Unknown Artist"

                new_event['artist'] = artist

                event_id = event.get('id', 'No Event ID')

                new_event['event_id'] = event_id

                venues = event.get('_embedded', {}).get('venues', [])
                venue = venues[0]['name'] if venues else "Unknown Venue"

                new_event['venue'] = venue

                city = venues[0]['city']['name'] if venues else "Unknown City"
                state = venues[0]['state']['name'] if venues and 'state' in venues[0] else "Unknown State"

                new_event['city'] = city
                new_event['state'] = state

                date = event['dates']['start']['localDate']

                new_event['date'] = date

                events.append(new_event)

            return events

        except Exception as err:
            print(f"Error: {err}")
            return None

    def _get_raw_concert_data(self, artist: str, start_date: str = None, end_date: str = None, state: str = None):

        params = {
            'keyword': artist,
            'startDateTime': format_sz_time(start_date),
            'endDateTime': format_sz_time(end_date),
            'stateCode': state
        }

        try:
            response = requests.get(self.api_route, params=params)

            if response.status_code == 200:
                data = response.json()
                events = data.get('_embedded', {}).get('events', [])
                return events
            else:
                raise ValueError('Bad request')
        except Exception as err:
            print(f"Error: {err}")
            return None
