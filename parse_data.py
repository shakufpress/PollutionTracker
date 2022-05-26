import collections

import conf


def parse_data(results):
    abnormalities = collections.defaultdict(list)
    for station in results:
        station_id = station["StationId"]
        station_name = conf.STATION_MAPPING[station_id]
        for material in station["data"][0]["channels"]:
            material_name = material["DisplayName"]
            if material_name in conf.LIMITS:
                material_value = material["value"]
                if material_value > conf.LIMITS[material_name]:
                    abnormalities[station_name].append((material_name, material_value))

    return abnormalities


import query_api

print(parse_data(query_api.get_data()))
