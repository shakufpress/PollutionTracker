#!/usr/bin/python3
import collections
import logging
from datetime import datetime

import sys

import conf
import image_template
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
        station_name = station["name"]
        for pollutant in station["data"][0]["channels"]:
            if pollutant["valid"]:
                pollutant_name = pollutant["name"]
                if pollutant_name in conf.LIMITS:
                    pollutant_value = pollutant["value"]
                    if pollutant_value > conf.LIMITS[pollutant_name]["max"]:
                        abnormalities[station_name].append((pollutant_name, pollutant_value))

    logging.info(f"Finished parsing results. Found {len(abnormalities)} abnormalities")
    return abnormalities


def report(station, pollutant_id, pollutant_value):
    pollutant_name = conf.LIMITS[pollutant_id]["name"]
    recommended_maximum = conf.LIMITS[pollutant_id]["max"]
    units = conf.LIMITS[pollutant_id]["units"]
    logging.info(
        f"Reporting found high values of {pollutant_name} in station {station}. average is {pollutant_value} {units} (Maximum recommended is {recommended_maximum} {units})")

    when = datetime.now(conf.LOCAL_TZ).strftime("%d/%m/%y %H:%M")
    image_path = image_template.get_image_path(when, pollutant_value, recommended_maximum, pollutant_name, station)

    media_id = twitter_helper.upload_media(image_path)
    tweet_pollutant_name = pollutant_name.replace("\n", " ")
    tweet_text = conf.TWEET_TEXT.format(tweet_pollutant_name, station, str(pollutant_value) + " " + units,
                                        str(recommended_maximum) + " " + units)
    twitter_helper.tweet_with_media(tweet_text, media_id)


def main():
    set_logger()

    logging.info('Starting script...')
    try:
        data = query_api.get_data()
        stations = parse_raw_data(data)
        for station, abnormalities in stations.items():
            for pollutant_id, pollutant_value in abnormalities:
                report(station, pollutant_id, pollutant_value)


    except Exception:
        logging.exception('Code exited')

    logging.info('Finished script')


if __name__ == "__main__":
    main()
