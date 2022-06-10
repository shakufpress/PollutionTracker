import os
import json
import time
import logging

import requests

import conf

PLACID_AUTH = os.environ.get('PLACID_AUTH')


def get_image_url(when, pollutant_value, recommended_maximum, pollutant_name, station):
    logging.debug("Sending request for image...")
    try:
        response = requests.post(
            url=conf.PLACID_URL,
            headers={
                "Authorization": PLACID_AUTH,
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "layers": {
                    "Date and Time": {
                        "text": when
                    },
                    "Actual Value": {
                        "text": pollutant_value
                    },
                    "Permitted Value": {
                        "text": recommended_maximum
                    },
                    "Polluter": {
                        "text": pollutant_name
                    },
                    "Monitoring Station": {
                        "text": station
                    }
                }
            })

        )

        polling_url = response.json()["polling_url"]

        for _ in range(conf.PLACID_ATTEMPTS):
            time.sleep(conf.PLACID_SLEEP)
            logging.debug("Polling on url...")
            response = requests.get(
                url=polling_url,
                headers={
                    "Authorization": PLACID_AUTH,
                    "Content-Type": "application/json; charset=utf-8",
                })
            if response.json()["image_url"] is not None:
                break
        logging.info("Got image!")
        return response.json()["image_url"]

    except requests.exceptions.RequestException:
        logging.exception("Could not get picture url")


def get_image_path(when, pollutant_value, recommended_maximum, pollutant_name, station):
    logging.debug(
        f"Attempting to create image for {when}, {pollutant_value}, {recommended_maximum}, {pollutant_name}, {station}")

    image_url = get_image_url(when, pollutant_value, recommended_maximum, pollutant_name, station)
    if image_url is None:
        logging.error(
            f"Could not get image for {when}, {pollutant_value}, {recommended_maximum}, {pollutant_name}, {station}")
        return
    file_name = os.path.basename(image_url)
    file_path = os.path.join("imgs", file_name)
    try:
        with open(file_path, "wb") as f:
            logging.debug(f"Fetching image {image_url}")
            request = requests.get(image_url)
            if request:
                f.write(request.content)
            else:
                logging.error(f"Could not get image url {image_url}")
                return
            logging.debug(f"Got image saved to {file_path}")
    except requests.exceptions.RequestException:
        logging.exception("Could not download image")

    return file_path
