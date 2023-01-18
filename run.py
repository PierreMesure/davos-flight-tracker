from dotenv import load_dotenv
load_dotenv()
from services.downloader import Downloader
from services.writer import Writer
import services.dater as dater
import services.reader as reader
import services.parser as parser

AIRPORTS = [
    {
        'name': 'Zurich',
        'code': 'LSZH',
        'lat': 47.4612324,
        'lon': 8.5146443
    },
    {
        'name': 'Samedan',
        'code': 'LSZS',
        'lat': 46.530013,
        'lon': 9.8764143
    },
    {
        'name': 'Davos Stilli Helipad',
        'code': 'LSMV',
        'lat': 46.812204,
        'lon': 9.849693
    },
    {
        'name': 'Basel',
        'code': 'LFSB',
        'lat': 47.5972866,
        'lon': 7.5119118
    },
    {
        'name': 'Dubendorf',
        'code': 'LSMD',
        'lat': 47.4071945,
        'lon': 8.6374091
    },
    {
        'name': 'Friedrichshafen',
        'code': 'EDNY',
        'lat': 47.6727707,
        'lon': 9.5206065
    },
    {
        'name': 'St.Gallen Altenrhein',
        'code': 'LSZR',
        'lat': 47.4877695,
        'lon': 9.5524299
    }
]

RADIUS = 10 # NM, 1NM = 1,852km

for airport in AIRPORTS:
    data = Downloader().fetch_aircraft_list(airport['lat'], airport['lon'], RADIUS)
    #print(data['ac'])
    date = dater.date_from_epoch(data["now"])
    Writer.write_json(data, f'data/{airport["name"]}/{date}.json')
    #Writer.write_csv(data['ac'], f'data/{airport["name"]}/{data["now"]}.csv')

    existing_aircrafts = reader.read_json(f'data/{airport["name"]}/summary.json')
    existing_aircraft_ids = [a['hex'] for a in existing_aircrafts]

    for aircraft in data['ac']:
        hex = aircraft['hex']
        position = parser.parse_aircraft_position(aircraft, date)

        if hex in existing_aircraft_ids:
            existing_aircrafts[existing_aircraft_ids.index(hex)]['positions'].append(position)
        else:
            new_aircraft = parser.parse_aircraft(aircraft, date)
            existing_aircrafts.append(new_aircraft)

        Writer.write_json(existing_aircrafts, f'data/{airport["name"]}/summary.json')



