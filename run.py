from services.downloader import Downloader
from services.writer import Writer

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
        'lat': 47.4071945,
        'lon': 8.6374091
    },
    {
        'name': 'St.Gallen Altenrhein',
        'code': 'LSZR',
        'lat': 47.4877695,
        'lon': 9.5524299
    }
]

RADIUS = 10

for airport in AIRPORTS[:3]:
    data = Downloader().fetch_aircraft_list(airport['lat'], airport['lon'], RADIUS)
    #print(data['ac'])
    Writer.write_json(data, f'data/{airport["name"]}/{data["now"]}.json')
    #Writer.write_csv(data['ac'], f'data/{airport["name"]}/{data["now"]}.csv')
