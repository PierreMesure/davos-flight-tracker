
def parse_aircraft_position(aircraft, date):
    return {
        'date': date,
        'lat': aircraft.get('lat'),
        'lon': aircraft.get('lon'),
        'alt_baro': aircraft.get('alt_baro'),
        'dst': aircraft.get('dst')
    }


def parse_aircraft(aircraft, date):
    return {
        'hex': aircraft.get('hex'),
        'flight': aircraft.get('flight'),
        'r': aircraft.get('r'),
        't': aircraft.get('t'),
        'positions': [parse_aircraft_position(aircraft, date)]
    }

def update_estimated_behaviour(aircraft):
    positions = aircraft['positions']

    if positions[-1]['alt_baro'] == 'ground':
        aircraft['estimated_behaviour'] = 'landed'
    else:
        aircraft['estimated_behaviour'] = 'too dumb to guess right now' # Need to write some logic to guess whether the plane is flying by, landing or taking off based on the behaviour

