import os
from requests.adapters import HTTPAdapter
from requests import Session
from ssl import create_default_context, Purpose
from urllib3.util import Retry

URL = 'https://adsbexchange-com1.p.rapidapi.com/v2/lat/{}/lon/{}/dist/{}/'
API_KEY = os.environ['API_KEY']

class HttpAdapterWithLegacySsl(HTTPAdapter):

    def __init__(self, **kwargs):
        OP_LEGACY_SERVER_CONNECT = 4  # Available as ssl.OP_LEGACY_SERVER_CONNECT in Python 3.12
        self.ssl_context = create_default_context(Purpose.SERVER_AUTH)
        self.ssl_context.options |= OP_LEGACY_SERVER_CONNECT
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        HTTPAdapter.init_poolmanager(self, *args, ssl_context=self.ssl_context, **kwargs)


class Downloader(object):

    def __init__(self):
        adapter = HttpAdapterWithLegacySsl(max_retries=Retry(total=10, backoff_factor=0.1))

        self.s = Session()
        self.s.mount('https://', adapter)
        self.s.headers.update({
            'X-RapidAPI-Key': API_KEY,
            'X-RapidAPI-Host': 'adsbexchange-com1.p.rapidapi.com'
  })

    def fetch_aircraft_list(self, lat, lon, radius):
        data = self.s.get(URL.format(lat, lon, radius)).json()
        print(f'Fetched {data["total"]} aircraft(s) for {lat}, {lon} ({radius})')

        return data
