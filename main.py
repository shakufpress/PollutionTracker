#!/usr/bin/python3
import collections
import logging
import sys

import conf
import query_api
import twitter_helper


def set_logger():
    logging_filehandler = logging.FileHandler(filename='log.log',
                                              encoding='utf-8', mode='a+')
    handlers = [logging_filehandler, logging.StreamHandler(sys.stdout)]
    logging.basicConfig(handlers=handlers,
                        format='%(asctime)s %(name)13s %(levelname)8s: %(message)s',
                        level=logging.DEBUG)

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("requests_oauthlib").setLevel(logging.WARNING)
    logging.getLogger("tweepy").setLevel(logging.WARNING)
    logging.getLogger("oauthlib").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def parse_raw_data(raw_data):
    logging.info("Parsing results...")
    abnormalities = collections.defaultdict(list)
    for station in raw_data:
        station_id = station["StationId"]
        station_name = conf.STATION_MAPPING[station_id]
        for pollutant in station["data"][0]["channels"]:
            pollutant_name = pollutant["DisplayName"]
            if pollutant_name in conf.LIMITS:
                pollutant_value = pollutant["value"]
                if pollutant_value > conf.LIMITS[pollutant_name]["max"]:
                    abnormalities[station_name].append((pollutant_name, pollutant_value))

    logging.info(f"Finished parsing results. Found {len(abnormalities)} abnormalities")
    return abnormalities


def main():
    set_logger()

    logging.info('Starting script...')
    try:
        data = query_api.get_data()
        stations = parse_raw_data(data)
        for station, abnormalities in stations.items():
            for pollutant_id, pollutant_value in abnormalities:
                twitter_helper.tweet_report(station, pollutant_id, pollutant_value)
    except Exception:
        logging.exception('Code exited')

    logging.info('Finished script')


if __name__ == "__main__":
    main()
