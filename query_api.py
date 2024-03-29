import logging
import json
import os

import requests

import conf

AUTH_HEADERS = json.loads(os.environ.get('AUTH_HEADERS'))


def get_all_stations():
    logging.debug("Requesting all stations...")
    try:
        result = requests.get(conf.GET_ALL_STATIONS_URL, headers=AUTH_HEADERS).json()
    except json.decoder.JSONDecodeError:
        raise Exception("Could not parse JSON response!")
    stations = [(station["stationId"], f'{station["name"]} ({station["city"]})') for station in result if station["active"]]
    logging.debug(f"Retrieved {len(stations)} stations")
    return stations


def get_latest(station_id):
    try:
        result = requests.get(conf.GET_STATION_AVERAGE.format(station_id),
                              headers=AUTH_HEADERS).json()
    except json.decoder.JSONDecodeError:
        raise Exception("Could not parse JSON response!")
    return result


def get_data():
    results = []
    logging.debug("Querying stations...")
    for station_id, station_name in get_all_stations():
        data = get_latest(station_id)
        data[conf.NAME_KEY] = station_name
        results.append(data)
    logging.debug("Finished querying stations...")
    return results
