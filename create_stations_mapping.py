import json

# note that data is from https://www.svivaaqm.net/Report/stationreport?InPopUp=True
# and replace all of \" to \\" was done

data = """[
    {
        "name": "צפון",
        "regionId": 1,
        "stations": [
            {
                "DisplayName": "מצפה נטופה",
                "stationId": 426,
                "name": "מצפה נטופה",
                "shortName": "Station 426",
                "stationsTag": "426",
                "location": {
                    "latitude": 32.80261302,
                    "longitude": 35.38301059
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "אבן וסיד",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת - 2 רכבת ישראל",
                "stationId": 334,
                "name": "ניידת - 2 רכבת ישראל",
                "shortName": "Station 334",
                "stationsTag": "334",
                "location": {
                    "latitude": 32.924311,
                    "longitude": 35.297032
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "רכבת ישראל",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "ניידת",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "בית העמק",
                "stationId": 538,
                "name": "בית העמק",
                "shortName": "Station 538",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.970444,
                    "longitude": 35.144404
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מחצבת אושרת",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 2,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "ITemp",
                        "channelId": 3,
                        "name": "ITemp",
                        "alias": "טמפרטורת פנים תחנה",
                        "active": true,
                        "typeId": 31,
                        "pollutantId": null,
                        "units": "°C",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "טורעאן החדשה",
                "stationId": 427,
                "name": "טורעאן החדשה",
                "shortName": "Station 427",
                "stationsTag": "427",
                "location": {
                    "latitude": 32.77727,
                    "longitude": 35.37972
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "אבן וסיד",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 2,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": false,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "געתון",
                "stationId": 537,
                "name": "געתון",
                "shortName": "Station 537",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 33.005078,
                    "longitude": 35.213146
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מחצבת אושרת",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 2,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "ITemp",
                        "channelId": 3,
                        "name": "ITemp",
                        "alias": "טמפרטורת פנים תחנה",
                        "active": true,
                        "typeId": 31,
                        "pollutantId": null,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 4,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כחל",
                "stationId": 536,
                "name": "כחל",
                "shortName": "Station 536",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.8921811730742,
                    "longitude": 35.5083950062766
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מחצבות כפר גלעדי",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גליל מערבי",
                "stationId": 11,
                "name": "גליל מערבי",
                "shortName": "גליל מער",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.915933,
                    "longitude": 35.29425167
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 7,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 8,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 10,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 12,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 13,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 14,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כפר מסריק החדשה",
                "stationId": 326,
                "name": "כפר מסריק החדשה",
                "shortName": "כפר מסריק",
                "stationsTag": "326",
                "location": {
                    "latitude": 32.88970721,
                    "longitude": 35.09713274
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 8,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 9,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 10,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת -  2",
                "stationId": 47,
                "name": "ניידת -  2",
                "shortName": "ניידת -  2",
                "stationsTag": "7",
                "location": {
                    "latitude": 32.665838,
                    "longitude": 35.554896
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 7,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 8,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 18,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כפר מסריק 1",
                "stationId": 28,
                "name": "כפר מסריק 1",
                "shortName": "כפר מסרי",
                "stationsTag": "28",
                "location": {
                    "latitude": 32.88955,
                    "longitude": 35.09822
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": false,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": false,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 8,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 9,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 10,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "ppb",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מכללת תל חי",
                "stationId": 387,
                "name": "מכללת תל חי",
                "shortName": "תל חי",
                "stationsTag": "387",
                "location": {
                    "latitude": 33.23167887,
                    "longitude": 35.58098132
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 1,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 4,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 9,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "חיפה וקריות",
        "regionId": 2,
        "stations": [
            {
                "DisplayName": "איבטין",
                "stationId": 501,
                "name": "איבטין",
                "shortName": "Station 501",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.75978563,
                    "longitude": 35.11261337
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חוצה ישראל",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ד.עכו - חיפה",
                "stationId": 354,
                "name": "ד.עכו - חיפה",
                "shortName": "Station 354",
                "stationsTag": "354",
                "location": {
                    "latitude": 32.828911,
                    "longitude": 35.078746
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "משרד הרישוי הישן",
                "stationId": 533,
                "name": "משרד הרישוי הישן",
                "shortName": "Station 533",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.8014633,
                    "longitude": 35.0497708
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 4,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "None",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "עצמאות חיפה",
                "stationId": 189,
                "name": "עצמאות חיפה",
                "shortName": "עצמאות ח",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.81707628,
                    "longitude": 35.00236365
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 5,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 13,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 22,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "רגבים",
                "stationId": 324,
                "name": "רגבים",
                "shortName": "קרית חיים רגבים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.82919872,
                    "longitude": 35.05660067
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "WD",
                        "channelId": 1,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 3,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 13,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 18,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קריית טבעון",
                "stationId": 137,
                "name": "קריית טבעון",
                "shortName": "קריית טבעון",
                "stationsTag": "137",
                "location": {
                    "latitude": 32.72222324,
                    "longitude": 35.13018868
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 8,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 9,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 10,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 11,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 12,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 18,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נווה שאנן",
                "stationId": 86,
                "name": "נווה שאנן",
                "shortName": "נווה שאנן",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.78746681,
                    "longitude": 35.02135722
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "Rain",
                        "channelId": 1,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 5,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 7,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 9,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 10,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 12,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 13,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 15,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "דרום",
                "stationId": 380,
                "name": "דרום",
                "shortName": "דרום",
                "stationsTag": "380",
                "location": {
                    "latitude": 32.814143,
                    "longitude": 35.077715
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 7,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 8,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 9,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 14,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נחל הקישון",
                "stationId": 517,
                "name": "נחל הקישון",
                "shortName": "Station 517",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.7948632,
                    "longitude": 35.0492165
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "None",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שוק",
                "stationId": 91,
                "name": "שוק",
                "shortName": "שוק",
                "stationsTag": "(null)",
                "location": {
                    "latitude": null,
                    "longitude": null
                },
                "timebase": 30,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 6,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 7,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 8,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 9,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 11,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Filter",
                        "channelId": 12,
                        "name": "Filter",
                        "alias": "פילטר",
                        "active": true,
                        "typeId": 32,
                        "pollutantId": null,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 13,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "ppm",
                        "description": null
                    },
                    {
                        "DisplayName": "Time",
                        "channelId": 14,
                        "name": "Time",
                        "alias": "זמן",
                        "active": true,
                        "typeId": 35,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 15,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 20,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Filter",
                        "channelId": 21,
                        "name": "Filter",
                        "alias": "פילטר",
                        "active": true,
                        "typeId": 32,
                        "pollutantId": null,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "60,1440",
                "AllTimebases": [
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קריית ים",
                "stationId": 92,
                "name": "קריית ים",
                "shortName": "קריית ים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.85223486,
                    "longitude": 35.07955152
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 5,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 6,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 13,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 14,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 19,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "חורב",
                "stationId": 393,
                "name": "חורב",
                "shortName": "שדרות מוריה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.78603979,
                    "longitude": 34.98614426
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 5,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נשר",
                "stationId": 87,
                "name": "נשר",
                "shortName": "נשר",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.77027358,
                    "longitude": 35.04255669
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "Rain",
                        "channelId": 1,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": false,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 5,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 9,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 10,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 13,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 15,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 17,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קריית שפרינצק",
                "stationId": 93,
                "name": "קריית שפרינצק",
                "shortName": "קריית שפרינצק",
                "stationsTag": "93",
                "location": {
                    "latitude": 32.82296298,
                    "longitude": 34.96575296
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 7,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 8,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 9,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת חיפה",
                "stationId": 344,
                "name": "ניידת חיפה",
                "shortName": "ניידת חיפה",
                "stationsTag": "123456",
                "location": {
                    "latitude": 32.8091017,
                    "longitude": 35.07439062
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "WD",
                        "channelId": 1,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 6,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 7,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 9,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 10,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 11,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 17,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 18,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אחוזה",
                "stationId": 136,
                "name": "אחוזה",
                "shortName": "אחוזה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.7859038,
                    "longitude": 34.98571761
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 10,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 11,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 12,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 20,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 30,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "הרצל - בלפור",
                "stationId": 391,
                "name": "הרצל - בלפור",
                "shortName": "Station 391",
                "stationsTag": "391",
                "location": {
                    "latitude": 32.81141454,
                    "longitude": 34.99738996
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 5,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 9,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כפר חסידים",
                "stationId": 98,
                "name": "כפר חסידים",
                "shortName": "כפר חסידים",
                "stationsTag": "98",
                "location": {
                    "latitude": 32.7430541,
                    "longitude": 35.09522842
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 9,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 10,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 12,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "פארק הכרמל",
                "stationId": 69,
                "name": "פארק הכרמל",
                "shortName": "פארק הכרמל",
                "stationsTag": "30",
                "location": {
                    "latitude": 32.73695541,
                    "longitude": 35.03551151
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 10,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 11,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 13,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אינשטיין",
                "stationId": 90,
                "name": "אינשטיין",
                "shortName": "אינשטיין",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.77791293,
                    "longitude": 35.00066973
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 13,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 17,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נווה גנים",
                "stationId": 382,
                "name": "נווה גנים",
                "shortName": "מוצקין הצעירה ונווה גנים",
                "stationsTag": "382",
                "location": {
                    "latitude": 32.85471723,
                    "longitude": 35.09191889
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 5,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 6,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 7,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 8,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 10,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 13,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קריית בנימין",
                "stationId": 97,
                "name": "קריית בנימין",
                "shortName": "קריית בנימין",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.78816675,
                    "longitude": 35.08591807
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 2,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 3,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 4,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 8,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 20,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 21,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 22,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כרמל צרפתי",
                "stationId": 68,
                "name": "כרמל צרפתי",
                "shortName": "כרמל צרפ",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.82054,
                    "longitude": 34.97518
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": false,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": false,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": false,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": false,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": false,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת - 4",
                "stationId": 322,
                "name": "ניידת - 4",
                "shortName": "ניידת - 4",
                "stationsTag": "322",
                "location": {
                    "latitude": 32.786812,
                    "longitude": 35.076883
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "NO2",
                        "channelId": 1,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 3,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 5,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 8,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מרכז הכרמל",
                "stationId": 80,
                "name": "מרכז הכרמל",
                "shortName": "מרכז הכרמל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.8011974,
                    "longitude": 34.99144547
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "צ\u0027ק פוסט",
                "stationId": 96,
                "name": "צ\u0027ק פוסט",
                "shortName": "צ\u0027ק פוסט",
                "stationsTag": "96",
                "location": {
                    "latitude": 32.78928792,
                    "longitude": 35.04065409
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "Rain",
                        "channelId": 1,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 5,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 9,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 10,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 12,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 13,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 15,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2/NOX",
                        "channelId": 23,
                        "name": "NO2/NOX",
                        "alias": null,
                        "active": false,
                        "typeId": 268,
                        "pollutantId": null,
                        "units": "_",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 25,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קרית חיים - מערבית",
                "stationId": 499,
                "name": "קרית חיים - מערבית",
                "shortName": "קרית חיים מערבית",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.829129,
                    "longitude": 35.056529
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "WD",
                        "channelId": 1,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 3,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 13,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 17,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 18,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קקל",
                "stationId": 29,
                "name": "קקל",
                "shortName": "קקל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": null,
                    "longitude": null
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "CO",
                        "channelId": 1,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "ppm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מרכז העיר",
                "stationId": 88,
                "name": "מרכז העיר",
                "shortName": "מרכז העיר",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.81190414,
                    "longitude": 35.11309366
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים חיפה",
                "regionId": 2,
                "monitors": [
                    {
                        "DisplayName": "Rain",
                        "channelId": 1,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 3,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 5,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 9,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 10,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 12,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 13,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 15,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 17,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "עמק יזרעאל",
        "regionId": 3,
        "stations": [
            {
                "DisplayName": "עפולה",
                "stationId": 1,
                "name": "עפולה",
                "shortName": "עפולה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.60372041,
                    "longitude": 35.29175519
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 3,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 6,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 7,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 8,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 9,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 10,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "דחי",
                "stationId": 73,
                "name": "דחי",
                "shortName": "דחי",
                "stationsTag": "41",
                "location": {
                    "latitude": 32.61959412,
                    "longitude": 35.35491173
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנת הכוח MRC(אלון תבור)",
                "regionId": 3,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "דברת",
                "stationId": 72,
                "name": "דברת",
                "shortName": "דברת",
                "stationsTag": "40",
                "location": {
                    "latitude": 32.64450245,
                    "longitude": 35.35252341
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנת הכוח MRC(אלון תבור)",
                "regionId": 3,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אחוזת ברק",
                "stationId": 539,
                "name": "אחוזת ברק",
                "shortName": "Station 539",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.645436914073,
                    "longitude": 35.3367315342783
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנת הכוח MRC(אלון תבור)",
                "regionId": 3,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "עין דור",
                "stationId": 147,
                "name": "עין דור",
                "shortName": "עין דור",
                "stationsTag": "39",
                "location": {
                    "latitude": 32.65404581,
                    "longitude": 35.41366854
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "תחנת הכוח MRC(אלון תבור)",
                "regionId": 3,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "שרון כרמל",
        "regionId": 4,
        "stations": [
            {
                "DisplayName": "זכרון יעקב",
                "stationId": 103,
                "name": "זכרון יעקב",
                "shortName": "זכרון יע",
                "stationsTag": "(null)",
                "location": {
                    "latitude": null,
                    "longitude": null
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "None",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": false,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": false,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": false,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": false,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "RainAccu",
                        "channelId": 9,
                        "name": "RainAccu",
                        "alias": "גשם מצטבר",
                        "active": true,
                        "typeId": 72,
                        "pollutantId": null,
                        "units": "mm",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נחשולים",
                "stationId": 472,
                "name": "נחשולים",
                "shortName": "Station 472",
                "stationsTag": "472",
                "location": {
                    "latitude": 32.61409807,
                    "longitude": 34.920975
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 9,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 10,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 11,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "טורבינת הגז קיסריה",
                "stationId": 140,
                "name": "טורבינת הגז קיסריה",
                "shortName": "קיסריה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.49922102,
                    "longitude": 34.93463685
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": false,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כרם מהר\\"ל",
                "stationId": 110,
                "name": "כרם מהר\\"ל",
                "shortName": "כ.מהרל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.64940928,
                    "longitude": 34.98902432
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 8,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 9,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כפר סבא",
                "stationId": 375,
                "name": "כפר סבא",
                "shortName": "כפר סבא",
                "stationsTag": "375",
                "location": {
                    "latitude": 32.1775496,
                    "longitude": 34.93651231
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 7,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": false,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 13,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 16,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 18,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 19,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 20,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כביש 65",
                "stationId": 113,
                "name": "כביש 65",
                "shortName": "כביש 65",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.53476536,
                    "longitude": 35.1495469
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": false,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 21,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 23,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 27,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": false,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מעיין צבי - איגוד",
                "stationId": 452,
                "name": "מעיין צבי - איגוד",
                "shortName": "Station 452",
                "stationsTag": "452",
                "location": {
                    "latitude": 32.56686283,
                    "longitude": 34.94028062
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 12,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 13,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כפר הנוער שפיה",
                "stationId": 341,
                "name": "כפר הנוער שפיה",
                "shortName": "שפיה",
                "stationsTag": "341",
                "location": {
                    "latitude": 32.58834395,
                    "longitude": 34.97333221
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "אבן וסיד",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 1,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 3,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 4,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "אום אל קוטוף",
                "stationId": 309,
                "name": "אום אל קוטוף",
                "shortName": "אום אל קוטוף",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.47363499,
                    "longitude": 35.05769552
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מחצבות",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 2,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 4,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גן שמואל",
                "stationId": 108,
                "name": "גן שמואל",
                "shortName": "גן שמואל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.44079673,
                    "longitude": 34.96090646
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "המעפיל",
                "stationId": 109,
                "name": "המעפיל",
                "shortName": "המעפיל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.36998189,
                    "longitude": 34.97511165
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 8,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "חוף דור",
                "stationId": 455,
                "name": "חוף דור",
                "shortName": "Station 455",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.60750474,
                    "longitude": 34.92019677
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "נובל אנרגיה",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 10,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 11,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 12,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 13,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מגל",
                "stationId": 114,
                "name": "מגל",
                "shortName": "מגל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.38485092,
                    "longitude": 35.03765809
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ברטעה ישנה",
                "stationId": 308,
                "name": "ברטעה ישנה",
                "shortName": "ברטעה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.47699,
                    "longitude": 35.086
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "מחצבות",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 2,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH-INT",
                        "channelId": 3,
                        "name": "RH-INT",
                        "alias": null,
                        "active": true,
                        "typeId": 250,
                        "pollutantId": null,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ברקאי החדשה",
                "stationId": 454,
                "name": "ברקאי החדשה",
                "shortName": "ברקאי",
                "stationsTag": "454",
                "location": {
                    "latitude": 32.47722798,
                    "longitude": 35.03242415
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 9,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 14,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 18,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 20,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מעיין צבי - נובל",
                "stationId": 456,
                "name": "מעיין צבי - נובל",
                "shortName": "מעיין צבי - נובל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.566933,
                    "longitude": 34.940415
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "נובל אנרגיה",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 7,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 8,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 9,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 10,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "חריש",
                "stationId": 505,
                "name": "חריש",
                "shortName": "חריש",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.456515,
                    "longitude": 35.049343
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אזור התעשייה",
                "stationId": 100,
                "name": "אזור התעשייה",
                "shortName": "אזור התעשייה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.44757787,
                    "longitude": 34.91412785
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אתר החדרה נחלי מנשה",
                "stationId": 106,
                "name": "אתר החדרה נחלי מנשה",
                "shortName": "נחלי מנשה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.47127037,
                    "longitude": 34.92374248
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אליקים",
                "stationId": 102,
                "name": "אליקים",
                "shortName": "אליקים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.63263773,
                    "longitude": 35.06607883
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 10,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גבעת עדה",
                "stationId": 107,
                "name": "גבעת עדה",
                "shortName": "גבעת עדה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.51825925,
                    "longitude": 35.00348232
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 10,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קריית השרון",
                "stationId": 321,
                "name": "קריית השרון",
                "shortName": "Station 321",
                "stationsTag": "נייד שרון-כרמל",
                "location": {
                    "latitude": 32.31125699,
                    "longitude": 34.87267303
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 9,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 10,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 17,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "בית אליעזר",
                "stationId": 99,
                "name": "בית אליעזר",
                "shortName": "בית אליעזר",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.43352116,
                    "longitude": 34.93933048
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 10,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": false,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ברקאי - ישנה",
                "stationId": 159,
                "name": "ברקאי - ישנה",
                "shortName": "ברקאי",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.47548,
                    "longitude": 35.02228
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 9,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Filter",
                        "channelId": 11,
                        "name": "Filter",
                        "alias": "פילטר",
                        "active": true,
                        "typeId": 32,
                        "pollutantId": null,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Spare",
                        "channelId": 13,
                        "name": "Spare",
                        "alias": null,
                        "active": true,
                        "typeId": 1,
                        "pollutantId": null,
                        "units": "ng/m3",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 14,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "RainAccu",
                        "channelId": 15,
                        "name": "RainAccu",
                        "alias": "גשם מצטבר",
                        "active": true,
                        "typeId": 72,
                        "pollutantId": null,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "TMPL",
                        "channelId": 16,
                        "name": "TMPL",
                        "alias": "טמפרטורה פנימית",
                        "active": true,
                        "typeId": 48,
                        "pollutantId": null,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 18,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 20,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מוזיאון ראלי",
                "stationId": 453,
                "name": "מוזיאון ראלי",
                "shortName": "Station 453",
                "stationsTag": "453",
                "location": {
                    "latitude": 32.51404711,
                    "longitude": 34.90732668
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 11,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 12,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 14,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת - 8, אתר חפציבה",
                "stationId": 398,
                "name": "ניידת - 8, אתר חפציבה",
                "shortName": "ניידת - 8",
                "stationsTag": "398",
                "location": {
                    "latitude": 32.46514232,
                    "longitude": 34.89828669
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 4,
                "monitors": [],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "אליכין",
                "stationId": 105,
                "name": "אליכין",
                "shortName": "אליכין",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.40846997,
                    "longitude": 34.9184201
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 10,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": false,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "עמיקם",
                "stationId": 112,
                "name": "עמיקם",
                "shortName": "עמיקם",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.56533561,
                    "longitude": 35.02531331
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת קטנה",
                "stationId": 305,
                "name": "ניידת קטנה",
                "shortName": "ניידת קטנה",
                "stationsTag": "305",
                "location": {
                    "latitude": 32.46045,
                    "longitude": 35.06914
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 4,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 10,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "פרדס חנה",
                "stationId": 104,
                "name": "פרדס חנה",
                "shortName": "פ.חנה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.46637429,
                    "longitude": 34.96305008
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 10,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "תחנת הכוח אורות רבין",
                "stationId": 84,
                "name": "תחנת הכוח אורות רבין",
                "shortName": "אורות רב",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.46713965,
                    "longitude": 34.89642911
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב אחוזה",
                "stationId": 154,
                "name": "רחוב אחוזה",
                "shortName": "רעננה",
                "stationsTag": "154",
                "location": {
                    "latitude": 32.17912646,
                    "longitude": 34.88189021
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "דליית אל כרמל",
                "stationId": 111,
                "name": "דליית אל כרמל",
                "shortName": "ד.א.כרמל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.68127143,
                    "longitude": 35.06988492
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קרון איגוד שרון-כרמל 2",
                "stationId": 428,
                "name": "קרון איגוד שרון-כרמל 2",
                "shortName": "Station 428",
                "stationsTag": "428",
                "location": {
                    "latitude": 32.60264,
                    "longitude": 35.00648
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 9,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 10,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 11,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קציר",
                "stationId": 378,
                "name": "קציר",
                "shortName": "Station 378",
                "stationsTag": "378",
                "location": {
                    "latitude": 32.48706514,
                    "longitude": 35.09650712
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 12,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "חפציבה",
                "stationId": 401,
                "name": "חפציבה",
                "shortName": "Station 401",
                "stationsTag": "401",
                "location": {
                    "latitude": 32.45850596,
                    "longitude": 34.89846869
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים שרון-כרמל",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "ניידת נובל אנרג\u0027י",
                "stationId": 462,
                "name": "ניידת נובל אנרג\u0027י",
                "shortName": "Station 462",
                "stationsTag": "462",
                "location": {
                    "latitude": 32.622536,
                    "longitude": 35.04597
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "נובל אנרגיה",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Toluene",
                        "channelId": 2,
                        "name": "Toluene",
                        "alias": "טולואן",
                        "active": true,
                        "typeId": 10,
                        "pollutantId": null,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "EthylB",
                        "channelId": 3,
                        "name": "EthylB",
                        "alias": "אטיל בנזן",
                        "active": true,
                        "typeId": 36,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "M+P-XY",
                        "channelId": 4,
                        "name": "M+P-XY",
                        "alias": "מטה פרה קסילן",
                        "active": true,
                        "typeId": 37,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O-Xyle",
                        "channelId": 5,
                        "name": "O-Xyle",
                        "alias": "או - קסילן",
                        "active": true,
                        "typeId": 38,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת -1",
                "stationId": 46,
                "name": "ניידת -1",
                "shortName": "ניידת - תחנה 1",
                "stationsTag": "12",
                "location": {
                    "latitude": 32.279778,
                    "longitude": 34.864306
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 11,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": false,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 12,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 15,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ברטעה",
                "stationId": 416,
                "name": "ברטעה",
                "shortName": "ברטעה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.47612906,
                    "longitude": 35.0792547
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מחצבות",
                "regionId": 4,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 2,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            }
        ]
    },
    {
        "name": "שומרון",
        "regionId": 5,
        "stations": [
            {
                "DisplayName": "אריאל",
                "stationId": 3,
                "name": "אריאל",
                "shortName": "אריאל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.10380957,
                    "longitude": 35.1693325
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 5,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 7,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 17,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "שפלה פנימית",
        "regionId": 6,
        "stations": [
            {
                "DisplayName": "בני עטרות",
                "stationId": 357,
                "name": "בני עטרות",
                "shortName": "כביש 859 רגבה",
                "stationsTag": "בני עטרות",
                "location": {
                    "latitude": 32.02477659,
                    "longitude": 34.91189169
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "רשות שדות התעופה",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 6,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 8,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 13,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 14,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 15,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "יד רמבם 1",
                "stationId": 40,
                "name": "יד רמבם 1",
                "shortName": "יד רמבם 1",
                "stationsTag": "40",
                "location": {
                    "latitude": null,
                    "longitude": null
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "נשר",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 6,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "בית שמש",
                "stationId": 7,
                "name": "בית שמש",
                "shortName": "בית שמש",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.75059505,
                    "longitude": 34.99381333
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 7,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 13,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אור יהודה",
                "stationId": 371,
                "name": "אור יהודה",
                "shortName": "Station 371",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.02531036,
                    "longitude": 34.85226183
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "רשות שדות התעופה",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 6,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 9,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "מודיעין",
                "stationId": 64,
                "name": "מודיעין",
                "shortName": "מודיעין",
                "stationsTag": "25",
                "location": {
                    "latitude": 31.89295205,
                    "longitude": 34.99531847
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "יד רמב\\"ם החדשה",
                "stationId": 338,
                "name": "יד רמב\\"ם החדשה",
                "shortName": "יד רמבם 2",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.90413031,
                    "longitude": 34.89581407
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "נשר",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 6,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אחיסמך",
                "stationId": 78,
                "name": "אחיסמך",
                "shortName": "אחיסמך",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.9350483,
                    "longitude": 34.90873938
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחובות",
                "stationId": 32,
                "name": "רחובות",
                "shortName": "רחובות",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.8995478,
                    "longitude": 34.81639829
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 6,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 9,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 10,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 17,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רובע א",
                "stationId": 510,
                "name": "רובע א",
                "shortName": "Station 510",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.056055,
                    "longitude": 34.962542
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "דנה הנדסה",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 7,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אלעד",
                "stationId": 465,
                "name": "אלעד",
                "shortName": "Station 465",
                "stationsTag": "465",
                "location": {
                    "latitude": 32.05352021,
                    "longitude": 34.95562719
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מחצבת מגדל צדק",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 4,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כפר שמואל",
                "stationId": 77,
                "name": "כפר שמואל",
                "shortName": "כפר שמוא",
                "stationsTag": "ישנה",
                "location": {
                    "latitude": 31.89254,
                    "longitude": 34.92509
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 4,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 10,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מודיעין",
                "stationId": 31,
                "name": "מודיעין",
                "shortName": "מודיעין",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.90824,
                    "longitude": 35.00921
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": false,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 6,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": false,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 7,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 8,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 9,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "GSR",
                        "channelId": 10,
                        "name": "GSR",
                        "alias": "קרינת שמש",
                        "active": true,
                        "typeId": 17,
                        "pollutantId": 38,
                        "units": "w/m2",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 11,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 13,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 14,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 15,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 16,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "עינת",
                "stationId": 473,
                "name": "עינת",
                "shortName": "Station 473",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.08253776,
                    "longitude": 34.94110093
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "מחצבת מגדל צדק",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת - 7",
                "stationId": 397,
                "name": "ניידת - 7",
                "shortName": "Station 397",
                "stationsTag": "397",
                "location": {
                    "latitude": 31.920067,
                    "longitude": 34.889532
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 4,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 10,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כרמי יוסף",
                "stationId": 76,
                "name": "כרמי יוסף",
                "shortName": "כרמי יוס",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.84661321,
                    "longitude": 34.91951304
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "בית חשמונאי",
                "stationId": 367,
                "name": "בית חשמונאי",
                "shortName": "Station 367",
                "stationsTag": "367",
                "location": {
                    "latitude": 31.88952134,
                    "longitude": 34.91520583
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "בעלות משותפת",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 12,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 14,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 15,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "שכונת האמנים",
                "stationId": 513,
                "name": "שכונת האמנים",
                "shortName": "Station 513",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.915084,
                    "longitude": 34.874771
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "נשר",
                "regionId": 6,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 2,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 3,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 4,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 6,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "גוש דן",
        "regionId": 7,
        "stations": [
            {
                "DisplayName": "תחנת רכבת וולפסון",
                "stationId": 348,
                "name": "תחנת רכבת וולפסון",
                "shortName": "ניידת רכבת",
                "stationsTag": "2",
                "location": {
                    "latitude": 32.03509243,
                    "longitude": 34.7596658
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "רכבת ישראל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "RH",
                        "channelId": 1,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 2,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות פנים מבניות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מכבי אש",
                "stationId": 56,
                "name": "מכבי אש",
                "shortName": "מכבי אש",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.06798231,
                    "longitude": 34.83292973
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גבעתיים",
                "stationId": 19,
                "name": "גבעתיים",
                "shortName": "גבעתיים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.06923,
                    "longitude": 34.81039
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 6,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 7,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 8,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 9,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 12,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 14,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "GSR",
                        "channelId": 15,
                        "name": "GSR",
                        "alias": "קרינת שמש",
                        "active": true,
                        "typeId": 17,
                        "pollutantId": 38,
                        "units": "w/m2",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב לחי",
                "stationId": 2,
                "name": "רחוב לחי",
                "shortName": "עמיאל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.0474345,
                    "longitude": 34.79336065
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 5,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 11,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "איילון",
                "stationId": 528,
                "name": "איילון",
                "shortName": "Station 528",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.127073809098881,
                    "longitude": 34.852546362304935
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "נתיבי איילון",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת - 5",
                "stationId": 339,
                "name": "ניידת - 5",
                "shortName": "ניידת - 5",
                "stationsTag": "3",
                "location": {
                    "latitude": 32.120137,
                    "longitude": 34.791389
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 2,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 6,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 7,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 8,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 9,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת 1 אשדוד - לא פעילה",
                "stationId": 120,
                "name": "ניידת 1 אשדוד - לא פעילה",
                "shortName": "נייד אשד",
                "stationsTag": "120",
                "location": {
                    "latitude": 31.825258,
                    "longitude": 34.683338
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 2,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 3,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 4,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM1",
                        "channelId": 7,
                        "name": "PM1",
                        "alias": "חלקיקים נשימים בגודל 1 מיקרון",
                        "active": true,
                        "typeId": 51,
                        "pollutantId": null,
                        "units": "ug/m3L",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 8,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 10,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 11,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 12,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 13,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "תחנת רכבת קוממיות",
                "stationId": 386,
                "name": "תחנת רכבת קוממיות",
                "shortName": "Station 386",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.00072393,
                    "longitude": 34.75937677
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "רכבת ישראל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "RH",
                        "channelId": 1,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 2,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות פנים מבניות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב גיסין",
                "stationId": 53,
                "name": "רחוב גיסין",
                "shortName": "אחד העם",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.09989507,
                    "longitude": 34.87123593
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 1,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 3,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 4,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 9,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 17,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 20,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "תחנת רכבת יוספטל",
                "stationId": 385,
                "name": "תחנת רכבת יוספטל",
                "shortName": "Station 385",
                "stationsTag": "385",
                "location": {
                    "latitude": 32.01454913,
                    "longitude": 34.76213594
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "רכבת ישראל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "RH",
                        "channelId": 1,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 2,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות פנים מבניות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב יפת",
                "stationId": 170,
                "name": "רחוב יפת",
                "shortName": "יפת יפו",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.04974941,
                    "longitude": 34.75281843
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "חולון",
                "stationId": 24,
                "name": "חולון",
                "shortName": "חולון",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.01821589,
                    "longitude": 34.76892424
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 10,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב הרצל",
                "stationId": 139,
                "name": "רחוב הרצל",
                "shortName": "ראשון לציון",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.95815705,
                    "longitude": 34.80206243
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "תחנת רכבת השלום",
                "stationId": 346,
                "name": "תחנת רכבת השלום",
                "shortName": "רכבת השלום",
                "stationsTag": "5554",
                "location": {
                    "latitude": 32.07336049,
                    "longitude": 34.79319171
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "רכבת ישראל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 5,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 6,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות פנים מבניות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "תחנת רכבת ההגנה",
                "stationId": 384,
                "name": "תחנת רכבת ההגנה",
                "shortName": "Station 384",
                "stationsTag": "384",
                "location": {
                    "latitude": 32.05393539,
                    "longitude": 34.78478646
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "רכבת ישראל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "RH",
                        "channelId": 1,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 2,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות פנים מבניות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שיכון בבלי",
                "stationId": 55,
                "name": "שיכון בבלי",
                "shortName": "שיכון בב",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.10162,
                    "longitude": 34.7955
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב לוינסקי",
                "stationId": 414,
                "name": "רחוב לוינסקי",
                "shortName": "Station 414",
                "stationsTag": "414",
                "location": {
                    "latitude": 32.05680394,
                    "longitude": 34.77962707
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנה מרכזית תל אביב",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 6,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "שכונת המשתלה",
                "stationId": 406,
                "name": "שכונת המשתלה",
                "shortName": "Station 406",
                "stationsTag": "406",
                "location": {
                    "latitude": 32.13002204,
                    "longitude": 34.83178828
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 4,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 6,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "אוניברסיטה",
                "stationId": 39,
                "name": "אוניברסיטה",
                "shortName": "יד אבנר",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.11942564,
                    "longitude": 34.80503325
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 6,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 7,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 8,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 9,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 13,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כביש 4",
                "stationId": 34,
                "name": "כביש 4",
                "shortName": "כביש 4",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.0712286,
                    "longitude": 34.8422153
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 14,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": false,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "תורן רמת השרון",
                "stationId": 79,
                "name": "תורן רמת השרון",
                "shortName": "תורן רמת",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.13086,
                    "longitude": 34.83267
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 1,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 3,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp1",
                        "channelId": 4,
                        "name": "Temp1",
                        "alias": null,
                        "active": true,
                        "typeId": 83,
                        "pollutantId": null,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "Ws65",
                        "channelId": 5,
                        "name": "Ws65",
                        "alias": null,
                        "active": true,
                        "typeId": 84,
                        "pollutantId": null,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Wd65",
                        "channelId": 6,
                        "name": "Wd65",
                        "alias": null,
                        "active": true,
                        "typeId": 85,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 7,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp6",
                        "channelId": 8,
                        "name": "Temp6",
                        "alias": null,
                        "active": true,
                        "typeId": 86,
                        "pollutantId": null,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 12,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 13,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב ז\u0027בוטינסקי",
                "stationId": 33,
                "name": "רחוב ז\u0027בוטינסקי",
                "shortName": "רמז",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.09215942,
                    "longitude": 34.82685735
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 8,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "יד לבנים",
                "stationId": 54,
                "name": "יד לבנים",
                "shortName": "יד לבנים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.07723676,
                    "longitude": 34.82150648
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 2,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 3,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "הצפון החדש",
                "stationId": 59,
                "name": "הצפון החדש",
                "shortName": "אנטוקולס",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.08428242,
                    "longitude": 34.78260351
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 9,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "לב תל אביב",
                "stationId": 82,
                "name": "לב תל אביב",
                "shortName": "דרך פ\u0027ת",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.06223408,
                    "longitude": 34.77734636
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 12,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב יהודה המכבי",
                "stationId": 26,
                "name": "רחוב יהודה המכבי",
                "shortName": "עירוני ד",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.09380567,
                    "longitude": 34.7909179
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "NOX",
                        "channelId": 1,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 9,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שיכון ל",
                "stationId": 60,
                "name": "שיכון ל",
                "shortName": "שיכון ל",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 32.10834032,
                    "longitude": 34.79025907
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 7,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "ירושלים",
        "regionId": 8,
        "stations": [
            {
                "DisplayName": "בקעה",
                "stationId": 13,
                "name": "בקעה",
                "shortName": "אפרתה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.7572077,
                    "longitude": 35.2182598
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 10,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 12,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כיכר ספרא",
                "stationId": 36,
                "name": "כיכר ספרא",
                "shortName": "ספרא",
                "stationsTag": "36",
                "location": {
                    "latitude": 31.78052854,
                    "longitude": 35.22471394
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 6,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 14,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב דבורה הנביאה",
                "stationId": 458,
                "name": "רחוב דבורה הנביאה",
                "shortName": "Station 458",
                "stationsTag": "458",
                "location": {
                    "latitude": 31.78427131,
                    "longitude": 35.22387011
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 8,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 10,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רציף 10 תחנה מרכזית",
                "stationId": 310,
                "name": "רציף 10 תחנה מרכזית",
                "shortName": "ניידת התחנה המרכזית בירושלים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.78971089,
                    "longitude": 35.20388373
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "התחנה המרכזית בירושלים ניהול",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות פנים מבניות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניידת - 6",
                "stationId": 337,
                "name": "ניידת - 6",
                "shortName": "ניידת - 6",
                "stationsTag": "2",
                "location": {
                    "latitude": 31.850512,
                    "longitude": 35.223773
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 7,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 9,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 16,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מלכי ישראל",
                "stationId": 509,
                "name": "מלכי ישראל",
                "shortName": "Station 509",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.791673,
                    "longitude": 35.212422
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 4,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 11,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רחוב בר אילן",
                "stationId": 5,
                "name": "רחוב בר אילן",
                "shortName": "בר אילן",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.79501272,
                    "longitude": 35.22040892
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 4,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 15,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אזור תעשייה עטרות",
                "stationId": 328,
                "name": "אזור תעשייה עטרות",
                "shortName": "עטרות א.תעשיה",
                "stationsTag": "328",
                "location": {
                    "latitude": 31.8534034,
                    "longitude": 35.2152478
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "עיריית ירושלים",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "WD",
                        "channelId": 1,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 3,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 5,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 6,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "CO",
                        "channelId": 7,
                        "name": "CO",
                        "alias": "פחמן חד חמצני",
                        "active": true,
                        "typeId": 27,
                        "pollutantId": 3,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תעשייתית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "רוממה",
                "stationId": 193,
                "name": "רוממה",
                "shortName": "תחנה מרכ",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.78971089,
                    "longitude": 35.20388373
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "התחנה המרכזית בירושלים ניהול",
                "regionId": 8,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "אזור יהודה",
        "regionId": 9,
        "stations": [
            {
                "DisplayName": "גוש עציון",
                "stationId": 21,
                "name": "גוש עציון",
                "shortName": "גוש עציו",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.65679414,
                    "longitude": 35.11842887
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 9,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 3,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 7,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 8,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 9,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 15,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 16,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "לוט",
                "stationId": 182,
                "name": "לוט",
                "shortName": "לוט",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.06919789,
                    "longitude": 35.39764091
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מפעלי ים המלח",
                "regionId": 9,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 17,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 19,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נאות הכיכר",
                "stationId": 184,
                "name": "נאות הכיכר",
                "shortName": "נאות הכי",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 30.9457708,
                    "longitude": 35.38825658
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מפעלי ים המלח",
                "regionId": 9,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 18,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 21,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נחל אשלים",
                "stationId": 183,
                "name": "נחל אשלים",
                "shortName": "נחל אשלים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.01549158,
                    "longitude": 35.35340223
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מפעלי ים המלח",
                "regionId": 9,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 17,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 19,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "מישור החוף הדרומי",
        "regionId": 10,
        "stations": [
            {
                "DisplayName": "לב אשדוד",
                "stationId": 467,
                "name": "לב אשדוד",
                "shortName": "Station 467",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.796882,
                    "longitude": 34.648296
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אביגדור",
                "stationId": 468,
                "name": "אביגדור",
                "shortName": "Station 468",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.71074595,
                    "longitude": 34.74474297
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנת כוח באר טוביה",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "O3",
                        "channelId": 1,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רובע טו",
                "stationId": 121,
                "name": "רובע טו",
                "shortName": "רובע טו",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.77196,
                    "longitude": 34.62715
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "Temp",
                        "channelId": 1,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 7,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 8,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 9,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 12,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "T.Mass",
                        "channelId": 13,
                        "name": "T.Mass",
                        "alias": null,
                        "active": true,
                        "typeId": 124,
                        "pollutantId": null,
                        "units": "None",
                        "description": null
                    },
                    {
                        "DisplayName": "T.VOL",
                        "channelId": 14,
                        "name": "T.VOL",
                        "alias": null,
                        "active": true,
                        "typeId": 52,
                        "pollutantId": null,
                        "units": "ng/m3",
                        "description": null
                    },
                    {
                        "DisplayName": "DATE",
                        "channelId": 15,
                        "name": "DATE",
                        "alias": null,
                        "active": true,
                        "typeId": 53,
                        "pollutantId": null,
                        "units": "ng/m3",
                        "description": null
                    },
                    {
                        "DisplayName": "RADON",
                        "channelId": 17,
                        "name": "RADON",
                        "alias": null,
                        "active": true,
                        "typeId": 256,
                        "pollutantId": null,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 18,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קבוצת יבנה",
                "stationId": 118,
                "name": "קבוצת יבנה",
                "shortName": "חבל יבנה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.81881,
                    "longitude": 34.72049
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שמשון",
                "stationId": 160,
                "name": "שמשון",
                "shortName": "אשקלון ד",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.65426883,
                    "longitude": 34.55150309
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "בעלות משותפת",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 13,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 14,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 16,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "יבנה",
                "stationId": 65,
                "name": "יבנה",
                "shortName": "יבנה עיר",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.87510874,
                    "longitude": 34.7385917
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קריית גת",
                "stationId": 124,
                "name": "קריית גת",
                "shortName": "קריית גת",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.60675904,
                    "longitude": 34.76148294
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שדרות",
                "stationId": 126,
                "name": "שדרות",
                "shortName": "שדרות",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.52829568,
                    "longitude": 34.60220366
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קריית מלאכי",
                "stationId": 125,
                "name": "קריית מלאכי",
                "shortName": "ק.מלאכי",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.72836381,
                    "longitude": 34.74113179
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גן יבנה",
                "stationId": 116,
                "name": "גן יבנה",
                "shortName": "גן יבנה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.78299037,
                    "longitude": 34.70598745
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 7,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 11,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "זיקים",
                "stationId": 379,
                "name": "זיקים",
                "shortName": "Station 379",
                "stationsTag": "379",
                "location": {
                    "latitude": 31.61223341,
                    "longitude": 34.52034008
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "קצאא",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גדרה",
                "stationId": 117,
                "name": "גדרה",
                "shortName": "גדרה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.81407047,
                    "longitude": 34.77891506
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 7,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 8,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 9,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 13,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קבוצת יבנה מערב",
                "stationId": 511,
                "name": "קבוצת יבנה מערב",
                "shortName": "Station 511",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.82009451,
                    "longitude": 34.71608607
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 5,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 6,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 9,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אגן כימיקלים",
                "stationId": 307,
                "name": "אגן כימיקלים",
                "shortName": "אגן כימיקלים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": null,
                    "longitude": null
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "אדמה אגן",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "WD",
                        "channelId": 1,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 3,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 5,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "BP",
                        "channelId": 6,
                        "name": "BP",
                        "alias": "לחץ ברומטרי",
                        "active": false,
                        "typeId": 33,
                        "pollutantId": 36,
                        "units": "mb",
                        "description": null
                    },
                    {
                        "DisplayName": "DCM",
                        "channelId": 8,
                        "name": "DCM",
                        "alias": null,
                        "active": true,
                        "typeId": 253,
                        "pollutantId": null,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "TCE",
                        "channelId": 9,
                        "name": "TCE",
                        "alias": null,
                        "active": true,
                        "typeId": 254,
                        "pollutantId": null,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "Toluene",
                        "channelId": 10,
                        "name": "Toluene",
                        "alias": "טולואן",
                        "active": true,
                        "typeId": 10,
                        "pollutantId": null,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "MIBK",
                        "channelId": 11,
                        "name": "MIBK",
                        "alias": null,
                        "active": true,
                        "typeId": 255,
                        "pollutantId": null,
                        "units": "ppb",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "אזור תעשייה קלה",
                "stationId": 115,
                "name": "אזור תעשייה קלה",
                "shortName": "אשדוד",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.8188349,
                    "longitude": 34.66970541
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 7,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 8,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 9,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 11,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 12,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 15,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 23,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניר גלים 2",
                "stationId": 353,
                "name": "ניר גלים 2",
                "shortName": "ניר גלים 2",
                "stationsTag": "353",
                "location": {
                    "latitude": 31.82502767,
                    "longitude": 34.67988361
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "אדמה אגן",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 6,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 9,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כרמיה",
                "stationId": 130,
                "name": "כרמיה",
                "shortName": "כרמיה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.60457859,
                    "longitude": 34.54293549
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 24,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "בני דרום",
                "stationId": 365,
                "name": "בני דרום",
                "shortName": "Station 365",
                "stationsTag": "בני דרום",
                "location": {
                    "latitude": 31.81964492,
                    "longitude": 34.69345435
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 2,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 4,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 8,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "יד בנימין",
                "stationId": 122,
                "name": "יד בנימין",
                "shortName": "יד בנימי",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.79834338,
                    "longitude": 34.81878594
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 4,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 5,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 7,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 8,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 9,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 10,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 12,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "H2S",
                        "channelId": 15,
                        "name": "H2S",
                        "alias": "מימן גופרתי",
                        "active": true,
                        "typeId": 56,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 18,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ארז",
                "stationId": 131,
                "name": "ארז",
                "shortName": "ארז",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.55983402,
                    "longitude": 34.56516934
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 18,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "תימורים",
                "stationId": 469,
                "name": "תימורים",
                "shortName": "Station 469",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.71589819,
                    "longitude": 34.75563692
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנת כוח באר טוביה",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "O3",
                        "channelId": 1,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 5,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 7,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 8,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גן הורדים",
                "stationId": 123,
                "name": "גן הורדים",
                "shortName": "אשקלון",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.66024328,
                    "longitude": 34.57023959
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 13,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 22,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניר ישראל",
                "stationId": 129,
                "name": "ניר ישראל",
                "shortName": "ניר ישרא",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.68647598,
                    "longitude": 34.63689557
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שדה יואב",
                "stationId": 128,
                "name": "שדה יואב",
                "shortName": "שדה יואב",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.64596631,
                    "longitude": 34.67488274
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ניר גלים 1",
                "stationId": 61,
                "name": "ניר גלים 1",
                "shortName": "ניר גלים 1",
                "stationsTag": "18",
                "location": {
                    "latitude": 31.82500079,
                    "longitude": 34.67992601
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "רובע ט\\"ו החדשה",
                "stationId": 383,
                "name": "רובע ט\\"ו החדשה",
                "shortName": "Station 383",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.77322005,
                    "longitude": 34.62820632
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 7,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 9,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 12,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 25,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "איזור תעשייה צפוני",
                "stationId": 535,
                "name": "איזור תעשייה צפוני",
                "shortName": "Station 535",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.838837,
                    "longitude": 34.683926
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 2,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Toluene",
                        "channelId": 3,
                        "name": "Toluene",
                        "alias": "טולואן",
                        "active": true,
                        "typeId": 10,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גברעם",
                "stationId": 127,
                "name": "גברעם",
                "shortName": "ק.גברעם",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.58960675,
                    "longitude": 34.61059639
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": false,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "פארק לכיש",
                "stationId": 423,
                "name": "פארק לכיש",
                "shortName": "Station 423",
                "stationsTag": "423",
                "location": {
                    "latitude": 31.81332221,
                    "longitude": 34.65013575
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 2,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 5,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 7,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "לוזית",
                "stationId": 85,
                "name": "לוזית",
                "shortName": "לוזית",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.68508698,
                    "longitude": 34.88256686
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אורט",
                "stationId": 156,
                "name": "אורט",
                "shortName": "אורט",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.81461,
                    "longitude": 34.64737
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 4,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "TSP",
                        "channelId": 5,
                        "name": "TSP",
                        "alias": "TSP",
                        "active": true,
                        "typeId": 7,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "פלוגות",
                "stationId": 531,
                "name": "פלוגות",
                "shortName": "Station 531",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.6351328,
                    "longitude": 34.7465805
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנת כוח או.פי.סי. צומת אנרגיה",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 5,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 8,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 9,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "יהלום",
                "stationId": 157,
                "name": "יהלום",
                "shortName": "יהלום",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.81162,
                    "longitude": 34.64339
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 2,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "TSP",
                        "channelId": 3,
                        "name": "TSP",
                        "alias": "TSP",
                        "active": true,
                        "typeId": 7,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מבקיעים",
                "stationId": 306,
                "name": "מבקיעים",
                "shortName": "מבקיעים",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.62210548,
                    "longitude": 34.57772845
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 3,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 4,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": false,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 7,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 9,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 14,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 15,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 18,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כפר מנחם",
                "stationId": 71,
                "name": "כפר מנחם",
                "shortName": "כפר מנחם",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.72910789,
                    "longitude": 34.83345495
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גן דרום",
                "stationId": 63,
                "name": "גן דרום",
                "shortName": "גן דרום",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.80570663,
                    "longitude": 34.70121898
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שדרות ירושלים",
                "stationId": 405,
                "name": "שדרות ירושלים",
                "shortName": "Station 405",
                "stationsTag": "405",
                "location": {
                    "latitude": 31.79396561,
                    "longitude": 34.64315573
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "תחבורתית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "בת הדר",
                "stationId": 81,
                "name": "בת הדר",
                "shortName": "בת הדר",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.64765901,
                    "longitude": 34.59730274
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שכונת ההרחבה",
                "stationId": 331,
                "name": "שכונת ההרחבה",
                "shortName": "דליה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.72754914,
                    "longitude": 34.83394653
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשקלון",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "O3",
                        "channelId": 1,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Rain",
                        "channelId": 6,
                        "name": "Rain",
                        "alias": "גשם",
                        "active": true,
                        "typeId": 5,
                        "pollutantId": 37,
                        "units": "mm",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 7,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 8,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 9,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 10,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 11,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "רובע הבנים",
                "stationId": 532,
                "name": "רובע הבנים",
                "shortName": "Station 532",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.6202102,
                    "longitude": 34.7575935
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנת כוח או.פי.סי. צומת אנרגיה",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 5,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 6,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "בניה",
                "stationId": 119,
                "name": "בניה",
                "shortName": "בניה",
                "stationsTag": "119",
                "location": {
                    "latitude": 31.8431,
                    "longitude": 34.75082
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "איגוד ערים אשדוד",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 7,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 8,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "StWd",
                        "channelId": 9,
                        "name": "StWd",
                        "alias": "סטיית התקן של כיוון הרוח",
                        "active": true,
                        "typeId": 18,
                        "pollutantId": null,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 10,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כפר נופש חיילים",
                "stationId": 498,
                "name": "כפר נופש חיילים",
                "shortName": "Station 498",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.67248789,
                    "longitude": 34.55190288
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "נובל אנרגיה",
                "regionId": 10,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 9,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "צפון הנגב",
        "regionId": 11,
        "stations": [
            {
                "DisplayName": "קריית ההדרכה",
                "stationId": 132,
                "name": "קריית ההדרכה",
                "shortName": "קריית ההדרכה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.05376846,
                    "longitude": 34.82861064
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 1,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 4,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 13,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 14,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נחל בקע",
                "stationId": 138,
                "name": "נחל בקע",
                "shortName": "ב\u0027\u0027ש נ.ח",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.22370265,
                    "longitude": 34.77745837
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 1,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 4,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 13,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 14,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שגב שלום",
                "stationId": 134,
                "name": "שגב שלום",
                "shortName": "שגב שלום",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.19881909,
                    "longitude": 34.83901337
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 1,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 4,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 13,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 14,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "פזורה",
                "stationId": 133,
                "name": "פזורה",
                "shortName": "פזורה",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.15588148,
                    "longitude": 34.8123614
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 1,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 4,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 13,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 14,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שכונה ו",
                "stationId": 6,
                "name": "שכונה ו",
                "shortName": "שכונה ו\u0027",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.25716968,
                    "longitude": 34.78208472
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 7,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 8,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 9,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 10,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 14,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 16,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גבעת התצפית",
                "stationId": 345,
                "name": "גבעת התצפית",
                "shortName": "TABAM",
                "stationsTag": "321321",
                "location": {
                    "latitude": 31.13325951,
                    "longitude": 34.75910626
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "H2S",
                        "channelId": 1,
                        "name": "H2S",
                        "alias": "מימן גופרתי",
                        "active": true,
                        "typeId": 56,
                        "pollutantId": null,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 2,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 4,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 5,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "RH",
                        "channelId": 8,
                        "name": "RH",
                        "alias": "לחות אויר",
                        "active": true,
                        "typeId": 16,
                        "pollutantId": 18,
                        "units": "%",
                        "description": null
                    },
                    {
                        "DisplayName": "Temp",
                        "channelId": 9,
                        "name": "Temp",
                        "alias": "טמפרטורה",
                        "active": true,
                        "typeId": 24,
                        "pollutantId": 15,
                        "units": "°C",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 10,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 11,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 14,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נגב מזרחי",
                "stationId": 158,
                "name": "נגב מזרחי",
                "shortName": "נגב מזרח",
                "stationsTag": "158",
                "location": {
                    "latitude": 31.24963786,
                    "longitude": 35.2157187
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "O3",
                        "channelId": 2,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 4,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 5,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 6,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 7,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 9,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "ירוחם",
                "stationId": 135,
                "name": "ירוחם",
                "shortName": "ירוחם",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 30.99100101,
                    "longitude": 34.92805617
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "WS",
                        "channelId": 1,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 2,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 4,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 11,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 13,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 14,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "כסייפה",
                "stationId": 530,
                "name": "כסייפה",
                "shortName": "Station 530",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.247374,
                    "longitude": 35.098239
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 1,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 3,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 7,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 8,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נאות חובב דרום",
                "stationId": 186,
                "name": "נאות חובב דרום",
                "shortName": "רמת חובב",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.12319091,
                    "longitude": 34.79343596
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "H2S",
                        "channelId": 7,
                        "name": "H2S",
                        "alias": "מימן גופרתי",
                        "active": true,
                        "typeId": 56,
                        "pollutantId": null,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Nh3",
                        "channelId": 9,
                        "name": "Nh3",
                        "alias": "אמוניה",
                        "active": true,
                        "typeId": 57,
                        "pollutantId": null,
                        "units": "ppb",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 10,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "גבעת שמן",
                "stationId": 75,
                "name": "גבעת שמן",
                "shortName": "גבעת השמן",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.14545118,
                    "longitude": 34.82915124
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נאות חובב מזרח",
                "stationId": 187,
                "name": "נאות חובב מזרח",
                "shortName": "רמת חובב",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.13241818,
                    "longitude": 34.80219311
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 10,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נאות חובב צפון",
                "stationId": 188,
                "name": "נאות חובב צפון",
                "shortName": "רמת חובב",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.15138956,
                    "longitude": 34.78644526
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 10,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אשלים",
                "stationId": 417,
                "name": "אשלים",
                "shortName": "אשלים",
                "stationsTag": "417",
                "location": {
                    "latitude": 30.96435682,
                    "longitude": 34.70078742
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "תחנת כוח אשלים",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 2,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 5,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 6,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "אולפנת בני עקיבא",
                "stationId": 349,
                "name": "אולפנת בני עקיבא",
                "shortName": "אולפנת בני עקיבא",
                "stationsTag": "ערד אולפנה",
                "location": {
                    "latitude": 31.24943944,
                    "longitude": 35.21567668
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מישור רותם",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 2,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 3,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 4,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Benzene",
                        "channelId": 7,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "מחנה נתן",
                "stationId": 74,
                "name": "מחנה נתן",
                "shortName": "מחנה נתן",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.2197339,
                    "longitude": 34.80543396
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "נאות חובב מרכזית",
                "stationId": 185,
                "name": "נאות חובב מרכזית",
                "shortName": "רמת חובב",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 31.13506386,
                    "longitude": 34.78616039
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "מועצה נאות חובב",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "Benzene",
                        "channelId": 1,
                        "name": "Benzene",
                        "alias": "בנזן",
                        "active": true,
                        "typeId": 9,
                        "pollutantId": 24,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "SO2",
                        "channelId": 8,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 10,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 11,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 12,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "קטורה",
                "stationId": 400,
                "name": "קטורה",
                "shortName": "Station 400",
                "stationsTag": "400",
                "location": {
                    "latitude": 29.96685938,
                    "longitude": 35.05955144
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "המשרד להגנת הסביבה",
                "regionId": 11,
                "monitors": [
                    {
                        "DisplayName": "NO",
                        "channelId": 1,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 2,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 3,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 4,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM2.5",
                        "channelId": 5,
                        "name": "PM2.5",
                        "alias": "חלקיקים נשימים בגודל 2.5 מיקרון",
                        "active": true,
                        "typeId": 8,
                        "pollutantId": 21,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    },
    {
        "name": "אילת",
        "regionId": 12,
        "stations": [
            {
                "DisplayName": "בית ספר גולדווטר",
                "stationId": 377,
                "name": "בית ספר גולדווטר",
                "shortName": "בית ספר גולדווטר",
                "stationsTag": "377",
                "location": {
                    "latitude": 29.5545404,
                    "longitude": 34.94919144
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 12,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "WS",
                        "channelId": 2,
                        "name": "WS",
                        "alias": "מהירות רוח",
                        "active": true,
                        "typeId": 13,
                        "pollutantId": 19,
                        "units": "m/s",
                        "description": null
                    },
                    {
                        "DisplayName": "WD",
                        "channelId": 3,
                        "name": "WD",
                        "alias": "כוון רוח",
                        "active": true,
                        "typeId": 14,
                        "pollutantId": 20,
                        "units": "deg",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60",
                "AllTimebases": [
                    5,
                    30,
                    60
                ]
            },
            {
                "DisplayName": "מש\u0027\u0027 אילת חח\\"י",
                "stationId": 141,
                "name": "מש\u0027\u0027 אילת חח\\"י",
                "shortName": "מש\u0027\u0027 אילת",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 29.56646,
                    "longitude": 34.94859
                },
                "timebase": 5,
                "active": false,
                "isNonContinuous": false,
                "owner": "חברת חשמל",
                "regionId": 12,
                "monitors": [
                    {
                        "DisplayName": "SO2",
                        "channelId": 1,
                        "name": "SO2",
                        "alias": "גופרית דו חמצנית",
                        "active": true,
                        "typeId": 49,
                        "pollutantId": 4,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Spare",
                        "channelId": 2,
                        "name": "Spare",
                        "alias": null,
                        "active": true,
                        "typeId": 1,
                        "pollutantId": null,
                        "units": "None",
                        "description": null
                    },
                    {
                        "DisplayName": "Spare",
                        "channelId": 3,
                        "name": "Spare",
                        "alias": null,
                        "active": true,
                        "typeId": 1,
                        "pollutantId": null,
                        "units": "None",
                        "description": null
                    },
                    {
                        "DisplayName": "Spare",
                        "channelId": 4,
                        "name": "Spare",
                        "alias": null,
                        "active": true,
                        "typeId": 1,
                        "pollutantId": null,
                        "units": "None",
                        "description": null
                    },
                    {
                        "DisplayName": "O3",
                        "channelId": 5,
                        "name": "O3",
                        "alias": "אוזון",
                        "active": true,
                        "typeId": 4,
                        "pollutantId": 2,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NOX",
                        "channelId": 6,
                        "name": "NOX",
                        "alias": "תחמוצות חנקן",
                        "active": true,
                        "typeId": 3,
                        "pollutantId": 9,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO",
                        "channelId": 7,
                        "name": "NO",
                        "alias": "חנקן חד חמצני",
                        "active": true,
                        "typeId": 2,
                        "pollutantId": 8,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "NO2",
                        "channelId": 8,
                        "name": "NO2",
                        "alias": "חנקן דו חמצני",
                        "active": true,
                        "typeId": 19,
                        "pollutantId": 1,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "PM10",
                        "channelId": 9,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 23,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    },
                    {
                        "DisplayName": "Spare",
                        "channelId": 10,
                        "name": "Spare",
                        "alias": null,
                        "active": true,
                        "typeId": 1,
                        "pollutantId": null,
                        "units": "None",
                        "description": null
                    }
                ],
                "StationTarget": "תחנות לא פעילות",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            },
            {
                "DisplayName": "שכונת שחמון",
                "stationId": 304,
                "name": "שכונת שחמון",
                "shortName": "שכונת שחמון",
                "stationsTag": "(null)",
                "location": {
                    "latitude": 29.5464477,
                    "longitude": 34.93084677
                },
                "timebase": 5,
                "active": true,
                "isNonContinuous": false,
                "owner": "נמל אילת",
                "regionId": 12,
                "monitors": [
                    {
                        "DisplayName": "PM10",
                        "channelId": 1,
                        "name": "PM10",
                        "alias": "חלקיקים נשימים בגודל 10 מיקרון",
                        "active": true,
                        "typeId": 6,
                        "pollutantId": 22,
                        "units": "µg/m³",
                        "description": null
                    }
                ],
                "StationTarget": "כללית",
                "additionalTimebases": "30,60,1440",
                "AllTimebases": [
                    5,
                    30,
                    60,
                    1440
                ]
            }
        ]
    }
]
"""

obj = json.loads(data)

stations_mapping = {}

for region in obj:
    for station in region["stations"]:
        stations_mapping[station["stationId"]] = f'{station["DisplayName"]} ({station["owner"]})'


print(stations_mapping)