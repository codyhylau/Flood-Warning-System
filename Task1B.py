
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    final = stations_by_distance(stations,(52.2053, 0.1218))
    print ("10 closest stations are: ")
    print(final[:10])
    print ("10 furthest stations are: ")
    print(final[-10:])

if __name__ == "__main__":
    run()