from pytz import timezone

LIMITS = {
    "NO2": {
        "max": 200,
        "units": "µg/m³",
        "name": "חנקן דו חמצני NO2"
    },
    "SO2": {
        "max": 350,
        "units": "µg/m³",
        "name": "גפרית דו-חמצנית SO2"
    },
    "Benzene": {
        "max": 3.9,
        "units": "µg/m³",
        "name": "בנזן\n(Benzene-C6H6)"
    }
}

TIMEZONE = 'Israel'
LOCAL_TZ = timezone(TIMEZONE)

PLACID_URL = "https://api.placid.app/api/rest/2ctlvbqbl"
PLACID_ATTEMPTS = 10
PLACID_SLEEP = 1

TWEET_TEXT = 'זוהתה מדידה גבוהה של המזהם {}, בתחנת ניטור {}. הערך הממוצע בשעה האחרונה: {} (ערך חוקי מקסימלי: {' \
             '}).\n\n#הקנרית - בוט זיהום האוויר של "הגחלילית" '


GET_ALL_STATIONS_URL = "https://api.svivaaqm.net/v1/envista/stations"
GET_STATION_AVERAGE = "https://api.svivaaqm.net/v1/envista/stations/{}/data/latest?timebase=60"
NAME_KEY = "name"