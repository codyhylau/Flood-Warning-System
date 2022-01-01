from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """Requirements for Task 1C"""

    stations = build_station_list()

    rivers=sorted(rivers_with_station(stations))
    print('Number of rivers with stations: ' + str(len(rivers)))
    print(rivers[:10])

    dict_rivers=stations_by_river(stations)
    print("\nStations on River Aire:")
    print(sorted(dict_rivers["River Aire"]))
    print("\nStations on River Cam:")
    print(sorted(dict_rivers["River Cam"]))
    print("\nStations on River Thames:")
    print(sorted(dict_rivers["River Thames"]))

if __name__ == "__main__":
    run()
